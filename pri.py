num = int(input())
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime num")
            break
    else:
        print(num, "yes")

else:
    print(num,"no")
