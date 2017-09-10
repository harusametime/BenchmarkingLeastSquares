'''
Created on 2017/09/05

@author: Masaki Samejima
'''
import numpy as np
import scipy.sparse.linalg
import sparseqr
import time

if __name__ == '__main__':    

    n_trials = 10
    
    matrix_size = np.array([2000,1000])
    matrix_density = 0.1

    # Solve an overdetermined linear system  A x = b  in the least-squares sense
    #
    # The same routine also works for the usual non-overdetermined case.
    #
    total_time = 0
    for i in range(n_trials):
        A = scipy.sparse.rand(matrix_size[0],matrix_size[1], density = matrix_density )  
        b = np.random.random(matrix_size[0])  
        start = time.clock()
        x = scipy.sparse.linalg.lsqr(A, b)    
        end = time.clock()
        total_time += end-start
    print total_time/float(n_trials), "sec."
    
    # Solve an overdetermined linear system  A x = b  in the least-squares sense
    #
    # The same routine also works for the usual non-overdetermined case.
    #
    total_time = 0
    for i in range(n_trials):
        A = scipy.sparse.rand(matrix_size[0],matrix_size[1], density = matrix_density )  
        b = np.random.random(matrix_size[0])  
        start = time.clock()
        x = sparseqr.solve( A, b, tolerance = 0 )    
        end = time.clock()
        total_time += end-start
    
    print total_time/float(n_trials), "sec."