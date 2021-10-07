phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#Alternatively
phonebook2 = {
        "John" : 938477566,
        "Jack" : 938377264,
        "Jill" : 947662781
}
print(phonebook)

#iterating over dictionaries
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
#Removing a value
del phonebook["John"]
print(phonebook)

phonebook2.pop("John")
print(phonebook2)
