'''Estrutura à fins de estudo:
Neste cenário, estava estudando princípios básicos, mas fundamentais, de "lista encadeada".
Trabalho este necessário também com princípios de OPP (Programação orientada a objetos).'''

class Node: #Classe base NODE.
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        
        new_node = Node(data)

        if self.head == None:
            self.head = new_node #Define a "head" como um novo nó.
            return
        
        current_node = self.head #Define a "head como nó atual".

        while current_node.next: #Percorre a lista, com os elementos presentes até o instante.
            current_node = current_node.next #Dá sequência, percorrendo até finalizar em FALSE o while.
        
        current_node.next = new_node
        return
    
    def length(self): #Comprimento de lista.
        if self.head == None: #Se não existir "head", logo a list é nula.
            return 0
        
        current_node = self.head #Parte do primeiro parâmentro: Head da lista.
        total = 0 #Inicia contador.

        while current_node: #Percorre a lista.
            total += 1 #Adiciona '+1' ao contador.
            current_node = current_node.next #Dá sequência, percorrendo até finalizar em FALSE o while.
        return total

    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data
    
    def display(self):
        contents = self.head

        if contents is None:
            print('A lista não tem elementos.')
            return
        
        while contents:
            print(contents.data)
            contents = contents.next
        print('---------')

#--
my_list = LinkedList()
my_list.display() #Exibindo uma mensagem, no caso de a lista estar vazia.

my_list.append(60)
my_list.append(102)
my_list.append(50)
my_list.append(200)

my_list.display() #Exibindo um display. Desta vez, com conteúdo.

print("O número total de elementos é: " + str(my_list.length()))
print(my_list.to_list())

