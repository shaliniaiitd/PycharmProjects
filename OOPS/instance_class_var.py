class MyClass:
    class_var = 2

obj1 = MyClass()

print(obj1.class_var)
print(MyClass.class_var)

obj2 = MyClass()

MyClass.class_var = 3
print(obj2.class_var)

print(obj1.class_var)
print(MyClass.class_var)