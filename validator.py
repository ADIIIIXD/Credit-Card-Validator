sum_even = 0
sum_digits = 0
total = 0

cardnum = input("Enter Your Card Number: ")
cardnum = cardnum.replace("-", "")
cardnum = cardnum.replace(" ", "")

cardnum = cardnum[::-1]

for x in cardnum[::2]:
    sum_even += int(x)

for x in cardnum[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_digits += (1 + (x % 10))
    else:
        sum_digits += x

total = sum_even + sum_digits
if total % 10 == 0:
    print("This Card is Valid")
else:
    print("This Card is Invalid")






