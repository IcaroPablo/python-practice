def build_triangle(nlines):
    triangle = []
    if (nlines >= 1):
        linha1 = [1]
        triangle.append(linha1)
    
    if (nlines >= 2):
        linha2 = [1, 1]
        triangle.append(linha2)
    
    if (nlines >= 3):
        previous_line = [1, 1]
        
        for linha in range(3, nlines + 1):
            current_line = []
            
            for elemento in range(0, linha):
                if (elemento == 0):
                    current_line.append(1)
                elif (elemento == linha - 1):
                    current_line.append(1)
                else:
                    current_line.append(previous_line[elemento] + previous_line[elemento - 1])

            triangle.append(current_line)
            previous_line = current_line

    return triangle

number_of_lines = int(input("digite o número de linhas do triângulo:\n> "))
built_triangle = build_triangle(number_of_lines)

for line in built_triangle:
    print(line)
