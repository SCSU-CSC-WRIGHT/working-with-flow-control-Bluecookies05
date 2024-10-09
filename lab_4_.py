import random 

### ================ Lab 1 =================
random_number = int(input(" guess a number between 1-10:  "))

number = random.randbint (1-10)

attempts = 3
count = 1
max_number = 10

while count <= attempts:
    random_number = int(input(" guess a number between 1-10:  "))
if random_number>number:
    print ("too hight")
elif random_number<number:
    print ("too low")
else:
    print ("correct!!")

if attempts>3:
    print ("STOP! YOU ALREADY LOST")

### ================ Lab 1 =================

### ================ Lab 2 =================

countdown_number = int(input(" type in a number:  "))
while countdown_number!= 0:
    print (countdown_number)
    countdown_number-=1


### ================ Lab 2 =================

### ================ Lab 3 ================= 

user_number = int(input(" Be our guest and pick a number:  "))

total = 0
for i in range (1,user_number+1):
    total+=i
print(total)

### ================ Lab 3 =================