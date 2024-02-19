a = int(input("enter your age"))
print("your age is:", a)
# conditional operations 
# >, <, >=, ==, !=

print(a>18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("you can drive")
else:
    print("you cannot drive")  
    
# if else program    
    
b = int(input("enter your age"))
print("your age is:",b)

if (b>24):
    print("you are eligibile for this")
else:
    print("you are not eligibile for this")    



# if-else-elif program

appleprice = int(input("enter your apple price"))
budget = 300
if (appleprice<=budget):
    print("Vijay, add 2 kg apples to your cart.")
elif (budget - appleprice > 70):
    print("its okay you can buy")
else:
    print("Vijay,do not add 2 kg apples to your cart.")   
    
    
# elif program 

num = int(input("enter the value"))
if (num < 0):
    print("number is negative.")
elif (num == 0):
    print("number is zero.")
else:
    print("number is positive.")        
