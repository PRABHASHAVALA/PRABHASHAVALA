import math
x=float(input("enter the value"))
n=int(input("enter no.of terms"))
cosine_sum = 0
for n in range(n):
    term = ((-1)**n)*(x**(2*n))/math.factorial(2*n)
    cosine_sum+=term
print(f"the cosine sum of {n} terms of {x} are {cosine_sum}")
