data01 = [1,2,3,4,5]
data02 = [99, 98, 65, 45]
data03 = ['a', 'b','c','d','e']
print(f'''
Data 01 = {data01} adrress {hex(id(data01))}
Data 02 = {data02} adrress {hex(id(data02))}
Data 03 = {data03} adrress {hex(id(data03))}
''')

data_all = [data01,data02,data03]
print(f'Data combination = {data_all} adress {hex(id(data_all))}\n')

import copy 
data_copy = copy.deepcopy(data_all)
data01[0] = 0
print("Data Copy = \n", data_copy, "adress = \n", hex(id(data_copy)),"\n")
print("Data all = \n", data_all, "adress = \n", hex(id(data_all)))



