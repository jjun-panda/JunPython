class People :
    name = None
    ago = 0

    def __init__(self, name, ago) :
        self.name = name
        self.ago = ago

    def __str__(self) :
        return  f"이름은{self.name}, 나이는 {self.ago}세 입니다."


class Score :
    kor = 0
    eng = 0
    mat = 0
    total = 0

    def __init__(self, kor, eng, mat) :
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.total = kor + eng + mat
    
    def __str__(self) :
        return  f"국어:{self.kor} \n영어:{self.eng} \n수학:{self.mat}\n총점:{self.total}"

class Student :
    no_id = 0 #학번
    person = None
    sung = None # 성적

    def __init__(self, no_id, person, sung) :
        self.no_id = no_id
        self.person = person
        self.sung = sung

    def __str__(self) :
        return f"학번:{self.no_id} \n{self.person} \n{self.sung}"
    
student01 = Student(1001, People("김코딩", 24), Score(95, 100, 100))

print(student01)