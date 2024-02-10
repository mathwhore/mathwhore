x=float(input("Enter the no. of calories in your food"))
y=float(input("Enter the total quantity of fat in your food(in grams)"))
a=y*9
if x<0 or y<0 or a>x:
    print("Either the total calories or the quantity of fat were incorrectly entered")
elif a<(30/100)*x:
    print("Your food is low in fat")    
else:
    print("The percentage of calories from fat in your food is",(a/x)*100,"%")    
