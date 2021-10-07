class MyClass:
    variable = "blah"
    
    def function(self):
        print("This is a message inside the class")

myobjectx = MyClass()
myobjecty = MyClass()

print(myobjectx.variable)
myobjecty.variable = "yackity"

print(myobjecty.variable)

myobjectx.function()

