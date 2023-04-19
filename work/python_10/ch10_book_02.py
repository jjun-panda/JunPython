from pprint import pprint

hello = [[1,2],[3,4],[5,6]]
pprint(hello, width=15, indent=8)

s = "무궁화 무궁화 우리나라 꽃 삼천리 강산에 우리나라 꽃"
pprint(s, width=10, indent=20)

json_data = '''{"id":"kim",
	"name":"\uae40\ucf54\ub529",
	"age":20
}'''

print(json_data)
pprint(json_data)