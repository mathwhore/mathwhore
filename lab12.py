import random
# cities=['Karachi', 'Lahore','Islamabad','Quetta','Peshawar','Hyderabad','Multan','Faisalabad','Sialkot']
# random.shuffle(cities)
# print(cities)
# scholarship_std=['Kaif','Muzzammil','Haider','Adil','Yaafay','Alishba','Rasheeda','Manahil','Ahsan','Ali'
#                  ,'Mohsin','Javed']
# scholarship_std.remove(random.choice(scholarship_std))
# secondList=[i for i in scholarship_std]
# print('The two students who will get scholarship are:',random.sample(secondList,2)) 
dice1=[i for i in range(1,7)]
dice2=[i for i in range(1,7)]
while True:
    ask=input('Do you want to continue playing?(y/n)')
    if 'y' in ask:
        print('Dice1:',random.choice(dice1))
        print('Dice2:',random.choice(dice2))
    else:
        break
    
