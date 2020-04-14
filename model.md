Solution Model
===
## Calculator
- for `224`, `227`, `772`, `770`
- ![](assets/markdown-img-paste-20200414144532950.png)

### model
```py

while i < len(s):
    c = s[i]
    if isdigit():
        # build-digit()
    elif c == '(':
        cnt = 0
        for j in range(i, len(s)):
            if s[j] == '(':
                cnt += 1
            if s[j] == ')':
                cnt -= 1
            if cnt == 0:
                break
        num = self.calculate(s[i+1:j])
        i = j

    if c is not digit or i is last digit:
        switch(op) to update curRes
        update res if c is + or -
            init curRes
        update op and init num
    inc i
```

### example:
```py
    def calculate(self, s: str) -> int:
        res, curRes, num, op = 0, 0, 0, '+'
        i = 0

        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '(':
                cnt = 0
                for j in range(i, len(s)):
                    if s[j] == '(':
                        cnt += 1
                    if s[j] == ')':
                        cnt -= 1
                    if cnt == 0:
                        break
                num = self.calculate(s[i+1:j])
                i = j


            if c in ['+', '-', '*', '/'] or i == len(s)-1:
                # update curRes
                if op == '+':
                    curRes += num
                elif op == '-':
                    curRes -= num
                elif op == '*':
                    curRes *= num
                elif op == '/':
                    curRes = int(curRes / num)

                # determine whether update res from curRes
                if c in ['+', '-'] or i == len(s)-1:
                    res += curRes
                    curRes = 0

                # update
                op, num = c, 0

            i += 1
        return res
```
