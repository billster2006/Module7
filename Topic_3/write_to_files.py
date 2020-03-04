def write_to_file():
    f = open('testscores.txt', 'w')
    f.write("First line\n")
    input_list = ['1\t', '3\t', '5\n']
    f.writelines(input_list)
    f.close()

def get_student_info(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

def read_from_file():
    f = open('testscores.txt', 'r')
    line = f.readline()
    print(line)

if __name__ == '__main__':
    get_student_info()
    read_from_file()
    input('Press any key to end.')