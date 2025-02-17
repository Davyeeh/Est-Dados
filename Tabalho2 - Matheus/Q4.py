import random
import time

class Node:
    def __init__(self, id_participante, pontuacao):
        self.id_participante = id_participante
        self.pontuacao = pontuacao
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, id_participante, pontuacao):
        if not root:
            return Node(id_participante, pontuacao)
        elif id_participante < root.id_participante:
            root.left = self.insert(root.left, id_participante, pontuacao)
        elif id_participante > root.id_participante:
            root.right = self.insert(root.right, id_participante, pontuacao)
        else:
            root.pontuacao = pontuacao

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

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
        if not root:
            return root
        elif id_participante < root.id_participante:
            root.left = self.remove(root.left, id_participante)
        elif id_participante > root.id_participante:
            root.right = self.remove(root.right, id_participante)
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
            root.id_participante = temp.id_participante
            root.pontuacao = temp.pontuacao
            root.right = self.remove(root.right, temp.id_participante)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

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
        if root is None or root.id_participante == id_participante:
            return root
        if id_participante < root.id_participante:
            return self.search(root.left, id_participante)
        return self.search(root.right, id_participante)

    def update_score(self, root, id_participante, nova_pontuacao):
        node = self.search(root, id_participante)
        if node:
            node.pontuacao = nova_pontuacao

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append((root.id_participante, root.pontuacao))
            self.inorder(root.right, result)

    def top_10(self, root):
        result = []
        self.inorder(root, result)
        return sorted(result, key=lambda x: x[1], reverse=True)[:10]

    def min_score(self, root):
        min_node = self.getMinValueNode(root)
        return (min_node.id_participante, min_node.pontuacao) if min_node else None

    def scores_above(self, root, threshold, result):
        if root:
            if root.pontuacao >= threshold:
                self.scores_above(root.right, threshold, result)
                result.append((root.id_participante, root.pontuacao))
                self.scores_above(root.left, threshold, result)

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
