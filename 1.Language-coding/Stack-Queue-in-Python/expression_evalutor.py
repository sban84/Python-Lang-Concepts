"""
This code will validate expression
"""

ex1 = "(2*3)+5 + {2*3} "

stack = []
opening_operator_list = ['(', '{', '[']
closing_operator_list = [')', '}', ']']

isValid = True


def check_matching_parenthesys(previous_opr, curr_opr, isValid):
    print(f"inside check_matching_parenthesys {previous_opr} and {curr_opr}")
    if (previous_opr == '(') & (curr_opr == ')'):
        return True
    elif (previous_opr == '{') & (curr_opr == '}'):
        return True
    elif (previous_opr == '[') & (curr_opr == ']'):
        return True
    else:
        return False


for i in ex1:
    if isValid:
        # print(i , stack)
        if i in opening_operator_list:
            stack.append(i)
        elif i in closing_operator_list:
            if len(stack) <= 0:
                isValid = False
                break
            else:
                isValid = check_matching_parenthesys(stack.pop(), i, isValid)
                print(isValid)
                if not isValid:  # i.e isValid == False
                    break

print("isValid>>> ", isValid)
if (len(stack) == 0) & isValid:
    print("Expression is valid")
else:
    print("Expression is NOT valid")


