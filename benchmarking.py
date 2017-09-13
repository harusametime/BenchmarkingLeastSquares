'''
Created on 2017/09/05

@author: Masaki Samejima
'''
import numpy as np
import scipy.sparse.linalg
import sparseqr
import time

from pysparse.sparse import spmatrix, sparseMatrix
from pysparse.precon import precon
from pysparse.tools import poisson, spmatrix_util
from pysparse.itsolvers import krylov
from nlp import optimize
from nlp.model.nlpmodel import QPModel, LPModel

from cvxpy import *

if __name__ == '__main__':    

    # Libraries to be evaluated
    ScipyLSQR, PySPQR, CVXPY_SCS, PySparse =(0,0,1,0)
    
    n_trials = 10
    
    matrix_size = np.array([2000,1000])
    matrix_density = 0.1

    
    # ScipyLSQR
    if ScipyLSQR == 1:
        total_time = 0
        total_error = 0
        for i in range(n_trials):
            A = scipy.sparse.rand(matrix_size[0],matrix_size[1], density = matrix_density )  
            x_true = np.random.random(matrix_size[1])
            b = A * x_true
            A = A.tocsr()
            start = time.clock()
            x = scipy.sparse.linalg.lsqr(A, b)[0]
            end = time.clock()
            total_time += end-start
            total_error += np.linalg.norm(x-x_true, ord=2)
        print "Average time:", total_time/float(n_trials), "sec."
        print "Average error:", total_error/float(n_trials)
     
    # PySPQR
    if PySPQR == 1:
        total_time = 0
        total_error = 0
        for i in range(n_trials):
            A = scipy.sparse.rand(matrix_size[0],matrix_size[1], density = matrix_density )  
            x_true = np.random.random(matrix_size[1])
            b = A * x_true
            start = time.clock()
            A = A.tocsr()
            x = sparseqr.solve( A, b, tolerance= 1e-4)    
            end = time.clock()
            total_time += end-start
            total_error += np.linalg.norm(x-x_true, ord=2)
        print "Average time:", total_time/float(n_trials), "sec."
        print "Average error:", total_error/float(n_trials)
  
    # CVXPY
    if CVXPY_SCS == 1:
        total_time = 0
        total_error = 0
        for i in range(n_trials):
            A = scipy.sparse.rand(matrix_size[0],matrix_size[1], density = matrix_density )  
            x_true = np.random.random(matrix_size[1])
            b = A * x_true
            x = Variable(matrix_size[1])
            objective = Minimize(sum_squares(A*x - b))
            constraints = []
            prob = Problem(objective, constraints)
            start = time.clock()
            prob.solve(solver=SCS)
            end = time.clock()
            x = np.asarray(x.value).reshape((-1))            
            total_time += end-start
            total_error += np.linalg.norm(x-x_true, ord=2)
            
        print "Average time:", total_time/float(n_trials), "sec."
        print "Average error:", total_error/float(n_trials)    
    
    # PySparse & NL.py & 
#     A = scipy.sparse.rand(matrix_size[0],matrix_size[1], density = matrix_density )  
#     x_true = np.random.random(matrix_size[1])
#     b = A * x_true
#     qp = QPModel(-b.T * A , A.T*A)


#     b = np.ones(n*n)
#     x = np.empty(n*n)
#     info, iter, relres = krylov.pcg(L.to_sss(), b, x, 1e-12, 2000)
#     print info
#     
#     total_time = 0
#     total_error = 0
#     for i in range(n_trials):
#         A = scipy.sparse.rand(matrix_size[0],matrix_size[1], format = "lil", density = matrix_density)
#         A = sparseMatrix.SparseMatrix(nrow=matrix_size[0], ncol=matrix_size[1])
#         x_true = np.random.random(matrix_size[1])
#         b = A * x_true
#         
#         A_sp = A
#         x = np.empty(matrix_size[1])
#         
#         b = A.T * b
#         #print b
#         A = A.T * A
#         start = time.clock()
#         A_sp = spmatrix.ll_mat(matrix_size[1],matrix_size[1], 1) 
#         #A_sp  = A
#         #print A_sp
#         info, iter, relres = krylov.pcg(A_sp.to_sss(), b, x, 1e-8, 2000)
#         end = time.clock()
#         total_time += end-start
#         total_error += np.linalg.norm(x-x_true, ord=2)
#     print "Average time:", total_time/float(n_trials), "sec."
#     print "Average error:", total_error/float(n_trials)