class CodeCesar: 
    def __init__(self, cle):
        self.cle = cle 
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

    def decale(self, lettre):
        num1 = self.alphabet.find(lettre)
        num2 = num1 + self.cle 
        if num2 >= 26: 
            num2 = num2-26
        if num2 < 0: 
            num2 = num2+26
        nouvelle_lettre = self.alphabet[num2] 
        return nouvelle_lettre 

    def cryptage(self, message):
        message_crypte = "" 
        for lettre in message: 
            message_crypte += self.decale(lettre) 
        return message_crypte
    
    def decryptage(self, message): 
        self.cle = -self.cle 
        message = self.cryptage(message)
        self.cle = -self.cle 
        return message
     

code1 = CodeCesar(3) 
print(code1.decale("A")) 
print(code1.decale("X"))
print(code1.cryptage("NSI"))
print(code1.decryptage("PSX"))
print(CodeCesar(10).cryptage("PSX"))