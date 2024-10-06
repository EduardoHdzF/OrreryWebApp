from shiny.types import ImgData
from shiny import App, ui, reactive, render

from shiny import App, ui, render
import pandas as pd

data = {
    "Name":                         ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    "Diameter (km)":                [4879,      12.104,  12.756,   6792,   142.984,   120.536,  51.118,    49.528],
    "Mass (10^{24}kg)":             [0.330,      4.87,    5.97,   0.642, 	1898,	   568,    	86.8,	    102],
    "Distance from Sun (10^6 km)":  [57.9,      108.2,   149.6,  228.0,	    778.5, 	 1432.0,	2867.0,    4515.0]
}

df = pd.DataFrame(data)

app_ui = ui.page_fluid(
    ui.h2("Planets"),
    ui.output_table("planet_table")
)


# CSS Styles
css_styles = """
<style>

    body {
        font-family: 'Montserrat', sans-serif;
        color: var(blue);
        text-align: center;
        font-size: 14px;
    }

    /* Hero Section Styles */
    .header {
        position: relative;
        height: 500px;
        width: 100%;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center; 
        overflow: hidden;
    }

    /* Background image */
    .header img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        background: linear-gradient(black, grey);
        z-index: -1; 
    }

    .header-title {
        font-size: 5rem;
        letter-spacing: 1rem;
        font-weight: bold;
        text-transform: uppercase;
        z-index: 1;
    }


    .centered {
        text-align: center;
    }
    */

    /* Estilos para la tabla */
    .table-container {
        justify-content: center;
        margin: 20px auto; /* Centrar la tabla y agregar margen */
        width: 80%; /* Ajustar el ancho de la tabla */
    }

    .button-container {
        display: flex; /* Flexbox to align buttons */
        justify-content: center; 
        padding: 100px 0; 
        overflow-x: auto;
    }


    .circular-button {
        border-radius: 50%; 
        border: 0;
        height: 100px;
        width: 100px;
        margin: 5px; 
        transition: transform 1s ease;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        text-decoration: none;
        position: relative;
        z-index: 1;
    }

    .circular-button img {
        position: relative;
        width: 200%; /* Cambiar este valor para hacer la imagen más pequeña */
        height: 100%; /* Ajustar la altura proporcionalmente */
        right: 45px;
        object-fit: contain; /* Mantener el aspecto de la imagen */
    }

    .circular-button:hover {
        transform: scale(2); /* Escalado suave */
        transition: transform 1s ease; /* Mantiene la suavidad al hacer hover */
        z-index: 999; /* Elevar el z-index cuando se hace hover para que esté encima de todo */
    }


    .footer {
        padding: 2rem 0;
        background-color: #303130;
        font-size: 0.9rem;
        color: #f7f7f7
    }




</style>



"""

# App Layout
app_ui = ui.page_fluid(
    # Header - Hero
    ui.HTML(css_styles),
    ui.div(
        ui.panel_title("", "ORRERY - EsnupiCoders"), 
        ui.output_image("orrery"), 
        ui.h1("OVERRY", class_="header-title"),
        class_="header"
    ),

    # Body
    ui.div(
        ui.h3("Welcome to our page"),
        ui.p("This is the body."),     
        ui.p("This is still the body."), 
        class_="centered"
    ),
    
    ui.h2("Planets"),
    ui.output_table("planet_table"),

    ui.hr(),
    
    # Planets buttons
    ui.div(
        ui.h5("Planets", class_="centered"),
        ui.div(
            ui.row(
                ui.input_action_button("button_1", 
                    ui.output_image("planet1"), 
                    class_="circular-button"),
                ui.input_action_button("button_2", 
                    ui.output_image("planet2"), 
                    class_="circular-button"),
                ui.input_action_button("button_3", 
                    ui.output_image("planet3"), 
                    class_="circular-button"),
                ui.input_action_button("button_4", 
                    ui.output_image("planet4"), 
                    class_="circular-button"),
                ui.input_action_button("button_5", 
                    ui.output_image("planet5"), 
                    class_="circular-button"),
                ui.input_action_button("button_6", 
                    ui.output_image("planet6"), 
                    class_="circular-button"),
                ui.input_action_button("button_7", 
                    ui.output_image("planet7"), 
                    class_="circular-button"),
                ui.input_action_button("button_8", 
                    ui.output_image("planet8"), 
                    class_="circular-button"),
            ),
            class_="button-container"
        ),
        class_="planet-button"
    ),

    #Footer
    ui.div(
        ui.tags.small("Developed and designed by EsnupiCoders y sus secuaces. ©2024. All rights reserved."),
        class_="footer"  
    )
)

def server(input, output, session):

    @output
    @render.table
    def planet_table():
        return df

    def show_modal(content, title):
        modal = ui.modal(
            ui.div(
                ui.h3(title),
                ui.p(content),
            ),
            title=title,
            easy_close=True,
            fade=True
        )
        ui.modal_show(modal)

    @render.image
    def orrery():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/orrery.jpg"), "width": "100px"}
        return img
    

    @render.image
    def planet1():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet1.png"), "width": "180px"}
        return img
    
    @render.image
    def planet2():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet2.png"), "width": "100px"}
        return img
    
    @render.image
    def planet3():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet3.jpg"), "width": "100px"} # planet3.jpg está bien
        return img
    
    @render.image
    def planet4():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet4.png"), "width": "100px"}
        return img
    
    @render.image
    def planet5():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet5.png"), "width": "100px"}
        return img
    
    @render.image
    def planet6():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet6.jpg"), "width": "100px"}
        return img
    
    @render.image
    def planet7():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet7.png"), "width": "100px"}
        return img
    
    @render.image
    def planet8():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet8.png"), "width": "100px"}
        return img

    
    # Set up button click reactions
    @reactive.Effect
    @reactive.event(input.button_1)
    def _():
        show_modal("This is the content for Modal 1.", "Modal 1")

    @reactive.Effect
    @reactive.event(input.button_2)
    def _():
        show_modal("This is the content for Modal 2.", "Modal 2")

    @reactive.Effect
    @reactive.event(input.button_3)
    def _():
        show_modal("This is the content for Modal 3.", "Modal 3")

    @reactive.Effect
    @reactive.event(input.button_4)
    def _():
        show_modal("This is the content for Modal 4.", "Modal 4")

    @reactive.Effect
    @reactive.event(input.button_5)
    def _():
        show_modal("This is the content for Modal 5.", "Modal 5")

    @reactive.Effect
    @reactive.event(input.button_6)
    def _():
        show_modal("This is the content for Modal 6.", "Modal 6")

    @reactive.Effect
    @reactive.event(input.button_7)
    def _():
        show_modal("This is the content for Modal 7.", "Modal 7")

    @reactive.Effect
    @reactive.event(input.button_8)
    def _():
        show_modal("This is the content for Modal 8.", "Modal 8")

app = App(app_ui, server=server)
