# def my_function():
#     global msg
#     msg="Hello"
#     return None
#
# my_function()
# print(msg)

def my_function():
    def my_second_function():
        print(locals(), "local la nivel de my function")

        global msg
        msg="hello"
        return None

    my_second_function()
    #print(msg)
    msg="Hello1"
    print("functia principala {msg}")
    return None

def functie2():
    print(msg,">>>>")
    return None
my_function()
functie2()
print(msg)
print(locals())