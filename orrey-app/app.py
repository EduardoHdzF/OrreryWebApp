from shiny import render, ui #Shiny html implementaion
from shiny.express import input #Shiny interactive implementation
from shinywidgets import render_widget #Makes shiny compatible with widgets
import plotly.express as px #plotly import
import virtualOrrery.sphere as sp
import virtualOrrery.orbit as op

##own imports
from virtualOrrery.orrey import Orrey



### Equipo fronten no toques aqui ###

#Renders the virtual orrey
@render_widget
def orrey():
    orrey =  Orrey() #Creates object orrey
    # return orrey.get_Orrey()
    return op.show_orbit(10,180,0.6)

"""
oh hola no me prestes atención

diameter = [((i / 12756)*2) for i in celestial_body_diameter ]
celestial_body_diameter = [20000,4879,12104, 12756, 6792,142984, 120536, 51,118,49528,]

sun = draw_sphere(diameter[0],yellow, 0)

fig = go.Figure(data = [sun])

celestial_body_diameter = [200000, 4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]
diameter = [((i / 12756) * 2) for i in celestial_body_diameter]

sun = draw_sphere(diameter[0], 'yellow', 0, name='Sun', angle=0)
mercury = draw_sphere(diameter[1]* 1.1, "grey", 57.9, name='Mercury',angle=0)

fig = go.Figure(data=[sun, mercury])
fig.update_layout(scene=dict(aspectmode='data'))  # Ajusta la relación de aspecto
fig.show()

"""

###Equipo frontend puedes tocar desde aqui para abajo ###




