from dataAnalysis.main_module import average

import numpy as np
from math import sqrt

def SimpleLR(X:list,Y:list, *,poly1d=False,approx=3,format=False):
    """Retorna os valores de alpha, beta e R2 que realizam 
    a regressao linear simples do conjunto de dados
    
    alpha -> coeficiente linear                            
     beta -> coeficiente angular

    Args:
        X (list): conjunto de valores da variavel x
        Y (list): conjunto de valores da variavel y
        poly1d (bool, optional): Se sera usado para criar linha de tendencia no matplotlib.pyplot. Defaults to False.
        format (bool, optional): Se o valor retornado sera uma string com a funcao formatada
        approx (int, optional):  numero de casas decimais desejadas. Se approx=0, nao realiza aproximacao. Defaults to 3.

    Returns:
        If poly1d == True:
            list: [[0,beta,alpha],R2]
            Retorna o elemento 0 no formato de entrada do np.poly1d
        If poly1d == False:
            If format == True:
                String: y(x) = {b}x+{a}
                        R = {R}
            If format == False:
                list: [alpha,beta,R2]    
            
    """    
   
    xm = average(X)
    ym = average(Y)
    
    sumT = 0
    sumB = 0
    
    n = len(X)
    for i in range(n):
        sumT += ((X[i]-xm)*(Y[i]-ym))
        sumB += pow((X[i]-xm),2)
         
    b = sumT/sumB
    a = ym - (b*xm)
    
    SQT = 0
    SQE = 0
    
    for i in range(n):
        SQT += pow((Y[i]-ym),2)
        SQE += pow(Y[i]-(a+b*X[i]),2)
        
    R = (SQT - SQE)/SQT
    
    if(approx != 0):
        b = round(b,approx)
        a = round(a,approx)
        R = round(R,approx)
    
    if(poly1d):
        return [[0,b,a],R]
    else:
        if(format):
            return f"y(x) = {b}x + {a}\nR² = {R}"
        else:
            return [a,b,R]
        
def pearsonCoefficient(X:list,Y:list,*,approx=3,format=False):
    """Retorna o valor do Coeficiente de Correlação Linear de Pearson

    Args:
        X (list): conjunto de valores da variavel x
        Y (list): conjunto de valores da variavel y
        approx (int, optional): numero de casas decimais desejadas. Defaults to 3.

    Returns:
        if format == True:
            string: Pearson = r
                    Variancia = S
                    Desvio Padrao = sigma
        if format == False:
            list: [r,S,sigma]\n
            r = coeficiente de Pearson\n
            S = variancia\n
            sigma = desvio padrao
    """    
   
   #Transforms the arrays into numpy arrays
    X = np.array(X)
    Y = np.array(Y)
    
    #Gets the value n: the array's lenght
    n = len(X)
    
    #Creates the auxiliary arrays
    XY = X*Y
    X2 = X**2
    Y2 = Y**2
    
    #Calculates the parts of the nominator
    sum_XY = np.sum(XY)
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    
    #Calculates the x part of the denominator
    sum_X2 = np.sum(X2)
    sum_X_2 = sum_X**2   
    sq1 = (n*sum_X2)-sum_X_2
    
    #Calculates the y part of the denominator
    sum_Y2 = np.sum(Y2)
    sum_Y_2 = sum_Y**2
    sq2 = (n*sum_Y2)-sum_Y_2
    
    #Calculates the nominator, denominator and the value r
    up = (n*sum_XY)-(sum_X*sum_Y)
    down = sqrt(sq1)*sqrt(sq2)
    r = up/down
    
    
    #Calculates the Variation
    ym = average(Y)
    Y_Ym = [y-ym for y in Y]
    Y_Ym = np.array(Y_Ym)
    S = np.sum(Y_Ym)/n
    
    #Calculates the Standar Deviation
    sigma = sqrt(S*(1-r**2))
    
    if(approx != 0):
        r = round(r,approx)
        S = round(S,approx)
        sigma = round(sigma,approx)
    
    #Returns the values
    if (format):
        return f'Pearson = {r}\nVariancia = {S}\nDesvio Padrao = {sigma}'
    else:
        return [r,S,sigma]

def MultiLR(x1:list,x2:list,y:list, *,approx=3):
    """Retorna os valores de b0,b1 e b2 que realizam 
    a regressao linear multipla do conjunto de dados

    Args:
        x1 (list): variavel explicativa 1
        x2 (list): variavel explicativa 2
        y (list):  variavel de resposta
        approx (int, optional): numero de casas decimais desejadas. Defaults to 3.

    Returns:
        list: [b0,b1,b2]
    """    
    n = len(x1)
    
    #Creates all the auxiliary arrays
    x1 = np.array(x1)
    x2 = np.array(x2)
    y = np.array(y)
    x1_2 = x1**2
    x2_2 = x2**2
    x1x2 = x1*x2
    x1y = x1*y
    x2y = x2*y
    
    #Transforms the arrays into their sums to plug in the formula
    sum_x1 = np.sum(x1)
    sum_x2 = np.sum(x2)
    sum_y = np.sum(y)
    sum_x1_2 = np.sum(x1_2)
    sum_x2_2 = np.sum(x2_2)
    sum_x1y = np.sum(x1y)
    sum_x2y = np.sum(x2y)
    sum_x1x2 = np.sum(x1x2)
    
    #Calculates the matrices and the values of b0, b1, b2
    mat = [[n,sum_x1,sum_x2],[sum_x1,sum_x1_2,sum_x1x2],[sum_x2,sum_x1x2,sum_x2_2]]
    matI = np.linalg.inv(mat)
    solutions = [sum_y,sum_x1y,sum_x2y]
    b = np.matmul(solutions,matI)
    if (approx != 0):
        b = [round(i,approx) for i in b]
    return [b[0],b[1],b[2]]