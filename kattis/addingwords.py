# https://open.kattis.com/problems/addingwords

variables = {}

commands = 0
printed = False
while commands < 2000:
    tokens = input().split()
    if tokens[0] == "def":
        variables[tokens[1]] = int(tokens[2])
    elif tokens[0] == "calc":
        value = 0
        for token in tokens[1:]:
            if token in ["+", "-"]: continue
            if token not in variables.keys():
                print(" ".join(tokens) + " = undefined")
                printed = True
                break
            value += variables[token]
        if value not in variables.values() and not printed: 
            print(" ".join(tokens) + " = undefined")
            continue
        for k, v in variables.items():
            if v == value:
                print(" ".join(tokens) + " = " + k)
                break
    elif tokens[0] == "clear":
        variables = {}
    commands += 1
    printed = False
