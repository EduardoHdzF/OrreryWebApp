import numpy as np
import math
import plotly.graph_objects as go

#Function for drawing in 3D a celest body
def draw_sphere(size, clr, dist=0, name='', angle=0): 

    theta = np.linspace(0,2*np.pi,100)
    phi = np.linspace(0,np.pi,100)
    
    x0 = dist + size * np.outer(np.cos(theta),np.sin(phi))
    y0 = size * np.outer(np.sin(theta),np.sin(phi))
    z0 = size * np.outer(np.ones(100),np.cos(phi)) + angle
    
    trace= go.Surface(x=x0, y=y0, z=z0, colorscale=[[0,clr], [1,clr]],hoverinfo='text',
        hovertext=f'{name}')
    trace.update(showscale=False)

    return trace

def show_sphere(size, clr, dist=0,name= '', angle = 0):
    trace = draw_sphere(size, clr, dist,name,angle)
    fig = go.Figure(data=[trace])
    return fig
    # fig.show()aaaaaaa

# Mostrar una esfera de ejemplo
show_sphere(size=1, clr='yellow', dist=0, name='Sun', angle = 5)

"""
Creación de planetas para después juntarlas 
traceSun = (0, 'yelow', 0)
traceMercury = ()
traceEarth = (calculate_diameter(2000))


def calculate_diameter(diameter 0):
    diameter = [((diameter / 12756) * 2) for i in diameter_km]

    # Note, true diameter of the Sun is 1,392,700km. Reduced it for better visualization
diameter_km = [200000, 4878, 12104, 12756, 6787, 142796, 120660, 51118, 48600]
diameter = [((i / 12756) * 2) for i in diameter_km]
distance_from_sun = [0, 57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]


trace0 = draw_sphere(diameter[0], '#ffff00', distance_from_sun[0], name='Sun')  # Sun
trace1 = draw_sphere(diameter[1], '#87877d', distance_from_sun[1], name='Mercury')  # Mercury


fig = go.Figure(data=[trace0, trace1])

# Show the figure
fig.show()
"""