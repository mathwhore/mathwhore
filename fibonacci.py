def fib(size):
    cons=[1,1]
    previous=1
    curr=1
    while curr<size:
     previous,curr=curr,previous+curr    
     cons.append(curr)
    return cons        
x=int(input("Enter limit of fibonacci sequence"))    
print("The Fibonacci sequence of length",x,"is",fib(x))
# def fib(x):
#     cons=[1,1]
#     if x==1:
#      return cons.pop()
#     elif x==2:
#        return cons
#     else:
#        for i in range(x-2):
#         cons.append(cons[i]+cons[i+1])
#     return cons    
# x=int(input("Enter length of fibonacci sequence"))    
# print("The Fibonacci sequence of length",x,"is",fib(x))