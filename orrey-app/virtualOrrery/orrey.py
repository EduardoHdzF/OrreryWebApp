import plotly.express as px 
from shinywidgets import render_widget
from orbit import show_orbit as so
from sphere import show_sphere as ss
import plotly.graph_objects as go

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
            self.data.append(ss(diameter[i], colours[i], distance[i], names[i], angles[i]))
            
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
            self.data.append(so(distance[i],angle[i],e[i]))
            

    
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
    