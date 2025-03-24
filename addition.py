class Addition:
    def add(self, a, b):
        return a+b
    
    def add(self, *args):
        s=0
        for i in args:
            s+=i
        return s

