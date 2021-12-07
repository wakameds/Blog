using Plots, LinearAlgebra, LaTeXStrings

function sol_L(L, b)
    #perform forward substitution
    n = size(L)[1] 
    y = zeros(n)
    for i in 1:n
        prod = dot(y[1:i-1], L[i,1:i-1])
        y[i] = (b[i] - prod)/L[i,i]
    end
    y
end


function sol_U(U, y)
    #perform backward substitution
    n = size(U)[1] 
    x = zeros(n)
    for i in n:-1:1
        prod = dot(x[i+1:n],U[i,i+1:n])
        x[i] = (y[i] - prod)/U[i,i]
    end
    x
end


function sol_LU(A, b)
    #implement LU decompositon
    L, U = lu(A)
    y = sol_L(L,b)
    return sol_U(U, y)
end



errs = []
for n in 1:1000
    A = rand(1:100,n,n)
    b = ones(n)
    err = norm(sol_LU(A,b)-A\b)
    push!(errs, err)
end

N = 1:1000
plot(N, errs,legend = false, xlabel = L"n", ylabel=L"error")
plot!(size=(450,300))
savefig("LU_error.png")







#tiem complexity
using Plots, LaTeXStrings
A = rand(10^6,10^6)
b = rand(10^6)
t = @elapsed A\b #sec

times_O1 = []
times_O2 = []

for n in 1:100:10^4
    O1 = log10(n^2)
    O2 = log10(n^3)
    push!(times_O1, O1)
    push!(times_O2, O2)
end


N=1:100:10^4
plot(N, [times_O1 times_O2], label=[L"O(n^2)" L"O(n^3)"], xlabel = L"n", ylabel=L"log_{10} (time complexity)")
plot!(size=(450,300))
savefig("timecomplexity.png")
