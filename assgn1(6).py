def indexes(a,b):
    lst=[]
    for j in range(len(a)):
     if b==a[j]:
      lst.append(j)
    return lst        
            
word=input("Enter a word:")
search=input("Enter the letter you want the index of:")
print("The index(es) of",search,"is",indexes(word.casefold(),search.casefold()))