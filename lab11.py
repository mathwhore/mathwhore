# family={"Father":"Shahid Hussain","Mother":"Atia Shahid","Sisters":"Samra, Anaya"}
# for i,j in family.items():
#  print(i,":",j)
# family.update({"Paternal Grandparents":"Ilyas Zaidi, Jameela Nighat"})
# family.update({"Maternal Grandparents":"Mehmood-ul-Haq, Kaisar Jahan"})
# family.update({"Uncles":"Salman, Sajid, Shakeel, Rashid, Waqar, Khawar, Khurram, Qamar"})
# family.update({"Aunts":"Sabeeha, Shagufta, Razia, Shakeela, Yasmeen, Kishwer"})
# print("UPDATED FAMILY DICTIONARY")
# for i,j in family.items():
#  print(i,":",j)

# def phonebook(x):
#     phone_dir={}
#     for i in range(x):
#         name=input("Enter the name of the contact: ")
#         no=input("Enter the phone number: ")
#         phone_dir.update({name:no})
#     del_no(phone_dir)
# def del_no(x):
#     no=input("Enter the name of the contact you want to delete: ")
#     del x[no]
#     print(x)
#     print('The no. of contacts in the directory are',len(x))

# n=int(input('Enter the no. of comtacts you want to add: '))
# phonebook(n)

# def hexASCII(dict):
#     for i,j in dict.items():
#         print(f'The hexadecimal representation of {i} is {j:x}'.format(j))

# alphascii={"a":97,"b":98,"c":99,"d":100,"e":101,"f":102,"g":103,"h":104,"i":
#            105,"j":106,"k":107,"l":108,"m":109,"n":110,"o":111,"p":112,"q":113,"r":114,"s":115,
#            "t":116,"u":117,"v":118,"w":119,"x":120,"y":121,"z":122}
# hexASCII(alphascii)

# dishes={"fvrt_dishes":{'dish1':'Biryani','dish2':'Pulao','dish3':'Daal chawal','dish4':'Nihari','dish5':'Curry'},
#         "cooked_dishes":{'dish1':'Daal chawal','dish2':'Karhai','dish3':'Gobi gosht',
#                          'dish4':'Aloo mattar','dish5':'Biryani'}}
# choice=dishes['fvrt_dishes']
# cooked=dishes['cooked_dishes']
# choice_cooked=set(choice.values())&set(cooked.values())
# print('The no. of times you will get dishes of your choice cooked in next week is',len(choice_cooked))
# print('The dishes are',{i for i in choice_cooked})

def guest_info(x):
    no=1
    for i in x:
        print(no,':',i) 
        no+=1


guests={"Invited By Parents":{1:"Shakeel",2:"Hamid",3:"Shakeela",4:"Rashida",5:"Sajid",6:"Ahmed",7:"Amin"
                              ,8:"Raza",9:"Razia",10:"Salman"}
        ,"Invited By Me":{1:"Abdullah",2:"Waseem",3:"Rashid",4:"Shakeel",5:"Raza",6:"Khawar",7:"Sajid"
                           ,8:"Hunain",9:"Yasmin",10:"Kishwer"}}

common=set(guests['Invited By Parents'].values())|set(guests['Invited By Me'].values())
print('The total no. of guests are',len(common),"and their names are:")
guest_info(common)