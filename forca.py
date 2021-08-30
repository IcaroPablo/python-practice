import os
import random

class hangman_game():
    def __init__(self):
        self.words_list = ["carro", "cavalo", "navio", "casa", "livro", "morango"]
        self.word = self.words_list[random.randint(0, len(self.words_list) - 1)]
        self.history = []
        self.life = 6
        self.pos = []
        self.printed_word = []
        self.game_status = "ongoing"
    
    def set_game_up(self):
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
                
        print("\n" + " ".join(self.printed_word))

    def show_history(self):
        if self.history != []:
            print("\nletras já digitadas:")
            print(",".join(self.history))

    def check_letter(self):
        if self.game_status == "ongoing":
            letter = str(input("\ndigite uma letra:\n>"))

            if len(letter) == 1:  # é uma única letra ?  
                if letter not in self.history:  # está no histórico ?
                    self.history.append(letter)
                    if letter in self.word:  # está na palavra ?
                        for i in range(len(self.word)):
                            if self.word[i] == letter:
                                self.pos.append(i)
                    else:
                        self.life -= 1
                    
    def check_status(self):
        if self.life == 0:
            print("\nvocê perdeu :(")
            self.game_status = "finished"
            pause = input("\ndigite qualquer tecla para continuar...")
        if len(self.pos) == len(self.word):
            print("\nvocê venceu :D")
            self.game_status = "finished"
            pause = input("\ndigite qualquer tecla para continuar...")
    
    def start_game_loop(self):
        while self.game_status != "finished":
            os.system("clear")
            # mostrar bonequinho
            self.show_doll()
            # mostrar palavra
            self.show_word()
            # mostrar histórico
            self.show_history()
            # verificar condição de vitória
            self.check_status()
            # verificar letra
            self.check_letter()            
    
    def show_menu(self):
        # resetar o jogo
        self.__init__()

        os.system("clear")
        print("###---JOGO DA FORCA---###")
        print("\n1 - iniciar jogo")
        print("\n2 - inserir nova palavra")
        option = input("\nescolha um numero:\n>")
        
        if option == "1":
            self.set_game_up()
            self.start_game_loop()
        if option == "2": 
            os.system("clear")
            new_word = input("digite uma palavra:\n>")
            self.word = new_word
            self.set_game_up()
            self.start_game_loop()
            
game = hangman_game()
while True:
    game.show_menu()
