import pickle


try:
    with open('record.txt', 'rb') as f:
        record = pickle.load(f)
except:
    with open('record.txt', 'wb') as f:
        pickle.dump(set(), f, True)
    with open('record.txt', 'rb') as f:
        record = pickle.load(f)

record.add('123123')
with open('record.txt', 'wb') as f:
    pickle.dump(set(), f, True)