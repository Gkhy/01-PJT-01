with open('data/fruits.txt','r',encoding='utf-8') as f:
    a=f.read()

    print(a,type(a))
    name=a.split('\n')
    cnt=()
    b=0
    for i in name:
        if i not in cnt:
            b+=1
    c=str(b)        
    with open('01.txt','w',encoding='utf-8') as file:
        file.write(c)