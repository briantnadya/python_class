flag = True
with open("out_file.txt", "w") as out_f:
    while flag:
        user_input = raw_input("Please enter the data that you want to write into the .txt file: ")
        if user_input == "":
            print("You decided to exit the program!")
            flag = False
        else:
            out_f.writelines(user_input + '\n')
