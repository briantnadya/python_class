class Data:
    def __init__(self, data_info):
        self.data_info = data_info

    @classmethod
    def parse_data(cls, data_info):
        updated_data = ''
        data_parts = data_info.split('-')
        for el in data_parts:
            updated_data = updated_data + el
        return "The final parsing is: {}".format(updated_data)

    @staticmethod
    def numbers_validation(data_info):
        result = ''
        data_parts = data_info.split('-')
        data_parts = [int(data_parts[i]) for i in range(0, len(data_parts))]

        if type(data_parts[0]) == int:
            result = result + "Everything is good with the day.\n"
        else:
            result = result + "Please write the day again.\n"

        if 0 < data_parts[1] < 13:
            result = result + "Everything is good with the month.\n"
        else:
            result = result + "Please write the month between 1 and 12 again.\n"

        if type(data_parts[2]) == int:
            result = result + "Everything is good with the year.\n"
        else:
            result = result + "Please write a year again.\n"

        return result


print(Data.parse_data("12-08-2010"))
print(Data.numbers_validation("12-08-2010"))
