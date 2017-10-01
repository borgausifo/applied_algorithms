from datetime import datetime

import pickle


from operator import ge as greater, lt as lesser

def quickSort(listTosort, start, end):
    if ((start - end) > 0):
        p = partition(listTosort, start, end)
        quickSort(listTosort, start, p-1)
        quickSort(listTosort, p+1, end)
def partition(listToSort, start, end):
    divider = start
    pivot = end

    for i in range(start, end):
        if(listToSort[i] < listToSort[pivot]):
            listToSort[i], listToSort[divider] = listToSort[divider], listToSort[i]
            divider += 1
    listToSort[pivot], listToSort[divider] = listToSort[divider], listToSort[pivot]

    return divider


start_1 = datetime.now()
pickle_in = open('ni_random_integers_1.pickle', 'rb')
seq = pickle.load(pickle_in)
quickSort(seq)
end_1 = datetime.now()
print('Quick  Sort Time Taken 1st is {}'.format(end_1 - start_1))

start_2 = datetime.now()
pickle_in_2 = open('ni_random_integers_2.pickle', 'rb')
seq = pickle.load(pickle_in_2)
quickSort(seq)
end_2 = datetime.now()
print('Quick  Sort Time Taken 2nd is {}'.format(end_2 - start_2))

start_3 = datetime.now()
pickle_in_3 = open('ni_random_integers_3.pickle', 'rb')
seq = pickle.load(pickle_in_3)
quickSort(seq)
end_3 = datetime.now()
print('Quick  Sort Time Taken for 3rd is {}'.format(end_3 - start_3))

start_4 = datetime.now()
pickle_in_4 = open('ni_random_integers_4.pickle', 'rb')
seq = pickle.load(pickle_in_4)
quickSort(seq)
end_4 = datetime.now()
print('Quick  Sort Time Taken for 4th is {}'.format(end_4 - start_4))

start_5 = datetime.now()
pickle_in_5 = open('ni_random_integers_5.pickle', 'rb')
seq = pickle.load(pickle_in_5)
quickSort(seq)
end_5 = datetime.now()
print('Quick  Sort Time Taken for 5th is {}'.format(end_5 - start_5))

start_6 = datetime.now()
pickle_in_6 = open('ni_random_integers_6.pickle', 'rb')
seq = pickle.load(pickle_in_6)
quickSort(seq)
end_6 = datetime.now()
print('Quick  Sort Time Taken for 6th is {}'.format(end_6 - start_6))

start_7 = datetime.now()
pickle_in_7 = open('ni_random_integers_7.pickle', 'rb')
seq = pickle.load(pickle_in_7)
quickSort(seq)
end_7 = datetime.now()
print('Quick  Sort Time Taken for 7th is {}'.format(end_7 - start_7))

start_8 = datetime.now()
pickle_in_8 = open('ni_random_integers_8.pickle', 'rb')
seq = pickle.load(pickle_in_8)
quickSort(seq)
end_8 = datetime.now()
print('Quick  Sort Time Taken for 8th is {}'.format(end_8 - start_8))

start_9 = datetime.now()
pickle_in_9 = open('ni_random_integers_9.pickle', 'rb')
seq = pickle.load(pickle_in_9)
quickSort(seq)
end_9 = datetime.now()
print('Quick  Sort Time Taken for 9th is {}'.format(end_9 - start_9))

start_10 = datetime.now()
pickle_in_10 = open('nd_random_integers_10.pickle', 'rb')
seq = pickle.load(pickle_in_10)
quickSort(seq)
end_10 = datetime.now()
print('Quick  Sort Time Taken for 10th is {}'.format(end_10 - start_10))

start_11 = datetime.now()
pickle_in_11 = open('ni_random_integers_11.pickle', 'rb')
seq = pickle.load(pickle_in_11)
quickSort(seq)
end_11 = datetime.now()
print('Quick  Sort Time Taken for 11th is {}'.format(end_11 - start_11))

start_12 = datetime.now()
pickle_in_12 = open('ni_random_integers_12.pickle', 'rb')
seq = pickle.load(pickle_in_12)
quickSort(seq)
end_12 = datetime.now()
print('Quick  Sort Time Taken for 12th is {}'.format(end_12 - start_12))

start_13 = datetime.now()
pickle_in_13 = open('ni_random_integers_13.pickle', 'rb')
seq = pickle.load(pickle_in_13)
quickSort(seq)
end_13 = datetime.now()
print('Quick  Sort Time Taken for 13th is {}'.format(end_13 - start_13))

start_14 = datetime.now()
pickle_in_14 = open('ni_random_integers_14.pickle', 'rb')
seq = pickle.load(pickle_in_14)
quickSort(seq)
end_14 = datetime.now()
print('Quick  Sort Time Taken for 14th is {}'.format(end_14 - start_14))

start_15 = datetime.now()
pickle_in_15 = open('ni_random_integers_15.pickle', 'rb')
seq = pickle.load(pickle_in_15)
quickSort(seq)
end_15 = datetime.now()
print('Quick  Sort Time Taken for 15th is {}'.format(end_15 - start_15))

start_16 = datetime.now()
pickle_in_16 = open('ni_random_integers_16.pickle', 'rb')
seq = pickle.load(pickle_in_16)
quickSort(seq)
end_16 = datetime.now()
print('Quick  Sort Time Taken for 16th is {}'.format(end_16 - start_16))

start_17 = datetime.now()
pickle_in_17 = open('ni_random_integers_17.pickle', 'rb')
seq = pickle.load(pickle_in_17)
quickSort(seq)
end_17 = datetime.now()
print('Quick  Sort Time Taken for 17th is {}'.format(end_17 - start_17))

start_18 = datetime.now()
pickle_in_18 = open('ni_random_integers_18.pickle', 'rb')
seq = pickle.load(pickle_in_18)
quickSort(seq)
end_18 = datetime.now()
print('Quick  Sort Time Taken for 18th is {}'.format(end_18 - start_18))

start_19 = datetime.now()
pickle_in_19 = open('ni_random_integers_19.pickle', 'rb')
seq = pickle.load(pickle_in_19)
quickSort(seq)
end_19 = datetime.now()
print('Quick  Sort Time Taken for 19th is {}'.format(end_19 - start_19))

start_20 = datetime.now()
pickle_in_20 = open('ni_random_integers_20.pickle', 'rb')
seq = pickle.load(pickle_in_20)
quickSort(seq)
end_20 = datetime.now()
print('Quick  Sort Time Taken for 20th is {}'.format(end_20 - start_20))