def temp_check():
    temp = input()
    if float(temp) > 28:
        print("ЖАРКО")
    else:
        print("НОРМАЛЬНО")
        
if __name__ == "__main__":
    temp_check()