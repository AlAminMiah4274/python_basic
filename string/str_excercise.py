# Ex: 1
# def varity_str(string):
#     result = []
#     string_one = ""
#     for capital_letter in string:
#         if capital_letter.isupper():
#             string_one += capital_letter
#     print(string_one)
#     result.append(string_one)

#     string_two = ""
#     for small_letter in string:
#         if small_letter.islower():
#             string_two += small_letter
#     print(string_two)
#     result.append(string_two)

#     string_three = ""
#     for number in string:
#         if number.isdigit():
#             string_three += number
#     print(string_three)
#     result.append(string_three)

#     string_four = ""
#     for others in string:
#         if not others.isalnum() and not others.isspace():
#             string_four += others
#     print(string_four)
#     result.append(string_four)

#     return result


# line = input("Please write a sentence. Which contains capital and small letter, number and special characters: ")
# print(varity_str(line))

# Ex: 2

def position_exchange(string):
    characters = list(string)

    for i in range(0, len(string)-1, 2):
        characters[i], characters[i + 1] = characters[i + 1], characters[i]

    result = ''.join(characters)

    return result

function_parameter = input("Write a word: ")
print(position_exchange(function_parameter))