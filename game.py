import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def next_idx(idx):
    ifs_map = {
            1 : [[],[]],
            2 : [[],[]],
            3 : [[],[]],
    }
    next_ifs = random.choice([0,1,2])
    return ifs_map[next_ifs]

def animate(i):
    next_idx = next_idx(i)

if __name__ == "__main__":
    frac = np.zeros((1000, 1000))
    last_idx = (random.randint(0,999), random.randint(0,999))
    fig = plt.figure()
    ax = plt.axes(xlim=(0,1000), ylim=(0,1000))
    print frac, last_idx
