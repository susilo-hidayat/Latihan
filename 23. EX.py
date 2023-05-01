sisi = 13

#FOR
count = 1
for i in range(sisi):
   
    print("*"*count)
    count += 1

print("End of For Loop")
    
#WHILE
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break

#WHILE
count = 1
while True:
    if (count%2):
     print(" "*((sisi-count)//2), "*"*count)
    count += 1
    if count > sisi:
        break

count = 1
while True:
    if (count%2):
     print(" "*((sisi-count)//2), "*"*count)
    count += 1
    if count > sisi:
        break

count = count-2
while True:
    if (count%2):
        print(" "*((sisi-count)//2), "*"*count)
    count -= 1
    if count < 0:
        break