import numpy as np
import math
import plotly.graph_objects as go


def draw_sphere(size, clr, dist=0, name=" ", angle=0): 
    """
    Function to draw a sphere for the 3D layout using plotly.
    It's used for the 3D representation of the solar system celestial bodies.
    For the parameters like diameter or the distance from the Sun we used the 
    information in the next source:
    source: https://nasa.github.io/mission-viz/RMarkdown/Elliptical_Orbit_Design.html
    ----------------------------------------------------------
    Parameters
    ----------
    size: size of the celestial body based on the diameter.
    clr: the celestial body color.
    dist: distance in km of a planet from the sun.
    name: name of the celestial body
    angle: the position in the z axis for the display

    Returns
    -------
    A plotly graph object scattered representing an celestial body.
    """
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
    """
    Auxiliar function for draw_shpere, its used to return a figure of a sphere
    ----------------------------------------------------------
    Parameters
    ----------
    size: size of the celestial body based on the diameter.
    clr: the celestial body color.
    dist: distance in km of a planet from the sun.
    name: name of the celestial body
    angle: the position in the z axis for the display

    Returns
    -------
    A plotly graph object scattered representing an celestial body.
    """
    return draw_sphere(size, clr, dist,name,angle) 