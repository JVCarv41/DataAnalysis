def determinant(matrix:list[list[int|float]])->int|float:
    """Calculates and returns the determinant of a matrix

    Args:
        matrix (list[list[int | float]]): the matrix

    Returns:
        int|float: the matrix's determinant
    """    
   
    sum_p:int|float = 0
    sum_n:int|float = 0
    product_p:int|float = 1
    product_n:int|float = 1
    matrix_order:int = len(matrix[0])
    
    if (matrix_order == 1):
        sum_p = matrix[0][0]
        sum_n = 0
    elif (matrix_order == 2):
        product_p = matrix[0][0]*matrix[1][1]
        sum_p = product_p
        
        product_n = matrix[0][1]*matrix[1][0]
        sum_n = product_n
    else:
        for i in range(matrix_order):
            for j in range (matrix_order):
                index:int = (j+i)%(matrix_order)
                product_p *= matrix[j][index]
                product_n *= matrix[j][-(index+1)]
            sum_p += product_p
            sum_n += product_n
            product_p = 1
            product_n = 1    
    return (sum_p-sum_n)


def crammer(coefficients_matrix:list[list[int|float]],results:list[int|float])->list[int|float]:
    """Using crammer's rule, solves a group of 3 equations with 3 variables

    Args:
        coefficients_matrix (list[list[int|float]]): the 3x3 matrix of coefficients
        results (list[int|float]): the 3x1 matrix of results

    Returns:
        list[int|float]: the 3x1 matrix of values that solves for x,y and z
    """  
    from copy import deepcopy
    
    matrix_det:int|float = determinant(coefficients_matrix)
    if(matrix_det == 0):
        raise ValueError("Matrix's determinant can't be 0")
    
    variable_matrix:list[list[list[int|float]]] = []
    variable_det:list[int|float] = []
    for i in range(3):
        variable_matrix.append(deepcopy(coefficients_matrix))
        for j in range(3):
            variable_matrix[i][j][i] = results[j]
        variable_det.append(determinant(variable_matrix[i]))
    return [variable_det[0]/matrix_det, variable_det[1]/matrix_det, variable_det[2]/matrix_det]