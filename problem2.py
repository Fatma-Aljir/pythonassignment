def calculator(c,d):
    if type(c) == int and type(d) == int:
        sum = c + d
        difference = c - d
        product = c * d
        if d == 0:
            return "division by zero is not allowed"
        else:
            division = c / d
            if c == d:
                return "a and  b are equal\nsum: {}\ndiffernce: {}\nproduct: {}\division: {}".format(sum, difference, product, division)
            else:
                return"\nsum: {}\ndiffernce: {}\nproduct: {}\division: {}".format(sum, difference, product, division)
    else:
        return "invalid input"

c = int(input(" Enter number c : "))
d = int(input(" Enter number d : "))
print(calculator(c,d))
