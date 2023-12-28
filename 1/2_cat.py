def meow():
    n = input()
    for i in range(int(n)):
        line = input()
        if "кот" in line or "Кот" in line:
            print("МЯУ")
            return
    print("НЕТ")
        
if __name__ == "__main__":
    meow()