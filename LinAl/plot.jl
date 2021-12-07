using Plots

x = range(-5,5,length=10)
y1 = 3*ones(10) - x
y2 = 4*ones(10) + 2*x

plot(x, y1, framestyle = :origin,  legend = :none, xlabel = "x", ylabel ="y")
plot!(x, y2, annotations = [(-4, 7, "y=-x+3"),(-5, -5, "y=2x+4")])
plot!(size=(450,300))
savefig("plot.png")


#3 pattern
x = range(-5,5,length=10)
y1 = 3*ones(10) - x
y2 = 4*ones(10) + 2*x
y3 = 3*ones(10) - x
y4 = 5*ones(10) - x


p1 = plot(x, y1, framestyle = :origin,  legend = :none, xlabel = "x", ylabel ="y", ylims = (-5,10))
plot!(x,y2, title = "case1", annotations =[(-4, 7, "y=-x+3"),(-5, -5, "y=2x+4")])

p2 = plot(x, y1, framestyle = :origin,  legend = :none, xlabel = "x", ylims = (-5,10))
plot!(x, y3, lw = 3, title = "case2", annotations =[(-4, 8, "y=-x+3"),(-4, 6, "2y=-2x+6")])

p3 = plot(x, y1, framestyle = :origin,  legend = :none, xlabel = "x", ylims = (-5,10))
plot!(x, y4, title = "case3", annotations =[(-4, 7, "y=-x+3"),(-4, 10, "y=-x+5")])

plot(p1,p2,p3, layout = (1, 3))
plot!(size=(800,300))
savefig("plot.png")







#vector
x_vals = [0 0 0 ; 2 -3 -4]
y_vals = [0 0 0 ; 4 3 -3.5]

plot(x_vals, y_vals, arrow = true, color = :blue,
     legend = :none, xlims = (-5, 5), ylims = (-5, 5),
     annotations = [(2.2, 4.4, "[2, 4]"),
                    (-3.3, 3.3, "[-3, 3]"),
                    (-4.4, -3.85, "[-4, -3.5]")],
     xticks = -5:1:5, yticks = -5:1:5,
     framestyle = :origin)