from functools import reduce
numeros = [1,43,52,25,67,21,35,12,18,93]
impares = filter(lambda x: x%2,numeros)
total = reduce(lambda a,b: a+b, impares)
print(f'La suma de los numeros impares de la lista es {total}')
