#  return a list of user input
def make_list():
    list.new_list()
    count = 0
    while count < 3:
        user_number = get_input()
        count += 1
        y = int(user_number)
        new_list.append(y)
    print(new_list)


#  get one input and return it
def get_input():
    user_input = input('Please enter an number: ')
    return user_input


if __name__ == '__main__':
    make_list()
