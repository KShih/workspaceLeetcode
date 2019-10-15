def prefix2infix(str):
    stack = []
    operator = ['+', '-', '*', '/']
    for i in range(len(str)-1,-1,-1):
        if str[i] in operator:
            if stack:
                operand1 = stack.pop()
            else:
                print("cannot get op1");break
            if stack:
                operand2 = stack.pop()
            else:
                print("cannot get op2");break

            stack.append(operand1 + str[i] + operand2)
        else:
            stack.append(str[i])
    if len(stack) == 1:
        return stack[0]
    else:
        print("stack size error")


def postfix2infix(str):
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

            stack.append(operand2 + str[i] + operand1)
        else:
            stack.append(str[i])
    if len(stack) == 1:
        return stack[0]
    else:
        print("stack size error")

if __name__ == '__main__':
    print(prefix2infix("*+AB-CD")) #((A+B)*(C-D))
    print(postfix2infix("AB+CD-*")) #((A+B)*(C-D))
