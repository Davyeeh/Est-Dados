import random
import time
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # Define se o nó é folha
        self.keys = []  # Lista de chaves (IDs dos clientes)
        self.children = []  # Lista de filhos (nós)
        self.records = [] if leaf else None  # Apenas folhas armazenam registros
        self.count = 0  # Número de registros no nó e seus filhos

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)  # Inicializa a árvore com um nó folha
        self.t = t  # Grau mínimo da árvore B

    def insert(self, id_cliente):
        """Insere um novo ID de cliente na árvore B"""
        root = self.root
        if len(root.keys) == (2 * self.t - 1):  # Se a raiz estiver cheia
            new_root = BTreeNode(False)  # Cria um novo nó raiz
            new_root.children.append(self.root)
            self.split_child(new_root, 0)  # Divide a raiz
            self.root = new_root
        self._insert_non_full(self.root, id_cliente)

    def _insert_non_full(self, node, id_cliente):
        """Insere um ID em um nó que não está cheio"""
        node.count += 1  # Atualiza a contagem
        if node.leaf:
            node.keys.append(id_cliente)
            node.keys.sort()
            node.records.append(id_cliente)
        else:
            i = len(node.keys) - 1
            while i >= 0 and id_cliente < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):  # Se o filho estiver cheio
                self.split_child(node, i)
                if id_cliente > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], id_cliente)

    def split_child(self, parent, i):
        """Divide um filho cheio do nó pai"""
        t = self.t
        node = parent.children[i]
        new_node = BTreeNode(node.leaf)
        parent.keys.insert(i, node.keys[t - 1])  # Move a chave do meio para o pai
        parent.children.insert(i + 1, new_node)  # Adiciona um novo filho
        new_node.keys = node.keys[t:]  # Metade superior das chaves vai para o novo nó
        node.keys = node.keys[:t - 1]  # Metade inferior permanece
        if node.leaf:
            new_node.records = node.records[t:]
            node.records = node.records[:t]
        else:
            new_node.children = node.children[t:]
            node.children = node.children[:t]
        new_node.count = len(new_node.keys) if new_node.leaf else sum(child.count for child in new_node.children)
        node.count = len(node.keys) if node.leaf else sum(child.count for child in node.children)
        parent.count = sum(child.count for child in parent.children)

    def search(self, node, id_cliente):
        """Busca um ID de cliente na árvore"""
        if node is None:
            return None
        i = 0
        while i < len(node.keys) and id_cliente > node.keys[i]:
            i += 1
        if i < len(node.keys) and id_cliente == node.keys[i]:
            return node.records[i] if node.leaf else self.search(node.children[i + 1], id_cliente)
        return self.search(node.children[i], id_cliente) if not node.leaf else None

    def remove(self, id_cliente):
        """Remove um ID de cliente da árvore"""
        self._remove(self.root, id_cliente)

    def _remove(self, node, id_cliente):
        """Método auxiliar para remoção"""
        if node.leaf:
            if id_cliente in node.keys:
                idx = node.keys.index(id_cliente)
                node.keys.pop(idx)
                node.records.pop(idx)
                node.count -= 1
        else:
            i = 0
            while i < len(node.keys) and id_cliente > node.keys[i]:
                i += 1
            if i < len(node.keys) and node.keys[i] == id_cliente:
                node.keys.pop(i)
                node.children[i].count -= 1
            else:
                self._remove(node.children[i], id_cliente)
            node.count -= 1

    def update(self, id_cliente, novo_id):
        """Atualiza um ID de cliente na árvore"""
        self.remove(id_cliente)
        self.insert(novo_id)

    def minimo(self):
        """Retorna o menor ID armazenado"""
        node = self.root
        while not node.leaf:
            node = node.children[0]
        return node.keys[0]

    def maximo(self):
        """Retorna o maior ID armazenado"""
        node = self.root
        while not node.leaf:
            node = node.children[-1]
        return node.keys[-1]

    def listar_intervalo(self, inicio, fim):
        """Retorna os IDs dentro do intervalo especificado"""
        result = []
        self._listar_intervalo(self.root, inicio, fim, result)
        return result

    def _listar_intervalo(self, node, inicio, fim, result):
        if node is None:
            return
        i = 0
        while i < len(node.keys) and node.keys[i] < inicio:
            i += 1
        while i < len(node.keys) and node.keys[i] <= fim:
            if node.leaf:
                result.append(node.records[i])
            else:
                self._listar_intervalo(node.children[i], inicio, fim, result)
                result.append(node.keys[i])
            i += 1
        if not node.leaf:
            self._listar_intervalo(node.children[i], inicio, fim, result)

    def contar_registros(self):
        """Retorna o número total de registros na árvore sem percorrê-la completamente"""
        return self.root.count

# Exemplo de uso
b_tree = BTree(3)
b_tree.insert(10)
b_tree.insert(20)
b_tree.insert(5)
b_tree.insert(6)
b_tree.insert(12)
b_tree.insert(30)
b_tree.insert(7)
b_tree.insert(17)

print("Mínimo:", b_tree.minimo())
print("Máximo:", b_tree.maximo())
print("Buscar 12:", b_tree.search(b_tree.root, 12))
print("Listar intervalo 6-17:", b_tree.listar_intervalo(6, 17))
print("Total de registros:", b_tree.contar_registros())

# Gerador aleatório e análise de tempo
tamanhos = [100, 1000, 10000, 1000000]
for tamanho in tamanhos:
    ids = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    # Medir tempo de inserção
    b_tree = BTree(3)
    inicio = time.time()
    for id_cliente in ids:
        b_tree.insert(id_cliente)
    fim = time.time()
    print(f"Tempo para inserir {tamanho} elementos: {fim - inicio:.6f} segundos")
    
    # Medir tempo de remoção
    inicio = time.time()
    for id_cliente in ids:
        b_tree.remove(id_cliente)
    fim = time.time()
    print(f"Tempo para remover {tamanho} elementos: {fim - inicio:.6f} segundos")