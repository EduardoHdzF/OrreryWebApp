from shiny import App, ui, reactive

# CSS Styles
css_styles = """
<style>
    .centered {
        text-align: center;
    }
    .button-container {
        display: flex; /* Flexbox to align buttons */
        justify-content: center; 
        padding: 100px 0; 
        overflow-x: auto; 
    }
    .footer {
        padding: 20px;
    }
    .circular-button {
        border-radius: 50%; /* Para hacer un círculo */
        width: 50px;
        height: 50px;
        margin: 5px; /* Espacio entre botones */
        transition: transform 1s ease; /* Transición suave tanto al entrar como al salir del hover */
    }

    .circular-button:hover {
        transform: scale(3); /* Escalado suave */
        transition: transform 1s ease; /* Mantiene la suavidad al hacer hover */
    }
</style>
"""

# App Layout
app_ui = ui.page_fluid(
    ui.HTML(css_styles),
    ui.div(
        ui.panel_title("ORRERY"),  
        class_="centered"
    ),
    # Body
    ui.div(
        ui.h3("Welcome to our page"),
        ui.p("This is the body."),     
        ui.p("This is still the body."), 
        class_="centered"
    ),
    ui.hr(),
    # Footer with buttons
    ui.div(
        ui.h5("Planets", class_="centered"),
        ui.div(
            ui.row(
                ui.input_action_button("button_1", "1", class_="circular-button"),
                ui.input_action_button("button_2", "2", class_="circular-button"),
                ui.input_action_button("button_3", "3", class_="circular-button"),
                ui.input_action_button("button_4", "4", class_="circular-button"),
                ui.input_action_button("button_5", "5", class_="circular-button"),
                ui.input_action_button("button_6", "6", class_="circular-button"),
                ui.input_action_button("button_7", "7", class_="circular-button"),
                ui.input_action_button("button_8", "8", class_="circular-button"),
            ),
            class_="button-container"
        ),
        class_="footer"
    ),
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