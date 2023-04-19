import logging
import time

root_logger= logging.getLogger()
handler = logging.FileHandler('log_fish_order.txt', 'w', 'utf-8')
handler.setFormatter(logging.Formatter('%(name)s - %(asctime)s - %(message)s'))
root_logger.addHandler(handler)

fish_list = ['오징어', '꼴뚜기', '대구', '명태', '거북이']
print("생선을 주문하세요!")
for i, fish in enumerate(fish_list) :
    print(f"({i+1}) {fish} ", end="")

while True :
    try :        
        choice = int(input(">> "))
        print("-"*55)
        if choice <= 0 :
            raise Exception("알 수 없는 예외가 발생했습니다.")
        print(fish_list[choice - 1], end = "")
        break
    except IndexError as e:
        print(f"목록에 없는 번호 입니다. [{i-(i-1)}부터 {len(fish_list)}까지 입력해주세요!]")
        root_logger.error("IndexError 발생")
    except ValueError as e:
        print(f"목록에 없는 번호 입니다. [{i-(i-1)}부터 {len(fish_list)}까지 입력해주세요!]")
        root_logger.error("ValueError 발생")
    except Exception as e:
        print(f"알 수 없는 예외가 발생했습니다. [{i-(i-1)}부터 {len(fish_list)}까지 입력해주세요!]")
        root_logger.error("Exception 발생")

    time.sleep(0.1)
    print("다시 선택", end = "")

print("주문완료")