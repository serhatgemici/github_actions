def total(my_list):
    """ returns the sum of the elements of a list """

    if type(my_list) == int :
        return (my_list)

    result : float = 0.0

    for item in my_list:
        result += item

    return (result)