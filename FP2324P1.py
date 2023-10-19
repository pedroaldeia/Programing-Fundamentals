def eh_territorio(arg): #2.1.1
    for b in range(len(arg)):
        if not ( type(arg) == tuple and type(arg[b-1]) == tuple and len (arg[b-1]) == len (arg[0]) and len(arg)>=1 and len(arg[0])>=1):
            return False
        for n in arg[b]: #wtf não sei porque é que isto nao funciona
            if not n in (0,1):
                return False
    return True


def obtem_ultima_intersecao(t): #2.1.2
    #faz corresponder a quantidade de tuplos em t à letra do alfabeto dessa ordem.
    #  Devolve a letra e a quantidade de elementos em cada tuplo
    coordenadas = (chr(len(t)+64), len(t[0]))
    return coordenadas


def eh_intersecao(t): #2.1.3
    #Se o primeiro elemento do tuplo faz parte do alfabeto e se o segundo é um inteiro entre 0 e 100
    if not (isinstance(t, tuple) and isinstance(t[0], str) and len(t[0]) == 1\
             and (64<ord(t[0])<91) and (isinstance(t[1] , int)) and (0<t[1]<100)):
        return False
    return True
print(eh_intersecao((25, 'B')))


def eh_intersecao_valida(t, i): #2.1.4
    #O código vai buscar a ordem da letra (da coordenada) e verifica se é 
    # maior do que a len de t.~
    #  Também verifica se o número da coordenada é maior do que a len dos tuplos em t
    if (ord(i[0])-64>len(t) or i[1]>len(t[0])):
            return False
    return True


def eh_intersecao_livre(t, i): #2.1.5
    #Transforma a letra em i na ordem de tup1; verifica se o objeto do tuplo dentro do tuplo é 1, se for o caso muda "a" para false
    if t[ord(i[0])-65][i[1]-1] == 0:
        return True
    return False


def obtem_intersecoes_adjacentes(t, i): #2.1.6
    #
    intersecoes = ()
    if i[1] != 1:
        intersecoes += ((chr(ord(i[0])), i[1]-1),)
    if i[0] != "A":
        intersecoes += ((chr(ord(i[0])-1), i[1]),)
    if ord(i[0]) -64 != len(t):
        intersecoes += ((chr(ord(i[0])+1), i[1]),)
    if i[1] != len(t[0]):
        intersecoes += ((chr(ord(i[0])), i[1]+1),)
    
    return intersecoes



def ordena_intersecoes(tup): #2.1.7
    #
    a = 0
    lis = list(tup)
    while a != 1:
        a = 1
        for i in range (len(lis) -1):
            if lis[i][1] > lis[i+1][1]:
                    lis[i], lis[i+1] = lis[i+1], lis[i]
                    a=0
            elif lis[i][1] == lis[i+1][1]:
                if lis[i][0] > lis[i+1][0]:
                    lis[i], lis[i+1] = lis[i+1], lis[i]
                    a=0
    tup = tuple(lis)
    return tup


def territorio_para_str(tup): #2.1.8
    #
    string = " "
    mid = ""
    a = 0
    b = len(tup[0])
    n = 0
    if len(tup[0]) > 9:
        string += " "
    while not (chr(len(tup)+64) in string):
        string += " " + chr(a+65)
        a += 1
    while b != 0:
        if len(tup[0]) > 9:
            if b >= 10:
                mid += "\n " + str(b)
            else:
                mid += "\n " + " " + str(b)
        else:
            mid += "\n " + str(b)
        while n != len(tup):
            
            if tup[n][b-1] == 0:
                mid += " ."
            else:
                mid += " X"
            n +=1
        if len(tup[0]) > 9:
            if b > 9:
                mid += " " + str(b)
            else:
                mid += "  " + str(b)
        else:
            mid += "  " + str(b)
        b -= 1
        n = 0
    
    return " " + string + mid + "\n " + string

t=((1,1,1,0,0,0,0,0,1,1),)
territorio_para_str(t)



def obtem_cadeia(t, inp): #2.2.1
    #
    cadeia = [inp]
    if not (eh_territorio(t) or eh_intersecao(inp) or eh_intersecao_valida(t, inp)):
        raise ValueError("obtem_cadeia: argumentos invalidos")
    for tup in cadeia:
        tup_adj = obtem_intersecoes_adjacentes(t, tup)
        for adj in tup_adj:
            if (eh_intersecao_livre(t, adj) == eh_intersecao_livre(t, inp) and not adj in cadeia):
                    cadeia += [adj]
    
    return ordena_intersecoes(cadeia)


def obtem_vale(t, inp): #2.2.2
    if eh_intersecao_livre(t, inp):
        raise ValueError("obtem_vale: argumentos invalidos")
    tup1 = obtem_cadeia(t, inp)
    vales = ()
    for a in tup1:
        tup2 = obtem_intersecoes_adjacentes(t, a)
        for b in tup2:
            if eh_intersecao_livre(t, b) and not b in vales:
                vales += (b,)
    
    return ordena_intersecoes(vales)


def verifica_conexao(t, a, b): #2.3.1
    cadeia = obtem_cadeia(t, a)
    if not (eh_territorio(t)  and eh_intersecao_valida(t, a) and eh_intersecao_valida(t, b) and eh_intersecao(a) and eh_intersecao(b)):
        raise ValueError ("verifica_conexao: argumentos invalidos")
    if b in cadeia:
        return True
    return False

def calcula_numero_montanhas(t): #2.3.2
    if not eh_territorio(t):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    count = 0
    for a in t:
        for b in a:
            if b == 1:
                count += 1
    return count

def calcula_numero_cadeias_montanhas(t): #2.3.3
    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    cadeias = ()
    for i in range(len (t)):
        for n in range(len(t[i])):
            if t[i][n] == 1:
                cadeia1 = obtem_cadeia(t, (chr(i+65), n+1))
                if not cadeia1 in cadeias:
                    cadeias += (cadeia1, )
    return len(cadeias)

def calcula_tamanho_vales(t): #2.3.4
    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    cadeias = ()
    total_vales = ()
    for i in range(len (t)):
        for n in range(len(t[i])):
            if t[i][n] == 1:
                cadeia1 = obtem_cadeia(t, (chr(i+65), n+1))
                if not cadeia1 in cadeias:
                    cadeias += (cadeia1, )
    for cadeia in cadeias:
        vales = obtem_vale(t, cadeia[0])
        for vale in vales:
            if not vale in total_vales:
                total_vales += (vale, )
    
    return len(total_vales)

