def add(a, b):
    if type(a) == int and type(b)==int:
        return a+b
    if type(a) == str and type(b) == str:
        return str+str
    
print(add(1,2))
print(add("Sneha", "Aneja"))  
