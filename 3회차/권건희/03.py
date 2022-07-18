with open('data/fruits.txt','r',encoding='utf-8') as f:
     file=open('03.txt','w',encoding='utf-8')
     a=f.read().split("\n")
     dic={}
     for i in a:
        if i not in dic:
            dic[i]=1
        else:
          dic[i]+=1
     for i in dic:
       print(i,dic[i])
       file.write(f'{i},{dic[i]}\n')

   
