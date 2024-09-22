def calculadora(operacao):
    def som(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b

    match operacao:
        case '+':
            return som
        case '-':
            return sub
        case '*':
            return mul
        case '/':
            return div

print(calculadora('+')(1,1))
op = calculadora('-')
print(op(2,1))
print(calculadora('*')(5,2))
print(calculadora('/')(4,2))

        