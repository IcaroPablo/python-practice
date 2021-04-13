import os

class hangman_game():
    def __init__(self):
        self.words_list = ["carro", "cavalo"]
        self.word = self.words_list[0]
        self.playing_word = []
        self.history = []
        self.life = 6
        self.pos = []
        self.printed_word = []
        self.game_status = "ongoing"
    
    def reset_game(self):
        for c in range(len(self.word)):
            self.printed_word.append("_")
    
    def show_doll(self):
        if self.life == 6:
            print("____")
            print("|  |")
            print("|")
            print("|")
            print("|")
            
        if self.life == 5:
            print("____")
            print("|  |")
            print("|  o")
            print("|")
            print("|")
            
        if self.life == 4:
            print("____")
            print("|  |")
            print("|  o")
            print("|  |")
            print("|")
            
        if self.life == 3:
            print("____")
            print("|  |")
            print("|  o")
            print("| /|")
            print("|")
            
        if self.life == 2:
            print("____")
            print("|  |")
            print("|  o")
            print("| /|\\")
            print("|")
            
        if self.life == 1:
            print("____")
            print("|  |")
            print("|  o")
            print("| /|\\")
            print("| /")
            
        if self.life == 0:
            print("____")
            print("|  |")
            print("|  o")
            print("| /|\\")
            print("| / \\")
    
    def show_word(self):
        if self.pos != []:
            for p in self.pos:
                self.printed_word[p] = self.word[p]
                
        print(" ".join(self.printed_word))
        
    def check_letter(self, letter = None):        
        if letter != None:
            if letter not in self.history:
                self.history.append(letter)
                if letter in self.word:
                    for i in range(len(self.word)):
                        if self.word[i] == letter:
                            self.pos.append(i)
                else:
                    self.life -= 1
                    
    def check_status(self):
        if self.life == 0:
            print("você perdeu :(")
            self.game_status = "finished"
            os.system("pause")
        if self.pos == range(len(self.word)):
            print("você venceu :D")
            self.game_status = "finished"
            os.system("pause")
    
    def start_game_loop(self):
        self.reset_game()
        
        while self.game_status != "finished":
            os.system("clear")
            # mostrar bonequinho
            self.show_doll()
            # mostrar palavra
            self.show_word()
            # mostrar histórico
            print(self.history)
            # solicitar letra
            letter = str(input("\n\n> digite uma letra:\n"))
            # verificar letra
            self.check_letter(letter)
            # verificar condição de vitória
            self.check_status()
    
    def show_menu(self):
        os.system("clear")
        print("###---JOGO DA FORCA---###")
        print("\n1 - iniciar jogo")
        print("\n2 - inserir nova palavra")
        option = input()
        
        if option == "1":
            self.start_game_loop()
        if option == "2":
            pass
            
game = hangman_game()
while True:
    game.show_menu()