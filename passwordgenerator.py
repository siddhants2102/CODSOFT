import random

output_list = []


def selector(number, start, end):
    for i in range(number):
        choice = chr(random.randint(start, end))
        output_list.append(choice)


print("WELCOME TO THE CODSOFT'S PASSWORD GENERATOR:\n")

capital_letters = int(input("ENTER THE NUMBER OF CAPITAL LETTERS IN THE PASSWORD:"))
small_letters = int(input("ENTER THE NUMBER OF SMALL LETTERS IN THE PASSWORD:"))
numeric_values = int(input("ENTER THE NUMBER OF NUMERIC VALUES IN THE PASSWORD:"))
special_characters = int(input("ENTER THE NUMBER OF SPECIAL CHARACTERS IN THE PASSWORD:"))

selector(capital_letters, 65, 90)
selector(small_letters, 97, 122)
selector(numeric_values, 48, 57)
selector(special_characters, 33, 47)

random.shuffle(output_list)
result = ""
for x in output_list:
    result += x
print(f"\nTHE REQUIRED PASSWORD IS: {result}")
