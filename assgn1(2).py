def cfmch(a,b,c):
    periods_w=[15,15,20,2,4,20]
    periods_b=[20,20,25,15,25]
    instruct=["Add water","Add sugar","Mix well","Add coffee","Add milk","Mix well again"]
    if "yes" in c:
         if "w" in a:
             if "yes" in b: 
               for i in range(len(instruct)):
                print(instruct[i],"for",periods_w[i]*1.5,"mins. Press enter to proceed")
             else:
              for i in range(len(instruct)):
               print(instruct[i],"for",periods_w[i],"mins. Press enter to proceed") 
         elif "b" in a:
            instruct.pop(4)
            if "yes" in b:  
               for i in range(len(instruct)):
                print(instruct[i],"for",periods_b[i]*1.5,"mins. Press enter to proceed")
            else:
             for i in range(len(instruct)):
                print(instruct[i],"for",periods_b[i],"mins. Press enter to proceed")

    else:
       if "yes" in b:
          print("Your coffee will be ready in 10 minutes")
       else:
          print("Your coffee will be ready in 5 minutes") 

c_type=input("What type of coffee do you want? (Type B for Black and W for White)")
c_size=input("Do you want the cup size to be double?(yes/no)")
c_med=input("Do you want the coffee to be prepared manually?(yes/no)")
cfmch(c_type.casefold(),c_size.casefold(),c_med.casefold())
# def instrct():
#    input("Add water (15 mins). Press enter to proceed")
#    input("Add sugar (15 mins). Press enter to proceed")
#    input("Mix well (20 mins). Press enter to proceed")
#    input("Add coffee (2 mins). Press enter to proceed")
#    input("Add milk(4 mins). Press enter to proceed")
#    input("Mix well again (20 mins). Press enter to proceed")
#    input("Your coffee is ready!. Press enter to proceed")
# def instruct():
#    input("Add water (20 mins). Press enter to proceed")
#    input("Add sugar (20 mins). Press enter to proceed")
#    input("Mix well (25 mins). Press enter to proceed")
#    input("Add coffee (15 mins). Press enter to proceed")
#    input("Mix well again (25 mins). Press enter to proceed")
#    input("Your coffee is ready!. Press enter to proceed")
        
# def c_prep(a,b,c):
#     if "yes" in c:
#      if "w" in a:
#         bak_time=76
#         if "yes" in b:
#          bak_time+=(bak_time*0.5)
#          print("The estimated time for your coffee is",bak_time,"mins")
#          print(instrct())
#         else:
#          print("The estimated time for your coffee is",bak_time,"mins")
#          print(instrct())
         
#      if "b" in a:
#         bak_time=105
#         if "yes" in b:
#          bak_time+=(bak_time*0.5)
#          print("The estimated time for your coffee is",bak_time,"mins")
#          print(instruct()) 
#         else:
#          print("The estimated time for your coffee is",bak_time,"mins")
#          print(instruct())            
#     else:
#         b_time=3
#         if "yes" in b:
#          b_time+=(b_time*0.5)
#          print("Your coffee will be ready in",b_time,"minutes")
#         else:
#          print("Your coffee will be ready in",b_time,"minutes") 
