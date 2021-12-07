using LinearAlgebra, Plots, LaTeXStrings

n = 3 # vector length
N = 10^5 # run times
results = [] #list

for _ in 1:N
    a = rand(n)
    b = rand(n)
    result = norm(a)*norm(b)-abs(a'*b)
    push!(results, result) #append result into list
end

minimum(results)
histogram(results, legend=false, xlabel = L"\Vert a\Vert \Vert b \Vert -|a^Tb|", ylabel="count")
histogram!(size=(450,300))
savefig("cs.png")
