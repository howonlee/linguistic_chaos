from fbm_stats import generate_fbm
from stats import count_wordmap
import numpy as np
import collections
import operator
import matplotlib.pyplot as plt

def gen_and_save_fbm():
    fbm = generate_fbm(25000)
    fbm = fbm * 3000
    np.save("digitized_fbm", fbm)

def load_fbm(name="quick_fbm.npy"):
    return (np.load(name) * 3000)

def load_corpus(name="corpus.txt"):
    with open(name, "r") as corpus_file:
        corpus = corpus_file.read().split()
        word_counts, word_map = count_wordmap(corpus)
    return word_counts, word_map

def fbm_commons():
    fbm = collections.Counter(map(int, list(load_fbm())))
    return fbm.most_common()

def fbm_list():
    return map(int, list(load_fbm()))

def fbm_inspect():
    word_counts, word_map = load_corpus()
    word_common = word_counts.most_common()
    plt.hist(map(operator.itemgetter(1), fbm_commons()))
    plt.yscale("log")
    plt.show()

def generate():
    word_counts, _ = load_corpus()
    word_commons = word_counts.most_common()
    curr_val = 0
    val_map = {}
    for word, val in fbm_commons():
        val_map[word] = word_commons[curr_val][0]
        curr_val += 1
    genned = []
    for word in fbm_list():
        genned.append(val_map[word])
    return genned

if __name__ == "__main__":
    #fbm_inspect()
    print " ".join(generate())
