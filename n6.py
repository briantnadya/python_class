def int_func(word_small):
    return word_small.capitalize()


def main():
    user_input = raw_input("Please enter the message consisting of small latin letters: ")
    for word in user_input.split():
        user_input = user_input.replace(word, int_func(word))

    print("The resulting message: {}".format(user_input))


if __name__ == "__main__":
    main()
