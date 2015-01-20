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
    dim_len = 1000
    times = range(1, dim_len + 1)
    gamma = np.zeros((dim_len, dim_len))
    h = 0.75
    double_h = h * 2
    for i in times:
        for j in times:
            gamma[i-1, j-1] = (i ** (double_h) + j ** (double_h) - (abs(j - i) ** double_h)) / 2
    sigma = np_lin.cholesky(gamma)
    vec = np_rand.normal(size=(dim_len,))
    u = np.dot(sigma, vec)
    u = normalize(u)
    return u

def generate_sin():
    return np.sin(np.linspace(0, 10, 100))

def return_map(vals, num_pts=100):
    #implement this properly
    vals = vals[:num_pts]
    ret_mat = np.zeros((num_pts, num_pts))
    #probably a vectorized way to do it
    for x in xrange(num_pts):
        for y in xrange(num_pts):
            ret_mat[x,y] = abs(vals[x] - vals[y])
    plt.matshow(ret_mat)
    plt.show()
    plt.savefig("fbm_retmap")

#return_map(generate_sin())
return_map(generate_fbm())
#plt.plot(generate_fbm())
#plt.show()
