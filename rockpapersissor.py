# rps.py
import random

OPTIONS = {"r": "Rock", "p": "Paper", "s": "Scissors"}

def winner(player, comp):
    if player == comp:
        return "draw"
    rules = {("r","s"), ("s","p"), ("p","r")}
    return "player" if (player, comp) in rules else "comp"

def play():
    score_p = score_c = 0
    print("=== Oẳn tù tì === (r=rock, p=paper, s=scissors). g để thoát")
    while True:
        choice = input("Chọn (r/p/s) hoặc g để thoát: ").strip().lower()
        if choice == "g":
            print("Bye!")
            break
        if choice not in OPTIONS:
            print("Chọn r, p hoặc s.")
            continue
        comp = random.choice(list(OPTIONS.keys()))
        print(f"Bạn: {OPTIONS[choice]}  |  Máy: {OPTIONS[comp]}")
        res = winner(choice, comp)
        if res == "draw":
            print("Hòa.")
        elif res == "player":
            print("Bạn thắng!")
            score_p += 1
        else:
            print("Máy thắng!")
            score_c += 1
        print(f"Điểm — Bạn: {score_p}  Máy: {score_c}\n")

if __name__ == "__main__":
    play()
