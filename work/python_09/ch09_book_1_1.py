def say_hello(name):
    print("hello", name)

def say_hello2(name):
    print("good morning", name)

if __name__ == "__main__" :
    say_hello("kim")
    say_hello2("hong")

from ch09_book_1_1 import say_hello
from ch09_book_1_1 import say_hello2

if __name__ == "__main__":
    say_hello("kim")
    say_hello2("hong")