money=int(input("교환할 돈은 얼마? "))

for coin in [500,100,50,10] :
    print("%d원짜리 ==> %d개" %(coin, money//coin))
    money%=coin

print("잔돈: %d원" %money)
