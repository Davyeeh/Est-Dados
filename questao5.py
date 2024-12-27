# Classe para representar um nó da pilha
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Classe para implementar a pilha com alocação dinâmica/encadeada
class Stack:
    def __init__(self):
        self.top = None

    # Verifica se a pilha está vazia
    def is_empty(self):
        return self.top is None

    # Adiciona um elemento ao topo da pilha
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # Remove e retorna o elemento do topo da pilha
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop em uma pilha vazia")
        value = self.top.value
        self.top = self.top.next
        return value

    # Retorna o elemento do topo da pilha sem removê-lo
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek em uma pilha vazia")
        return self.top.value

    # Representação da pilha como string (para depuração)
    def __str__(self):
        values = []
        current = self.top
        while current:
            values.append(current.value)
            current = current.next
        return " -> ".join(map(str, values))


# Função para associar valores às literais (A a J)
def associate_literals():
    literals = {}
    print("Associe valores às literais (A a J):")
    for literal in "ABCDEFGHIJ":
        value = float(input(f"Digite o valor para {literal}: "))
        literals[literal] = value
    return literals


# Função para converter uma expressão infixa para pós-fixa
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Precedência dos operadores
    stack = Stack()
    postfix = []

    for char in expression:
        if char.isalnum():  # Operandos (variáveis ou números)
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            # Desempilha até encontrar um '('
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operadores
            while (not stack.is_empty() and
                   precedence.get(char, 0) <= precedence.get(stack.peek(), 0)):
                postfix.append(stack.pop())
            stack.push(char)

    # Desempilha os operadores restantes
    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)


# Função para avaliar uma expressão pós-fixa
def evaluate_postfix(expression, literals):
    stack = Stack()

    for char in expression:
        if char.isalnum():  # Operandos (variáveis ou números)
            stack.push(literals[char])
        else:  # Operadores
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)
            elif char == '^':
                stack.push(a ** b)

    return stack.pop()


# Função principal para executar o programa
def main():
    # Associa valores às variáveis literais
    literals = associate_literals()

    # Escolha do formato da expressão
    print("Escolha o formato da expressão:")
    print("1. Forma pós-fixa")
    print("2. Forma infixa")
    choice = int(input("Sua escolha: "))

    if choice == 1:
        # Entrada da expressão em formato pós-fixo
        expression = input("Digite a expressão em forma pós-fixa: ")
    elif choice == 2:
        # Entrada da expressão em formato infixo e conversão para pós-fixo
        expression = input("Digite a expressão em forma infixa: ")
        expression = infix_to_postfix(expression)
        print(f"Expressão convertida para pós-fixa: {expression}")
    else:
        print("Escolha inválida.")
        return

    # Avaliação da expressão
    result = evaluate_postfix(expression, literals)
    print(f"Resultado da expressão: {result}")


# Executa o programa principal
if __name__ == "__main__":
    main()