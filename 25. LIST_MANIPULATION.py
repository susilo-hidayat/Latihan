data = ['donut','pizza','beer','burger']
print(f'Data awal = {data}')
print("\n")

#data indexes
data = data[0]
print(f'Data indeks nomor ke 0 dari list: \n{data}')
print("\n")

#data akhir
data = ['donut','pizza','beer','burger']
data = data[-1]
print(f'Data paling akhir: \n{data}')
print("\n")

#Menambah data di akhir
data = ['donut','pizza','beer','burger']
data.append('taco')
print(f'Menambhakna data di bagian akhir: \n{data}')
print("\n")

#Slice data
data = data[0:2]
print(f'Melakukan slice data 0 ke 1: \n{data}')
print("\n")

#Info jumlah data
data = ['donut','pizza','beer','burger']
print(f'Data awal: {data}')
pnajang_data = len(data)
print(f'Panjang data dalam list: {pnajang_data}')
data.insert(0,"bakso")
print(f'Insert data Bakso dengan indeks 0 ke list: \n{data}')
print("\n")

#Manipulasi data list
#Menambah berdasarkan posisi
data = ['donut','pizza','beer','burger']
print(f'Data awal: {data}')
#data.insert(posisi,item)
data.insert(0, 'Bagel')
print(f'Insert bagel dengan indeks 0 ke list: {data}')
#menambah di akhir
#data.append(item)
data.append('rendang')
print(f'Menambahkan rendang ke bagian akhir list: \n{data}')
print("\n")

#menambah data baru
print(f'Data awal:\n{data}')
new_data = ['sushi', 'loumie','laksa']
print(f'Data baru: {new_data}')
data.extend(new_data)
print(f'Menambahkan data awal dengan data baru: \n{data}')
print("\n")

#mengubak data
data[0] = "gudeg"
print(f'Mengubah data ke 0 di list menjadi gudeg: \n{data}')
print("\n")
#remove
data.remove("burger")
print(f'Menghapus data burger dari list: \n{data}')

#remove data paling belakang
data.pop()
print(f'Menghapus data paling belakang dalam list: \n{data}')