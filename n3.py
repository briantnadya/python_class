
min_salary = 20000
salary_list = []

with open("workers_salary.txt", "r") as f_obj:
    for line in f_obj:
        if line != "\n":
            words = line.split()
            salary_list.append(int(words[1]))
            if int(words[1]) < min_salary:
                print(words[0])

print("Average salary is: {}".format(sum(salary_list)/len(salary_list)))