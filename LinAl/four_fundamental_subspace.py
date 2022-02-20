import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# column space
col1 = np.array([1,0,1]).T
col2 = np.array([0,1,0]).T
col3 = np.array([1,1,1]).T
A = np.array([col1,col2,col3])

# row space
row1 = np.array([1,0,1]).T
row2 = np.array([0,1,1]).T
row3 = np.array([1,0,1]).T
AT = np.array([row1,row2,row3])

# null space
null_basis = np.array([-1,-1,1]).T

# left bull space
leftnull_basis = np.array([-1,0,1]).T


origin = np.array([[0,0,0],[0,0,0],[0,0,0]])


def randam():
    ra = np.random.randn()
    return ra

N = 3000

POINTS_COL = [randam()*col1+randam()*col2+randam()*col3 for i in range(N)]
POINTS_COL = np.vstack(POINTS_COL)

POINTS_ROW =  [randam()*row1+randam()*row2+randam()*row3 for i in range(N)]
POINTS_ROW = np.vstack(POINTS_ROW)

POINTS_NULL = [randam()*null_basis for i in range(N)]
POINTS_NULL = np.vstack(POINTS_NULL)

POINTS_LNULL = [randam()*leftnull_basis for i in range(N)]
POINTS_LNULL = np.vstack(POINTS_LNULL)


# figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def init():
    #column space
    ax.scatter(POINTS_COL[:, 0], POINTS_COL[:, 1], POINTS_COL[:, 2], s=1, alpha=0.05, color='gray')
    ax.text(3,1,3,r'$C(A)$',color='gray')
    ax.quiver(*origin, A[:,0], A[:,1],A[:,2], color='black')
    ax.text(1.2,1.2,1.2,r'column vectors',color='black')

    # row space
    ax.scatter(POINTS_ROW[:, 0], POINTS_ROW[:, 1], POINTS_ROW[:, 2], s=1, alpha=0.05, color='cyan')
    ax.text(3,1,5,r'$C(A^T)$',color='cyan')
    ax.quiver(*origin, AT[:,0],AT[:,1],AT[:,2], color='blue')
    ax.text(1.2,0,1.2,r'row vectors',color='blue')

    # null space
    ax.quiver(0,0,0,-1,-1,1,color='red')
    ax.text(-1.2,-1.2,1.2, r'basis of $N(A)$',color='red')
    ax.plot(POINTS_NULL[:,0],POINTS_NULL[:,1],POINTS_NULL[:,2], color='orange')
    ax.text(4,4,-4, r'$N(A)$', color='orange')

    # left null space
    ax.quiver(0,0,0,-1,0,1,color='green')
    ax.text(-1.2,0,1.2,r'basis of $N(A^T)$',color='green')
    ax.plot(POINTS_LNULL[:,0],POINTS_LNULL[:,1],POINTS_LNULL[:,2], color='lime')
    ax.text(4,0,-4, r'$N(A^T)$', color='lime')

    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_zlim(-6,6)
    return fig,

def animate(angle):
    ax.view_init(elev=20, azim=10*angle)
    ax.set_title(f'Angle:{10*angle}°')
    ax.set_xlabel(r'$x_1$')
    ax.set_ylabel(r'$x_2$')
    ax.set_zlabel(r'$x_3$')
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=36, interval=300, blit=True)
ani.save('animation.gif')