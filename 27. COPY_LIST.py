a = [3,4,7,11,18]
print(a)
b = a
print(b)

a[0] = 2
print(f'Data list a: {a}, \nData list b: {b}')

#andress
print(f'''
Adress list a: {hex(id(a))}
Adress list b: {hex(id(b))}
''')

#Duplikasi list dengan method .copy
c = a.copy()
print(f'Data list c hasil copy: {c}')

#andress untuk prove copy beda adress
print(f'''
Adress list a: {hex(id(a))}
Adress list b: {hex(id(b))}
Adress list c: {hex(id(c))}
''')

c[0] = 0
print(f'''
Data list a: {a} adress: {hex(id(a))} <- data awal
Data list b: {b} adress: {hex(id(b))} <- murni clone/duplikat
Data list c: {c} adress: {hex(id(c))} <- copy, dan bisa diubah salah
''')