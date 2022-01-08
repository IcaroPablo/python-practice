import sys
import math
import numpy
import random
import pygame

from scipy.spatial import distance
from shapely.geometry import box, Polygon

BLUE = (0, 0, 230)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SIZE = (1500, 800)

width = 50
height = 50
pygame.init()
screen = pygame.display.set_mode(SIZE)

class robot():
    def __init__(self, x, y,end_x, end_y, vel, num_targets):
        self.x = x
        self.y = y
        self.vel = vel
        self.end_x = end_x
        self.end_y = end_y
        
        self.angle = 0
        self.path = [[], []]
        self.targets = []
        self.detected = []

        for t in range(num_targets):
            x = random.randint(100, 1400)
            y = random.randint(100, 700)

            self.targets.append([x, y])

    def adjust_angle(self):
        while self.angle > 360:
            self.angle -= 360

        while self.angle < 0:
            self.angle += 360

def directions(action, rot=0.4):
    if action == "ahead":
        zed.x += zed.vel*math.cos(zed.angle*3.14/180)
        zed.y -= zed.vel*math.sin(zed.angle*3.14/180)
        zed.path[0].append([zed.x + 25, zed.y + 25])
        zed.path[1].append([zed.angle])

    if action == "back":
        zed.x -= zed.vel*math.cos(zed.angle*3.14/180)
        zed.y += zed.vel*math.sin(zed.angle*3.14/180)
        zed.path[0].append([zed.x + 25, zed.y + 25])
        zed.path[1].append([zed.angle])

    if action == "turn_r":
        zed.angle -= rot
        zed.path[0].append([zed.x + 25, zed.y + 25])
        zed.path[1].append([zed.angle])
    
    if action == "turn_l":
        zed.angle += rot
        zed.path[0].append([zed.x + 25, zed.y + 25])
        zed.path[1].append([zed.angle])

def move_robot(zed, mode='ctrl'):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        directions("turn_l")

    if keys[pygame.K_RIGHT]:
        directions("turn_r")

    if keys[pygame.K_UP]:
        directions("ahead")

    if keys[pygame.K_DOWN]:
        directions("back")

    if mode == 'auto':
        if zed.detected == []:
            # directions("turn_l")
            zed.detected = [[zed.end_x, zed.end_y]]
        else:
            x_target = zed.detected[0][0]
            y_target = zed.detected[0][1]
            x_zed = (zed.x + 25)
            y_zed = (zed.y + 25)

            x_dif = x_target - x_zed
            y_dif = y_zed - y_target

            angle = (180/math.pi) * numpy.arctan(y_dif/x_dif)
            angle = round(angle, 2)

            sig_x = x_dif/abs(x_dif)
            sig_y = y_dif/abs(y_dif)

            if (sig_x == -1 and sig_y == -1) or (sig_x == -1 and sig_y == 1):
                angle += 180
            else:
                angle += sig_x*180 + sig_y*(-180)

            rot = (angle - zed.angle)

            if zed.angle > 270 and angle < zed.angle - 180:
                rot = angle + (360 - zed.angle)

            if zed.angle < angle - 180 and angle > 270:
                rot = -zed.angle -(360 - angle)

            rot = rot/30
            directions("turn_l", rot)
            directions("ahead")

def draw_robot(zed, screen):
    x = zed.x
    y = zed.y
    angle = zed.angle

    icon_rect = pygame.draw.rect(screen, BLACK, (x, y, width, height))

    centro = (x+25, y+25)

    theta = numpy.radians(angle)
    c, s = numpy.cos(theta), numpy.sin(theta)
    r_mat = [[c,-s], [s, c]]
    base1 = (200, 571)
    base2 = (200, -571)

    rotated1 = numpy.dot(base1, r_mat)
    rotated2 = numpy.dot(base2, r_mat)

    l1e = (centro[0] + rotated1[0], centro[1] + rotated1[1])
    l2e = (centro[0] + rotated2[0], centro[1] + rotated2[1])

    pygame.draw.line(screen, BLUE, centro, l1e)
    pygame.draw.line(screen, BLUE, centro, l2e)
    pygame.draw.line(screen, BLUE, l1e, l2e)

    icon = pygame.image.load("icon.jpg")
    icon = pygame.transform.scale(icon, (width, height))
    icon = pygame.transform.rotate(icon, angle)

    screen.blit(icon, icon_rect)

    for target in zed.targets:
        if [target[0], target[1]] in zed.detected:
            pygame.draw.rect(screen, RED, [target[0], target[1], 25, 25])
            continue
        pygame.draw.rect(screen, BLUE, [target[0], target[1], 25, 25])

    if len(zed.path[0]) > 2:
        pygame.draw.lines(screen, GREEN, False, zed.path[0])

    return [centro, l1e, l2e]

def detect_collision(zed, points):
    vision_field = Polygon(points)

    for target in zed.targets:
        gridcell_shape = box(target[0], target[1]+25, target[0]+25, target[1])
        
        if vision_field.intersection(gridcell_shape).area != 0 :
            if not [target[0], target[1]] in zed.detected:
                zed.detected.append([target[0], target[1]])

    for i in range(len(zed.targets)):
        point = [zed.targets[i][0], zed.targets[i][1]]
        if distance.euclidean([zed.x + 25, zed.y + 25], point) < 30:
            if point in zed.detected:
                zed.detected.pop(zed.detected.index(point))
            zed.targets.pop(i)
            break

def detect_obstacles():
    #ver o objeto e identificar se é lixo ou não (isso vai retornar o retangulo do objeto)
    #criar um novo caminho para contornar o obstáculo
        #a partir do objeto identificado
        #serão criados dois pontos perto dos limites visualizados
        #o novo "próximo" ponto vai ser o ponto de extremidade mais pŕoximo do próximo alvo
    pass

def define_path(zed, screen):
    points = zed.detected
    ref = [zed.x + 25, zed.y + 25]
    path = []
    aux = 0

    if [zed.end_x, zed.end_y] in zed.detected and len(zed.detected) > 1:
        points.pop(points.index([zed.end_x, zed.end_y]))

    for k in range(len(points)):
        minimum = 10000
        for point in points:
            dist = distance.euclidean(ref, point)
            if ref != point:
                if dist < minimum:
                    if point not in path:
                        minimum = dist
                        aux = point
        
        ref = aux
        path.append(ref)

    zed.detected = path

    if len(zed.detected) > 1:
        pygame.draw.lines(screen, RED, False, zed.detected)
    
a = 2
while a != 1:
    for event in pygame.event.get():
        if a == 0 and event.type == pygame.MOUSEBUTTONDOWN:
            ex, ey = pygame.mouse.get_pos()
            a = 1
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            bx, by = pygame.mouse.get_pos()
            a = 0

zed = robot(bx, by, ex, ey, 1, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)

    if len(zed.detected) > 0:
        define_path(zed, screen)

    zed.adjust_angle()
    move_robot(zed, "auto")
    detect_collision(zed, draw_robot(zed, screen))

    pygame.display.update()