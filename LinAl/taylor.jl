using TaylorSeries, Plots, LaTeXStrings

f(x) = exp(x)
X = -5:0.1:5 # -5 ≤ x ≤ 5 
Y = [f(x) for x in X]

ani = Animation()
for i in 1:10
    c = 2
    t = Taylor1(i) # Independent variable with order i
    p = exp(t+c) # Taylor series of `exp` around c
    ty = [p(x-c) for x in -5:0.1:5]
    plot(X, Y, fillrange = ty, fillalpha = 0.35, label = "error", legend = :topleft, xlabel=L"x", ylabel=L"y", ylim = (-10,150))
    plot!(X,[Y ty], label = [L"f(x)" L"P(x)"], linewidth = 4, linecolor = [:blue :orange], annotations = (0, 50, "order is $i"))
    scatter!([c], [exp(c)], color = "red", label = "", markersize = 8)
    frame(ani)
end

gif(ani,"TaylorSeries_exp.gif",fps=1)




using TaylorSeries, Plots, LaTeXStrings
f(x) = cos(x)
X = -5:0.1:5 # -5 ≤ x ≤ 5 
Y = [f(x) for x in X]

ani = Animation()
for i in 1:16
    c = 0
    t = Taylor1(i) # Independent variable with order i
    p = cos(t+c) # Taylor series of `cos` around c
    ty = [p(x-c) for x in -5:0.1:5]
    plot(X, Y, fillrange = ty, fillalpha = 0.35, label = "error", legend = :topleft, xlabel=L"x", ylabel=L"y", ylim = (-1.5,1.5))
    plot!(X,[Y ty], label = [L"f(x)" L"P(x)"], linewidth = 4, linecolor = [:blue :orange], annotations = (0, 0, "order is $i"))
    scatter!([c], [cos(c)], color = "red", label = "", markersize = 8)
    frame(ani)
end

gif(ani,"TaylorSeries_cos.gif",fps=1.5)






t = Taylor1(5)
p = exp(t)

intp = integrate(p)
intp(3)-intp(2)
