
n = int(input())

a = list(map(int, input().split()))

def response(array):
    if not array:
        return "Ordenado"
    
    last_number = array[0]

    for i in range(1, len(array)):
        if(last_number > array[i]):
            return "Desordenado"
        last_number = array[i]

    return "Ordenado"

print(response(a))