
line_count = 0
number_of_words = 0

with open("n2_data.txt", "r") as f_obj:
    for line in f_obj:
        if line != "\n":
            words = line.split()
            number_of_words = len(words)
            line_count += 1
            print("words: {} in line {}".format(number_of_words, line_count))

print("\nlines: {}".format(line_count))

