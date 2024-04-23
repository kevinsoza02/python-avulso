import requests
import os 

def estado(vida):
    structure = ""
    if vida == 4:
        structure = """
              O
            """
    elif vida == 3:
        structure = """
              O
            | 
            """
    elif vida == 2:
        structure = """
              O
            | H |
        """
    elif vida == 1:
        structure = """
              O
            | H |
             / 
        """
    elif vida == 0:
        structure = """
              O
            | H |
             / \\
        """
    return structure

def getitens(lista, chave):
    indexes = []
    eq = 0
    for i in lista:
        if i == chave:
            indexes.append(eq)
        eq += 1
    return indexes
        
        
class Forca:
    def __init__(self, word):
        self.word = word
        self.mask = ''.join(["_" for i in range(len(self.word))])
        self.tries = 5
        self.historic = []
        self.is_win = None

    def guess(self, atempt):
        if atempt == self.word:
            print(f" VOCÊ ACERTOU {self.word} !!! ")
        elif atempt in self.word:
            if atempt not in self.historic:
                indexes = getitens(self.word, atempt)
                mask = [i for i in self.mask]
                for i in indexes:
                    mask[i] = atempt
                
                self.mask = "".join(mask)
                self.historic.append(atempt)
                if "_" not in self.mask:
                    self.win()
            else:
                print("letra já foi tentada!!")
        else:
            self.erro()

    def erro(self):
        self.tries -= 1
        if self.tries == 0:
            self.gameover()
            
        
    def gameover(self):
        print("\nFim de jogo!!\n")
        print(f"Palavra correta: {self.word}")
        self.is_win = False 
        
    def win(self):
        print("\nVocê ganhou!!\n")
        self.is_win = True

if __name__ == "__main__":
    req = requests.get("https://api.dicionario-aberto.net/random")
    if req.status_code == 200:
        palavra = req.json()["word"]
        jogo = Forca(str(palavra))
        inicio = False
        while(True):
            os.system('cls')
            print(estado(jogo.tries))
            print(jogo.mask)
            if not inicio:
                print("Bem vindo ao jogo da forca!!")
                inicio = True
            letra = input("Entre com uma letra: ")
            jogo.guess(letra)
            if jogo.is_win != None:
                break
        
        