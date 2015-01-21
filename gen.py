from fbm_stats import generate_fbm
import numpy as np
import collections
import operator
import matplotlib.pyplot as plt

def gen_and_save_fbm():
    fbm = generate_fbm(10000)
    bins = np.linspace(0, 1, 1000)
    np.save("digitized_fbm", np.digitize(fbm, bins))

def load_fbm(name="digitized_fbm.npy"):
    return np.load(name)

if __name__ == "__main__":
    fbm = collections.Counter(list(load_fbm()))
    common = fbm.most_common()
    plt.hist(map(operator.itemgetter(1), common))
    plt.show()
