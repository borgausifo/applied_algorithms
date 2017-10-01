import pickle

import random

random_1 = [(random.randint(0, 50000)) for k in range(0, 500)]
random_2 = [(random.randint(0, 50000)) for k in range(0, 1000)]
random_3 = [(random.randint(0, 50000)) for k in range(0, 1500)]
random_4 = [(random.randint(0, 50000)) for k in range(0, 2000)]
random_5 = [(random.randint(0, 50000)) for k in range(0, 2500)]
random_6 = [(random.randint(0, 50000)) for k in range(0, 3000)]
random_7 = [(random.randint(0, 50000)) for k in range(0, 3500)]
random_8 = [(random.randint(0, 50000)) for k in range(0, 4000)]
random_9 = [(random.randint(0, 50000)) for k in range(0, 4500)]
random_10 = [(random.randint(0, 50000)) for k in range(0, 5000)]
random_11 = [(random.randint(0, 50000)) for k in range(0, 5500)]
random_12 = [(random.randint(0, 50000)) for k in range(0, 6000)]
random_13 = [(random.randint(0, 50000)) for k in range(0, 6500)]
random_14 = [(random.randint(0, 50000)) for k in range(0, 7000)]
random_15 = [(random.randint(0, 50000)) for k in range(0, 7500)]
random_16 = [(random.randint(0, 50000)) for k in range(0, 8000)]
random_17 = [(random.randint(0, 50000)) for k in range(0, 8500)]
random_18 = [(random.randint(0, 50000)) for k in range(0, 9000)]
random_19 = [(random.randint(0, 50000)) for k in range(0, 9500)]
random_20 = [(random.randint(0, 50000)) for k in range(0, 10000)]

nondecreasing_1 = sorted(random_1, key= int, reverse = True)
nondecreasing_2 = sorted(random_2, key= int, reverse = True)
nondecreasing_3 = sorted(random_3, key= int, reverse = True)
nondecreasing_4 = sorted(random_4, key= int, reverse = True)
nondecreasing_5 = sorted(random_5, key= int, reverse = True)
nondecreasing_6 = sorted(random_6, key= int, reverse = True)
nondecreasing_7 = sorted(random_7, key= int, reverse = True)
nondecreasing_8 = sorted(random_8, key= int, reverse = True)
nondecreasing_9 = sorted(random_9, key= int, reverse = True)
nondecreasing_10 = sorted(random_10, key= int, reverse = True)
nondecreasing_11 = sorted(random_11, key= int, reverse = True)
nondecreasing_12 = sorted(random_12, key= int, reverse = True)
nondecreasing_13 = sorted(random_13, key= int, reverse = True)
nondecreasing_14 = sorted(random_14, key= int, reverse = True)
nondecreasing_15 = sorted(random_15, key= int, reverse = True)
nondecreasing_16 = sorted(random_16, key= int, reverse = True)
nondecreasing_17 = sorted(random_17, key= int, reverse = True)
nondecreasing_18 = sorted(random_18, key= int, reverse = True)
nondecreasing_19 = sorted(random_19, key= int, reverse = True)
nondecreasing_20 = sorted(random_20, key= int, reverse = True)

pickle_out = open('ni_random_integers_1.pickle', 'wb')
pickle.dump(nondecreasing_1, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_2.pickle', 'wb')
pickle.dump(nondecreasing_2, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_3.pickle', 'wb')
pickle.dump(nondecreasing_3, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_4.pickle', 'wb')
pickle.dump(nondecreasing_4, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_5.pickle', 'wb')
pickle.dump(nondecreasing_5, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_6.pickle', 'wb')
pickle.dump(nondecreasing_6, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_7.pickle', 'wb')
pickle.dump(nondecreasing_7, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_8.pickle', 'wb')
pickle.dump(nondecreasing_8, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_9.pickle', 'wb')
pickle.dump(nondecreasing_9, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_10.pickle', 'wb')
pickle.dump(nondecreasing_10, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_11.pickle', 'wb')
pickle.dump(nondecreasing_11, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_12.pickle', 'wb')
pickle.dump(nondecreasing_12, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_13.pickle', 'wb')
pickle.dump(nondecreasing_13, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_14.pickle', 'wb')
pickle.dump(nondecreasing_14, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_15.pickle', 'wb')
pickle.dump(nondecreasing_15, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_16.pickle', 'wb')
pickle.dump(nondecreasing_16, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_17.pickle', 'wb')
pickle.dump(nondecreasing_17, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_18.pickle', 'wb')
pickle.dump(nondecreasing_18, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_19.pickle', 'wb')
pickle.dump(nondecreasing_19, pickle_out)
pickle_out.close()

pickle_out = open('ni_random_integers_20.pickle', 'wb')
pickle.dump(nondecreasing_20, pickle_out)
pickle_out.close()