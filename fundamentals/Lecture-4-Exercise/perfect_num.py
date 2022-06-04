n = int(input(""))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")