# prime number

num=int(input("enter a number"))
count =0
if num > 1:
    if (num%1)==0:
        count=count+1
    if count==2:
        print("this is prime number")
    else:
        print("this is not prime number")
else:
    print("this is invalid")

# list

vegetables=("onion","brinjal","carrot","tapioca")
print(len(vegetables))
fruits=list(vegetables)
print(fruits)
print(fruits.append("banana"))
vegetables = tuple(fruits)
print(vegetables)

# 
num1=input("enter a num1")
num2=input("enter a num2")

num1,num2=num2,num1
print("value of num1 after swapping",num1)
print("value of num2 after swapping",num2)


