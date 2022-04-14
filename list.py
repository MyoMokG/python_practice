while True :
    print("------------------------------------------------------------------")
    print("리스트 연습에 오신 것을 환영합니다. 원하는 기능을 선택해 주세요.")
    print("1. 새 리스트 생성하기")
    print("2. 리스트 뒤에 데이터 추가하기")
    print("3. 데이터 제거하기")
    print("4. 데이터 정렬하기")
    print("5. 리스트를 역순으로 뒤집기")
    print("6. 원하는 데이터의 위치 찾기")
    print("7. 특정 위치에 데이터 삽입하기")
    print("8. 특정 위치에서 데이터 뽑아내기")
    print("9. 다른 리스트 이어붙이기")
    print("10. 특정 데이터의 갯수 세기")
    print("0. 종료")
    user_select=int(input("어떤 작업을 수행할까요? : "))

    if user_select == 0 :
        break
    
    if user_select == 1 :
        user_list = []
        user_list_length=int(input("몇 칸짜리 리스트를 만들까요? : "))
        print("이제 새 리스트를 생성합니다. %d개의 값을 차례로 입력해 주세요." %user_list_length)
        for i in range(1, user_list_length+1, 1) :
            user_list.append(input("%d번째 값을 입력해 주세요. : " %i))
        print("리스트 생성이 완료되었습니다.")
        print(user_list)
        
    if user_select == 2 :
        user_list.append(input("추가할 데이터를 입력해 주세요. : "))
        print(user_list)

    if user_select == 3 :
        user_list.remove(input("제거할 데이터를 입력해 주세요. : "))
        print(user_list)
        
    if user_select == 4 :
        user_list.sort()
        print(user_list)

    if user_select == 5 :
        user_list.reverse()
        print(user_list)

    if user_select == 6 : 
        print(user_list.index(input("찾고자 하는 데이터를 정확히 입력하세요. : ")))

    if user_select == 7 :
        where = int(input("삽입할 위치를 입력해 주세요. : "))
        what = input("삽입할 데이터를 입력해 주세요. : ")
        user_list.insert(where, what)
        print(user_list)

    if user_select == 8 :
        user_list.pop(int(input("뽑아낼 위치를 입력해 주세요. : ")))
        print(user_list)

    if user_select == 9 :
        plus_list = []
        print("이어붙일 리스트를 생성합니다.")
        plus_list_length=int(input("몇 칸짜리 리스트를 만들까요? : "))
        print("이제 새 리스트를 생성합니다. %d개의 값을 차례로 입력해 주세요." %plus_list_length)
        for i in range(1, plus_list_length+1, 1) :
            plus_list.append(input("%d번째 값을 입력해 주세요. : " %i))
        print("이어붙일 리스트 생성이 완료되었습니다.")
        print(plus_list)
        user_list.extend(plus_list)
        print("리스트 이어붙이기가 완료되었습니다.")
        print(user_list)

    if user_select == 10 :
        print(user_list.count(input("갯수를 셀 데이터를 정확히 입력하세요. : ")))

        

    
        

