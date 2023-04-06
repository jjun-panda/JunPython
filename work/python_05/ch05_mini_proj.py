import sys

pList = [
    {"seq":1, "name":"Choi", "phone":"010", "addr":"seoul"},
    {"seq":2, "name":"Kim", "phone":"010", "addr":"busan"},
    {"seq":3, "name":"Park", "phone":"010", "addr":"incheon"},
    {"seq":4, "name":"Lee", "phone":"010", "addr":"jeju"}
]

sequence = 5

def  menu() :
    print("1.입력\t2.출력\t3.검색\t4.수정\t5.삭제\t6.종료")
    no = int(input("선택: "))
    return no

def title() :
    print("-"*53)
    print("{: ^50}".format("주소록"))
    print("-"*53)

def search() :
    search = input("이름으로 검색>> ")
    while len(search) == 0:
        print("검색어를 입력하지 않았습니다.")
        search = input("이름으로 검색>> ")
    
    newList = []
    for p in pList:
        if p['name'] == search:
            newList.append(p)
    if len(newList) == 0:
        print("검색결과가 없습니다.")
        return False
        
    print("{: <3}|{: ^10}|{: ^20}|{: ^30}".format('no','name','phone','addr'))
    print("-"*60)
    for i, p in enumerate(pList):
        print("{: <3}|{: ^10}|{: ^20}|{: ^30}".format(p['seq'],p['name'],p['phone'],p['addr']))
    
    # 검색 결과가 있을 경우 True 반환
    return True

def process():
    global sequence
    title()
    print("{:-^50}".format("주소록"))

    while True:
        no = menu();
        print(f"{no}번 선택했습니다.")

        if no == 1:
            print("===== 입력기능 =====")
            p = {
                "seq":sequence,
                "name": input("성명 입력>> "),
                "phone": input("전화번호 입력>> "),
                "addr": input("주소 입력>> ")
            }
            pList.append(p)
            # 함수 외부 변수(gList)는 전변수로 지정 해야 한다.
            # 함수 안에서 함수 외부의 변수를 수정하기 위해 gList 사용.
            
            sequence = sequence + 1
        elif no == 2:
            print("===== 출력기능 =====")
            print("{: <3}|{: ^10}|{: ^20}|{: ^30}".format('no','name','phone','addr'))
            print("-"*60)
            for i, p in enumerate(pList):
                print("{: <3}|{: ^10}|{: ^20}|{: ^30}".format(p['seq'],p['name'],p['phone'],p['addr']))
        elif no == 3:
            print("===== 검색기능 =====")
            # 이름으로 출력 : LEE
            # pList의 요소 중 name이 LEE인 요소를 새 리시트에 저장.
            # 새 리스트 출력
            search()            

        elif no == 4:
            print("===== 수정기능 =====")
            if search() :
                edit = int(input("수정할 번호 선택>> "))
                # edit로 seq가 같은 요소를 찾는다.
                # seq가 같은 요소의 내용을 새로 입력 받는다.
                for p in pList:
                    if p["seq"] == edit:
                        p["name"] = input("성명 입력>> ")
                        p["phone"] = input("전화번호 입력>> ")
                        p["addr"] = input("주소 입력>> ")
                        print("수정이 완료되었습니다.")

        elif no == 5:
            print("===== 삭제기능 =====")
            if search() :
                dele = int(input("수정할 번호 선택>> "))
                # edit로 seq가 같은 요소를 찾는다.
                # seq가 같은 요소의 내용을 새로 입력 받는다.
                for p in pList:
                    if p["seq"] == dele:
                        pList.remove(p)
                        print("삭제가 완료되었습니다")
        elif no == 6:
            print("===== 종료빠잉 =====")
            print("다음에 만나요.")
            sys.exit(0)
            break
        else:
            print("해당 사항이 없습니다.");

if __name__ == "__main__":
    process()
