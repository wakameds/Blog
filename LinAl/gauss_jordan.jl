using Plots, Statistics

#gauss-jordan elimination
function gauss_jordan(A::Matrix{Float64}, b::Vector{Float64})
    #augumented matrix
    AM = hcat(A, b)
    n = size(A, 1)

    for i = 1:n
        temp = AM[i,i]
        AM[i, i:end] /= temp
        
        for j = 1:n
            if i != j
                temp = AM[j,i]
                for k = 1:n+1
                    AM[j, k] -= AM[i, k] * temp
                end
            end
        end
    end
    AM[:, n+1]
end


#gauss elimination
function gauss(A::Matrix{Float64}, b::Vector{Float64})
    #augmented matrix
    AM = hcat(A, b)
    n = size(A, 1)
    #forward elimination
    for i = 1:n-1
        for j = i+1:n
            temp = AM[j,i]/AM[i,i]
            for k = i:n+1
                AM[j,k] -= temp*AM[i, k]
            end
        end
    end
    #backward substitute
    for i = n:-1:1
        for j = i+1:n
            AM[i, n+1] -= AM[i, j]*AM[j, n+1]
        end
        AM[i, n+1] /= AM[i, i]
    end
    AM[:, n+1]
end


#time complexity
gj_times = []
g_times = []

for n in 1:10:500
    A = rand(n,n)
    b = rand(n)
    push!(gj_times, @elapsed gauss_jordan(A,b))
    push!(g_times, @elapsed gauss(A,b))
end

X = 1:10:500
plot(X, [gj_times g_times],label=[L"gj" L"g"], xlabel = L"n", ylabel=L"time (sec)")
plot!(size=(450,300))
savefig("gj_g.png")

mean(gj_times), mean(g_times)