#extremal optimization for graph matching

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
