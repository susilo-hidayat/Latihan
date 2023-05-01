#looping list for loop
number_list = [2,3,2,5,7,1]
print(f'''
Looping list menggunakan for loop
List angka = {number_list}
''')
for number in number_list:
    print(f'Data angka dari list = {number}')

daftar_nama = ["angga", "bahar", "sukarni"]
for nama in daftar_nama:
    print(f"Nama peserta = {nama}")

#while loop
number_list = [2,3,2,5,7,1]
print(f'''
\nLooping list menggunakan for while
List angka = {number_list}
''')
list_lenght = len(number_list)
i = 0
while i < list_lenght:
    print(f"Data angka = {number_list[i]}")
    i += 1

#list comprehension (cara lebih ringkas)
data_set = [2,3,"bahar",2,5,7,"angga",1]
print(f'''
\nList Comprehension
Dataset = {data_set}
''')
[print(f'Data = {i}') for i in data_set]

#enumerate
data_set = [2,3,"bahar",2,5,7,"angga",1]
print(f'''
\nEnumerate
Dataset = {data_set}
''')

for index,data in enumerate(data_set):
    print(f"Index = {index}, data = {data}")