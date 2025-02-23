import random
import time

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.collisions = 0  # Contador de colisões

    def _hash_function(self, key):
        return hash(key) % self.capacity

    def inserir(self, key, value):
        index = self._hash_function(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  # Atualiza o valor se a chave já existe
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]  # Insere no início da lista encadeada
            self.table[index] = new_node
            self.size += 1
            self.collisions += 1  # Incrementa o contador de colisões

            # Verifica se precisa fazer rehashing
            if self.size > self.capacity * 0.75:  # Limiar de 75%
                self._rehash()

    def remover(self, key):
        index = self._hash_function(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def buscar(self, key):
        index = self._hash_function(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def tamanho(self):
        return self.size

    def verificar_colisao(self, key):
        index = self._hash_function(key)
        return self.table[index] is not None and self.table[index].next is not None  # Verifica se há mais de um nó no índice

    def _rehash(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity
        old_table = self.table
        self.capacity = new_capacity
        self.table = new_table
        self.size = 0
        self.collisions = 0  # Reseta o contador de colisoes

        for i in range(len(old_table)):
            current = old_table[i]
            while current:
                self.inserir(current.key, current.value)  # Reinsere os elementos na nova tabela
                current = current.next

    def contar_colisoes(self):
        return self.collisions

# Função para medir o tempo de execução de uma operação
def measure_time(operation, *args):
    start_time = time.time()
    operation(*args)
    end_time = time.time()
    return end_time - start_time

# Função para gerar dados aleatórios
def generate_random_data(size):
    return [(f"Item_{i}", random.randint(1, 100)) for i in range(size)]

# Função para medir o tempo de inclusão de dados na tabela hash
def measure_insertion_time(hash_table, data):
    for key, value in data:
        hash_table.inserir(key, value)

# Função para medir o tempo de remoção de dados da tabela hash
def measure_removal_time(hash_table, data):
    for key, _ in data:
        try:
            hash_table.remover(key)
        except KeyError:
            pass

# Tamanhos dos dados
sizes = [100, 1000, 10000, 1000000]

# Medir tempos de inclusão e remoção para cada tamanho
for size in sizes:
    data = generate_random_data(size)
    hash_table = MyHash(size * 2)  # Inicializa a tabela hash com o dobro da capacidade para reduzir colisões
    
    # Medir tempo de inclusão
    insertion_time = measure_time(measure_insertion_time, hash_table, data)
    print(f"Tamanho: {size}, Tempo de inclusão: {insertion_time:.4f} segundos")
    
    # Medir tempo de remoção
    removal_time = measure_time(measure_removal_time, hash_table, data)
    print(f"Tamanho: {size}, Tempo de remoção: {removal_time:.4f} segundos")

# Driver code
if __name__ == '__main__':
    ht = MyHash(5)

    ht.inserir("lapis", 3)
    ht.inserir("caderno", 2)
    ht.inserir("caneta", 5)
    ht.inserir("borracha", 7)
    ht.inserir("regua", 9)
    ht.inserir("apontador", 11)
    ht.inserir("mochila", 13)

    print("\n*** Verificando se alguns itens estão na tabela: ***\n")
    # método buscar para verificar a existência da chave
    try:
        ht.buscar("lapis")
        print("lapis está na tabela")
    except KeyError:
        print("lapis não está na tabela")

    try:
        ht.buscar("estojo")
        print("estojo está na tabela")
    except KeyError:
        print("estojo não está na tabela")

    print(f"O caderno está no slot {ht.buscar("caderno")}")  # 2

    ht.inserir("caderno", 4)
    print(f"Atualizando o slot de caderno para o slot {ht.buscar("caderno")}")  # 4

    ht.remover("lapis")
    print(f"Tamanho da hash depois de remover 'lapis': {ht.tamanho()}")  # 6

    print("\n *** Verificando colisões, se True houve colisão, senão False ***\n")
    print(f"Caderno: {ht.verificar_colisao("caderno")}")  # True, pois "caderno" colidiu com outros elementos
    print(f"Borracha: {ht.verificar_colisao("borracha")}")  # True, pois "borracha" colidiu com outros elementos
    print(f"Apontador: {ht.verificar_colisao("apontador")}")  # True, pois "apontador" colidiu com outros elementos
    print(f"Mochila: {ht.verificar_colisao("mochila")}")  # True, pois "mochila" colidiu com outros elementos
    print(f"Estojo: {ht.verificar_colisao("estojo")}")  # False, pois "estojo" não está na tabela

    print(f"\nNúmero de colisões: {ht.contar_colisoes()}")  # Imprime o número de colisões

    print(f"Capacidade da tabela: {ht.capacity}")  # Imprime a capacidade da tabela após o rehashing