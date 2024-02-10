def interest(a):
    from math import log
    t=log(2)/log(1+a)
    return round(t)
interest_rate=float(input("Enter the interest rate(per year)"))
print("The amount of time it will take for the principal investment to double is",interest(interest_rate),"years")
