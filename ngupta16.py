import gensim
import logging
import pprint
from gensim.scripts.glove2word2vec import glove2word2vec
#Converting .txt file to wordvec file
print("Problem 1")
print("For Twitter Pre trained word vector accuracies are as follows:")
glove_input_file = 'glove.twitter.27B.50d.txt'
word2vec_output_file = 'glove.twitter.27B.50d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)

# Loading Glove's Pre-trained twitter word vectors
model = gensim.models.KeyedVectors.load_word2vec_format('glove.twitter.27B.50d.txt.word2vec', binary=False)
		
# for logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model.accuracy('word-text.txt')
print("\n")
print("Problem 2 Antonyms of the given word")
print("1. Cold")
pprint.pprint(model.wv.similar_by_word('cold', topn=10))
print("\n")
print("2. Come")
pprint.pprint(model.wv.similar_by_word('come', topn=10))
print("\n")
print("3. Small")
pprint.pprint(model.wv.similar_by_word('small', topn=10))
print("\n")
print("Problem 3")
model.accuracy('problem3.txt')
print("\n")
print("Problem 1")
print("For Wikipedia 2014 + Gigaword 5 Pre trained word vector accuracies are as follows:")
glove_input_file = 'glove.6B.100d.txt'
word2vec_output_file = 'glove.6B.100d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)

# Loading Glove's Pre-trained Wikipedia 2014 + Gigaword 5 word vectors 
model = gensim.models.KeyedVectors.load_word2vec_format('glove.6B.100d.txt.word2vec', binary=False)
		
# for logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model.accuracy('word-text.txt')


print("\n")
print(" Problem 2 Antonyms of the given word")
print("1. Cold")
pprint.pprint(model.wv.similar_by_word('cold', topn=10))
print("\n")
print("2. Come")
pprint.pprint(model.wv.similar_by_word('come', topn=10))
print("\n")
print("3. Small")
pprint.pprint(model.wv.similar_by_word('small', topn=10))
print("\n")
print("Problem 3")
model.accuracy('problem3.txt')