class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


flag = True
user_data = []
while flag:
    try:
        inp_data = raw_input("Please enter the number: ")

        if type(int(inp_data)) == int:
            user_data.append(int(inp_data))

    except ValueError:
        if inp_data == 'stop':
            print("You entered the key word for exit, buy!")
            flag = False
        else:
            print("Ooops! You didn't enter the number, please try again.")

    except OwnError as err:
        print(err)


print("Your final list is {}".format(user_data))
