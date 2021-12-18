desired_result = float(input("Please enter how many km do you wanna run: ")) # b
init_result = float(input("Please enter the number of km from your first day: ")) # a
improve_n = float(0.1)
day_number = 1

if init_result < desired_result:
    improvement = float(init_result*improve_n)
    next_result = init_result + improvement
    day_number += 1

    while next_result < desired_result:
        day_number += 1
        improvement = float(next_result*improve_n)
        next_result = next_result + improvement

else:
    print("You have already achieved your goal in 1 day! ")

print('The number of the day at which you will achieve your goal is: {}'.format(day_number))
