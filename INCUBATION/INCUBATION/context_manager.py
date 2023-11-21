#Provide automatic setup and teardown for resouces like files and database connections
# or objects like class/function
# 'with' is the KEYWORD that does this, as shown below

#For class level context management, class needs to implement the methods
# __enter__(setup) and __exit__ (teardown)
class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)

#Output : True

#2. for DB connection mgmt

from pymongo import MongoClient


class MongoDBConnectionManager():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


# connecting with a localhost
with MongoDBConnectionManager('localhost', '27017') as mongo:
    collection = mongo.connection.SampleDb.test
    data = collection.find({'_id': 1})
    print(data.get('name'))

#Using @contextmanager

from contextlib import contextmanager

@contextmanager
def MyContextManager():
    print("This is treated as __enter__")
    yield
    print("This is treated as __exit__")

