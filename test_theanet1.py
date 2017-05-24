import numpy as np
import theanets
import linecache


net = theanets.Regressor([353, 150, 1])
net.load('model_regressor_nomen_final')



#inputs = np.loadtxt('vector_list_usable_1')
#outputs = np.loadtxt('top_or_not_usable_binary_1')

g = np.loadtxt('vector_nomen_10')


#h = np.random.randn(34308, 1).astype('f')
#h = np.loadtxt('top_or_not_usable_binary_9')
#w = [h[x:x+1] for x in xrange(0, len(h), 1)] ##convert into list of numpy arrays
#q = np.asarray(w) ##convert into numpy array of numpy arrays


#net.train([g, q])

#net.save('model_regressor_nomen_final')

result = net.predict(g)
#score = net.score()

np.savetxt('result_regressor_nomen', result)
#np.savetxt('score', score)

#test = np.loadtxt('vector_list_usable_9')
#print(test)



