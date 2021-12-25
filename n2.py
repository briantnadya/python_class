def description_func(name="Vanya", surname="Petrov", birth_year=1995, city="Moscow", email="vanya.p@yandex.ru",
                     phone=543677):
    print("Your full name is {} {}, year of birth is {}, city is {}, an email is {}, and the phone number is {}".format(
        name, surname, birth_year, city, email, phone))


def main():
    user_description = {"name": '', "surname": '', "birth_year": '', "city": '', "email": '', "phone": ''}
    for f in user_description.keys():
        prop = raw_input("Please enter the following information {} - ".format(f))
        user_description[f] = int(prop) if f in ("birth_year", "phone") else prop

    description_func(name=user_description["name"], surname=user_description["surname"],
                     birth_year=user_description["birth_year"], city=user_description["city"],
                     email=user_description["email"])


if __name__ == "__main__":
    main()
