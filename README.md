# Benchmarking Least Squares

This reports performance of libraries for solving *Ax =b* in the least-squares sense.


# Libralies

- Scipy LSQR (scipy.sparse.linalg.lsqr)
- PySPQR (https://github.com/yig/PySPQR)
  - Use suitesparse-metis-for-windows for installing SuiteSparse
- PySparse (http://pysparse.sourceforge.net/)

# Machine

- OS: Windows 10 Enterprise 64bit
- CPU: Intel(R) Xeon(R) CPU E3-1225 v5 @3.30GHz 
- RAM: 32.0 GB


# Results

Matrix size| Density | Scipy LSQR | PySPQR| PySParse |
|:--------:|:-------:|:----------:|:-----:|:-----:|
|2000 x 1000| 0.1    |            |4.96 sec. |      |