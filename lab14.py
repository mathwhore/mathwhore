# nos1=[3,4,0,1,2,0]
# nos2=[4,0,6,3,10,8]

# for i in range(7):
#  for j in range(len(nos2)):
#     try:
#         x=nos1[i]/nos2[j]
#         print(nos1[i],'divided by',nos2[j],'=',x)
#     except EOFError as e:
#        print(e,'unexpected!')
#     except ArithmeticError as e:
#      print(e,'!')
#     except IndexError as e:
#          print(e,'!')
# try:  
#    num1=int(input('Enter a no'))
#    num2=int(input('Enter a no'))
#      ask=input('Enter your name')
#    print('The ratio of the no.s is',num1/num2)
# except IndentationError:
#    print('Unexpected indent')
# finally:
#    print('Done.')
# try:
#  import math
#   math.sqrt()
# except IndentationError:
#    print('!!!')
try:
   fname=input('Enter filename: ')
   f=open(fname,'r')
   fileinfo=f.read()
   print(fileinfo)
except IOError:
   print('No such file found!')
