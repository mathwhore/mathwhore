def many(a):
    word_len=[0,0,0,0]
    text=[]
    text+=a.split()
    for i in text:
        for j in range(1,5):
            if len(i)==j:
                word_len[j-1]+=1
    k=1            
    for i in word_len:
        print("Words of length",k,"=",i)   
        k+=1          

f=open("sample.txt")
many(f.read()) 
    # b=[]
    # b+=a.split(" ")
    # x=0
    # y=0
    # z=0        
    # w=0
    # for i in b:
    #     if len(i)==1:
    #         x+=1
    #     elif len(i)==2:
    #         y+=1                                                                                   
    #     elif len(i)==3:
    #         z+=1
    #     elif len(i)==4:
    #        w+=1
    # print("Words of length 1=",x)
    # print("Words of length 2=",y) 
    # print("Words of length 3=",z)
    # print("Words of length 4=",w)
