# 1. WAF: bmi() that takes the weight in kg and height in cm of a person, calculates and returns the
# BMI.
# Write code that calls this function after taking height and weight as inputs and then prints
# underweight, normal, overweight or obese depending on the value of BMI.
# Refer this link for the ranges:
# https://en.wikipedia.org/wiki/Body_mass_index

#BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg / m2,
#resulting from mass in kilograms and height in metres.
#underweight (under 18.5 kg/m2), normal weight (18.5 to 24.9), overweight (25 to 29.9), and obese (30 or more)
def bmi(wt,htcm):
    htm = htcm/100
    bmi = wt/(htm*htm)

    if bmi <= 18.5:
        return "underweight"
    elif 18.5 < bmi <= 24.9:
        return "normal weight"
    elif 25 < bmi < 29.9:
        return "overweight"
    else:
        return "obese"

print(bmi(60,154))


# 2. Take input of age of 3 people by user and determine oldest and youngest among them.
# ages = input("please enter 3 ages , seperated by space")
# ages = ages.split()
# #ages.sort()
# #print(f"eldest is {ages[2]} years, youngest is {ages[0]} years")
#
# #without using sort
#
# for i in range(len(ages)-1):
#     if ages[i]>ages[i+1]:
#         ages[i],ages[i+1] = ages[i+1],ages[i]
#
# print(f"eldest is {ages[2]} years, youngest is {ages[0]} years")
# 3. WAP to input a number and check if number is divisible by both 5 and 7.
#num = int(input("input a number"))
num = 35
if  (num%5 | num%7):
    print(f"number {num} is not divisile by both 5 and 7")
else:
    print(f"number {num} is divisile by both 5 and 7")

# 4. WAF: is_alphabet() that takes a string argument and returns True or False. True if all characters
# in the string are alphabets otherwise False. (write code using for loop and if. Do not use built in
# functions)
def is_alphabet(strg):

    for el in strg:
        if not 'a' <= el <='z' and not 'A' <= el <= 'Z':
            return False
    else:
            return True

print(is_alphabet("Sh3lini"))
print(is_alphabet("shal1ni"))
print(is_alphabet('1234'))
print(is_alphabet('exactly'))

# 5. WAF: is_leap_year() that takes a year as input and retuns True if year is leap year, otherwise false.
def is_leap_year(year):
    #divisible by 4 but not by 100 is leap year
     if not year%4 and year%100:
        return True
     else:
        return False
print(is_leap_year(1600))

# 6. WAF: days_in_month() that take name of month in 3 character format(MMM), and year (YYYY)
# as arguments and returns the number of days in the month.
# Use the function is_leap_year() to check the special case of 29 days in leap year for month of
# FEB. [Use dictionary to store the mapping of month and days.]
# 7. Update the above program to work with both 3 character month and complete name of month.
def days_in_month(month,year):
    month = month[:3]
    print(month)
    days = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
    if (is_leap_year(year)) and month == 'Feb':
        return 29
    else:
        return days[month]

print(days_in_month('Dec',1664))

# 8. WAF: uncommon_words() that takes two sentences (strings) as its arguments, and returns the
# common words in both the sentences.
# [Hint: store all the in a set. Read the documentation for set.]

def common_words(str1,str2):
    common_list = list(filter(lambda el: el in str2,str1))
    result = ''.join(common_list)
    return result

print(common_words("This is a book","This is a magzine"))

def uncommon_words(str1,str2):
    uncommon_list = list(filter(lambda el: el not in str2,str1))  + list(filter(lambda el: el not in str1,str2))
    return ''.join(uncommon_list)

print(uncommon_words("This is a book","This is a magzine"))

#using sets
def uncommon_words(str1,str2):
    set1 = set(str1)
    set2 = set(str2)
    uncommon_words = set1^set2
    return uncommon_words

print(uncommon_words("This is a book", "This is a magazine"))

def common_words(str1,str2):
    set1 = set(str1)
    set2 = set(str2)
    common_words = set1&set2
    return common_words

print(common_words("This is a book", "This is a magazine"))