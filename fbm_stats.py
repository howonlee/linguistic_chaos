import numpy as np
import numpy.linalg as np_lin
import numpy.random as np_rand
import matplotlib.pyplot as plt

def normalize(arr):
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    rng = arr_max - arr_min
    return 1 - ((arr_max - arr) / rng)

def generate_fbm():
    dim_len = 5000
    times = range(1, dim_len + 1)
    gamma = np.zeros((dim_len, dim_len))
    h = 0.6
    double_h = h * 2
    for i in times:
        for j in times:
            gamma[i-1, j-1] = (i ** (double_h) + j ** (double_h) - (abs(j - i) ** double_h)) / 2
    sigma = np_lin.cholesky(gamma)
    vec = np_rand.normal(size=(dim_len,))
    u = np.dot(sigma, vec)
    u = normalize(u)
    return u

def return_map(vals, num_pts=3000):
    #implement this properly
    xs_first = vals[:num_pts]
    xs_second = vals[1:num_pts+1]
    plt.scatter(xs_first, xs_second)
    plt.show()
    plt.savefig("fbm_retmap")

return_map(generate_fbm())
#plt.plot(generate_fbm())
#plt.show()
