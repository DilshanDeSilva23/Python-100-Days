
# while loop ( only condition true(with condition))

i = 0;
while(i<6):
    print("hello world")
    i = i+1

i = 1;
while(i<11):
    print(i)
    i = i+1  

i = 2;
while(i<11):
    print(i)
    i = i+2    

sum = 0
i = 1;
while(i<6):
    number = int(input("Enter number : "))
    sum = sum+number
    i=i+1
print("sum of numbers = ",sum)  



# for loop ( without conditions)

x = (1,2,3,4,5)
# print("s" in x)
print(5 in x)
for num in x:
    print(num)
    
x = {"name": "kamal",
     "age" : 40,
      "gender" : "male" }  
for i in x.keys(): # only get values like that (x.values)
    print(i)

for i,j in x.items():
    print(i,j) 

for i in range(6): # (default with 0) ( starting 1,6)
    print(i)       

for i in range(2,11,2): # ( default step size = 1)
    print(i)

print("------------------------")

# continue statement

for x in range(1,6):
    if(x==3):
        continue
    print(x)

# break statement

for x in (1,6):
    if(x==3):
        break
    print(x)




