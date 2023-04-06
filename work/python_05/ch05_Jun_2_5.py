person = {}
for key in ['no', 'name', 'phone', 'email'] : data = input(key+" 입력>> ")
	person[key] = data
	print(person, indent=4, width=20) keys = person.keys()
	values = person.values()
print(keys) 
print(values)