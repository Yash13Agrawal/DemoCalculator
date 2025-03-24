class Addition:
    def add(self, a, b):
        return a+b
    
    def add(self, *args):
        s=0
        for i in args:
            s+=i
        return s

a1 = Addition()
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

print(a1.add(n1, n2))