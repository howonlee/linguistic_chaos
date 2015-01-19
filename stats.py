import math
import random
import operator
import numpy as np
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bigrams(ls):
    return zip(ls, ls[1:])

def euclid_dist(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def first_dist(p0, p1):
    return (p0[0] - p1[0])

#def manhattan_dist(first, second):

word_map = {}
word_counts = {}

if __name__ == "__main__":
    corpus = []
    with open ("corpus.txt", "r") as corpus_file:
        corpus = corpus_file.read().split()
    word_range = range(len(corpus))
    random.shuffle(word_range) #look at that mutation
    for word in corpus:
        if word in word_map:
            word_counts[word] += 1
        else:
            word_map[word] = word_range.pop()
            word_counts[word] = 1
    wordmat = sci_sp.dok_matrix((len(corpus), len(corpus)))
    prev_pt = (0,0)
    #distances = []
    pts = []
    for word1, word2 in bigrams(corpus):
        curr_pt = (word_map[word1], word_map[word2])
        pts.append(curr_pt)
        #distances.append(first_dist(prev_pt, curr_pt))
        #prev_pt = curr_pt
    #print len(distances)
    xs = map(operator.itemgetter(0), pts)[:1000]
    ys = map(operator.itemgetter(1), pts)[:1000]
    zs = range(len(pts))[:1000]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xs, ys, zs)
    #plt.plot(distances[:100])
    plt.show()
