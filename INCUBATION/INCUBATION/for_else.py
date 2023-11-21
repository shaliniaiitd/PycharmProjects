#else is executed after for loop is over.
# The else block will not execute if the for loop is stopped by a break statement.

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else', counter)
    counter = 0
    while counter < 3:
        # loop ends because of break
        # the else part is not executed
        if counter == 1:
            break

        print('Inside loop')
        counter = counter + 1
    else:
        print('Inside else')