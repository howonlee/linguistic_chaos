import numpy as np
import random
import matplotlib.pyplot as plt

#no animations, but interesting distances and stuff

if __name__ == "__main__":
    frac = np.zeros((1000, 1000))
    last_idx = (random.randint(0,999), random.randint(0,999))
    fig = plt.figure()
    ax = plt.axes(xlim=(0,1000), ylim=(0,1000))
    print frac, last_idx
