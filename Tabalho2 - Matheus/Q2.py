import random
import time

class Node:
    def __init__(self, key):
        # Inicializa um nó com uma chave, ponteiros para os filhos esquerdo e direito, e a altura do nó
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        # Insere um valor na árvore AVL, balanceando-a conforme necessário
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # Atualiza a altura do nó ancestral
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Calcula o fator de balanceamento do nó ancestral
        balance = self.getBalance(root)

        # Realiza rotações para balancear a árvore se necessário
        # Caso 1 - Rotação à direita
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        
        # Caso 2 - Rotação à esquerda
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        
        # Caso 3 - Rotação à esquerda-direita
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # Caso 4 - Rotação à direita-esquerda
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def leftRotate(self, z):
        # Realiza uma rotação à esquerda
        y = z.right
        T2 = y.left

        # Realiza a rotação
        y.left = z
        z.right = T2

        # Atualiza as alturas dos nós envolvidos na rotação
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Retorna a nova raiz após a rotação
        return y
    
    def rightRotate(self, z):
        # Realiza uma rotação à direita
        y = z.left
        T3 = y.right

        # Realiza a rotação
        y.right = z
        z.left = T3

        # Atualiza as alturas dos nós envolvidos na rotação
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Retorna a nova raiz após a rotação
        return y
    
    def getHeight(self, root):
        # Retorna a altura de um nó
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        # Calcula e retorna o fator de balanceamento de um nó
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def remove(self, root, key):
        # Remove um valor da árvore AVL, balanceando-a conforme necessário
        if not root:
            return root
        elif key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.remove(root.right, temp.key)

        if root is None:
            return root
        
        # Atualização  da altura do nó atual
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Calcula o fator de balanceamento do nó
        balance = self.getBalance(root)

        # Realiza rotações para balancear a árvore se necessário
        # Caso 1 - Rotação à direita
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        
        # Caso 2 - Rotação à esquerda-direita
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # Caso 3 - Rotação à esquerda
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        
        # Caso 4 - Rotação à direita-esquerda
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def getMinValueNode(self, root):
        # Encontra o nó com o menor valor na árvore
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    def height(self):
        # Retorna a altura da árvore
        return self.getHeight(self.root)

    def search(self, root, key):
        # Verifica se um valor está na árvore
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
    
    def max(self, root):
        # Retorna o maior valor da árvore
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def min(self, root):
        # Retorna o menor valor da árvore
        current = root
        while current.left is not None:
            current = current.left
        return current.key

# Função para medir os tempos de execução
def measure_operations(tree, values):
    # Mede o tempo de inserção e remoção de valores na árvore
    start_time = time.time()
    for value in values:
        tree.root = tree.insert(tree.root, value)
    insert_time = time.time() - start_time

    start_time = time.time()
    for value in values:
        tree.root = tree.remove(tree.root, value)
    remove_time = time.time() - start_time

    return insert_time, remove_time

def main():
    # Gera dados aleatórios e mede os tempos de execução para diferentes tamanhos de entrada
    sizes = [100, 1000, 10000, 1000000]
    for size in sizes:
        values = random.sample(range(1, size * 10), size)
        tree = AVLTree()
        tree.root = None
        insert_time, remove_time = measure_operations(tree, values)
        print(f"Tamanho: {size}")
        print(f"Tempo de inserção: {insert_time:.6f} segundos")
        print(f"Tempo de remoção: {remove_time:.6f} segundos")
        print("=" * 40)

if __name__ == "__main__":
    main()