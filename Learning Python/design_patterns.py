#Singleton - allows only one instance of a class

class Singleton_eg():
    obj_count = 0
    def __init__(self):

        if Singleton_eg.obj_count == 0:
            Singleton_eg.obj_count += 1
        else:
            print("NO more instances allowed")

    def __del__(self):
        Singleton_eg.obj_count -= 1

