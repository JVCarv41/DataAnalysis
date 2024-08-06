from math import comb,pow,e,factorial,sqrt

def binomial(n:int,x:list,p:float, complementar:bool=False):
    """Retorna a probabilidade de um evento de distribuicao binomial ocorrer

    Args:
        n (int):  n de eventos totais
        x (list): lista com os numeros de eventos desejados 
        p (float): probabilidade de 1 evento ocorrer
        complementar (bool, optional): se a probabilidade desejada e a calculada ou a complementar dela. Defaults to False.

    Returns:
        float: probabilidade entre 0 e 1
    """    
    sum = 0
    if type(x) is list:
        for i in x:
            sum+=(comb(n,i)*(p**i)*((1-p)**(n-i)))
    else:
        sum = (comb(n,x)*(p**x)*((1-p)**(n-x)))
        
    if (complementar):
        return 1-sum
    else:
        return sum
            

def poisson(l:float,x:list,complementar:bool=False):
    """Retorna a probabilidade de um evento de distribuicao de Possion ocorrer

    Args:
        l (float): lamda, media de ocorrencias por unidade de medida
        x (list): lista com os numero de ocorrencias desejadas
        complementar (bool, optional): se a probabilidade desejada e a calculada ou a complementar dela. Defaults to False.

    Returns:
        float: probabilidade entre 0 e 1
    """   
    sum = 0 
    if type(x) is list:
        for i in x:
            sum += pow(e,-l)*(pow(l,i))/(factorial(i))
    else:
        sum =  pow(e,-l)*(pow(l,x))/(factorial(x))            
    if (complementar):
        return 1-sum
    else:
        return sum

def hiperGeometric(N:int,n:int,r:int,X:list,complementar:bool=False):
    """Retorna a probabilidade de um evento de distribuicao hipergeometrica ocorrer

    Args:
        N (int): Populacao
        n (int): Amostra
        r (int): Numero de individuos da populacao com determinada caracteristica 
        x (int): Numero de individuos desejados com determinada caracteristica
        complementar (bool, optional): se a probabilidade desejada e a calculada ou a complementar dela. Defaults to False.

    Returns:
        float: probabilidade entre 0 e 1
    """ 
    sum = 0   
    if type(X) is list:
        c = comb(N,n)
        for x in X:
            a = comb(r,x)
            b = comb(N-r,n-x)
            sum += (a*b/c)
    else: 
        a = comb(r,X)
        b = comb(N-r,n-X)
        c = comb(N,n)
        sum = (a*b/c) 
    if (complementar):
        return 1-sum
    else:
        return sum

def normal(a,b,med,dp):
    """
    WIP: no momento so retorna os valores de z
    Retorna a probabilidade de um evento de distribuicao normal ocorrer

    a -> valor minimo[]

    b -> valor maximo 

    med -> valor medio da distribuicao

    dp -> desvio padrao 
    """
    def calculatesZ(x,med,dp):
        """
        Calcula e retorna o valor do Z

        x -> Ponto

        med -> Media

        dp -> Desvio padrao
        """
        return (x-med)/dp
    
    z1 = calculatesZ(a,med,dp)
    z2 = calculatesZ(b,med,dp)
    return [z1,z2]

def exponential(a:float,b:float,med:float, complementar=False):
    """Retorna a probabilidade de um evento de distribuicao exponencial ocorrer

    Args:
        a (float): valor inicial
        b (float): valor final. Para ser infinito, insira "inf"
        med (float): a media (1/lambda)
        complementar (bool, optional): se a probabilidade desejada e a calculada ou a complementar dela. Defaults to False.

    Returns:
        float: probabilidade entre 0 e 1
    """    

    l = 1/med
    el1 = pow(e,-l*a)
    if b == "inf":
        el2 = 0
    else:
        el2 = (pow(e,-l*b))
       
    result = el1-el2
    if(complementar):
        return 1-result
    else:
        return result

def desvioMedia(dp,a):
    """
    Retorna o valor do desvio associada a media

    dp -> Desvio padrao

    a -> Tamanho da amostra
    """
    return (dp/sqrt(a))