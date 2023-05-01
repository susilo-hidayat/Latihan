#LIST dasar
number = [1,2,3,4]
string = ['donut','pizza','beer','burger']
mix_number_string = [1,'donut', 2,'pizza', 3,'beer', 4,'burger']
print(f'''
Data list angka  = {number}
Data list string = {string}
Data Campuran    = {mix_number_string}
''')

#Cara Membuat list advance
list_range = list(range(0,10)) #data range dari 0 sebelum 10
list_range2 = list(range(0,10,2)) #dari 0, jarak 2, sebelum 10 (start, stop, step)
list_for_loop = list(i for i in range(0,10))
list_for_loop2 = list(i**2 for i in range(0,10))
list_for_if = list(i for i in range(0,10) if i != 6) #Exclude 6
list_for_if2 = list(i for i in range(0,10) if i%2 == 1) #List ganjil
list_for_if3 = list(i for i in range(0,10) if i%2 != 1) #List Genap
print(f'''
Data List range (0-10)         = {list_range}
Data list range (0,2,10)       = {list_range2}
Data list dari for loop normal (0,10) = {list_for_loop}
Data list dari for loop kuadrat (0,10) = {list_for_loop2}
Data list fo loop if exclude 6  = {list_for_if}
Data list fo loop if ganjil = {list_for_if2}
Data list fo loop if genap = {list_for_if3}
''')