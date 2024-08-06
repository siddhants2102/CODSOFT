print("WELCOME TO CODSOFT'S CALCULATOR")
logo = """
 _____________________
|  _________________  |
| |   CALCULATOR    | |       
| |_________________| |               
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
print(logo)


def calculation():
    if operation == "+":
        return user_input1 + user_input2
    elif operation == "-":
        return user_input1 - user_input2
    elif operation == "*":
        return user_input1 * user_input2
    elif operation == "/":
        return user_input1 / user_input2
    else:
        return "INVALID OPERATION !!!"


lp = True
while lp:
    start = input("\nWANT TO PERFORM THE CALCULATION? TYPE 'Y' FOR YES AND 'N' FOR NO:").upper()
    if start == "Y":
        user_input1 = float(input("ENTER THE FIRST NUMBER:"))
        user_input2 = float(input("ENTER THE SECOND NUMBER:"))
        operation = input("WHICH OPERATION('+','-','*'&'/') DO YOU WANT TO PERFORM?:")
        output = calculation()
        if operation in ['+', '-', '*', '/']:
            print(f"OUTPUT:{user_input1}{operation}{user_input2} = {output} Ans ")
        else:
            print(output)
    elif start == "N":
        print("\nSEE YOU SOON !!!")
        lp = False
    else:
        print("INVALID INPUT !!!")
