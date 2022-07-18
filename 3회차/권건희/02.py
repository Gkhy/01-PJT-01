with open('data/fruits.txt','r',encoding='utf-8') as file:
     f= open('02.txt','w',encoding='utf-8')
     a=file.read()
     b=a.split("\n")
     d=set(b)
     c=0

     for i in d:
        if i.endswith('berry') :
             c+=1
     print(f'{c}')
     f.write(f'{c}\n')
     for i in d:
        if i.endswith('berry') :
            
             print(f'{i}\n')
             f.write(f'{i}\n')
