# c = open('chanchito.txt', 'a') # append
c = open('chanchito.txt', 'w') # write

# print(c.read())
# print(c.readline())
# print(c.readline())
# print(c.readline())

# for x in c:
#     print(x)
 
c.write('\nNueva linea al archivo\n')
c.close()

x = open('chanchito.txt')
print(x.read())

