for i in range(21):
    print(i)

for i in range(1, 11, 1):
    print(i)

for i in range(1, 101, 2):
    print(i)

for i in range(0, 101, 2):
    print(i)

i = int(input())

for i in range(1, i + 1, 1):
    print(i)

for i in range(0, 51, 5):
    print(i)

i = 1
while(i < 21):
    print(i)
    i = i + 1

i = 1
sum = 0

while(i < 11):
    sum = sum + i
    i = i + 1
print(sum)

num = 7
guess = int(input())
while(num != guess):
    guess = int(input())
print("acces granted")

password = "password123"
guess = input()
while(guess != password):
    guess = input()
print("acces granted")

print("What time is it?")
time = int(input())
if(time < 12):
    print("good morning")
else:
    print("good afternood")

number = int(input())
if(number // 2):
    print("even")
else:
    print("odd")

print("What is the temperature?")
temp = int(input())
if(temp > 30 ):
    print("its too hot!")
else:
    print("not too hot!")

print("How old are you?")
age = int(input())
if(age >= 13 and age <= 19):
    print("you are teenager")
else:
    print("you are not a teenager")


