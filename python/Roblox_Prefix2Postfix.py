def prefix2postfix(str):
    stack = []
    operator = ['+', '-', '*', '/']
    for i in range(len(str)-1, -1, -1):
        if str[i] in operator:
            if stack:
                operand1 = stack.pop()
            else:
                print("cannot get op1");break
            if stack:
                operand2 = stack.pop()
            else:
                print("cannot get op2");break

            stack.append(operand1+operand2+str[i])
        else:
            stack.append(str[i])
    if len(stack) == 1:
        return stack[0]
    else:
        print("stack size error")




if __name__ == '__main__':
    print(prefix2postfix("*+AB-CD")) #AB+CD-*
    print(prefix2postfix("*-A/BC-/AKL")) # ABC/-AK/L-*
