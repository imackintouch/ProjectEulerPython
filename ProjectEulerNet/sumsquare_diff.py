import sys

# Euler Problem link https://projecteuler.net/problem=6
def sum_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i*i
        print("i:", i, "square:", i * i, " running sum:", sum)
    return sum

def square_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
        print("i:", i, "running sum:", sum)
    print("Square of sum is:", sum*sum)
    return sum*sum

#
# default main input of square functions to 10 if no arguments
#

if len(sys.argv)<2:
    n=5
else:
    print(sys.argv[1])
    n=int(sys.argv[1])


print("Square Sum Difference of %d is: %d" % (n, square_sum(n)-sum_squares(n)))


