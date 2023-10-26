#sum of elements
list=[2,10,12,15,25,27]
total=0
for i in range(len(list)) :
	total = total +  i
print("Sum : ", total)

# list is empty

lis1 = []
if lis1!=[]:
	print("The list is not empty")
else:
	print("Empty List")

 #average

def Average(lst): 
	return sum(lst) / len(lst) 

lst = [15, 9, 55, 41, 35, 20, 62, 49] 
average = Average(lst) 

print("Average of the list =", round(average, 2)) 

# duplicate

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)