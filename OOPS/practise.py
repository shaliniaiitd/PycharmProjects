import re

st = "5shalini"

pattern = re.compile(r'$\c')

result = pattern.match(st)

print(result)


# class Test:
#     def method_one(self):
#         print ("Called method_one")
#     @staticmethod
#     def method_two():
#         print ("Called method_two")
#     @staticmethod
#     def method_three():
#         Test.method_two()
# class T2(Test):
#     @staticmethod
#     def method_two():
#         print ("T2")
# a_test = Test()
# a_test.method_one()
# a_test.method_two()
# a_test.method_three()
# b_test = T2()
# b_test.method_three()