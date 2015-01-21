using Brownian
using NPZ

p = FBM(0:1/2^20:1, 0.1)
#show(rand(p))
npzwrite("quick_fbm.npy", rand(p))
