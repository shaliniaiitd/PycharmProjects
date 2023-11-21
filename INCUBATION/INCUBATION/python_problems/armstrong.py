num = 1153
sum = 0
for digit in str(num):
    sum += int(digit)**len(str(num))

if sum == num:
    print(f"{num} is ARMSTRONG")
else:
    print(f"{num} is not ARMSTRONG")