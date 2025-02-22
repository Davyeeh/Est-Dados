import random
import time

class Node:
    def __init__(self, id_participante, pontuacao):
        # Inicializa um novo nó com ID do participante e pontuação
        self.id_participante = id_participante
        self.pontuacao = pontuacao
        self.left = None  # Filho esquerdo
        self.right = None  # Filho direito
        self.height = 1  # Altura do nó

class AVLTree:
    def __init__(self):
        # Inicializa a árvore AVL com a raiz como None
        self.root = None

    def getHeight(self, root):
        # Retorna a altura do nó
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        # Retorna o fator de balanceamento do nó
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def rightRotate(self, z):
        # Realiza uma rotação para a direita
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def leftRotate(self, z):
        # Realiza uma rotação para a esquerda
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insert(self, root, id_participante, pontuacao):
        # Insere um novo participante ou atualiza a pontuação de um existente
        if not root:
            return Node(id_participante, pontuacao)
        elif id_participante < root.id_participante:
            root.left = self.insert(root.left, id_participante, pontuacao)
        elif id_participante > root.id_participante:
            root.right = self.insert(root.right, id_participante, pontuacao)
        else:
            root.pontuacao = pontuacao

        # Atualiza a altura do nó
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Realiza rotações conforme necessário para manter balanceado
        if balance > 1 and id_participante < root.left.id_participante:
            return self.rightRotate(root)
        if balance < -1 and id_participante > root.right.id_participante:
            return self.leftRotate(root)
        if balance > 1 and id_participante > root.left.id_participante:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and id_participante < root.right.id_participante:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def remove(self, root, id_participante):
        # Remove um participante da árvore AVL
        if not root:
            return root
        elif id_participante < root.id_participante:
            root.left = self.remove(root.left, id_participante)
        elif id_participante > root.id_participante:
            root.right = self.remove(root.right, id_participante)
        else:
            # Caso com um ou nenhum filho
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Caso com dois filhos
            temp = self.getMinValueNode(root.right)
            root.id_participante = temp.id_participante
            root.pontuacao = temp.pontuacao
            root.right = self.remove(root.right, temp.id_participante)

        if root is None:
            return root

        # Atualiza a altura do nó
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Realiza rotações conforme necessário para manter balanceado
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def search(self, root, id_participante):
        # Busca um participante pelo ID
        if root is None or root.id_participante == id_participante:
            return root
        if id_participante < root.id_participante:
            return self.search(root.left, id_participante)
        return self.search(root.right, id_participante)

    def update_score(self, id_participante, nova_pontuacao):
        node = self.search(self.root, id_participante)
        if node:
            node.pontuacao = nova_pontuacao

    def inorder(self, root, result):
        # Percorre a árvore em ordem e armazena os participantes
        if root:
            self.inorder(root.left, result)
            result.append((root.id_participante, root.pontuacao))
            self.inorder(root.right, result)

    def top_10(self, root):
        # Retorna os 10 participantes com maior pontuação
        result = []
        self.inorder(root, result)
        return sorted(result, key=lambda x: x[1], reverse=True)[:10]

    def getMinValueNode(self, root):
        # Retorna o nó com a menor pontuação
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def scores_above(self, root, threshold, result):
        # Retorna participantes com pontuação acima de um limite
        if root:
            if root.pontuacao >= threshold:
                self.scores_above(root.right, threshold, result)
                result.append((root.id_participante, root.pontuacao))
                self.scores_above(root.left, threshold, result)

    def min_score(self, root):
        # Retorna o participante com a menor pontuação
        if root is None:
            return None
        min_node = self.getMinValueNode(root)
        return (min_node.id_participante, min_node.pontuacao)

# Exemplo de uso
if __name__ == "__main__":
    tree = AVLTree()
    root = None
    root = tree.insert(root, "Cristiano", 50)
    root = tree.insert(root, "Messi", 70)
    root = tree.insert(root, "Vini", 40)

    print("Top 10:", tree.top_10(root))
    print("Menor pontuação:", tree.min_score(root))
    result = []
    tree.scores_above(root, 45, result)
    print("Pontuações acima de 45:", result)

