name=input("이름: ")
AI=eval(input("기초AI와콘텐츠 성적: "))
SP=eval(input("사고와표현 성적: "))
EN=eval(input("영어 성적: "))
x=(AI+SP+EN)/3
print("%s의 평균 점수는 %6.2f입니다."%(name,x))
