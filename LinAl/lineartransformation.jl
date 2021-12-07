using Plots


quiver([0], [0], quiver=[1 ,6], xlims=(0,5), ylims=(0,5))


x=0
y=0
u=1
v=i    
df = 10


anim = @animate for i = 1:0.1:10
    quiver([x], [y], quiver=[u i])
end
 
gif(anim, "tutorial_anim_fps30.gif", fps = 1)
