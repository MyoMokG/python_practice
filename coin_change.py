money=int(input("교환할 돈은 얼마? "))

coin_500=money//500
money=money%500
print("500원짜리 ==> %d개" %coin_500)

coin_100=money//100
money=money%100
print("100원짜리 ==> %d개" %coin_100)

coin_50=money//50
money=money%50
print("50원짜리 ==> %d개" %coin_50)

coin_10=money//10
money=money%10
print("10원짜리 ==> %d개" %coin_10)

print("잔돈: %d원" %money)
