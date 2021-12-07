using LinearAlgebra, BenchmarkTools, Random, Plots

Random.seed!(42);
times = []

for n in 1:10:2500
    A = rand(n,n)
    b = rand(n)
    time = @elapsed A\b
    push!(times, time)
end

X = Array(1:10:2500)
plot(X, times, label = "inv_matrix")
xlabel!("n")
ylabel!("time (s)")
