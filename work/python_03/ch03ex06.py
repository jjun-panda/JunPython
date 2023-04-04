grade = 'F'
score = int(input("성적을 입력하세요: "))

while not(score >= 0 and score <= 100):
    print("Error")
    score = int(input("성적을 다시 입력해주세요: "))

if score >= 90 :
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'

num = score%10
# if score  == 100:
#     grade = str(grade) + '+'
if score >= 60 :
    if num > 7 or score == 100:
        grade = str(grade) + '+'
    elif num < 3 :
        grade = str(grade) + '-'

print("당신의 {}점이며 학점은 {}입니다" .format(score, grade))