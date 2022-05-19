student = []
score = []
total = 0

inwon = int(input("인원 입력 : "))

for i in range(inwon) :
    name = input("학생 이름 : ")
    student.append(name)

print("우리학급 학생명단", student)

for i in student :
    jumsu = int(input("%s의 성적 입력 : " %i))
    score.append(jumsu)
    total += jumsu

print("우리학급 총점: ", total, " / 우리학급 성적 평균: ", total/inwon)
