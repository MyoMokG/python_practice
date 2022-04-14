a,b,c,m=0,0,0,0

a=int(input("성인 인원수: "))
b=int(input("청소년 인원수: "))
c=int(input("어린이 인원수: "))
m=10000*a+9000*b

if a==0 and b==0 and c!=0:
    print("어린이 친구들은 무료로 입장하세요!")
else:    
    if a>0:
        print("성인 %d명, "%a, end="")

    if b>0:
        print("청소년 %d명, "%b, end="")

    if c>0:
        print("어린이 %d명, "%c, end="")
    print("요금은 %d원입니다."%m)






