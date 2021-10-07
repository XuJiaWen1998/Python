astring = "Hello world!"
astring2 = 'Hello world!'

print("single quotes are ' ")
print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[3:7:2]) #[start:stop:step]
print(astring[::-1]) #reverse a string
print(astring.upper())
print(astring.lower())
print(astring.startswith("hello"))
print(astring.endswith("asdfasdfasdf"))
afewwords = astring.split(" ")
