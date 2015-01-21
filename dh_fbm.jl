using Brownian
using NPZ

p = FBM(0:1/2^10:10, 0.1)
#show(rand(p))
npzwrite("quick_fbm.npy", rand(p, rtype=:chol))
