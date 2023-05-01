# Cara kerja While loop sama dengan For Loop hanya saja, pada while memungkinkan adanya kondisi tertentu
# yang mempengaruhi operasi

#bentuk loop while:
# while kondisi:
#   aksi 1
#   aksi 2
# End of program

#while
value = 0
print(f"Value = {value}")
while value <= 5:
    #aksi 1
    value += 1
    #aksi 2
    print(f"Value now = {value}")
    print("Value added")

print("End of Program\n")

#while
value = 5
print(f"Value = {value}")
while value > 4 and value < 10: #range while condition
    #aksi 1
    value += 1
    #aksi 2
    print(f"Value now = {value}")
    print("Value added")

print("End of Program\n")
