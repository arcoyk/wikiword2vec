import pickle
import random as rd

data = {}
with open('data/t_a.pickle', mode='rb') as f:
  data = pickle.load(f)

for k in rd.sample(data.keys(), 10):
  print(k, data[k][:5])
