#A Narcissistic Number is a positive number which is the sum of its own digits,
#each raised to the power of the number of digits in a given base.
# In this Kata, we will restrict ourselves to decimal (base 10).
number=int(input("Enter a number: "))

basamak=len(str(number))

sum=0
num=list(str(number))
for i in num:
    sum=int(i)**basamak +sum
if number==sum:
    print("{} narcissistics are  number. ".format(number))
else:
    print("{} narcissistics are not number".format(number))
    
