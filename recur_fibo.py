import time
start_time = time.time()

def fibo(n):
    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return fibo(n-1) + fibo(n-2)


for i in range(1, 35):
    print(fibo(i))

end_time = time.time()
print("The total time of execution of the program is: ",
      end_time - start_time)
