def simpleinsert(data):
    for i in range(len(data)):
        current = data[i]
        index = i - 1
        while index >= 0 and data[index] > current:
            data[index+1] = data[index]
            index -= 1
        data[index+1]=current






if __name__ == '__main__':
    import random
    import numpy
    data = [random.randint(-100, 100) for _ in range(6)]
    simpleinsert(data)
    print(data)