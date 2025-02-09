int_variable = 90
float_variable = 9.999
string_variable = "Partha Saradhi"
char_variable = 'a'
bool_variable = True
print(int_variable,float_variable,string_variable,char_variable,bool_variable)
print(type(char_variable),type(string_variable))

# list 
list_variable = ["partha saradhi","munakala","deepak","sreenivasulu"]

list_varable2 = ["string",1,False,4.567]

print(list_variable[2])
print(list_variable)

# dictonaries

dictioinary_variable = {
    "name" : "Partha Saradhi",
    "age" : 20,
    "gender" : "Male",
    "married" : False,
    "languages"  : ["Telugu","Hindi","English"]
}

print(dictioinary_variable["name"])
dictioinary_variable["languages"].append("German")
print(dictioinary_variable.keys())
print(dictioinary_variable.values())
print(dictioinary_variable)

# conditionals

age = int(input("What is your age"))

if age<18 : 
    print("You are a minor")
elif age>=18 and age<60:
    print("You are major")
else : 
    print("You are a senior citizen")

# for loop

for i in list_variable:
    print(i)

# for index,_ in enumerate(range(10)):
#     print(index)

# while loop

iterator = 0
while iterator<10:
    if iterator==4 : break
    print(iterator)
    iterator+=1

# Pythonic way of generating lists

square_and_cubes = [i*i if i%2==0 else i*i*i for i in range(5)]

print(square_and_cubes)


only_even = [num for num in range(20) if num%2==0]

print(only_even)

name = input("Please enter your name : \n")

if name:
    print("Your name is ",name)
else:
    print("You didn't enter a name")