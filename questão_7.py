class No:
    # Cria nós que armazenam um valor e uma referência para o próximo nó
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class FilaCircular:

    # Cria uma fila vazia definindo os ponteiros de início e fim como None
    def __init__(self): 
        self.inicio = None
        self.fim = None
        
    # Reinicia a fila para o estado vazio
    def inicializar_fila(self):
        self.inicio = None
        self.fim = None

    # Retorna True se a fila não tem elementos (início é None)
    def fila_e_vazia(self):
        return self.inicio is None
    

    # Sempre retorna False pois é uma implementação dinâmica
    def fila_e_cheia(self):
        return False
    
    def insere_fila(self, valor):

        # Cria um novo nó com o valor fornecido
        novo_no = No(valor)

        # Se a fila estiver vazia: novo nó aponta para si mesmo e se torna início e fim.
        if self.fila_e_vazia():
            self.inicio = novo_no
            self.fim = novo_no
            novo_no.proximo = novo_no
        # Se não estiver vazia: liga o novo nó no final mantendo a estrutura circular
        else:
            novo_no.proximo = self.inicio
            self.fim.proximo = novo_no
            self.fim = novo_no
    
    def remove_fila(self):
        #Retorna None se a fila estiver vazia
        if self.fila_e_vazia():
            print("Erro: Fila vazia!")
            return None
        
        #Armazena o valor a ser retornado
        valor = self.inicio.valor

        # Se tiver apenas um elemento: reinicia a fila para vazia
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        # Se tiver múltiplos elementos: avança o ponteiro de início e mantém o link circular
        else:
            self.inicio = self.inicio.proximo
            self.fim.proximo = self.inicio
        
        #Retorna o valor removido
        return valor
        
    def imprimir(self):

        # Mostra "Fila vazia!" se estiver vazia
        if self.fila_e_vazia():
            print("Fila vazia!")
            return
        
        # Caso contrário imprime todos os elementos do início ao fim
        atual = self.inicio
        print("Fila:", end=" ")

        # Usa a propriedade circular para saber quando parar (quando chegar ao início novamente)
        while True:
            print(atual.valor, end=" ")
            atual = atual.proximo
            if atual == self.inicio:
                break
        print()


fila = FilaCircular()
fila.insere_fila(1)
fila.insere_fila(2)
fila.insere_fila(3)
fila.imprimir()
fila.remove_fila()
fila.imprimir()
