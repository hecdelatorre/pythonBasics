product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "fistName": "Ryan",
    "lastName": "ray"
}

print(type(product))
# print(dir(product))
print(product.keys())
print(product.items())

person.clear()
print(person)
del person

products = [
    {"name": "book", "price": 10.22},
    {"name": "pencil", "price": 100.22}
]

print(products)