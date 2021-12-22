user_message = input('Please enter your sentence you want to split with the spaces between the words: ')

count = 1
for word in user_message.split():
    if len(word) > 10:
        part_1 = word[:10]
        part_2 = word[10:]
        print("{}. {}".format(count, part_1))
        count += 1
        print("{}. {}".format(count, part_2))
        count += 1

    else:
        print("{}. {}".format(count, word))
        count += 1

