with open("00.txt",'w',encoding='utf-8') as f:
    f.write('3회차 권건희\nHello, python!\n')
    from datetime import datetime
    a=int(datetime.now().day)
    b=a-10
    count=0
    for i in range(b):
        count+=1
        f.write(f'{count}일차 파이썬 공부\n')

        
