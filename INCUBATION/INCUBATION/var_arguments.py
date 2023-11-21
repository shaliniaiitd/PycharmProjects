def myFun(*args,**kwargs):
    for arg in args:
        print("arg:", arg)

    for key, value in kwargs.items():
        print("%s : %s" % (key, value))


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ()
print(type(args))
myFun("my", "name is Shalini",100)

kwargs = {"arg1": "Shalini", "arg2": "", "arg3": "Agarwal"}
myFun(**kwargs)