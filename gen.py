from fbm_stats import generate_fbm
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fbm = generate_fbm(10000)
    bins = np.linspace(0, 1, 1000)
    np.save("digitized_fbm", np.digitize(fbm, bins))
    #plt.plot(generate_fbm())
    #plt.show()
