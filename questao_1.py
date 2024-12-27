import time

class PilhaEstatica:
    def __init__(self, capacidade):
        """
        Inicializa a pilha com uma capacidade fixa.
        :param capacidade: Tamanho máximo da pilha.
        Complexidade: O(n), onde n é a capacidade da pilha, devido à inicialização da lista.
        """
        self.capacidade = capacidade
        self.pilha = [None] * capacidade  # Alocação estática com lista fixa
        self.topo = -1  # Índice do topo da pilha, -1 indica pilha vazia

    def inicializar_pilha(self):
        """
        Inicializa a pilha, limpando seu conteúdo.
        Complexidade: O(n), onde n é a capacidade da pilha.
        """
        self.pilha = [None] * self.capacidade
        self.topo = -1

    def pilha_e_vazia(self):
        """
        Verifica se a pilha está vazia.
        :return: True se vazia, False caso contrário.
        Complexidade: O(1).
        """
        return self.topo == -1

    def pilha_e_cheia(self):
        """
        Verifica se a pilha está cheia.
        :return: True se cheia, False caso contrário.
        Complexidade: O(1).
        """
        return self.topo == self.capacidade - 1

    def empilha(self, elemento):
        """
        Adiciona um elemento ao topo da pilha.
        :param elemento: Valor a ser adicionado.
        Complexidade: O(1).
        """
        inicio = time.time()
        if self.pilha_e_cheia():
            print("Erro: Pilha cheia!")
            return False
        self.topo += 1
        self.pilha[self.topo] = elemento
        fim = time.time()
        print(f"Tempo para empilhar: {fim - inicio:.8f} segundos")
        return True

    def desempilha(self):
        """
        Remove e retorna o elemento do topo da pilha.
        :return: Elemento removido ou None se a pilha estiver vazia.
        Complexidade: O(1).
        """
        inicio = time.time()
        if self.pilha_e_vazia():
            print("Erro: Pilha vazia!")
            return None
        elemento = self.pilha[self.topo]
        self.pilha[self.topo] = None  # Limpa o espaço na lista
        self.topo -= 1
        fim = time.time()
        print(f"Tempo para desempilhar: {fim - inicio:.8f} segundos")
        return elemento

    def le_topo(self):
        """
        Lê o elemento no topo da pilha sem removê-lo.
        :return: Elemento do topo ou None se a pilha estiver vazia.
        Complexidade: O(1).
        """
        inicio = time.time()
        if self.pilha_e_vazia():
            print("Erro: Pilha vazia!")
            return None
        fim = time.time()
        print(f"Tempo para ler o topo: {fim - inicio:.8f} segundos")
        return self.pilha[self.topo]

    def imprimir(self):
        """
        Imprime os elementos da pilha do topo para a base.
        Complexidade: O(n), onde n é o número de elementos na pilha.
        """
        inicio = time.time()
        if self.pilha_e_vazia():
            print("Pilha vazia!")
        else:
            print("Pilha (topo -> base):", end=" ")
            for i in range(self.topo, -1, -1):
                print(self.pilha[i], end=" ")
            print()
        fim = time.time()
        print(f"Tempo para imprimir: {fim - inicio:.8f} segundos")

    def imprimir_reversa(self):
        """
        Imprime os elementos da pilha da base para o topo.
        Complexidade: O(n), onde n é o número de elementos na pilha.
        """
        inicio = time.time()
        if self.pilha_e_vazia():
            print("Pilha vazia!")
        else:
            print("Pilha (base -> topo):", end=" ")
            for i in range(0, self.topo + 1):
                print(self.pilha[i], end=" ")
            print()
        fim = time.time()
        print(f"Tempo para imprimir reverso: {fim - inicio:.8f} segundos")

    def liberar(self):
        """
        Libera todos os elementos da pilha.
        Complexidade: O(n), onde n é a capacidade da pilha.
        """
        inicio = time.time()
        self.inicializar_pilha()
        fim = time.time()
        print(f"Tempo para liberar a pilha: {fim - inicio:.8f} segundos")
        print("Pilha liberada!")

    def palindromo(self, string):
        """
        Verifica se uma string é um palíndromo usando a pilha.
        :param string: String a ser verificada.
        :return: True se for palíndromo, False caso contrário.
        Complexidade: O(n), onde n é o comprimento da string.
        """
        inicio = time.time()
        self.inicializar_pilha()
        for char in string:
            self.empilha(char)

        for char in string:
            if char != self.desempilha():
                fim = time.time()
                print(f"Tempo para verificar palíndromo: {fim - inicio:.8f} segundos")
                return False
        fim = time.time()
        print(f"Tempo para verificar palíndromo: {fim - inicio:.8f} segundos")
        return True

    def elimina(self, elemento):
        """
        Elimina um elemento específico da pilha, mantendo a ordem original.
        :param elemento: Elemento a ser removido.
        Complexidade: O(n), onde n é o número de elementos na pilha.
        """
        inicio = time.time()
        auxiliar = PilhaEstatica(self.capacidade)
        encontrado = False

        while not self.pilha_e_vazia():
            atual = self.desempilha()
            if atual == elemento and not encontrado:
                encontrado = True
                print(f"Elemento {elemento} removido!")
            else:
                auxiliar.empilha(atual)

        while not auxiliar.pilha_e_vazia():
            self.empilha(auxiliar.desempilha())

        fim = time.time()
        print(f"Tempo para eliminar elemento: {fim - inicio:.8f} segundos")

        if not encontrado:
            print(f"Elemento {elemento} não encontrado na pilha!")

    def pares_e_impares(self, valores):
        """
        Distribui os valores em duas pilhas: uma com os números pares e outra com os ímpares.
        :param valores: Lista de valores a serem inseridos.
        :return: Tupla com as pilhas de pares e ímpares.
        Complexidade: O(n), onde n é o número de valores fornecidos.
        """
        inicio = time.time()
        pares = PilhaEstatica(self.capacidade)
        impares = PilhaEstatica(self.capacidade)

        for valor in valores:
            self.empilha(valor)
            if valor % 2 == 0:
                pares.empilha(valor)
            else:
                impares.empilha(valor)

        print("Pilha original:")
        self.imprimir()
        print("Pilha de pares:")
        pares.imprimir()
        print("Pilha de ímpares:")
        impares.imprimir()

        fim = time.time()
        print(f"Tempo para distribuir pares e ímpares: {fim - inicio:.8f} segundos")
        return pares, impares

# Testando a TAD PilhaEstatica
if __name__ == "__main__":
    print("--- Teste da TAD Pilha Estática ---")
    pilha = PilhaEstatica(5)

    # Teste de empilhamento
    print("\nEmpilhando elementos: 10, 20, 30")
    pilha.empilha(10)
    pilha.empilha(20)
    pilha.empilha(30)
    pilha.imprimir()

    # Teste de desempilhamento
    print("\nDesempilhando elemento")
    pilha.desempilha()
    pilha.imprimir()

    # Teste de leitura do topo
    print("\nLendo o topo da pilha")
    print(f"Topo: {pilha.le_topo()}")

    # Teste de impressão reversa
    print("\nImprimindo reverso")
    pilha.imprimir_reversa()

    # Teste de palíndromo
    print("\nTestando palíndromo com a palavra 'radar'")
    palavra = "radar"
    print(f"'{palavra}' é palíndromo? {pilha.palindromo(palavra)}")

    # Teste de eliminação
    print("\nTestando eliminação do elemento 20")
    pilha.empilha(40)
    pilha.empilha(20)
    pilha.empilha(50)
    pilha.imprimir()
    pilha.elimina(20)
    pilha.imprimir()

    # Teste de pares e ímpares
    print("\nTestando pares e ímpares com os valores [1, 2, 3, 4, 5, 6]")
    valores = [1, 2, 3, 4, 5, 6]
    pilha.inicializar_pilha()
    pilha.pares_e_impares(valores)
