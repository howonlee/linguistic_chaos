from fbm_stats import generate_fbm
from stats import count_wordmap
import numpy as np
import collections
import operator
import matplotlib.pyplot as plt

def gen_and_save_fbm():
    fbm = generate_fbm(10000)
    fbm = fbm * 3000
    np.save("digitized_fbm", fbm)

def load_fbm(name="digitized_fbm.npy"):
    return np.load(name)

def load_corpus(name="corpus.txt"):
    with open(name, "r") as corpus_file:
        corpus = corpus_file.read().split()
        word_counts, word_map = count_wordmap(corpus)
    return word_counts, word_map

def fbm_inspect():
    word_counts, word_map = load_corpus()
    word_common = word_counts.most_common()
    fbm = collections.Counter(map(int, list(load_fbm())))
    common = fbm.most_common()
    plt.hist(map(operator.itemgetter(1), common))
    plt.yscale("log")
    plt.show()

if __name__ == "__main__":
    word_counts, _ = load_corpus()
    print word_counts.most_common()[:100]
    #fbm_inspect()
    #plt.plot(load_fbm())
    #plt.show()
