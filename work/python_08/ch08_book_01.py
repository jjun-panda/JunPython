def player(callback) :
	try:
		print("{:-^50}".format("try"))
		print("예외가 발생 할 가능성이 있는 문장에 try해준다")
		resylt = callback()
		print("처리결과: ", resylt)
	except TypeError :
		print("{:-^50}".format("except TypeError"))
		print("TypeError 예외가 발생하면 실행되는 구문")
		print("Exceprion : callback은 함수가 아닙니다!")
		print(callback)
	except :
		print("{:-^50}".format("except TypeError"))
		print("TypeError 예외 이외의 예외")
	else :
		print("{:-^50}".format("else"))
		print("예외가 발생하지 않은 경우에 실행되는 구문")
	finally :
		print("{:-^50}".format("finally"))
		print("에러발생 여부와 관계없이 마무리 작업으로 실행되는 구문")
		

def sayHello():
	return "Hello world"

# player(sayHello)
player("Hello")

