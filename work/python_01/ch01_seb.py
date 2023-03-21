# ch01_01.py 파일 import
# 외부 파일에서 import하면 __name__는 파일명이 된다.
from ch01_main import print_hi

print("ch01_seb 실행")
print_hi("JJUN")

if __name__ == "__main__" :
    print("ch01_seb에서 __name__은 : ", __name__)