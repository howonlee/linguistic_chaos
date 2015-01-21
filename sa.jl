#simulated annealing of the thing

using Optim
using NPZ
#read a data matrix, a model matrix,
#create a matching matrix, learn a matching matrix

#the data matrix is the fbm
#the model matrix is the real words

function read_data(file="data_mat.npy")
  data = npzread(file)
  data
end

function read_model(file="model_mat.npy")
  data = npzread(file)
  data
end

function matching_wrapper()
  matching_cost = function()
    #this is the only real thing which we'll fold into the optimization algorithm
  end
  matching_cost
end


