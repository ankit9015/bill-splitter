# write your code here
# Total number of people joining
import random


# lucky_one is used to choose a random person from the dictionary of friends
def lucky_one(do, input_dict):
    if do == 'Yes':
        choosen = random.choice(list(input_dict.keys()))
        print(f"{choosen} is the lucky one!")
        return choosen
    elif do == 'No':
        print("No one is going to be lucky")
        return ''
    else:
        print("Please answer Yes or No")
        return ''


# bill_split splits the bill equally among the friends
def bill_split(name, input_dict, bill_value):
    if len(name) > 0:
        # this is the case when we have a lucky person
        split_value = round((bill_value / (len(friends) - 1)), 2)
    else:
        # when no lucky person is selected
        split_value = round((bill_value / len(friends)), 2)
    for key in input_dict.keys():
        if key == name:  # the dictionary value for the lucky person is kept 0
            continue
        friends[key] = split_value


try:
    total_people = int(input("Enter the number of friends joining (including you) :\n"))
    if total_people <= 0:
        # this is the case when the input from the user is not valid to form a bill splitter
        print("No one is joining for the party")
        exit()
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for _ in range(total_people)}
    final_bill = float(input("Enter the total bill value:\n"))
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    is_lucky = input()
    choosen_one = lucky_one(is_lucky, friends)  # lucky person is selected from the dictionary of friends
    bill_split(choosen_one, friends, final_bill)  # equally splits bill among friends
    print(friends)

except (ZeroDivisionError, TypeError, ValueError):
    print("No one is joining for the party")
