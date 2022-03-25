num=int(input("Enter a number: "))
if num%2==0:
    print("The number entered is even")
    if num%4==0:
        print("The number entered is a multiple of 4.")
else:
    print("The number entered is odd")
    
#iki sayı iste ve bunların tam bölümüyor mu kontırk et?

check=int(input("Again Enter a number: "))

if num%check==0:
    print(f'{check} divides evenly into {num} and the quotient is {num/check}')
else:
    print(f'{check} does not divide evenly into {num}')