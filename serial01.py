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
