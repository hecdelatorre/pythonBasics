def hello(name = "Person"): # En caso de no recibir un parametro muestra Person por defecto
    print(f"Hello {name}") 

hello("Hec")
hello("Joe")
hello()

def add(n1, n2):
    return n1 + n2
print(add(1, 2))

multiply = lambda num1, num2: num1 * num2
print(multiply(5, 6))
