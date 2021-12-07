using LinearAlgebra

#matrices
A = [1 2; 7 0; 5 1]
B = [3 4; 0 2; 1 1]A
C = [8 3; 5 4]
D = [5 1; 2 0]
E = rand([1,2,3],5,5)

#3x2 zero matrix
zero = zeros(3,2)

#3x3 identity matrix
Matrix(I,3,3)
C+I
D-I
E-I

#Diagonal matrix of A
Diagonal(A)
Diagonal(C)
Diagonal(E)


#Triangli matrix
UpperTriangular(E)
LowerTriangular(E)

#Transposed matrix
Transpose(A)
A'

#addiction
A + B
A.+ 3

#subtraction
C - D
C.- 1

#multiplication with scalar
3A
3*A

#multimpication with vector
v = [1; 2]
v2 = vec([1 2])

A*v
A*v2

#multiplication with matrix
A*C
B*C
