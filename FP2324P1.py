def eh_territorio(arg): #2.1.1
    '''eh territorio: universal → booleano
    Verifica se um argumento é território, se for devolve True, caso contrário devolve False'''

    if not (type(arg) == tuple and len(arg)>=1 and len(arg)<=26): #Verifica se o elemento é um tuplo e se tem len >= 1
        return False
    for b in range(len(arg)): #Verifica se os elementos dentro do tuplo são tuplos
        if not (type(arg[b]) == tuple):
            return False
    for b in range(len(arg)): #Verifica se a len dos tuplos é >= 1  e <= 99 e se todos os tuplos têm a mesma len
        if not (len(arg[0])>=1 and len(arg[0])<=99 and len(arg[b-1]) == len(arg[0])):
            return False
        for n in arg[b]: #Verifica se os elementos dentro dos tuplos são 0 ou 1
            if not (type(n) == int and n in (0,1)):
                return False
    return True


def obtem_ultima_intersecao(t): #2.1.2
    '''obtem ultima intersecao: territorio → intersecao
    Devolve a interseção de última ordem em linhas e colunas'''

    #Faz corresponder a quantidade de tuplos em t à letra do alfabeto dessa ordem.
    #Devolve a letra e a quantidade de elementos em cada tuplo
    coordenadas = (chr(len(t)+64), len(t[0]))
    return coordenadas


def eh_intersecao(t): #2.1.3
    '''eh intersecao: universal → booleano
    Verifica se um argumento é uma interseção, se for devolve True, caso contrário devolve False'''

    #Verifica se o argumento é um tuplo, se tem len 2, se o tipo do primeiro caracter é uma string,
    #se a len da string é 1, se é um caracter entre as ordens 65 e 90 inclusive, se o segundo elemento
    #é um número inteiro e, finalmente, se é um número entre 1 e 99 inclusive
    if not (isinstance(t, tuple) and len(t) == 2 and isinstance(t[0], str) and len(t[0]) == 1\
             and (64 < ord(t[0]) < 91) and (isinstance(t[1] , int)) and (0 < t[1] < 100)):
        return False
    return True


def eh_intersecao_valida(t, i): #2.1.4
    '''eh intersecao valida: territorio × intersecao → booleano
    Verifica se uma interseção dada pertence a um terreno, se for devolve True, caso contrário 
    devolve False'''

    #O código vai buscar a ordem da letra (da coordenada) e verifica se é maior do que a len de t
    #Também verifica se o número da coordenada é maior do que a len dos tuplos em t
    if (ord(i[0]) - 64 > len(t) or i[1] > len(t[0])):
            return False
    return True


def eh_intersecao_livre(t, i): #2.1.5
    '''eh intersecao livre: territorio × intersecao → booleano
    Devolve True se uma dada interseção não for uma montanha, caso contrário devolve False'''

    #Verifica se a interseção dada corresponde a um zero nos tuplos
    if t[ord(i[0]) - 65][i[1] - 1] == 0:
        return True
    return False


def obtem_intersecoes_adjacentes(t, i): #2.1.6
    '''obtem intersecoes adjacentes: territorio × intersecao → tuplo
    Recebe uma interseção e um território e devolve as interseções adjacentes à interseção dada
    nesse território'''

    #Verifica se a interseção corresponde à primeira ou última linha ou coluna, e consoantemente 
    #adiciona as interseções adjacentes
    intersecoes = ()
    if i[1] != 1:
        intersecoes += ((i[0], i[1] - 1),)
    if i[0] != "A":
        intersecoes += ((chr(ord(i[0]) - 1), i[1]),)
    if ord(i[0]) - 64 != len(t):
        intersecoes += ((chr(ord(i[0]) + 1), i[1]),)
    if i[1] != len(t[0]):
        intersecoes += ((i[0], i[1] + 1),)
    
    return intersecoes



def ordena_intersecoes(tup): #2.1.7
    '''ordena intersecoes: tuplo → tuplo
    Recebe um tuplo com interseções e devolve um tuplo com as mesmas interseões, mas ordenadas por
    linha e por coluna'''
    
    a = 0
    lis = list(tup) #Torna o tuplo numa lista
    while a != 1:   #Verifica se houveram alterações no tuplo, se não for o caso termina o ciclo
        a = 1
        for i in range (len(lis) - 1):  
            #Verifica se, para cada interseção, se a interseção seguinte 
            #tem linha de ordem menor, se for o caso, trocam de ordem no tuplo 
            if lis[i][1] > lis[i + 1][1]:
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
                    a=0
            elif lis[i][1] == lis[i + 1][1]:
                #Se tiverem a mesma linha verifica se a seguinte tem coluna de menor ordem,
                #se for o caso, trocam de ordem no tuplo
                if lis[i][0] > lis[i + 1][0]:
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
                    a=0
    tup = tuple(lis) #Torna a lista num tuplo
    return tup


def territorio_para_str(tup): #2.1.8
    '''territorio para str: territorio → cad. carateres
    Recebe um território e devolve uma string que representa o território visualmente'''

    string = " "
    mid = ""
    a = 0
    b = len(tup[0])
    n = 0
    while not (chr(len(tup) + 64) in string): #Adiciona as letras
        string += " " + chr(a + 65)
        a += 1
    while b != 0:  #Adiciona o número da linha correspondente no início de cada linha da string
        if b >= 10:
            mid += "\n" + str(b)
        else:
            mid += "\n " + str(b)
        while n != len(tup):
             #Adiciona um "." de a interseção correspondente for livre e um "X" caso contrário
            if tup[n][b - 1] == 0:
                mid += " ."
            else:
                mid += " X"
            n += 1
        if b > 9:   #Adiciona o número da linha correspondente no fim de cada linha da string
            mid += " " + str(b)
        else:
            mid += "  " + str(b)
        b -= 1
        n = 0
    
    return " " + string + mid + "\n " + string



def obtem_cadeia(t, inp): #2.2.1
    '''obtem cadeia: territorio × intersecao → tuplo
    recebe um território e uma interseçãoao do território e devolve o tuplo formado por todas as 
    interseçõees que estão conetadas a essa interseção ordenadas de acordo com a ordem de leitura 
    de um território'''

    if not (eh_territorio(t) and eh_intersecao(inp) and eh_intersecao_valida(t, inp)): 
        #Verifica se o território e a interseção são válidos
        raise ValueError("obtem_cadeia: argumentos invalidos")
    cadeia = [inp] 
    for tup in cadeia:
        tup_adj = obtem_intersecoes_adjacentes(t, tup)  #cria um tuplo para as interseções adjacentes
        for adj in tup_adj:
            if (eh_intersecao_livre(t, adj) == eh_intersecao_livre(t, inp) and not adj in cadeia):
                    #Verifica se as interseções adjacentes são do mesmo tipo (livres ou ocupadas) que 
                    #a original e também se já estão contidas na lista
                    cadeia += [adj] #Se for o caso são adicionadas à lista
                    #O ciclo repete-se para todos os elementos da lista
    
    return ordena_intersecoes(cadeia)


def obtem_vale(t, inp): #2.2.2
    ''' territorio × intersecao → tuplo
    recebe um território e uma interseção do território ocupada por uma montanha, e devolve o tuplo 
    formado por todas as interseções que formam parte do vale da montanha da interseção fornecida 
    como argumento ordenadas de acordo com ordem de leitura de um território'''

    if (not ((eh_territorio(t) and eh_intersecao(inp) and eh_intersecao_valida(t, inp))) or \
        (eh_intersecao_livre(t, inp))):
        #Verifica se o território e a interseção são válidos e se a interseção é livre
        raise ValueError("obtem_vale: argumentos invalidos")
    tup1 = obtem_cadeia(t, inp) #obtém a cadeia de montanhas na qual a interseção está contida
    vales = ()
    for a in tup1:
        tup2 = obtem_intersecoes_adjacentes(t, a) #obtém as interseções adjacentes a cada elemento 
        #da cadeia
        for b in tup2:
            if eh_intersecao_livre(t, b) and not b in vales:
                #Se forem interseções livres são adicionadas ao tuplo vales
                vales += (b,)
    
    return ordena_intersecoes(vales) #Ordena os elementos do tuplo


def verifica_conexao(t, a, b): #2.3.1
    '''verifica conexao: territorio × intersecao ×-intersecao → booleano
    recebe um território e duas interseções do território e devolve
    True se as duas interseções estão conetadas e False caso contrário'''

    if not (eh_territorio(t) and eh_intersecao_valida(t, a) and eh_intersecao_valida(t, b) and \
            eh_intersecao(a) and eh_intersecao(b)): #Verifica se o terreno e interseções são válidas
        raise ValueError ("verifica_conexao: argumentos invalidos")
    cadeia = obtem_cadeia(t, a) #Obtém a cadeia de "a"
    if b in cadeia: 
        return True #Verifica se "b" está na cadeia de "a"
    return False

def calcula_numero_montanhas(t): #2.3.2
    '''calcula numero montanhas: territorio → int
    Recebe um território e devolve o número de interseções ocupadas por montanhas no território'''

    if not eh_territorio(t):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    count = 0
    for a in t:
        for b in a:
            if b == 1: #Se dentro do terreno houver um 1, adiciona +1 ao nº de montanhas
                count += 1
    return count

def calcula_numero_cadeias_montanhas(t): #2.3.3
    ''''''
    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    cadeias = ()
    for i in range(len (t)):
        for n in range(len(t[i])):
            if t[i][n] == 1:
                cadeia1 = obtem_cadeia(t, (chr(i+65), n + 1))
                if not cadeia1 in cadeias:
                    cadeias += (cadeia1, )
    return len(cadeias)

def calcula_tamanho_vales(t): #2.3.4
    '''calcula tamanho vales: territorio → int
    recebe um território e devolve o número total de interseções diferentes que formam todos os 
    vales do território'''

    if not eh_territorio(t): #Verifica se o território é válido
        raise ValueError("calcula_tamanho_vales: argumento invalido")
    cadeias = ()
    total_vales = ()
    for i in range(len(t)): #Cria cadeia para cada interseção ocupada do terreno
        for n in range(len(t[i])):
            if t[i][n] == 1:
                cadeia1 = obtem_cadeia(t, (chr(i + 65), n + 1))
                if not cadeia1 in cadeias: 
                    #Se a cadeia ainda não estiver contida em "cadeias" é adicionada
                    cadeias += (cadeia1, )
    for cadeia in cadeias: #Para cada cadeia obtém os vales da cadeia
        vales = obtem_vale(t, cadeia[0])
        for vale in vales: #Se os vales não estiverem contidos em "vales" são adicionados
            if not vale in total_vales:
                total_vales += (vale, )
    
    return len(total_vales)

