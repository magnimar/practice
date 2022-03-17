from myhashkey import *
from random import Random

if __name__ == "__main__":
    k1 = MyHashableKey(1, "one")
    print(hash(k1))
    k2a = MyHashableKey(2, "two")
    print(hash(k2a))
    k2b = MyHashableKey(2, "two")
    print(hash(k2b))
    test = MyHashableKey(10, "two")
    test2 = MyHashableKey(12, "two")
    print(test.__hash__())
    print(test2.__hash__())
    print(k1 == k2a)
    print(k2a == k2b)
    rand = Random()
    rand.seed(1)
    
    keep_hash = [0] * 8
    for i in range(1000):
        has = MyHashableKey(rand.randint(0, 1000000), str(rand.randint(0, 100000))).__hash__()
        keep_hash[has%8] += 1

    print(keep_hash)
    