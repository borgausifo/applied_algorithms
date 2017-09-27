from datetime import datetime
import pickle

def insertion_sort(x):
    # First we need to have loop over which starts from 2nd item
    for i in range(1, len(x)): # It starts from second item on the list.
        position = i # Need to know what position we are in
        value = x[i] # Need to know assigned number on that position
        while position > 0 and x[position-1] > value:
            x[position] = x[position-1] # Changing the number's position
            position = position - 1
        x[position] = value


start_1 = datetime.now()
pickle_in = open('ni_random_integers_1.pickle', 'rb')
x = pickle.load(pickle_in)
insertion_sort(x)
end_1 = datetime.now()

print('Insertion Sort Time Taken 1st is {}'.format(end_1 - start_1))


start_2 = datetime.now()
pickle_in_2 = open('ni_random_integers_2.pickle', 'rb')
x = pickle.load(pickle_in_2)
insertion_sort(x)
end_2 = datetime.now()
print('Quick  Sort Time Taken 2nd is {}'.format(end_2 - start_2))

start_3 = datetime.now()
pickle_in_3 = open('ni_random_integers_3.pickle', 'rb')
x = pickle.load(pickle_in_3)
insertion_sort(x)
end_3 = datetime.now()
print('Quick  Sort Time Taken for 3rd is {}'.format(end_3 - start_3))

start_4 = datetime.now()
pickle_in_4 = open('ni_random_integers_4.pickle', 'rb')
x = pickle.load(pickle_in_4)
insertion_sort(x)
end_4 = datetime.now()
print('Quick  Sort Time Taken for 4th is {}'.format(end_4 - start_4))

start_5 = datetime.now()
pickle_in_5 = open('ni_random_integers_5.pickle', 'rb')
x = pickle.load(pickle_in_5)
insertion_sort(x)
end_5 = datetime.now()
print('Quick  Sort Time Taken for 5th is {}'.format(end_5 - start_5))

start_6 = datetime.now()
pickle_in_6 = open('ni_random_integers_6.pickle', 'rb')
x = pickle.load(pickle_in_6)
insertion_sort(x)
end_6 = datetime.now()
print('Quick  Sort Time Taken for 6th is {}'.format(end_6 - start_6))

start_7 = datetime.now()
pickle_in_7 = open('ni_random_integers_7.pickle', 'rb')
x = pickle.load(pickle_in_7)
insertion_sort(x)
end_7 = datetime.now()
print('Quick  Sort Time Taken for 7th is {}'.format(end_7 - start_7))

start_8 = datetime.now()
pickle_in_8 = open('ni_random_integers_8.pickle', 'rb')
x = pickle.load(pickle_in_8)
insertion_sort(x)
end_8 = datetime.now()
print('Quick  Sort Time Taken for 8th is {}'.format(end_8 - start_8))

start_9 = datetime.now()
pickle_in_9 = open('ni_random_integers_9.pickle', 'rb')
x = pickle.load(pickle_in_9)
insertion_sort(x)
end_9 = datetime.now()
print('Quick  Sort Time Taken for 9th is {}'.format(end_9 - start_9))

start_10 = datetime.now()
pickle_in_10 = open('ni_random_integers_10.pickle', 'rb')
x = pickle.load(pickle_in_10)
insertion_sort(x)
end_10 = datetime.now()
print('Quick  Sort Time Taken for 10th is {}'.format(end_10 - start_10))

start_11 = datetime.now()
pickle_in_11 = open('ni_random_integers_11.pickle', 'rb')
x = pickle.load(pickle_in_11)
insertion_sort(x)
end_11 = datetime.now()
print('Quick  Sort Time Taken for 11th is {}'.format(end_11 - start_11))

start_12 = datetime.now()
pickle_in_12 = open('ni_random_integers_12.pickle', 'rb')
x = pickle.load(pickle_in_12)
insertion_sort(x)
end_12 = datetime.now()
print('Quick  Sort Time Taken for 12th is {}'.format(end_12 - start_12))

start_13 = datetime.now()
pickle_in_13 = open('ni_random_integers_13.pickle', 'rb')
x = pickle.load(pickle_in_13)
insertion_sort(x)
end_13 = datetime.now()
print('Quick  Sort Time Taken for 13th is {}'.format(end_13 - start_13))

start_14 = datetime.now()
pickle_in_14 = open('ni_random_integers_14.pickle', 'rb')
x = pickle.load(pickle_in_14)
insertion_sort(x)
end_14 = datetime.now()
print('Quick  Sort Time Taken for 14th is {}'.format(end_14 - start_14))

start_15 = datetime.now()
pickle_in_15 = open('ni_random_integers_15.pickle', 'rb')
x = pickle.load(pickle_in_15)
insertion_sort(x)
end_15 = datetime.now()
print('Quick  Sort Time Taken for 15th is {}'.format(end_15 - start_15))

start_16 = datetime.now()
pickle_in_16 = open('ni_random_integers_16.pickle', 'rb')
x = pickle.load(pickle_in_16)
insertion_sort(x)
end_16 = datetime.now()
print('Quick  Sort Time Taken for 16th is {}'.format(end_16 - start_16))

start_17 = datetime.now()
pickle_in_17 = open('ni_random_integers_17.pickle', 'rb')
x = pickle.load(pickle_in_17)
insertion_sort(x)
end_17 = datetime.now()
print('Quick  Sort Time Taken for 17th is {}'.format(end_17 - start_17))

start_18 = datetime.now()
pickle_in_18 = open('ni_random_integers_18.pickle', 'rb')
x = pickle.load(pickle_in_18)
insertion_sort(x)
end_18 = datetime.now()
print('Quick  Sort Time Taken for 18th is {}'.format(end_18 - start_18))

start_19 = datetime.now()
pickle_in_19 = open('ni_random_integers_19.pickle', 'rb')
x = pickle.load(pickle_in_19)
insertion_sort(x)
end_19 = datetime.now()
print('Quick  Sort Time Taken for 19th is {}'.format(end_19 - start_19))

start_20 = datetime.now()
pickle_in_20 = open('ni_random_integers_20.pickle', 'rb')
x = pickle.load(pickle_in_20)
insertion_sort(x)
end_20 = datetime.now()
print('Quick  Sort Time Taken for 20th is {}'.format(end_20 - start_20))