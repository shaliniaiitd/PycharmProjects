#Property decorator substitutes use of build in property() function.
# So lets see what property() function does.
# arg1 : getter function
# arg2: setter function
# arg3: deleter function
#arg4: doc string
# returns: an object of type property

class Learning():
    def __init__(self,var1):
        self.var1 = var1

    #getter function

    def get_var1(self):
        return self.var1

    #Setter

    def set_var1(self,val):
        self.var1 = val

    #deleter
    def del_var1(self):
        del(self.var1)

    obj1 = property(get_var1,set_var1,del_var1, "This is doc string for var1")
    print(obj1.__doc__)
    help(obj1)

    @property
    def func(self,x):
        print(x)
    # makes function func a property of the class, so we can write Learning.func instead of Learning.func()

    #To complete, we need setter for this property func

    @func.setter
    def func(self,x):
        self.x = x

    @func.deleter
    def func(self):
        self.x = None