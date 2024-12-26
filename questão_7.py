import random
import time
from typing import List

class No: # Define a estrutura básica de um nó
    #Armazena um valor e referência ao próximo nó
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class FilaCircular:
    def __init__(self): # Cria fila vazia inicializando ponteiros
        self.inicio = None
        self.fim = None
        
    def inicializar_fila(self): # Limpa a fila e mede tempo de execução
        inicio_tempo = time.time()
        self.inicio = None
        self.fim = None
        fim_tempo = time.time()
        return fim_tempo - inicio_tempo
        
    def fila_e_vazia(self):# Verifica se fila está vazia e retorna tempo da operação
        inicio_tempo = time.time()
        resultado = self.inicio is None
        fim_tempo = time.time()
        return resultado, fim_tempo - inicio_tempo
        
    def fila_e_cheia(self): # Sempre retorna falso (implementação dinâmica) e mede tempo
        inicio_tempo = time.time()
        resultado = False
        fim_tempo = time.time()
        return resultado, fim_tempo - inicio_tempo
        
    def insere_fila(self, valor): # Adiciona elemento no final da fila e mede tempo de inserção
        inicio_tempo = time.time()
        novo_no = No(valor)
        if self.fila_e_vazia()[0]:
            self.inicio = novo_no
            self.fim = novo_no
            novo_no.proximo = novo_no
        else:
            novo_no.proximo = self.inicio
            self.fim.proximo = novo_no
            self.fim = novo_no
        fim_tempo = time.time()
        return fim_tempo - inicio_tempo
            
    def remove_fila(self): # Remove elemento do início e retorna tempo da remoção
        inicio_tempo = time.time()
        if self.fila_e_vazia()[0]:
            fim_tempo = time.time()
            return None, fim_tempo - inicio_tempo
            
        valor = self.inicio.valor
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.fim.proximo = self.inicio
            
        fim_tempo = time.time()
        return valor, fim_tempo - inicio_tempo
        
    def imprimir(self): # Mostra elementos do início ao fim com tempo de impressão
        inicio_tempo = time.time()
        if self.fila_e_vazia()[0]:
            print("Fila vazia!")
            fim_tempo = time.time()
            return fim_tempo - inicio_tempo
            
        atual = self.inicio
        elementos = []
        while True:
            elementos.append(str(atual.valor))
            atual = atual.proximo
            if atual == self.inicio:
                break
        print("Fila:", " ".join(elementos))
        fim_tempo = time.time()
        return fim_tempo - inicio_tempo

def testar_fila(tamanho: int): # Função para testar performance com diferentes tamanhos
    # Cria fila e gera valores aleatórios
    print(f"\nTestando com {tamanho} elementos:")
    fila = FilaCircular()
    
    # Mede tempos de inicialização
    # Teste de inicialização
    tempo_init = fila.inicializar_fila()
    print(f"Tempo de inicialização: {tempo_init:.8f} segundos")
    
    # Teste de inserção
    tempo_total_insercao = 0
    valores = random.sample(range(1, tamanho*10), tamanho)
    for valor in valores:
        tempo_total_insercao += fila.insere_fila(valor)
    # Calcula média de tempo para inserções
    print(f"Tempo médio de inserção: {tempo_total_insercao/tamanho:.8f} segundos")
    
    # Teste de remoção
    tempo_total_remocao = 0
    for _ in range(tamanho):
        _, tempo = fila.remove_fila()
        tempo_total_remocao += tempo
    # Calcula média de tempo para remoções
    print(f"Tempo médio de remoção: {tempo_total_remocao/tamanho:.8f} segundos")

# Testando com diferentes tamanhos
tamanhos = [100, 1000, 10000, 1000000]
for tamanho in tamanhos:
    testar_fila(tamanho)

# Testa com arrays de 100, 1.000, 10.000 e 1.000.000 elementos
# Exibe resultados de performance para cada tamanho
# Permite comparação de eficiência entre diferentes volumes de dados
# Usa amostragem aleatória para dados mais realistas
