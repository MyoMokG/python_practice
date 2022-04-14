import random as r

key, answer = 0, 0

key = r.randrange(1,11)

while key != answer :
    answer = int(input("1부터 10까지의 수를 하나 입력해 주세요. : "))
    while not((answer >= 1) and (answer <= 10)) :
        answer = int(input("정확히 입력해 주세요. : "))

    if key > answer :
        print("더 큰 수를 입력해 보세요.")

    if key < answer :
        print("더 작은 수를 입력해 보세요.")

print("정답입니다!")
