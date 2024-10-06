from shiny.types import ImgData
from shiny import App, ui, reactive, render


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
        height: 500px; /* Altura fija del hero */
        width: 100%;
        color: white;
        display: flex;
        align-items: center;  /* Centrar verticalmente */
        justify-content: center; /* Centrar horizontalmente */
        overflow: hidden;
    }

    /* Background image */
    .header img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover; /* Asegurar que la imagen cubra todo */
        background: linear-gradient(black, grey);
        z-index: -1; /* La imagen queda detrás del texto */
    }

    /* Title Styles */
    .header-title {
        font-size: 5rem;
        letter-spacing: 1rem; /* Espacio entre letras */
        font-weight: bold;
        text-transform: uppercase;
        z-index: 1; /* Colocar el título sobre la imagen */
    }

    /* mejor poner header, body y footer como centered
    .centered {
        text-align: center;
    }
    */

    .button-container {
        display: flex; /* Flexbox to align buttons */
        justify-content: center; 
        padding: 100px 0; 
        overflow-x: auto;
    }


    .circular-button {
        border-radius: 50%; /* Para hacer un círculo */
        border: 0;
        height: 100px;
        width: 100px; /* Mantén el mismo ancho y alto */
        margin: 5px; /* Espacio entre botones */
        transition: transform 1s ease; /* Transición suave tanto al entrar como al salir del hover */
        padding: 0; /* Eliminar el padding para que la imagen ocupe todo el botón */
        display: flex;
        align-items: center;
        justify-content: center; /* Centrar el contenido */
        overflow: hidden; /* Asegurarse de que la imagen no se salga del círculo */
        text-decoration: none;
        position: relative; /* Agregar posición relativa para que z-index funcione */
        z-index: 1; /* El valor inicial del z-index */
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
        ui.h1("OVERRY", class_="header-title"),  # Title
        class_="header"
    ),

    # Body
    ui.div(
        ui.h3("Welcome to our page"),
        ui.p("This is the body."),     
        ui.p("This is still the body."), 
        class_="centered"
    ),
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

# Server logic to handle button clicks and display modal
def server(input, output, session):

    # Define reactive modals for each button
    def show_modal(content, title):
        modal = ui.modal(
            ui.div(
                ui.h3(title),
                ui.p(content),
            ),
            title=title,
            easy_close=True,  # Enables clicking outside to close the modal
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

# Run app
app = App(app_ui, server=server)
