import random
import time

class DequeEstatico:
    def __init__(self, capacidade): # Cria o deque com capacidade definida e inicializa ponteiros
        self.capacidade = capacidade
        self.deque = [None] * capacidade
        self.inicio = -1
        self.fim = -1
        
    def inicializar_deque(self): # Reseta o deque e mede tempo da operação
        inicio_tempo = time.time()
        self.inicio = -1
        self.fim = -1
        self.deque = [None] * self.capacidade
        fim_tempo = time.time()
        return fim_tempo - inicio_tempo
        
    def deque_e_vazia(self): # Verifica se está vazio e retorna tempo da verificação
        inicio_tempo = time.time()
        resultado = self.inicio == -1
        fim_tempo = time.time()
        return resultado, fim_tempo - inicio_tempo
        
    def deque_e_cheia(self): # Verifica se está cheio considerando estrutura circular
        inicio_tempo = time.time()
        resultado = (self.inicio == 0 and self.fim == self.capacidade - 1) or (self.inicio == self.fim + 1)
        fim_tempo = time.time()
        return resultado, fim_tempo - inicio_tempo
        
    def insere_inicio_deque(self, elemento): # Adiciona elemento no início e mede tempo
        inicio_tempo = time.time()
        if self.deque_e_cheia()[0]:
            fim_tempo = time.time()
            return False, fim_tempo - inicio_tempo
            
        if self.inicio == -1:
            self.inicio = 0
            self.fim = 0
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1
            
        self.deque[self.inicio] = elemento
        fim_tempo = time.time()
        return True, fim_tempo - inicio_tempo
        
    def insere_final_deque(self, elemento): # Adiciona elemento no final e mede tempo
        inicio_tempo = time.time()
        if self.deque_e_cheia()[0]:
            fim_tempo = time.time()
            return False, fim_tempo - inicio_tempo
            
        if self.inicio == -1:
            self.inicio = 0
            self.fim = 0
        elif self.fim == self.capacidade - 1:
            self.fim = 0
        else:
            self.fim += 1
            
        self.deque[self.fim] = elemento
        fim_tempo = time.time()
        return True, fim_tempo - inicio_tempo
        
    def remove_inicio_deque(self): # Remove do início e retorna elemento com tempo
        inicio_tempo = time.time()
        if self.deque_e_vazia()[0]:
            fim_tempo = time.time()
            return None, fim_tempo - inicio_tempo
            
        elemento = self.deque[self.inicio]
        
        if self.inicio == self.fim:
            self.inicio = -1
            self.fim = -1
        elif self.inicio == self.capacidade - 1:
            self.inicio = 0
        else:
            self.inicio += 1
            
        fim_tempo = time.time()
        return elemento, fim_tempo - inicio_tempo
        
    def remove_final_deque(self): # Remove do final e retorna elemento com tempo
        inicio_tempo = time.time()
        if self.deque_e_vazia()[0]:
            fim_tempo = time.time()
            return None, fim_tempo - inicio_tempo
            
        elemento = self.deque[self.fim]
        
        if self.inicio == self.fim:
            self.inicio = -1
            self.fim = -1
        elif self.fim == 0:
            self.fim = self.capacidade - 1
        else:
            self.fim -= 1
            
        fim_tempo = time.time()
        return elemento, fim_tempo - inicio_tempo

def testar_deque(tamanho): # Função para análise de performance
    # Realiza testes com diferentes volumes de dados
    print(f"\nTestando com {tamanho} elementos:")
    deque = DequeEstatico(tamanho)
    
    # Teste de inicialização
    tempo_init = deque.inicializar_deque()
    # Mede tempos de inicialização
    print(f"Tempo de inicialização: {tempo_init:.8f} segundos")
    
    # Teste de inserção no início
    tempo_total_insercao_inicio = 0
    valores = random.sample(range(1, tamanho*10), tamanho//2)
    for valor in valores:
        _, tempo = deque.insere_inicio_deque(valor)
        tempo_total_insercao_inicio += tempo
    # Calcula médias de tempo para inserções no início
    print(f"Tempo médio de inserção no início: {tempo_total_insercao_inicio/(tamanho//2):.8f} segundos")
    
    # Teste de inserção no final
    tempo_total_insercao_final = 0
    valores = random.sample(range(1, tamanho*10), tamanho//2)
    for valor in valores:
        _, tempo = deque.insere_final_deque(valor)
        tempo_total_insercao_final += tempo
        # Calcula médias de tempo para inserções no fim
    print(f"Tempo médio de inserção no final: {tempo_total_insercao_final/(tamanho//2):.8f} segundos")
    
    # Teste de remoção do início
    tempo_total_remocao_inicio = 0
    for _ in range(tamanho//4):
        _, tempo = deque.remove_inicio_deque()
        tempo_total_remocao_inicio += tempo
    #Calcula médias de tempo para remoções do início
    print(f"Tempo médio de remoção do início: {tempo_total_remocao_inicio/(tamanho//4):.8f} segundos")
    
    # Teste de remoção do final
    tempo_total_remocao_final = 0
    for _ in range(tamanho//4):
        _, tempo = deque.remove_final_deque()
        tempo_total_remocao_final += tempo
    # Calcula médias de tempo para remoções do fim
    print(f"Tempo médio de remoção do final: {tempo_total_remocao_final/(tamanho//4):.8f} segundos")

# Testando com diferentes tamanhos
tamanhos = [100, 1000, 10000, 1000000]
for tamanho in tamanhos:
    testar_deque(tamanho)

# Executa testes com 100, 1.000, 10.000 e 1.000.000 elementos
# Gera valores aleatórios para testes
# Exibe métricas de tempo para cada operação
# Permite análise comparativa de performance
