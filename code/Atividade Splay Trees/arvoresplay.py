
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.pai = None

class ArvoreSplay:
    def __init__(self):
        self.raiz = None

    #faz a rotação zig esquerda
    def zig_esquerda(self, x):
        y = x.dir #define o y
        x.dir = y.esq #transforma a subarvore a esquerda de y na subarvore direita de x
        if (y.esq != None): #se subarvore esquerda de y vazia entao o pai sera o x
            y.esq.pai = x
        y.pai = x.pai #liga o pai de x a y
        if (x.pai == None): 
            self.raiz = y
        elif (x == x.pai.esq):
            x.pai.esq = y
        else:
            x.pai.dir = y
        y.esq = x
        x.pai = y

    #faz a rotação zig direita
    def zig_direita(self, x):
        y = x.esq #define o y
        x.esq = y.dir #transforma a subarvore a esquerda de x na subarvore direita de y
        if (y.dir != None): #se subarvore direita de y vazia entao o pai sera o x
            y.dir.pai = x
        y.pai = x.pai #liga o pai de x a y
        if (x.pai == None):
            self.raiz = y
        elif (x == x.pai.dir):
            x.pai.dir = y
        else:
            x.pai.esq = y
        y.dir = x
        x.pai = y


    def busca(self, valor):
        if (self.raiz == None):
            return False
        atual = self.raiz
        while True: #faz a busca ate encontrar o no
            if (valor == atual.valor): #se existir o elemento na arvore faz splay
                self.raiz = self.splay(atual)
                return True
            elif (valor < atual.valor):
                if (atual.esq == None): #caso nao encontre o elemento entao faz com o seu sucessor
                    self.raiz = self.splay(atual)
                    return False
                atual = atual.esq
            else:
                if (atual.dir == None): #caso nao encontre o elemento entao faz com o seu antecessor
                    self.raiz = self.splay(atual)
                    return False
                atual = atual.dir


    def insere(self, valor):
        no_insere = No(valor)
        if (self.raiz == None):
            self.raiz = no_insere
            return
        atual = self.raiz
        while True: # faz a busca ate encontrar o no
            if (valor < atual.valor):
                if (atual.esq == None): #caso nao encontre o elemento faz sua insercao e faz splay nele
                    atual.esq = no_insere
                    no_insere.pai = atual
                    break
                atual = atual.esq
            elif (valor > atual.valor): #caso nao encontre o elemento faz sua insercao e faz splay nele
                if (atual.dir == None):
                    atual.dir = no_insere
                    no_insere.pai = atual
                    break
                atual = atual.dir
            else: #se existe elemento entao sai do loop e faz splay nele
                return
        self.raiz = self.splay(no_insere)


    def insere_sem_splay(self, valor):
        no_insere = No(valor)
        if (self.raiz == None):
            self.raiz = no_insere
            return
        atual = self.raiz
        while True: # faz a busca ate encontrar o no
            if (valor < atual.valor):
                if (atual.esq == None): #caso nao encontre o elemento faz sua insercao e faz splay nele
                    atual.esq = no_insere
                    no_insere.pai = atual
                    break
                atual = atual.esq
            elif (valor > atual.valor): #caso nao encontre o elemento faz sua insercao e faz splay nele
                if (atual.dir == None):
                    atual.dir = no_insere
                    no_insere.pai = atual
                    break
                atual = atual.dir
            else: #se existe elemento entao sai do loop
                return



    
    #faz o splay do no
    def splay(self, atual):
            while (atual.pai != None): #ate o no atual ser a raiz da arvore
                if (atual.pai.pai == None): #faz uma rotacao simples zig dependendo de onde o atual esta
                    if (atual == atual.pai.esq): #se atual for subarvore esquerda da raiz faz rotacao zig direita
                        print("fazendo zig direita " + str(atual.valor))
                        self.zig_direita(atual.pai)
                    else: #se atual for subarvore direita da raiz faz rotacao zig esquerda
                        print("fazendo zig esquerda " + str(atual.valor))
                        self.zig_esquerda(atual.pai)
                elif ((atual == atual.pai.esq) and (atual.pai == atual.pai.pai.esq)): # faz rotacao zig zig direita
                    print("fazendo zig zig direita " + str(atual.valor))
                    self.zig_direita(atual.pai.pai)
                    self.zig_direita(atual.pai)
                elif ((atual == atual.pai.dir) and (atual.pai == atual.pai.pai.dir)): # faz rotacao zig zig esquerda
                    print("fazendo zig zig esquerda " + str(atual.valor))
                    self.zig_esquerda(atual.pai.pai)
                    self.zig_esquerda(atual.pai)
                elif ((atual == atual.pai.dir) and (atual.pai == atual.pai.pai.esq)): # faz rotacao zig zag esquerda e direita
                    print("fazendo zig zag esquerda e direita " + str(atual.valor))
                    self.zig_esquerda(atual.pai)
                    self.zig_direita(atual.pai)
                else: # faz rotacao zig zag direita e esquerda
                    print("fazendo zig zag direita e esquerda " + str(atual.valor))
                    self.zig_direita(atual.pai)
                    self.zig_esquerda(atual.pai)
            return atual
    


    def remove(self, valor):
        if (self.raiz == None):
            return
        self.busca(valor) #faz a busca do elemento na arvore
        if (self.raiz.valor != valor): #se o valor nao for encontrado entao nao faz nada
            return
        if (self.raiz.esq == None): # se valor encontrado e subarvore esquerda vazia a raiz sera a subarvore direita
            self.raiz = self.raiz.dir
            if (self.raiz != None): # se raiz nao for nulo(arvore vazia) o pai da raiz sera vazio
                self.raiz.pai = None
        elif (self.raiz.dir == None): # se valor encontrado e subarvore direita vazia a raiz sera a subarvore esquerda
            self.raiz = self.raiz.esq
            if (self.raiz != None): # se raiz nao for nulo(arvore vazia) o pai da raiz sera vazio
                self.raiz.pai = None
        else:
            sucessor = self.raiz.dir
            while sucessor.esq is not None:
                sucessor = sucessor.esq
            if self.raiz.dir != sucessor:
                sucessor.pai.esq = sucessor.dir
                if sucessor.dir is not None:
                    sucessor.dir.pai = sucessor.pai
                sucessor.dir = self.raiz.dir
                self.raiz.dir.pai = sucessor
            sucessor.esq = self.raiz.esq
            self.raiz.esq.pai = sucessor
            pai = self.raiz.pai
            if pai is None:
                self.raiz = sucessor
            elif self.raiz == pai.esq:
                pai.esq = sucessor
            else:
                pai.dir = sucessor
            sucessor.pai = pai


    def pre_ordem(self, no):
        if no:
            print(no.valor, end=" ")
            self.pre_ordem(no.esq)
            self.pre_ordem(no.dir)


arvore = ArvoreSplay()


#insere sem splay para ficar igual ao exercicio
arvore.insere_sem_splay(10)
arvore.insere_sem_splay(11)
arvore.insere_sem_splay(12)
arvore.insere_sem_splay(13)
arvore.insere_sem_splay(4)
arvore.insere_sem_splay(6)
arvore.insere_sem_splay(8)
arvore.insere_sem_splay(9)
arvore.insere_sem_splay(7)
arvore.insere_sem_splay(5)
arvore.insere_sem_splay(2)
arvore.insere_sem_splay(1)
arvore.insere_sem_splay(3)

print("\n\narvore inicial")
arvore.pre_ordem(arvore.raiz)
print("\n\nbuscando 3")
arvore.busca(3)
print("\narvore buscado 3")
arvore.pre_ordem(arvore.raiz)
print("\n\nbuscando 9")
arvore.busca(9)
print("\narvore buscado 9")
arvore.pre_ordem(arvore.raiz)
print("\n\nbuscando 1")
arvore.busca(1)
print("\narvore buscado 1")
arvore.pre_ordem(arvore.raiz)
print("\n\nbuscando 5")
arvore.busca(5)
print("\narvore buscado 5")
arvore.pre_ordem(arvore.raiz)
