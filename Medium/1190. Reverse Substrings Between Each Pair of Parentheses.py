def reverseParentheses(s):
    stack = []
    for x in s:
        if x == ")":
            arr = []
            while stack[-1] != "(":
                last = stack.pop(-1)
                arr.append(last)
            stack.pop(-1)
            stack.append(arr)
        else:
            stack.append(x)

    if len(stack) > 1:
        sub = rev(stack, True)
    else:
        sub = rev(stack[0], False)
    return sub

def rev(arr, state):
    sub = ""
    for x in arr:
        if type(x) == list:
            if state:
                sub += rev(x, not state)
            else:
                sub += rev(x[::-1], not state)
        else:
            sub += x

    return sub



s = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses(s))