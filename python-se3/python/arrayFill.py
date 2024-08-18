import random

random_number_for_Counting_list_of_index = random.randint(4,10)
print("the random Number is:",random_number_for_Counting_list_of_index)



list_of_provided_numbers_by_for_loop = []

for i in range(random_number_for_Counting_list_of_index):
    random_number_for_index_list = random.randint(1,99)
    list_of_provided_numbers_by_for_loop.append(random_number_for_index_list)



print(set(list_of_provided_numbers_by_for_loop))