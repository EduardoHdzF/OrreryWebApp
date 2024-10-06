import math
import numpy as np
import plotly.express as px #plotly import
import plotly.graph_objects as go
import math
from scipy.spatial.transform import Rotation as R



def orbits(distance, angle, eccentricity, wdth=2):
    center = [0,0,0]
    x_c=0
    y_c=0
    z_c= 0
    xcord = []
    ycord = []
    zcord = []
    for i in np.linspace(-np.pi, np.pi, 80):
        x=distance*math.cos(i)-eccentricity
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
        rotation = R.from_rotvec(angle_rad*axis)
        vector = rotation.apply(vector)
        x_inc.append(vector[0])
        y_inc.append(vector[1])
        z_inc.append(vector[2])

    vector = np.array([center[0], center[1], center[2]])
    axis = np.array([1,0,0])
    rotation = R.from_rotvec(angle_rad*axis)
    vector = rotation.apply(vector)
    center = vector
    
    
    return go.Scatter3d(x=x_inc, y=y_inc, z=z_inc, mode='lines', line=dict(width=wdth), marker=dict(color='white'))

def show_orbit(distance, angle, eccentricity, clr='white', wdth=2):
    trace = orbits(distance, angle, eccentricity, wdth)
    trace2= orbits(10,0,0.6)
    trace3=orbits(10,45,0.6)

    fig = go.Figure(data=[trace,trace2,trace3])
    return fig

        
