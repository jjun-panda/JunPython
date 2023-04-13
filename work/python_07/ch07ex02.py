class People :
    def __init__(self, name) :
        self.name = name
    
    def setName(self, name) :
        self.name = name

    def greeting(self) :
        return self.name + "님 안녕"
    
kim = People("kim")
pList = [kim, People("Lee"), People("Park")]
pList[0].setName("Hong")
for person in pList :
    print(person.greeting())