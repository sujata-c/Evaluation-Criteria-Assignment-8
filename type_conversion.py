# different data types in python


def implicit_type_conversion():
    """Implicit Type Conversion is automatically
    performed by the Python interpreter. """

    integer_type = 20
    bool = True
    float_type = 30.87
    complex_type = 8j

    print("Data type of interger_type before type conversion: ", type(integer_type))
    print("Data type of float_type before type conversion: ", type(float_type))
    print("Data type of bool before type conversion: ", type(bool))

    type_conversion1 = float_type + integer_type  # implicit type conversion of interger to float
    print("Data type after implicit type conversion :", type(type_conversion1))

    type_conversion2 = bool + integer_type
    print("Data type after implicit type conversion :", type(type_conversion2))

    type_conversion3 = complex_type + float_type
    print("Data type after implicit type conversion :", type(type_conversion3))


def explicit_type_conversion():
    """ Explicit Type Conversion , the data types
     of objects are converted using predefined functions by
     the user"""
    integer_type = 40
    float_type = 80.09
    string_type = "Hello World"
    list_type = [1, 2, 3, 4, 5]
    set_type = {6, 7, 8, 9, 10}
    print("Data type of interger_type before type conversion: ", type(integer_type))
    print("Data type of float_type before type conversion: ", type(float_type))
    print("Data type of string_type before type conversion: ", type(string_type))

    print("Data type of interger_type after type conversion to float: ", type(float(integer_type)))
    print("Data type of interger_type after type conversion to string: ", type(str(integer_type)), str(integer_type))
    print("Data type of string_type after type conversion to list: ", type(list(string_type)))
    for i in list(string_type):
        print(i, end = ' ')



if __name__ == '__main__':
    print("-----------------Implicit Conversion-------------")
    implicit_type_conversion()
    print("-----------------Explicit Conversion----------------------")
    explicit_type_conversion()
