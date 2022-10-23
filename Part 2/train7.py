import numpy as np

#numlist = []
def enter():
    numlist = []
    while True:
        list = []
        while True:
            numbers = input('enter your num: end')
            if numbers == 'end':
                break
            list.append(numbers)
        numlist.append(list)
        choice = input('enter your choice: ')
        if choice == 'end':
            break
    a = np.array(numlist,dtype=int)
    print(a)
    b = a.shape
    c = np.zeros(b)
    print(c)
enter()