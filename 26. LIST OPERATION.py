number = [1,2,3,5,5,5,8,13,21,34,55]
print(f'numeric data: {number}')

#count data
count_4 = number.count(34)
count_5 = number.count(5)
print(f'''
Data count number 34: {count_4}
Data count number 5: {count_5}
''')

#mengambil posisi/indeks data
string = ['donut','pizza','beer','burger']
indeks = string.index('donut')
print(string)
print(f'Posisi data donut pada list adalah: {indeks}\n')

#mengurutkan list
data = [9,5,4,1,2,3,9,14,2,0,6,7,3]
print(f'Data unsorted: {data}')
data.sort()
print(f'Data sorted  : {data}')
#reverse list
data.reverse()
print(f'Reverse data : {data}')