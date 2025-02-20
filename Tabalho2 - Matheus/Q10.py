import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor): # Insere um valor no heap.
        heapq.heappush(self.heap, valor)

    def remover(self): # Remove o valor mínimo (raiz) do heap.
        return heapq.heappop(self.heap)

    def construir_heap(self, lista): # Constrói o heap a partir de uma lista de elementos.
        self.heap = lista[:]
        heapq.heapify(self.heap)

    def heapify(self):  # Reorganiza a árvore para garantir a propriedade do heap.
        heapq.heapify(self.heap)

    def heap_maximo(self): # Retorna o maior valor presente no heap.
        return max(self.heap)

def heapsort(lista): # Ordena uma lista usando o algoritmo Heapsort.
    heap = MinHeap()
    heap.construir_heap(lista)
    sorted_list = []
    while heap.heap:
        sorted_list.append(heap.remover())
    return sorted_list

def encontrar_5_maiores(lista): # Encontra os 5 maiores valores em uma lista utilizando heap.
    heap = MinHeap()
    heap.construir_heap(lista)
    return heapq.nlargest(5, heap.heap)

def construir_heap_a_partir_de_lista(lista): # Constrói um heap a partir de uma lista de números sem precisar inserir os elementos um a um.
    heap = MinHeap()
    heap.construir_heap(lista)
    return heap

# Exemplo de uso
if __name__ == "__main__":
    import random
    import time

    tamanhos = [100, 1000, 10000, 1000000]
    for tamanho in tamanhos:
        lista = [random.randint(1, 1000000) for _ in range(tamanho)]
        
        # Medir tempo de construção do heap
        inicio = time.time()
        heap = construir_heap_a_partir_de_lista(lista)
        fim = time.time()
        print(f"Tempo para construir heap com {tamanho} elementos: {fim - inicio:.6f} segundos")
        
        # Medir tempo de heapsort
        inicio = time.time()
        sorted_list = heapsort(lista)
        fim = time.time()
        print(f"Tempo para heapsort com {tamanho} elementos: {fim - inicio:.6f} segundos")
        
        # Medir tempo para encontrar os 5 maiores
        inicio = time.time()
        maiores = encontrar_5_maiores(lista)
        fim = time.time()
        print(f"Tempo para encontrar os 5 maiores com {tamanho} elementos: {fim - inicio:.6f} segundos")
        
        # Medir tempo de inserção
        heap = MinHeap()
        inicio = time.time()
        for valor in lista:
            heap.inserir(valor)
        fim = time.time()
        print(f"Tempo para inserir {tamanho} elementos: {fim - inicio:.6f} segundos")
        
        # Medir tempo de remoção
        inicio = time.time()
        while heap.heap:
            heap.remover()
        fim = time.time()
        print(f"Tempo para remover {tamanho} elementos: {fim - inicio:.6f} segundos")