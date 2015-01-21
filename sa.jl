#simulated annealing of the thing

using Distributions
using NPZ
#read a data matrix, a model matrix,
#create a matching matrix, learn a matching matrix

function read_data(file="data_mat.npy")
  data = npzread(file)
  data
end

function read_model(file="model_mat.npy")
  data = npzread(file)
  data
end

function neighbor(s)
  #permutation, really
  s_n
end

function temperature(i)
  #give some decaying temperature
end

function cost(s)
  #give the cost of the matching
end

function simulated_annealing(
  cost, #function from states to reals.
  s0, #initial state of system
  neighbor, #function from states to states (proposal creator)
  temperature, #function specifying temperature at time i
  iterations, #only termination conditions
  keep_best, #true if you want to return best state visited
  trace) #do we show a trace of system's evolution?
  s = s0
  best_s = s0
  for i = 1:iterations
    t = temperature(i)
    s_n = neighbor(s)
    if trace println("$i: s = $s") end
    if trace println("$i: s_n = $s_n") end
    y = cost(s)
    y_n = cost(s_n)
    if trace println("$i: y = $y") end
    if trace println("$i: y_n = $y_n") end
    if y_n <= y
      s = s_n
      if trace println("$i: accepted") end
    else
      p = exp(-((y_n - y) / t))
      if trace println("$i: p = $p") end
      if rand() <= p
        s = s_n
        if trace println("$i: accepted") end
      else
        s = s
        if trace println("$i: rejected") end
      end
      if trace println() end
      if cost(s) < cost(best_s)
        best_s = s
      end
    end
  end

  if keep_best
    best_s
  else
    s
  end
end

