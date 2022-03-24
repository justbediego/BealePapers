import numpy as np
import pickle

model = None
try:
    with open("./model.dat", "rb") as modelFile:
        model = pickle.load(modelFile)
except:
    print("no model")

if __name__== "__main__":
    ps = np.zeros((26, 26), dtype=np.float32)
    with open("./english.txt", "r") as dataFile:
        lastCode = None
        while dataFile.readable():
            one = dataFile.read(1)
            if not one:
                break
            code = ord(one) - 97
            if lastCode != None:
                ps[lastCode, code] = ps[lastCode, code] + 1
            lastCode = code
    ps = ps + 1
    ps = ps / np.sum(ps, axis = 1).reshape(26, 1)
    with open("./model.dat", "wb") as modelFile:
        pickle.dump(ps, modelFile)
        model = ps

def getLikelihood(signal):
    l = 0
    lastCode = ord(signal[0]) - 97
    for i in range(1, len(signal)):
        code = ord(signal[i]) - 97
        p = model[lastCode, code]
        l = l + np.log(p)
        lastCode = code
    return l
        
