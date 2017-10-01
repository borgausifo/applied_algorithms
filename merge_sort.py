# Merge Sort Algorithm

# Importing date time for time calculation
import pickle
from datetime import datetime


# Defining merge sort algorithm

def MergeSort(A):
    n = len(A)
# If the array is only has one element in it means already sorted
    if n < 2:
        return -1
# Dividing array into sub arrays until the smallest one
    else:
        mid = int(round(n/2))
        left = A[:mid]
        right = A[mid:]

        MergeSort(left)
        MergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1

# First Merge Sort

start_1 = datetime.now()
pickle_in = open('ni_random_integers_1.pickle', 'rb')
A = pickle.load(pickle_in)
MergeSort(A)
end_1 = datetime.now()

print('Merge Sort Time Taken 1st is {}'.format(end_1 - start_1))


start_2 = datetime.now()
pickle_in_2 = open('ni_random_integers_2.pickle', 'rb')
B = pickle.load(pickle_in_2)
MergeSort(A)
end_2 = datetime.now()
print('Merge Sort Time Taken 2nd is {}'.format(end_2 - start_2))

start_3 = datetime.now()
pickle_in_3 = open('ni_random_integers_3.pickle', 'rb')
B = pickle.load(pickle_in_3)
MergeSort(A)
end_3 = datetime.now()
print('Merge Sort Time Taken for 3rd is {}'.format(end_3 - start_3))

start_4 = datetime.now()
pickle_in_4 = open('ni_random_integers_4.pickle', 'rb')
B = pickle.load(pickle_in_4)
MergeSort(A)
end_4 = datetime.now()
print('Merge Sort Time Taken for 4th is {}'.format(end_4 - start_4))

start_5 = datetime.now()
pickle_in_5 = open('ni_random_integers_5.pickle', 'rb')
B = pickle.load(pickle_in_5)
MergeSort(A)
end_5 = datetime.now()
print('Merge Sort Time Taken for 5th is {}'.format(end_5 - start_5))

start_6 = datetime.now()
pickle_in_6 = open('ni_random_integers_6.pickle', 'rb')
B = pickle.load(pickle_in_6)
MergeSort(A)
end_6 = datetime.now()
print('Merge Sort Time Taken for 6th is {}'.format(end_6 - start_6))

start_7 = datetime.now()
pickle_in_7 = open('ni_random_integers_7.pickle', 'rb')
B = pickle.load(pickle_in_7)
MergeSort(A)
end_7 = datetime.now()
print('Merge Sort Time Taken for 7th is {}'.format(end_7 - start_7))

start_8 = datetime.now()
pickle_in_8 = open('ni_random_integers_8.pickle', 'rb')
B = pickle.load(pickle_in_8)
MergeSort(A)
end_8 = datetime.now()
print('Merge Sort Time Taken for 8th is {}'.format(end_8 - start_8))

start_9 = datetime.now()
pickle_in_9 = open('ni_random_integers_9.pickle', 'rb')
B = pickle.load(pickle_in_9)
MergeSort(A)
end_9 = datetime.now()
print('Merge Sort Time Taken for 9th is {}'.format(end_9 - start_9))

start_10 = datetime.now()
pickle_in_10 = open('ni_random_integers_10.pickle', 'rb')
B = pickle.load(pickle_in_10)
MergeSort(A)
end_10 = datetime.now()
print('Merge Sort Time Taken for 10th is {}'.format(end_10 - start_10))

start_11 = datetime.now()
pickle_in_11 = open('ni_random_integers_11.pickle', 'rb')
B = pickle.load(pickle_in_11)
MergeSort(A)
end_11 = datetime.now()
print('Merge Sort Time Taken for 11th is {}'.format(end_11 - start_11))

start_12 = datetime.now()
pickle_in_12 = open('ni_random_integers_12.pickle', 'rb')
B = pickle.load(pickle_in_12)
MergeSort(A)
end_12 = datetime.now()
print('Merge Sort Time Taken for 12th is {}'.format(end_12 - start_12))

start_13 = datetime.now()
pickle_in_13 = open('ni_random_integers_13.pickle', 'rb')
B = pickle.load(pickle_in_13)
MergeSort(A)
end_13 = datetime.now()
print('Merge Sort Time Taken for 13th is {}'.format(end_13 - start_13))

start_14 = datetime.now()
pickle_in_14 = open('ni_random_integers_14.pickle', 'rb')
B = pickle.load(pickle_in_14)
MergeSort(A)
end_14 = datetime.now()
print('Merge Sort Time Taken for 14th is {}'.format(end_14 - start_14))

start_15 = datetime.now()
pickle_in_15 = open('ni_random_integers_15.pickle', 'rb')
B = pickle.load(pickle_in_15)
MergeSort(A)
end_15 = datetime.now()
print('Merge Sort Time Taken for 15th is {}'.format(end_15 - start_15))

start_16 = datetime.now()
pickle_in_16 = open('ni_random_integers_16.pickle', 'rb')
B = pickle.load(pickle_in_16)
MergeSort(A)
end_16 = datetime.now()
print('Merge Sort Time Taken for 16th is {}'.format(end_16 - start_16))

start_17 = datetime.now()
pickle_in_17 = open('ni_random_integers_17.pickle', 'rb')
B = pickle.load(pickle_in_17)
MergeSort(A)
end_17 = datetime.now()
print('Merge Sort Time Taken for 17th is {}'.format(end_17 - start_17))

start_18 = datetime.now()
pickle_in_18 = open('ni_random_integers_18.pickle', 'rb')
B = pickle.load(pickle_in_18)
MergeSort(A)
end_18 = datetime.now()
print('Merge Sort Time Taken for 18th is {}'.format(end_18 - start_18))

start_19 = datetime.now()
pickle_in_19 = open('ni_random_integers_19.pickle', 'rb')
B = pickle.load(pickle_in_19)
MergeSort(A)
end_19 = datetime.now()
print('Merge Sort Time Taken for 19th is {}'.format(end_19 - start_19))

start_20 = datetime.now()
pickle_in_20 = open('ni_random_integers_20.pickle', 'rb')
B = pickle.load(pickle_in_20)
MergeSort(A)
end_20 = datetime.now()
print('Merge Sort Time Taken for 20th is {}'.format(end_20 - start_20))












