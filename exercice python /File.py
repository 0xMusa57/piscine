class File:

    def __init__(self):
        self.l = []

    def est_vide(self):
        return len(self.l) == 0 
    
    def enfile(self, val):
        self.l.append(val)

    def defile(self, val):
        if not self.est_vide():
            return self.l.pop(0)
        else:
            return None
        