
def reversed_string(string):
    if not string:
        return string
    else:
        print(string)
        return reversed_string(string[1:]) + string[0]


if __name__ == '__main__':
    word = "gabriel"
    print("Original word:", word)
    print("*"*24)
    reverse_word = reversed_string(word)
    print("*"*24)
    print("Reversed word:", reverse_word)
