import plotly.express as px 
from shinywidgets import render_widget
from orbit import show_orbit
from sphere import show_sphere

import plotly.graph_objects as go
import math
import numpy as np
from scipy.spatial.transform import Rotation as R

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
    Auxiliary function to orbi
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

class Orrey :
    """
    Class that generates an interactive 3d plot that simulates the main 9 planets 
    of the solar system plus their orbits using plotly.
    """

    def __init__(self):
        self.data=[]
        self.layout=[]
        self.create_Celestial_Bodies()
        self.create_Orbits()

    def create_Celestial_Bodies(self):
        """
        Adds to the plot the sun and the main nine plantes of the solar system 
        the information used can be found in the following link:https://nssdc.gsfc.nasa.gov/planetary/factsheet/ 
        """
        # Diameter for the 
        # Note: The Sun diameter is not accurate because its size. We reduced it for better 
        # displayability  of the solar system 
        celestial_body_diameter = [200000, 4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]
        diameter = [((i / 12756) * 2) for i in celestial_body_diameter]

        # Name of celestial bodies 
        names = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
        # Distance from the sun in 10^6 km
        distance = [0, 57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867.0, 4515.0]

        # Angle, this isn´t accurate, it's only  to help align each planet with 
        # it's orbit in the 3d plot 
        angles=[0, -7.5, -6 , 0.0, -7, -20, -60, -40, -142]
    
        # Colors of Celestial Bodies
        colours = ['#ffff00', '#808080', '#ffdd44', '#00aaff', '#ff5533', '#ff9900', '#ffcc00', '#66ccff', '#274687']

        # Add the celestial bodies to the figure
        for i in range(0, 9):  
            self.data.append(show_sphere(diameter[i], colours[i], distance[i], names[i], angles[i]))
            
    def create_Orbits(self):
        """
        Adds to the plot all orbits of the main nine plantes of the solar system 
        the information can be found in the following link:https://nssdc.gsfc.nasa.gov/planetary/factsheet/ 
        """
        #Name of each orbit 
        #Distance from the sun in 10^6 km
        distance=[57.9,108.2,149.6,228.0,778.5,1432.0,2867.0,4515.0]
        #Angle is given in degrees 
        angle=[7.0,3.4,0.0,1.8,1.3,2.5,0.8,1.8]
        #eccentricity 
        e=[0.206,0.007,0.017,0.094,0.049,0.052,0.047,0.010]
        
        for i in range(0,8):#0,8
            self.data.append(show_orbit(distance[i],angle[i],e[i]))
            

    
    def get_Orrey(self):
        """
        Funtion that creates the 3d plot and scene of the orrery

        Parameters
        ------------
        self: self reference to the same self data object 

        Returns
        ------------
        A plotly graph object scattered representing 3D solar system.
        """
        layout=go.Layout(title = 'Solar system Orrey', showlegend=False, margin=dict(l=0, r=0, t=0, b=0), 
                  scene = dict(xaxis=dict( 
                                          range=[-10000,10000], 
                                          showgrid=False,
                                          showline=False,
                                          zeroline=False,
                                          visible=False),
                               yaxis=dict(
                                          range=[-10000,10000],
                                          showgrid=False,
                                          showline=False,
                                          zeroline=False,
                                          visible=False
                                          ),
                               zaxis=dict( 
                                          range=[-10000,10000],
                                          showgrid=False,
                                          zeroline=False,
                                          visible=False,
                                         )), 
                                         scene_camera_eye=dict(x=0.1, y=0.5, z=0.3),
                                         )
        fig= go.Figure(data=self.data, layout=layout)
        return fig
    