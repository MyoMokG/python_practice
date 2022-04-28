def weeklypay(rate,hour) :
    if hour > 30 :
        money = 30*rate + (hour-30)*rate*1.5
    else :
        money = 30*rate
    return money

rate = int(input("시급을 입력해 주세요. : "))
hour = int(input("근무시간을 입력해 주세요. : "))
pay = weeklypay(rate, hour)
print(pay)
