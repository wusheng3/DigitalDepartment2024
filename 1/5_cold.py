def cold():
    line = input()
    new_line_list = [char + char for char in line]
    print(''.join(new_line_list))
    
if __name__ == "__main__":
    cold()