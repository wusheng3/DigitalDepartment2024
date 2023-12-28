def shoplist():
    n = input()
    shop_list = []
    for i in range(int(n)):
        item = input()
        shop_list.append(item)
    for item in shop_list:
        print(item)

if __name__ == "__main__":
    shoplist()