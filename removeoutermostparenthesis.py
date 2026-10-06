def removeOuter(s):
    ans = []
    n = len(s)

    start = 0

    while start < n:
        end = start

        # Find the end of the current primitive.
        while True:
            balance = 0

            # Recompute balance from scratch.
            for i in range(start, end + 1):
                if s[i] == '(':
                    balance += 1
                else:
                    balance -= 1

            if balance == 0:
                break

            end += 1

        # Remove outermost parentheses.
        for i in range(start + 1, end):
            ans.append(s[i])

        start = end + 1

    return "".join(ans)


s = "(()())(())"

print(removeOuter(s))