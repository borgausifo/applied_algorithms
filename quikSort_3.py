import pickle
from datetime import datetime

def quickSort(A, p, r):
    if  (p < r):
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if(A[j] <= x):
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i + 1


start = datetime.now()
pickle_in = open('ni_random_integers_1.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 499)
end = datetime.now()
print('1st TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('ni_random_integers_2.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 999)
end = datetime.now()
print('2nd TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('ni_random_integers_3.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 1499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('ni_random_integers_4.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 1999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('ni_random_integers_5.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 2499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_6.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 2999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_7.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 3499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_8.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 3999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_9.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 4499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_10.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 4999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_11.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 5499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_12.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 5999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_13.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 6499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_14.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 6999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_15.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 7499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_16.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 7999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_17.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 8499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_18.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 8999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_19.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 9499)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))

start = datetime.now()
pickle_in = open('nd_random_integers_20.pickle', 'rb')
A = pickle.load(pickle_in)
quickSort(A, 0, 9999)
end = datetime.now()
print('TIme Lapse for QuickSOrt A {}'.format(end - start))





















