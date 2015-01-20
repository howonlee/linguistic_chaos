import math
import random
import operator
import collections
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
word_counts = collections.Counter()

def bigram_plot3d(pts):
    xs = map(operator.itemgetter(0), pts)[:700]
    ys = map(operator.itemgetter(1), pts)[:700]
    zs = map(lambda x : x * 10, range(len(pts))[:700])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(xs, ys, zs)
    plt.show()
    plt.savefig("trajectory")

def dist_plot(dists, num_pts=200):
    plt.plot(dists[:num_pts])
    plt.show()
    plt.savefig("distances")

def return_map(dists, num_pts=200):
    xs_first = something ####
    xs_second = something ####
    plt.scatter(first, second)
    plt.show()
    plt.savefig("dist_retmap")

if __name__ == "__main__":
    corpus = []
    with open ("corpus.txt", "r") as corpus_file:
        corpus = corpus_file.read().split()
    vocab_range = range(len(set(corpus)))
    random.shuffle(vocab_range) #look at that mutation
    for word in corpus:
        word_counts[word] += 1
    for word in corpus:
        if word not in word_map:
            word_map[word] = vocab_range.pop()
    #for word, _ in word_counts.most_common():
        #word_map[word] = word_range.pop()
    wordmat = sci_sp.dok_matrix((len(corpus), len(corpus)))
    prev_pt = (0,0)
    distances = []
    pts = []
    for word1, word2 in bigrams(corpus):
        curr_pt = (word_map[word1], word_map[word2])
        pts.append(curr_pt)
        distances.append(first_dist(prev_pt, curr_pt))
        prev_pt = curr_pt
    dist_plot(distances)
