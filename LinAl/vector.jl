using LinearAlgebra

#vector
v1 = [1,2,3]
v2 = [4,5,6]

v2_2 = [4.0,5,6]


length(v1)

#addion and subtraction
v1 + v2
v1 - v2

#multiplication
α = 2
α*v1


#inner product
v1'*v2
sum(v1[i]*v2[i] for i in 1:length(v1))
dot(v1,v2)
v1⋅v2


#norm
norm(v1)
sqrt(v1'*v1)
sqrt(sum(v1[i]*v1[i] for i in 1:length(v1)))

norm(v1,1)