n1=int(input())
sum =0
temp = n1
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if n1 == sum:
   print("yes")
else:
   print("no")
