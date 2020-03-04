def average_scores(*args, **kwargs):
    # Use *args for average calculation
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    # return


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Bill', last_name='McCulley', major='SQL Certification'))