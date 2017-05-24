from gensim.models import word2vec

model = word2vec.Word2Vec.load_word2vec_format('german.model', binary=True)
model.save_word2vec_format('german.model_cconverted.txt', binary=False)



