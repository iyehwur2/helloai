print("안녕하세요! 나의 첫 파이썬 코드입니다.")

import random

# 1. 컴퓨터가 1부터 50 사이의 무작위 숫자를 하나 고릅니다.
secret_number = random.randint(1, 50)
print("🤖: 1부터 50 사이의 숫자를 하나 골랐습니다. 맞춰보세요!")

# 2. 정답을 맞출 때까지 계속 반복합니다.
while True:
    # 3. 사용자에게 숫자를 입력받습니다.
    guess = input("숫자를 입력하세요: ")
    guess = int(guess) # 입력받은 글자를 '숫자'로 바꿔줍니다.
    
    # 4. 입력한 숫자와 정답을 비교합니다.
    if guess == secret_number:
        print("🎉 정답입니다! 축하합니다!")
        break # 정답을 맞췄으니 게임(반복)을 끝냅니다.
        
    elif guess < secret_number:
        print("⬆️ 업 (Up)! 더 큰 숫자입니다.")
        
    else:
        print("⬇️ 다운 (Down)! 더 작은 숫자입니다.")