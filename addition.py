# class Addition:
#     def add(self, a, b):
#         return a+b
    
#     def add(self, *args):
#         s=0
#         for i in args:
#             s+=i
#         return s

# a1 = Addition()
# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter a number: "))

# print(a1.add(n1, n2))


def add(a, b):
    if type(a) == int and type(b)==int:
        return a+b
    if type(a) == str and type(b) == str:
        return a+b
    
print(add(1,2))
print(add("Sneha", "Aneja"))    

