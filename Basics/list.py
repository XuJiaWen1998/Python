mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

#prints out 1, 2, 3
for x in mylist:
    print(x)

#Accessing an index which does not exist generates an exception (an error)
#mylist = [1, 2, 3] 
#print(mylist[10])

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

#write your code here
second_name = []
numbers.append(1);
numbers.append(2);
numbers.append(3);
strings.append('hello');
strings.append('world');
second_name = names

# this code should write out the filled arrays and the second name in the names list
print(numbers)
print(strings)
print("The second name on the names list is %s" %second_name)
