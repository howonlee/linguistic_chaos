import math
import numpy as np
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt

def bigrams(ls):
    return zip(ls, ls[1:])

def euclid_dist(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

#def manhattan_dist(first, second):

word_map = {}
word_counts = {}

if __name__ == "__main__":
    corpus = []
    with open ("corpus.txt", "r") as corpus_file:
        corpus = corpus_file.read().split()
    curr_idx = 0
    for word in corpus:
        if word in word_map:
            word_counts[word] += 1
        else:
            word_map[word] = curr_idx
            word_counts[word] = 1
            curr_idx += 1
    wordmat = sci_sp.dok_matrix((curr_idx, curr_idx))
    prev_pt = (0,0)
    distances = []
    for word1, word2 in bigrams(corpus):
        curr_pt = (word_map[word1], word_map[word2])
        distances.append(euclid_dist(prev_pt, curr_pt))
        prev_pt = curr_pt
    print len(distances)
    plt.plot(distances[:1000])
    plt.show()
