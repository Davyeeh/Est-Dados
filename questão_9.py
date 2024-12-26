class DequeEstatico:

    # Cria o deque com uma capacidade fixa
    def __init__(self, capacidade):
        self.capacidade = capacidade
        
        # Inicializa a lista com valores None
        self.deque = [None] * capacidade
        
        # Define os ponteiros de início e fim como -1
        self.inicio = -1
        self.fim = -1

    def inicializar_deque(self): # Reinicia o deque para o estado vazio
        
        # Limpa todos os elementos
        self.inicio = -1
        self.fim = -1

        # Reseta os ponteiros
        self.deque = [None] * self.capacidade
        
    def deque_e_vazia(self): # Verifica se o deque está vazio
        
        # Retorna True se início for -1
        return self.inicio == -1
        
    def deque_e_cheia(self): # Verifica se o deque está cheio

        # Considera casos de wrap-around na estrutura circular
        return (self.inicio == 0 and self.fim == self.capacidade - 1) or (self.inicio == self.fim + 1)
        
    def insere_inicio_deque(self, elemento): # Adiciona elemento no início do deque
        if self.deque_e_cheia():
            print("Erro: Deque cheia!")
            return False
        
        # Ajusta o ponteiro de início
        # Trata casos especiais (vazio e wrap-around)
        if self.inicio == -1:
            self.inicio = 0
            self.fim = 0
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1
            
        self.deque[self.inicio] = elemento
        return True
        
    def insere_final_deque(self, elemento): # Adiciona elemento no final do deque
        if self.deque_e_cheia():
            print("Erro: Deque cheia!")
            return False
        
        # Ajusta o ponteiro de fim
        # Trata casos especiais
        if self.inicio == -1:
            self.inicio = 0
            self.fim = 0
        elif self.fim == self.capacidade - 1:
            self.fim = 0
        else:
            self.fim += 1
            
        self.deque[self.fim] = elemento
        return True
        
    def remove_inicio_deque(self): # Remove e retorna elemento do início
        if self.deque_e_vazia():
            print("Erro: Deque vazia!")
            return None

        # Ajusta ponteiro de início
        elemento = self.deque[self.inicio]
        
        # Trata caso de último elemento
        if self.inicio == self.fim:
            self.inicio = -1
            self.fim = -1
        elif self.inicio == self.capacidade - 1:
            self.inicio = 0
        else:
            self.inicio += 1
            
        return elemento
        
    def remove_final_deque(self): # Remove e retorna elemento do final
        if self.deque_e_vazia():
            print("Erro: Deque vazia!")
            return None
        
        # Ajusta ponteiro de fim
        elemento = self.deque[self.fim]
        
        # Trata caso de último elemento
        if self.inicio == self.fim:
            self.inicio = -1
            self.fim = -1
        elif self.fim == 0:
            self.fim = self.capacidade - 1
        else:
            self.fim -= 1
            
        return elemento
        
    def imprimir(self): # Mostra elementos do início ao fim
        
        # Indica quando deque está vazio
        if self.deque_e_vazia():
            print("Deque vazia!")
            return
        # Trata casos de wrap-around na impressão
        print("Deque:", end=" ")
        if self.inicio <= self.fim:
            for i in range(self.inicio, self.fim + 1):
                print(self.deque[i], end=" ")
        else:
            for i in range(self.inicio, self.capacidade):
                print(self.deque[i], end=" ")
            for i in range(0, self.fim + 1):
                print(self.deque[i], end=" ")
        print()

deque = DequeEstatico(5)
deque.insere_inicio_deque(1)
deque.insere_final_deque(2)
deque.insere_inicio_deque(3)
deque.imprimir()
deque.remove_inicio_deque()
deque.remove_final_deque()
deque.imprimir()
