# 1. Module:pickle is for serialization.
import pickle


class A():
    def do_sth(self):
        pass


a = A()
print(a)
pickled = pickle.dumps(a)
print(pickled)
b = pickle.loads(pickled)
print(b)

with open('data.pickle', 'wb') as f:
    pickle.dump(b, f, pickle.HIGHEST_PROTOCOL)

with open('data.pickle', 'rb') as f:
    c = pickle.load(f)
    print(c)