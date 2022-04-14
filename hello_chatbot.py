name=input("이름을 입력하세요. : ")
print("채팅을 시작하려면 '안녕' 혹은 '안녕하세요'라고 먼저 인삿말을 넣어 주세요.")
hello=input()
if "안녕" in hello:
    print("안녕하세요 %s님 만나서 반가워요!"%name)
else:
    print("인사는 하고 시작하기로 해요.")
