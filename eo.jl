#simulated annealing of the thing

using Optim
using NPZ
#read a data matrix, a model matrix,
#create a matching matrix, learn a matching matrix

#the model matrix is the fbm
#the data matrix is the real words

function read_data(file="data_mat.npy")
  data = npzread(file)
  data
end

function read_model(file="model_mat.npy")
  data = npzread(file)
  data
end

function make_match(datamat, modelmat)
end

function matching_wrapper()
  total_cost = function()
    #this is the only real thing which we'll fold into the optimization algorithm
  end

  local_cost = function(i)
  end

  total_cost, local_cost
end

function eo()
  #implement eo
  #probably start with piecewise local search
end
