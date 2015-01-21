using Brownian
using NPZ

p = FBM(0:1/2^10:30, 0.1)
#show(rand(p))
npzwrite("quick_fbm.npy", rand(p, rtype=:chol))
