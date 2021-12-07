using LinearAlgebra

#matrix and vector
A = [1 1; 2 -1]
b = [3; -4]

#inverse matrix
det(A)

#solution
inv(A)*b
A \ b



#time complexity
using Statistics, Plots

inv_times = []
back_times = []
for _ in 1:1000
    B = rand(1000,1000)
    b = rand(1000)
    push!(inv_times, @elapsed inv(B)*b)
    push!(back_times, @elapsed B\b)
end


histogram([inv_times, back_times], alpha=0.4, bins = 300,
        label=[L"inv" L"bs"], xlabel = L"time (sec)", ylabel=L"count")
histogram!(size=(450,300))
savefig("tc.png")

mean(inv_times), std(inv_times)
mean(back_times), std(back_times)
