# hangman.py
import random

WORDS = ["python","laptrinh","giaanh","baiviet","nguoi"]
def play():
    secret = random.choice(WORDS)
    guessed = set()
    tries = 6
    print("=== Hangman ===")
    while tries > 0 and set(secret) - guessed:
        display = " ".join([c if c in guessed else "_" for c in secret])
        print(f"Từ: {display}   Thử còn: {tries}")
        guess = input("Nhập 1 chữ cái: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Nhập 1 chữ cái hợp lệ.")
            continue
        if guess in guessed:
            print("Bạn đã đoán chữ này rồi.")
            continue
        if guess in secret:
            print("Đúng!")
            guessed.add(guess)
        else:
            print("Sai!")
            tries -= 1
    if set(secret) - guessed:
        print(f"Bạn thua. Từ đúng là: {secret}")
    else:
        print(f"Bạn thắng! Từ: {secret}")

if __name__ == "__main__":
    play()
