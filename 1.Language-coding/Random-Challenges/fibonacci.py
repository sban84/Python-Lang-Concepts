

def fibo(n1,n2):
    while(n < 5):
        if (n1 == 0) & (n2 ==1):
            return 1
        else:
            sum = n1+n2
            print(sum, sep=",")
            n1 = n2
            n2 = sum
            return fibo(sum,n2)
        n -=1


fibo(1,1)
# for i in range(1,5):
#     fibo(0,i)