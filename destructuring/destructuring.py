def numbers():
    x = 6
    y = x * 2
    z = y + x
    return x, y, z

i = numbers()[0]
j = numbers()[1]
k = numbers()[2]
print('Numbers A ->', i, j, k)

a = numbers()
print('Numbers B ->', a)
print('Numbers C ->', a[0], a[1], a[2])

# Apply destructuring
[n, t, r] = numbers()
print('Numbers Destructuring ->', n, t, r)

ages = [17, 18, 19]
[_, age1, age2] = ages
print('Ages ->', age1, age2)
