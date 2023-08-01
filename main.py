'''def apply_operator(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b


def evaluate_expression(input_string):
    stack = []
    operators = {'+', '-', '*', '/'}

    for t in input_string.split():
        if t.isdigit():
            stack.append(int(t))
        elif t in operators:
            b = stack.pop()
            a = stack.pop()
            c = apply_operator(t, a, b)
            stack.append(c)

    return stack.pop()

input_expression = "4 5 + 2 *"
result = evaluate_expression(input_expression)
print("Result:", result)'''


def apply_operator(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

