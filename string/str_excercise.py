# Ex: 1
def varity_str(string):
    result = []
    string_one = ""
    for capital_letter in string:
        if capital_letter.isupper():
            string_one = string_one + capital_letter
    print(string_one)
    result.append(string_one)

    string_two = ""
    for small_letter in string:
        if small_letter.islower():
            string_two = string_two + small_letter
    print(string_two)
    result.append(string_two)

    string_three = ""
    for number in string:
        if number.isdigit():
            string_three = string_three + number
    print(string_three)
    result.append(string_three)

    string_four = ""
    for others in string:
        if not others.isalnum() and not others.isspace():
            string_four = string_four + others
    print(string_four)
    result.append(string_four)

    return result


line = "Hello! My Name is Jack. My age is 32. I was born in 1992, *&"
print(varity_str(line))