# 2022-1 상명대학교 기초AI와콘텐츠 팀프로젝트
# 작품명: 이거알고있슴?
# 팀명: 알려주조 = [202110421박소은, 202111421이수빈, 202211116이동건]

# 기능소개
# 1. 길잃은 사슴(길찾기)
# 출발지와 도착지를 입력받아 추천 경로를 제공한다.
# 2. 목마른 사슴(카페)
# 현재 위치를 입력받아 가장 가까운 카페를 알려준다.
# 3. 배고픈 사슴(학생식당)
# 현재 위치를 입력받아 가장 가까운 학생식당을 알려준다.

# 변수선언
optatio = 0
initium, obitus = "", ""
locus = ""
aedificia = ["A 사범대학관", "B 미술관", "C 가정관", "D 생활예술관", "E 학군단",\
               "F 체육관", "G 제1공학관", "H 학생회관", "I 제2교수회관", "J 대학본부",\
               "K 제2공학관", "L 학술정보관", "M 문화예술대학관 1관(월해관)", "N 인문사회과학대학관(자하관)",\
               "O 제1교수회관", "R 미래백년관", "S 중앙교수회관", "T 경영경제대학관(밀레니엄관)", "U 문화예술관"]

# 함수선언
def reinput_number() :
    respondere = ""
    
    while len(respondere) != 1 or respondere.isnumeric() == False :
        respondere = input("하나의 숫자로 입력해 주세요. : ")
        
    return int(respondere)

def reinput_upper() :
    respondere = ""
    
    while len(respondere) != 1 or respondere.isupper() == False :
        respondere = input("하나의 대문자로 입력해 주세요. : ")
        
    return respondere


# 프로그램
while optatio != 9 :
    print("=========================================================================")
    print("슴우들을 위한 캠퍼스 가이드, [이거알고있슴?]입니다!")
    print("아래에서 원하는 기능을 선택하세요. 프로그램을 종료하려면 9를 입력하세요.")
    print(" 1. 길잃은 사슴(길찾기) \n 2. 목마른 사슴(카페) \n 3. 배고픈 사슴(학생식당)")

    optatio = reinput_number()

    if optatio == 9 : # 종료
        print("이용해 주셔서 감사합니다.")
        
    elif optatio == 1 : # 길찾기
        print("[출발지를 선택하세요.]")
        for aedificium in aedificia :
            print(aedificium)
        initium = reinput_upper()
        print("[목적지를 선택하세요.]")
        for aedificium in aedificia :
            print(aedificium)
        obitus = reinput_upper()
        #############################미구현#############################
        print("서비스를 준비중입니다.")
        #############################미구현#############################
        
    elif optatio == 2 : # 카페
        print("[현 위치를 선택하세요.]")
        for aedificium in aedificia :
            print(aedificium)
        locus = reinput_upper()
        if locus in ["K"] :
            print("  [ 언덕에 있는 카페를 이용하세요. ]  ")
        elif locus in ["O", "N", "S", "G", "H"] :
            print("  [ 중앙교수회관 카페드림을 이용하세요. ]  ")
        elif locus in ["J", "A", "L", "T"] :
            print("  [ 중앙교수회관 카페드림 혹은 미래백년관 B1층 블루포트를 이용하세요. ]  ")
        else :
            print("미래백년관 블루포트 혹은 월해관 2층 안다미로 카페를 이용하세요.")
        
    elif optatio == 3 : # 학식
        print("[현 위치를 선택하세요.]")
        for aedificium in aedificia :
            print(aedificium)
        locus = reinput_upper()
        if locus in ["K"] :
            print("  [ 언덕에 있는 식당을 이용하세요. ]  ")
        elif locus in ["O", "N", "S", "G", "H", "J", "A", "L", "T", "R"] :
            print("  [ 미래백년관 5층 학생식당을 이용하세요. ]  ")
        else :
            print("  [ 월해관 2층 안다미로를 이용하세요. ]  ")



