"""
Uma biblioteca com funcoes que podemos usar na materia de Analise Inferencial de Dados
"""
import numpy as np
import math

def formatPerc(x:float):
    """Formata uma probabilidade em uma porcentagem 

    Args:
        x (float): probabilidade de entrada, entre 0 e 1

    Returns:
        String: Probabilidade formatada em %
    """    

    x = round(100*x,3)
    return f"{x}%"

def average(x:list,*,k=0):
    """Retorna a media da lista

    Args:
        x (list): lista de numeros
        k (int, optional): grau de liberdade. Defaults to 0.

    Returns:
        float: media
    """    
    #For lists inside another list, use recursion to calculate their averages
    for i in x:
        if type(i) is list:
            pos=x.index(i)
            x.remove(i)
            x.insert(pos,average(i))
            
    #Calculates the sum of all values
    x = np.array(x)        
    sum = np.sum(x)
    
    #Calculates the denominator, considering the degree of freedom
    div = np.size(x)-k
    
    #Returns the average
    return (sum/div)

def median(x:list):
    """Retorna a mediana da lista

    Args:
        x (list): lista de numeros

    Returns:
        float: mediana
    """    
    x = np.array(x)
    return np.median(x)

def quartile(n:int, l:list):
    """Returns the value of the nth quartile of a list of numbers

    Args:
        n (int): The number of the quartile. 1,2 or 3.
        l (list): The list of numbers

    Returns:
        int/float: the value of the nth quartile 
    """  
    if n>3:
        return None
    pos = n*(len(l)+1)/4
    pos = round(pos)
    return l[pos-1]

def decile(n:int,l:list):
    """Returns the value of the nth decile of a list of numbers

    Args:
        n (int): The number of the decile. 1 to 9
        l (list): The list of numbers

    Returns:
        int/float: the value of the nth decile 
    """  
    if n>9:
        return None
    pos = n*(len(l)+1)/10
    pos = round(pos)
    return l[pos-1]

def percentile(n:int,l:list):
    """Returns the value of the nth percentile of a list of numbers

    Args:
        n (int): The number of the decile. 1 to 99
        l (list): The list of numbers

    Returns:
        int/float: the value of the nth percentile 
    """  
    if n>99:
        return None
    pos = n*(len(l)+1)/100
    pos = round(pos)
    return l[pos-1]

def mode(X:list):
    """Calculates a list's mode, returning its values and how many times the values appear

    Args:
        X (list): The list of numbers

    Returns:
        dict: A dictionary:
                "values" will give the mode values
                "quantity" will give how many times the values appear 
    """        

    X.append(None)
    val = []
    mod = 1
    modx = 0
    xa = X[0]
    for x in X:
        if x is xa:
            modx+=1
        else:
            if modx > mod:
                val.clear()
                mod = modx
                val.append(xa)
            elif modx is mod:
                val.append(xa)
            modx = 1
        xa = x
    if len(val) == 1:
        val = val[0]
    result = {"values":val,"quantity":mod}
    return result

def variance(X:list):
    """Calcula a variancia de um grupo

    Args:
        X (list): Array de valores

    Returns:
        float: variancia dos valores
    """
    xm = average(X)
    v=[math.pow(i-xm,2) for i in X]
    return average(v,1)

def desvioPadrao(X:list):
    """Calcula o desvio padrao de um grupo

    Args:
        X (list): Array de valores

    Returns:
        float: desvio padrao dos valores
    """
    return math.sqrt(variance(X))

def calcZH(x,med,dh):
    """
    Calcula e retorna o valor do Z associado ao Ho

    x -> Variavel

    med -> Media

    dh -> Desvio associado ao H (use a funcao desvioMedia)
    """
    return (med-x)/dh