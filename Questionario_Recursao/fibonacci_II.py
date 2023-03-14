def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        resultados = fibonacci(n-1)
        resultados.append(sum(resultados[len(resultados)-2:len(resultados):]))
        return resultados
print(fibonacci(2))