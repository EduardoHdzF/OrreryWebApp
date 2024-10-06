import plotly.express as px 
from shinywidgets import render_widget

class Orrey :
    def __init__(self):
        self.x = 100
        self.df = px.data.iris()
        self.fig = px.scatter_3d(self.df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
    
    def get_Orrey(self):
        return self.fig
    