# friends={'Adil',"Yaafay",'Haider','Kaif','Muzammil',"Hunain","Abdullah"}
# print(friends)
# for i in range(2):
#     frnd_lft=input("Enter the name of the friend who has left NED: ")
#     friends.remove(frnd_lft)
# print("The names of my friends are:\n",friends)    
# fvrt_dishes=set()
# no=int(input("How many dishes do you like? "))
# for i in range(no):
#     dsh=input("Enter the name of your favourite dish: ") 
#     fvrt_dishes.add(dsh)
# print("These are your favourite dishes\n",fvrt_dishes)    
# for i in range(len(fvrt_dishes)):
#     fvrt_dishes.pop()
#     print(fvrt_dishes)\
# items=["Shampoo","Soap","Bleach","Detergent","Cooking Oil","Ghee","Cream","Milk","Spices"]
# prices=[1200,540,350,700,2900,2200,180,250,100]
# price_rec=set()
# items_sold=0
# while True:
#      print(items)
#      purchase=int(input("Enter the no. of item you want to buy? "))
#      ask=input("Do you want to buy?(Y/N)")
#      if "N" in ask:
#         print("The total items sold are",items_sold)
#         print("The maximum priced product product you purchased is", max(price_rec))
#         print("The minimum priced product product you purchased is", min(price_rec))
#         break
#      else:
#       x=prices[purchase]
#       print("The price of",items[purchase],"is",x)
#       items.pop(purchase) 
#       prices.pop(purchase)
#       price_rec.add(x)
#       items_sold+=1
# universal=set(range(40))
# hockey=set(range(21))
# hockeyandcricket=set(range(10))
# cricket=set(range(len(universal)-len(hockeyandcricket)-len(hockey)))
# print("The no. of students who play cricket only are",len(cricket))
# cat=set(range(101))
# dog=set(range(83))            
# fish=set(range(22)) 
# catanddog=set(range(31))
# dogandfish=set(range(8))
# catandfish=set(range(10))
# dogcatandfish=set(range(6))
# other=set(range(34))           
# print("The no. of total purchases are",len(dog)-len(dogandfish)-len(catanddog-dogcatandfish)
# +len(fish)-len(dogandfish)-len(catandfish-dogcatandfish)+len(cat)-len(catandfish)-len(catanddog-dogcatandfish)
# +len(catanddog-dogcatandfish)+len(catandfish-dogcatandfish)+len(dogandfish-dogcatandfish)+len(dogcatandfish)
#                                                                                               +len(other))
std=set(range(110))
eng_std=set(range(75))
spanish_std=set(range(52))
french_std=set(range(50))
eng_span_fren=set(range(13))
eng_span=set(range(33))
eng_fren=set(range(30))
span_fren=set(range(22))
eng_span_only=set(range(len(eng_span)-len(eng_span_fren)))
fren_only=set(range(len(french_std)-len(eng_fren)-len(span_fren)+len(eng_span_fren)))
eng_only=set(range(len(eng_std)-len(eng_fren)-len(eng_span)+len(eng_span_fren)))
span_only=set(range(len(spanish_std)-len(span_fren)-len(eng_span)+len(eng_span_fren)))
eng_fren_only=set(range(len(eng_fren)-len(eng_span_fren)))
fren_span_only=set(range(len(span_fren)-len(eng_span_fren)))
total_std=set(range(len(eng_only)+len(span_only)+len(fren_only)+len(eng_fren_only)
                    +len(eng_span_only)+len(fren_span_only)+len(eng_span_fren)))
print('French speaking students only:',len(fren_only))
print('Only one of three languages',len(eng_only)+len(span_only)+len(fren_only))
print('Neither of the three languages',len(std)-len(total_std))
print('Exactly two of the three languages',len(eng_fren_only)+len(fren_span_only)+len(eng_span_only))