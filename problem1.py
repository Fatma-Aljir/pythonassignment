def compare_numbers(a,b) :
    if type(a) == int and type(b) == int:
        if a == b:
            return "a and b are equal"
        elif a > b:
            return "a is greater than b"
        else:
            return "b is greater than a"
    else:
        return "invalid input"

a = int(input(" Enter number a : "))
b = int(input(" Enter number b : "))
print(compare_numbers(a,b))