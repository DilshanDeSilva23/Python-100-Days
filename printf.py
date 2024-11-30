
# \n - new line character
# \r - carriage return
# \t - tab space
# \b - backspace

print("hello\nworld")
print("hello\rworld")
print("hello\tworld")
print("hello\bworld")

name = "kamal"
age = 22
score = 67.85

print(name,end='\n')
print(age,end='\n')
print(score,end='\n')

print(name,age,score,sep='-')


# formatted printing

name,age,score = "kamal",24,75

# he is kamal.he is 24 years old,and his score is 75
print("he is "+name+ ".he is " +str(age)+ " years old, and his score is " +str(score))

name,age,marks = "dilshan",24,75.5
# he is dilshan. he is 24 years old,and his score is 75.5

print("he is " +name+ " he is " +str(age)+ " old year,and his score is "+str(marks))
print("he is %s.he is %d years old,and his marks is %.1f" %(name,age,marks))
print("He is {}.he is {} years old,and his marks is {}".format(name,age,marks))
print(f"He is {name}.he is {age} years old,and his marks is {marks}")