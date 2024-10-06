import math
import numpy as np
import plotly.graph_objects as go
from scipy.spatial.transform import Rotation as R



def orbits(distance, angle, eccentricity):
    """
    Function to crate a 2d elliptical orbit living in a 3d space.
    Created by following Daniel A. O’Neil Elliptical Orbit Simulator
    tutorial. 
    source: https://nasa.github.io/mission-viz/RMarkdown/Elliptical_Orbit_Design.html
    ----------------------------------------------------------
    Parameters
    ----------
    distance: Distance from the sun to x
    angle: Orbital incliantion in degrees
    eccentricity: Orbital eccentricity

    Returns
    -------
    A plotly graph object scattered representing an elliptical orbit.

    """
    xcord = []
    ycord = []
    zcord = []
    for i in np.linspace(-np.pi, np.pi, 80): # creates points of 2d ellipse
        x = distance*math.cos(i)-eccentricity
        y = distance*math.sin(i)*math.sqrt(1-eccentricity**2)
        z = 0
        xcord.append(x)
        ycord.append(y)
        zcord.append(z)
    
    
    angle_rad = math.radians(angle)
    x_inc = []
    y_inc = []
    z_inc = []

    for i in range(0,80): 
        vector = np.array([xcord[i], ycord[i], zcord[i]])
        axis = np.array([0,1,0])
        rotation = R.from_rotvec(angle_rad*axis)#Using an rotation matrix
        vector = rotation.apply(vector) #We rotate the ellipse into the 3d realm 
        x_inc.append(vector[0])
        y_inc.append(vector[1])
        z_inc.append(vector[2])
    
    
    return go.Scatter3d(x=x_inc, y=y_inc, z=z_inc, mode='lines', line=dict(width=2), marker=dict(color='black'))

def show_orbit(distance, angle, eccentricity):
    """
    Auxiliary function to orbit.

    Parameters
    ----------
    distance: Distance from the sun to x
    angle: Orbital incliantion in degrees
    eccentricity: Orbital eccentricity

    Returns
    -------
    A plotly graph object scattered representing an elliptical orbit.
    """
    trace = orbits(distance, angle, eccentricity)
    return trace
