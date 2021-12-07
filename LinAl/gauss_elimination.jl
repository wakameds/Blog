function gauss(A::Matrix{Float64}, b::Vector{Float64})
    #augmented matrix
    AM = hcat(A, b)
    n = size(A, 1)
    #forward setp
    for i = 1:n-1
        for j = i+1:n
            temp = AM[j,i]/AM[i,i]
            for k = i:n+1
                AM[j,k] -= temp*AM[i, k]
            end
        end
    end
    #backward step
    for i = n:-1:1
        for j = i+1:n
            AM[i, n+1] -= AM[i, j]*AM[j, n+1]
        end
        AM[i, n+1] /= AM[i, i]
    end
    AM[:, n+1]
end

