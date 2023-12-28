def read_words():
    word = ""
    word_list = []
    word = input()
    while word != "стоп":
        word_list.append(word)
        word = input()
    word_list.sort(key=len)
    shortest_word = word_list[-1]
    longest_word = word_list[0]
    if set(shortest_word) == set(longest_word):
        print("ДА")
    else:
        print("НЕТ")
    
if __name__ == "__main__":
    read_words()