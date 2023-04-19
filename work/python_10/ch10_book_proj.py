import json

with open('call.file', 'r') as f:
    obj = json.load(f)


contacts = obj['contacts']

# 리스트를 출력 한다.
print("%-7s%-20s%-40s%-20s" %('idx','name','phone','addr'))
for mem in contacts :
    idx = mem['idx']
    name = mem['name']
    phone = mem['phone']
    address = mem['addr']
    print("%-7s%-20s%-40s%-20s" %(idx, name, phone, address))