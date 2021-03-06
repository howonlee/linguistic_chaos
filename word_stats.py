import sys
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

def manhattan_dist(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])

def first_dist(p0, p1):
    return (p0[0] - p1[0])

def second_dist(p0, p1):
    return (p0[1] - p1[1])

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

def phase_space_plot(dists, num_pts=3000):
    xs_first = dists[:num_pts]
    xs_second = dists[1:num_pts+1]
    plt.plot(xs_first, xs_second)
    plt.show()
    plt.savefig("dist_retmap")

def return_map(dists, num_pts=3000):
    vals = dists[:num_pts]
    ret_mat = np.zeros((num_pts, num_pts))
    for x in xrange(num_pts):
        for y in xrange(num_pts):
            ret_mat[x,y] = abs(vals[x] - vals[y])
    plt.matshow(ret_mat)
    plt.show()
    plt.savefig("dist_retmap")

def return_poincare_plot(dists, num_pts=3000):
    """
    Make it a tensor
    """
    vals = dists[:num_pts]
    vals2 = dists[1:num_pts+1]
    vals3 = dists[2:num_pts+2]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(vals, vals2, vals3)
    plt.show()
    plt.savefig("poin_plot")

def word_plot(pts, num_pts=1000):
    wordmat = sci_sp.dok_matrix((len(corpus), len(corpus)))
    xs = map(operator.itemgetter(0), pts)[:num_pts]
    ys = map(operator.itemgetter(1), pts)[:num_pts]
    plt.scatter(xs, ys)
    plt.show()
    plt.savefig("word_retmap")

def random_wordmap(corpus):
    global word_counts, word_map
    vocab_range = range(len(set(corpus)))
    random.shuffle(vocab_range) #look at that mutation
    for word in corpus:
        word_counts[word] += 1
    for word in corpus:
        if word not in word_map:
            word_map[word] = vocab_range.pop()
    return word_counts, word_map

def inorder_wordmap(corpus):
    global word_counts, word_map
    vocab_range = range(len(set(corpus)))
    for word in corpus:
        word_counts[word] += 1
    for word in corpus:
        if word not in word_map:
            word_map[word] = vocab_range.pop()
    return word_counts, word_map

def count_wordmap(corpus):
    word_counts = collections.Counter()
    word_map = {}
    vocab_range = range(len(set(corpus)))
    for word in corpus:
        word_counts[word] += 1
    for word, _ in word_counts.most_common():
        word_map[word] = vocab_range.pop()
    return word_counts, word_map

def distance_hist(distances):
    distances = map(int, distances)
    dist_ctr = collections.Counter(distances)
    plt.hist(map(operator.itemgetter(1), dist_ctr.most_common()))
    plt.yscale("log")
    plt.savefig("distances_hist")
    plt.show()


if __name__ == "__main__":
    corpus = []
    with open ("corpus.txt", "r") as corpus_file:
        corpus = corpus_file.read().split()
    word_counts, word_map = random_wordmap(corpus)
    #word_counts, word_map = inorder_wordmap(corpus)
    #word_counts, word_map = count_wordmap(corpus)
    prev_pt = (0,0)
    distances = []
    pts = []
    for word1, word2 in bigrams(corpus):
        curr_pt = (word_map[word1], word_map[word2])
        pts.append(curr_pt)
        print curr_pt[0], curr_pt[1]
        distances.append(euclid_dist(prev_pt, curr_pt))
        prev_pt = curr_pt
    #distance_hist(distances)
    #plt.plot(distances[:5000])
    #plt.show()
    #return_poincare_plot(distances)
    #phase_space_plot(distances)
    #return_map(distances)
    #word_plot(pts)
