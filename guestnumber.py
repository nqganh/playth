# guess_number.py
import random

def play():
    print("=== Game: Đoán số ===")
    low, high = 1, 100
    secret = random.randint(low, high)
    tries = 0

    print(f"Mình đã nghĩ 1 số từ {low} đến {high}. Bạn đoán đi!")
    while True:
        tries += 1
        try:
            guess = int(input("Số bạn đoán: ").strip())
        except ValueError:
            print("Nhập 1 số nguyên hợp lệ.")
            continue

        if guess < secret:
            print("Thấp quá ↑")
        elif guess > secret:
            print("Cao quá ↓")
        else:
            print(f"Chính xác! Bạn đoán đúng sau {tries} lần.")
            break

if __name__ == "__main__":
    play()
    