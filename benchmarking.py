'''
Created on 2017/09/05

@author: Masaki Samejima
'''
import numpy
import scipy.sparse.linalg
import sparseqr

if __name__ == '__main__':    
    # QR decompose a sparse matrix M such that  Q R = M E
    #
    M = scipy.sparse.rand( 10, 10, density = 0.1 )
    Q, R, E, rank = sparseqr.qr( M )
    print( abs( Q*R - M*sparseqr.permutation_vector_to_matrix(E) ).sum() )  # should be approximately zero
