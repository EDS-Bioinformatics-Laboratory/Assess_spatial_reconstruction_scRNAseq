###########
# imports #
###########

from __future__ import print_function
import pandas as pd
import scanpy as sc
from numpy import isnan
import numpy as np
from sklearn.neighbors import kneighbors_graph
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
import os
from novosparc_preprocessing import log_normalize_dge

# Reading expression data to scanpy AnnData (cells x genes)
data_dir = 'C:/Users/deand/OneDrive/Documents/Liver_lobules/novosparc_files/'
data_path = os.path.join(data_dir, 'raw_expression_counts-Liver_novosparc_formatted.txt')
dataset = sc.read(data_path).T
gene_names = dataset.var.index.tolist()
num_cells, num_genes = dataset.shape
print('number of cells: %d' % num_cells)
print('number of genes: %d' % num_genes)
dataset.X=log_normalize_dge(dataset.X)
where_are_NaNs=isnan(dataset.X)
dataset.X[where_are_NaNs] = 0

num_neighbors_source = 4 # number of neighbors for nearest neighbors graph at source
A_expression = kneighbors_graph(dataset.X, num_neighbors_source, mode='connectivity', include_self=True, metric='correlation')
sp_expression = dijkstra(csgraph = csr_matrix(A_expression), directed = False, return_predecessors = False)
DF = pd.DataFrame(sp_expression)
DF.to_csv("C:/Users/deand/OneDrive/Documents/cortex_data/novosparc_files/mouse_lobules_dijkstra.csv")
sp_expression_max = np.nanmax(sp_expression[sp_expression != np.inf])
sp_expression[sp_expression > sp_expression_max] = sp_expression_max #set threshold for shortest paths

DF3 = pd.DataFrame(sp_expression)
DF3.to_csv("C:/Users/deand/OneDrive/Documents/cortex_data/novosparc_files/mouse_lobules_dijkstra_no_inf_values.csv")
# Set normalized cost matrices based on shortest paths matrices at target and source spaces
cost_expression = sp_expression / sp_expression.max()
print('cost',cost_expression)
DF1 = pd.DataFrame(cost_expression)
DF1.to_csv("C:/Users/deand/OneDrive/Documents/cortex_data/novosparc_files/normalized_mouse_lobules.csv")
cost_expression -= np.mean(cost_expression)
print('cost post',cost_expression)
DF = pd.DataFrame(cost_expression)
DF.to_csv("C:/Users/deand/OneDrive/Documents/cortex_data/novosparc_files/normalized_and_centered_mouse_lobules.csv")
