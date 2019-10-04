def findWarmday(temperature):
    nextWarmday = [0 for _ in range(len(temperature))]
    stack = [] # stack for looking for next warmer day

    for i in range(len(temperature)):
        print stack
        while len(stack)!= 0 and temperature[i] > temperature[stack[0]]:
            print("tem[i] > tem[top]", temperature[i], temperature[stack[0]])
            top = stack.pop(0)
            nextWarmday[top] = i - top
        stack.insert(0,i)

    return nextWarmday

if __name__ == "__main__":
    print(findWarmday([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
