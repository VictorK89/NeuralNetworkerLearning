import numpy as np

f = np.loadtxt("result_regressor_basic_old", dtype=float)
gold = np.loadtxt("top_or_not_usable_binary_10", dtype=float)



t = 0.02


for i in np.arange(0.01, 1.0, 0.01):
        truePositive = 0.0
        trueNegative = 0.0
        for g in range(0, len(f)):
                tempToCompare = 0.0        
                if i > f[g]:
                        tempToCompare = 0.0
                else:
                        tempToCompare = 1.0
                if tempToCompare == gold[g]:
                        truePositive = truePositive+1
                else:
                        trueNegative = trueNegative+1

        print(truePositive/(truePositive+trueNegative))


zero =  24725.0
total = 27674.0
one = total - zero

precision = zero/total

print("precision:", precision)
