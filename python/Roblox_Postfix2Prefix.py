def postfix2prefix(str):
    stack = []
    operator = ['+', '-', '*', '/']
    for i in range(len(str)):
        if str[i] in operator:
            if stack:
                operand1 = stack.pop()
            else:
                print("cannot get op1");break
            if stack:
                operand2 = stack.pop()
            else:
                print("cannot get op2");break

            stack.append(str[i] + operand2 + operand1)
        else:
            stack.append(str[i])
    if len(stack) == 1:
        return stack[0]
    else:
        print("stack size error")

if __name__ == '__main__':
    print(postfix2prefix("AB+CD-*")) #*+AB-CD
    print(postfix2prefix("ABC/-AK/L-*")) # *-A/BC-/AKL
