import numpy as np
import sklearn.preprocessing

if __name__ == "__main__":
    fbm = np.load("quick_fbm.npy")
    fbm_std = (fbm - fbm.min()) / (fbm.max() - fbm.min())
    new_fbm = fbm_std * 100000
    pts = map(int, list(new_fbm))
    for first, second in zip(pts, pts[1:]):
        print first, second
