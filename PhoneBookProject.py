path = "Web devlopment"
if path == "Web devlopment" :
    print("Javascript")

elif path == "IOS" :
    print("Swift")

elif path == "Anderoid" :
    print("Kotlin")

i = 0
while i <= 6 :
    print(i)
    i += 1

student = ["shatha" , "sana" , "alaa" , "abdullah"]
for s in student :
    print(s)

for num in range(10):
    print(num)


def greet():
    name = input("please enter your name:")
    time = input("please inter the time of the day :")
    print("Good " + time + "," + name + "!")
greet()

def add(first_number , secound_number):
    result = first_number * secound_number
    return result

value = add(2,7)
print(value)

