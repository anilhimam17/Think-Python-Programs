import time

start_time = time.time()
known = {0:0, 1:1}

def fibo(n):

    if n in known:
        return known[n]

    else:
        res = fibo(n - 1) + fibo(n - 2)
        known[n] = res
        return res

for i in range(1, 35):
    print(fibo(i))
    print(known.items())


end_time = time.time()
print("The total time of execution of the program was: ",
      end_time - start_time)
