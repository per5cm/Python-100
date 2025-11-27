# TypeError
# len(12345)

# Type checking - How do we know what data type is?
print(type("Hello"))
print(type(12345))
print(type(123.45))
print(type(True))

# Type conversion - int("abc") wont work though
print(int("123") + int("456"))

int()
float()
str()
bool()

# you can concatenate str not int
name_of_the_user = input("Enter your name: ")
lenght_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(lenght_of_name)) #int

print("Number of letters in your name: " + str(lenght_of_name))