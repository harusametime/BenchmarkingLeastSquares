# Benchmarking Least Squares

This reports performance of libraries for solving *Ax =b* in the least-squares sense.


# Libralies

- Scipy LSQR (scipy.sparse.linalg.lsqr)
- PySPQR (https://github.com/yig/PySPQR)
  - Use suitesparse-metis-for-windows for installing SuiteSparse
- PySparse (http://pysparse.sourceforge.net/)
- CVXPY+SCS (http://www.cvxpy.org/en/latest/)

# Machine

- OS: Windows 10 Enterprise 64bit
- CPU: Intel(R) Xeon(R) CPU E3-1225 v5 @3.30GHz 
- RAM: 32.0 GB


# Results


Matrix size| Density | Criteria| Scipy LSQR | Scipy LSMR |PySPQR| PySParse |CVXPY+SCS
|:--------:|:-------:|:--------:|:----------:|:-----:|:-----:|:-----:|:--------:|
|2000 x 1000| 0.1    | **Time** | 0.038 sec | 0.016 sec|4.996 sec. |      |0.36 sec.|
|           |        | **Error** | |0.0012 |2.01e-13 |     |0.0021|
