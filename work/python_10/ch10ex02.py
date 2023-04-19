lis = [
	{"seq":1, "name":"sonata", "price":2000},
	{"seq":2, "name":"제네시스", "price":7000},
	{"seq":3, "name":"WM", "price":4000},
	{"seq":4, "name":"Dasa", "price":5000}
]

with open("cars.data", "w") as fp:
	for car in lis :
		fp.write(f'{car["seq"]}|{car["name"]}|{car["price"]}\n')

print("Good")