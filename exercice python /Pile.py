class Pile: 
    def __init__(self):
        self.l = []

    def est_vide(self):
        return len(self.l) == 0 
    
    def empile(self, val):
        self.l.append(val)

    def depile(self):
        if not self.est_vide():
            return self.l.pop()
        else:
            return None 
        
    def len(self):
        return len(self.l)
    
