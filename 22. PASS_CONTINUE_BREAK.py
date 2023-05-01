#Pass digunakan untuk membuat code menjadi dummy atau tidak dioperasikan
value = 5
while value > 4 and value < 10:
    value += 1
    if value == 7:
        pass #tanpa pass akan eror
    print(f"{value}")


#Continue
value = 5
print(f"\nValue first = {value}")
while value > 4 and value < 10: #range while condition
    #aksi 1
    value += 1
    #aksi 2
    print(f"Value now = {value}")
    if value == 7:
        print("Its Seven")
        continue #Melompat ke awal loop, bukan lanjut ke print value added

    print("Value added")

print("End of Program\n")

#Break
value = 5
print(f"Value first = {value}")
while value > 4: 
    #aksi 1
    value += 1
    #aksi 2
    print(f"Value now = {value}")
    if value == 99:
        print("We found your Nine Nine")
        break #Melompat ke akhir loop, karena sudah menemukan value yang dicari

    print("Value added")

print("End of Program\n")