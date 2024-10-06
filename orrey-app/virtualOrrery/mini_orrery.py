import plotly.express as px 
from shinywidgets import render_widget
from virtualOrrery.orbit import show_orbit as so
from virtualOrrery.sphere import show_sphere as ss
import plotly.graph_objects as go

class MiniOrrery :

    def __init__(self):
        self.data=[]
        self.layout=[]
        self.create_Celestial_Bodies()
        self.create_Orbits()
        

    """
        Adds to the plot the sun and the main nine plantes of the solar system 
        the information can be found in the following link:https://nssdc.gsfc.nasa.gov/planetary/factsheet/ 
    """
    def create_Celestial_Bodies(self):
        # Diameter for the celestial bodies, it's used for placing the spheres
        # Note: The Sun diameter is not accurate because the size of it. We reduced de sizamfor better 
        # display of the solar system 
        celestial_body_diameter = [200000, 4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]
        diameter = [((i / 12756) * 2) for i in celestial_body_diameter]

        # Name of celestial bodies 
        names = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        #names = ['Sun', 'Mercury']
    
        # Distance from the sun in 10^6 km
        distance = [0, 57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867.0, 4515.0]

        # Angle, this is not accurate, it's just to place in the orbit for the 3d model
        angles=[0, -7.5, -6 , 0.0, -7, -20, -60, -40, -142]
    
        # Colors of Celestial Bodies
        colours = ['#ffff00', '#808080', '#ffdd44', '#00aaff', '#ff5533', '#ff9900', '#ffcc00', '#66ccff', '#274687']
        #colours = ['#ffff00', '#808080']

        # Add the celestial bodies to the figure
        for i in range(0, 4):  # Iterate over all celestial bodies
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
        
        for i in range(0,3):#0,8
            self.data.append(so(distance[i],angle[i],e[i]))
        self
            

    
    def get_MiniOrrery(self):

        layout=go.Layout(title = 'Solar system Orrey', showlegend=False, margin=dict(l=0, r=0, t=0, b=0), 
                         
                  #paper_bgcolor = 'black',
                  scene = dict(xaxis=dict(title='Distance from the Sun', 
                                          range=[-5000,5000], 
                                          showgrid=False,
                                          showline=False,
                                          zeroline=False,
                                          visible=False),
                               yaxis=dict(title='Distance from the Sun',
                                          range=[-5000,5000],
                                          showgrid=False,
                                          showline=False,
                                          zeroline=False,
                                          visible=False
                                          ),
                               zaxis=dict(title='', 
                                          range=[-5000,5000],
                                          showgrid=False,
                                          zeroline=False,
                                          visible=False,
                                         )), 
                                         scene_camera_eye=dict(x=0.1, y=0.5, z=0.3),
                                         )
        fig= go.Figure(data=self.data, layout=layout)
        return fig
    

