# https://open.kattis.com/problems/4thought

n = int(input())
solutions = [int(input()) for x in range(n)]

operations = ["+", "-", "*", "/"]

def solve(op1, op2, op3):
    equation = f"4{op1}4{op2}4{op3}4"
    
    equation = equation.replace("4/4/4/4", "0")
    equation = equation.replace("4/4/4", "0")
    equation = equation.replace("4/4", "1")

    return eval(equation)

for s in solutions:
    equations = []
    for op1 in operations:
        for op2 in operations:
            for op3 in operations:
                solve(op1, op2, op3)
                if solve(op1, op2, op3) == s:
                    equations.append(f"4{op1}4{op2}4{op3}4 = {s}")

    print("no solution") if len(equations) == 0 else print(equations[0])

