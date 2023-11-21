class MyClass:
    var1 = 1
    _var2 = 2
    __var3 = 3

obj = MyClass()

print(obj._var2)
#print(obj.__var3) #AttributeError: 'MyClass' object has no attribute '__var3'. Did you mean: '_var2'?
print(obj._MyClass__var3)

class SubClass(MyClass):
    pass

sub_obj = SubClass()
print("SUB")
print(sub_obj.var1)
print(sub_obj._var2)
print(sub_obj._MyClass__var3)