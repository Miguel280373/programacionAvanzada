from random import sample
import time

def bubble_sort(vector):
    size=len(vector)

    for i in range(size-1):
        for j in range(0,size-1-i):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1]= vector[j+1], vector[j]
    
    return vector

lista = list(range(1000))

vector = sample(lista,10)





def select_sort(vector):
    size= len(vector)
    for i in range(size):
        min= i
        for j in range(i+1, size):
            if vector[min] < vector[j]:
                min=j
                vector[i], vector[min] = vector[min], vector[i]
    return vector   

def inserction_sort(vector):
    size=len(vector)
    for i in range(1,size):
        if vector[i] < vector[i-1]:
            vector[i], vector[i-1] = vector[i-1], vector[i]
    return vector

start_time=time.time()
inserction_sort(vector)
print(inserction_sort(vector))
end_time=time.time()
print("el tiempo fue de ",end_time-start_time)