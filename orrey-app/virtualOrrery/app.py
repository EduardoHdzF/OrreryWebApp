from shiny import render, ui #
from shiny.express import input #Shiny interactive implementation
from shinywidgets import render_widget #Makes shiny compatible with widgets
import plotly.express as px #plotly import

##own imports
from virtualOrrery.orrey import Orrey



### Equipo fronten no toques aqui ###

#Renders the virtual orrey
@render_widget
def orrey():
    orrey =  Orrey() #Creates object orrey
    # sp.show_spheres()
    return orrey.get_Orrey()

###Equipo frontend puedes tocar desde aqui para abajo ###




