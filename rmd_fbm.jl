using Distributions

#translated from the glorious glorious fortran
function fbm(X, maxlevel, sigma, h)
  deltas = [] #array holding the standard deviations
  for i in 1:maxlevel
    delta[i] = sigma * power(0.5, i * h) * sqrt(1 - power(2, 2* (h-2)))
  end
  N = power(2, maxlevel)
  X[0] = 0
  X[N] = sigma * gaussian()
  mp_recursion(X, 0, N, 1, maxlevel, delta)
end

function mp_recursion(X, idx0, idx2, level, maxlevel, delta)
  idx1 = (idx0 + idx2) / 2
  X[idx1] = 0.5 * (X[idx0] + X[idx2]) + delta[level] * gaussian
  if level < maxlevel
    mp_recursion(X, idx0, idx1, level + 1, maxlevel, delta)
    mp_recursion(X, idx1, idx2, level + 1, maxlevel, delta)
  end
end
