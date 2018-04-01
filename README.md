# Milkolov-Analogies
In this problem, we are supposed to perform Mikolov analogy test on the Mikolov analogy dataset. The Mikolov analogy test states that to predict analogy among words a simple algebraic operations can be used. Word analogy can be predicted if we are given a pair of words<a,b> and a third word c then we choose a forth word say d such that the analogy a is to b is same as c is to d. That is, the relationship between c and d should be as close as possible to that of a and b. 
Word embedding is the collective name for a set of language modelling and feature learning techniques in natural language processing (NLP) where words or phrases from the vocabulary are mapped to vectors of real numbers.

The analogy test is executed on GloVe Wikipedia 2014 + Gigaword 5 and GloVe Twitter. These set contains pre-trained vectors trained using GloVe algorithm. The corpus is used as Wikipedia 2014 + Gigaword 5 database containing about 6 billion words and has a vocabulary size of 400K each of which are represented using 50,100,200 and 300 dimensional vectors. I have used 100 dimensional vector. This embedding can be downloaded from: http://nlp.stanford.edu/data/glove.6B.zip

The other corpus is used as Twitter containing about 2 billion tweets and has a vocabulary size of 1.2 million each of which are represented using 25, 50,100 and 200 dimensional vectors. I have used 50 dimension vector. This embedding can be downloaded from:
http://nlp.stanford.edu/data/glove.twitter.27B.zip

#### Requirements:
- Python 3.5 or later
- Gensim package. For installation instructions, refer to: https://radimrehurek.com/gensim/install.html

#### Execution:
Prerequisite (install the gensim package):
1. Open command prompt
2. Type "pip install --upgrage gensim" to install the gensim package

Now.
1. Please make sure you download and put the pre-trained embedding in the same folder before executing the program.
- 'glove.twitter.27B.50d.txt' can be downloaded from http://nlp.stanford.edu/data/glove.twitter.27B.zip
- 'glove.6B.100d.txt' can be downloaded from http://nlp.stanford.edu/data/glove.6B.zip
2. Once you have both the .txt files in the folder go to command prompt.
3. Type "py ngupta16.py" to execute the file and get the output
