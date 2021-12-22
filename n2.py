
draft_list = input("Please enter the list you wanna work with: ")
print("Initial list is: ", draft_list)

for elem in draft_list:
    if (len(draft_list)%2!=0) & (draft_list.index(elem)==len(draft_list)-1):
        print("Element {} is the last element, no elements to exchange, done!".format(draft_list[len(draft_list)-1]))
        break
    else:
        if draft_list.index(elem)%2==0:
            index1 = draft_list.index(elem)
            elem_next = draft_list[index1+1]
            index2 = draft_list.index(elem_next)
            draft_list[index1], draft_list[index2] = draft_list[index2], draft_list[index1]
print("Final list is: ", draft_list)

