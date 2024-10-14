import random 

### ================ Lab 1 =================
number = random.randint(1, 10)  

attempts = 3  
count = 1  

while count <= attempts:
    random_number = int(input("Guess a number between 1-10: "))
    
    if random_number > number:
        print("Too high")
    elif random_number < number:
        print("Too low")
    else:
        print("Correct!")
        break  
    
    count += 1  # Increment the attempt count
    
if count > attempts:  
    print("STOP! YOU ALREADY LOST. The correct number was:", number)

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