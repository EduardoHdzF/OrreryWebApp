from shiny.types import ImgData
from shiny import App, ui, reactive, render

url_na = 'https://cneos.jpl.nasa.gov/ca/'
url_planets = 'https://science.nasa.gov/solar-system/planet-sizes-and-locations-in-our-solar-system/'
url_dwarf = 'https://science.nasa.gov/dwarf-planets/'
url_neo = 'https://cneos.jpl.nasa.gov/about/neo_groups.html'
url_phaT = 'https://eyes.nasa.gov/apps/asteroids/#/story/asteroids_close_approach'
url_phaS = 'https://eyes.nasa.gov/apps/asteroids/#/watch/2024_sd6'

url_ess = 'https://eyes.nasa.gov/apps/solar-system/#/home'
url_ea = 'https://eyes.nasa.gov/apps/asteroids/#/home'
url_et = 'https://eyes.nasa.gov/apps/earth/#/'
url_ee = 'https://eyes.nasa.gov/apps/exo/'
url_dnsn = 'https://eyes.nasa.gov/dsn/dsn.html'
url_mrn = 'https://eyes.nasa.gov/apps/mrn'
url_medl = 'https://eyes.nasa.gov/apps/mars2020'

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
        font-size: 12rem;
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
        padding: 165px 0; 
        overflow-x: auto;
        position: relative; /* Agregar posición relativa para que z-index funcione */
        z-index: 1; /* El valor inicial del z-index */
    }


    .circular-button {
        border-radius: 50%; /* Para hacer un círculo */
        border: 0;
        height: 170px;
        width: 170px; /* Mantén el mismo ancho y alto */
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
        transform: scale(3); /* Escalado suave */
        transition: transform 1s ease; /* Mantiene la suavidad al hacer hover */
        z-index: 999; /* Elevar el z-index cuando se hace hover para que esté encima de todo */
    }

    /*Planets */
    .intro-planets {
        font-size: 1.5rem;
        font-family: "Lucida Console", "Courier New", monospace;
    }

    .intros {
        font-size: 1.5rem;
        font-family: "Lucida Console", "Courier New", monospace;
    }


    h2 {
        font-size: 8rem;
        font-family: "Lucida Console", "Courier New", monospace;
        letter-spacing: 1rem; /* Espacio entre letras */
        font-weight: bold;
        text-transform: uppercase;
    }

    a {
        color: #1D6161;
        text-decoration: none; 
        font-weight: bold; 
        font-size: 1.5rem;
        font-family: "Lucida Console", "Courier New", monospace; 
        letter-spacing: 0.1rem;
        cursor: pointer;
    }

    a:hover {
        text-shadow: 2px 2px 17px rgba(0, 0, 0, 57); 
        font-family: "Lucida Console", "Courier New", monospace;
    }

    .nasa a {
        color: #1D6161;
        text-decoration: none; 
        font-weight: bold; 
        font-size: 2.5rem; 
        font-family: "Lucida Console", "Courier New", monospace;
        letter-spacing: 0.1rem;
        cursor: pointer; 
    }

    .nasa a:hover {
        text-shadow: 2px 2px 17px rgba(0, 0, 0, 57); 
        font-family: "Lucida Console", "Courier New", monospace;
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
    ui.input_dark_mode(),
    ui.div(
        ui.panel_title("", "ORRERY - EsnupiCoders"), 
        ui.output_image("orrery"), 
        ui.h1("ORRERY", class_="header-title"),  # Title
        class_="header"
    ),

    # Graph
    ui.div(
        ui.h3("Welcome to our page"),
        ui.p("Description of the graph."),     
        ui.p("Here goes the graph :D."), 
        class_="centered"
    ),

    #Planets seccion
    ui.div(
        ui.HTML(
            "<br>".join(sentence.strip() for sentence in (
                "The cosmic ballet of planets orbiting the Sun is a captivating spectacle, and it's just the beginning.- "
                "The intricate interplay of gravitational forces, the composition of planetary atmospheres, and the potential for extraterrestrial life "
                "are just a few of the fascinating questions that continue to captivate scientists and stargazers alike.-"
                "While the eight planets and five dwarf planets offer a glimpse into its grandeur, there's so much more to discover.-"
                "From the fiery depths of the Sun to the icy fringes of the outer planets, each celestial body holds unique mysteries waiting to be unveiled.-"
                ""
                "This a simple guide with interestig data about them, we hope you like it, ¡Enjoy!-"
                "...-"
                "¡Let's get into it!"
            ).split('-'))
        ),
        class_="intro-planets"        
    ),
    ui.hr(),

    # Planets buttons
    ui.div(
        ui.h2("Planets", class_="centered"),
        ui.h3("The International Astronomical Union (IAU), a world organization of astronomers, came up with the definition of a planet in 2006. According to the IAU, a planet must do three things:"
                "Orbit its host star (In our solar system that is the Sun)."
                "Be mostly round."
                "Be big enough that its gravity cleared away any other objects of similar size near its orbit around the Sun.", class_="intros"),
        ui.tags.a("",
              href=url_planets,
              target='_blank'),
        ui.HTML(f'<a href="{url_planets}" target="_blank">Obtained from and Learn more about Planets of our Solar System</a>'),
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

    # Dwarf Planets buttons
    ui.div(
        ui.h2("Dwarf Planets", class_="centered"),
        ui.h3("According to the IAU, a dwarf planet defined as objects that orbit the Sun, and are nearly round, but have not been able to clear their orbit of debris."
                "So far, the IAU has only recognized five dwarf planets. In order of distance from the Sun they are: Ceres, Pluto, Haumea, Makemake, and Eris."
                "But the IAU says there may be many more dwarf planets, perhaps more than a hundred, waiting to be discovered.", class_="intros"),
        ui.tags.a("",
              href=url_dwarf,
              target='_blank'),
        ui.HTML(f'<a href="{url_dwarf}" target="_blank">Obtained from and Learn more about Dwarf Planets</a>'),
        ui.div(
            ui.row(
                ui.input_action_button("dwarf_button_1", 
                    ui.output_image("dwarf1"), 
                    class_="circular-button"),
                ui.input_action_button("dwarf_button_2", 
                    ui.output_image("dwarf2"), 
                    class_="circular-button"),
                ui.input_action_button("dwarf_button_3", 
                    ui.output_image("dwarf3"), 
                    class_="circular-button"),
                ui.input_action_button("dwarf_button_4", 
                    ui.output_image("dwarf4"), 
                    class_="circular-button"),
                ui.input_action_button("dwarf_button_5", 
                    ui.output_image("dwarf5"), 
                    class_="circular-button"),
            ),
            class_="button-container"
        ),
        class_="dwarf-button"
    ),

    # Near-Earth Asteroids buttons
    ui.div(
        ui.h2("Near-Earth Asteroids", class_="centered"),
        ui.h3("In terms of orbital elements, NEOs are asteroids and comets with perihelion distance q less than 1.3 au .  The vast majority of NEOs are asteroids, referred to as Near-Earth Asteroids (NEAs). "
              "NEAs are divided into groups (Atira, Aten, Apollo and Amor) according to their perihelion distance (q), aphelion distance (Q) and their semi-major axes (a)."
              "Below we show the 5 closest, but you can find a complete list in the following link.", class_="intros"),
        ui.tags.a("",
              href=url_neo,
              target='_blank'),
        ui.HTML(f'<a href="{url_neo}" target="_blank">Obtained from and Learn more about Near-Earth Objects and Asteroids</a>'),
        ui.p("\n"),
        ui.tags.a("",
              href=url_na,
              target='_blank'),
        ui.HTML(f'<a href="{url_na}" target="_blank">Obtained from and List of Near-Earth Asteroids</a>'),
        ui.div(
            ui.row(
                ui.input_action_button("asteroid_button_1", 
                    ui.output_image("asteroid1"), 
                    class_="circular-button"),
                ui.input_action_button("asteroid_button_2", 
                    ui.output_image("asteroid2"), 
                    class_="circular-button"),
                ui.input_action_button("asteroid_button_3", 
                    ui.output_image("asteroid3"), 
                    class_="circular-button"),
                ui.input_action_button("asteroid_button_4", 
                    ui.output_image("asteroid4"), 
                    class_="circular-button"),
                ui.input_action_button("asteroid_button_5", 
                    ui.output_image("asteroid5"), 
                    class_="circular-button"),
            ),
            class_="button-container"
        ),
        class_="asteroid-button"
    ),

    # Near-Earth Comets buttons
    ui.div(
        ui.h2("Near-Earth Comets", class_="centered"),
        ui.h3("In terms of orbital elements, NEOs are asteroids and comets with perihelion distance q less than 1.3 au . "
              "Near-Earth Comets (NECs) are further restricted to include only short-period comets (i.e., orbital period P less than 200 years)."
              "Below we show the 5 closest, before 1900 but you can find a complete list in the following link.", class_="intros"),
        ui.tags.a("",
              href=url_neo,
              target='_blank'),
        ui.HTML(f'<a href="{url_neo}" target="_blank">Obtained from and Learn more about Near-Earth Objects and Comets</a>'),
        ui.p("\n"),
        ui.tags.a("",
              href=url_na,
              target='_blank'),
        ui.HTML(f'<a href="{url_na}" target="_blank">Obtained from and List of Near-Earth Comets before 1900</a>'),
        ui.div(
            ui.row(
                ui.input_action_button("comet_button_1", 
                    ui.output_image("comet1"), 
                    class_="circular-button"),
                ui.input_action_button("comet_button_2", 
                    ui.output_image("comet2"), 
                    class_="circular-button"),
                ui.input_action_button("comet_button_3", 
                    ui.output_image("comet3"), 
                    class_="circular-button"),
                ui.input_action_button("comet_button_4", 
                    ui.output_image("comet4"), 
                    class_="circular-button"),
                ui.input_action_button("comet_button_5", 
                    ui.output_image("comet5"), 
                    class_="circular-button"),
            ),
            class_="button-container"
        ),
        class_="comets-button"
    ),

    # Potentially Hazardous Asteroids buttons
    ui.div(
        ui.h2("Potentially Hazardous Asteroids", class_="centered"),
        ui.h3("A Potentially Hazardous Object (PHO) is a Near-Earth bject (NEO) that is at least 140 meters (460 feet) in size, and whose orbit approaches Earth's orbit to within 7,480,000 km."
              "Those are potentially hazardous only in a long-term sense: almost all are not currently on Earth-crossing orbits, but/their orbits are close enough that over hundreds or thousands of years"
              "they may evolve to become Earth-crossing"
              "There are 2,458 PHOs currently.", class_="intros"),
        ui.tags.a("",
              href=url_phaT,
              target='_blank'),
        ui.HTML(f'<a href="{url_phaT}" target="_blank">Obtained from and Learn more about Potentially Hazardous Asteroids</a>'),
        ui.p("\n"),
        ui.tags.a("",
              href=url_phaS,
              target='_blank'),
        ui.HTML(f'<a href="{url_phaS}" target="_blank">Meet some of the  most dangerous closely here</a>'),
        ui.div(
            ui.row(
                ui.input_action_button("hazardous_button_1", 
                    ui.output_image("hazardous1"), 
                    class_="circular-button"),
                ui.input_action_button("hazardous_button_2", 
                    ui.output_image("hazardous2"), 
                    class_="circular-button"),
                ui.input_action_button("hazardous_button_3", 
                    ui.output_image("hazardous3"), 
                    class_="circular-button"),
                ui.input_action_button("hazardous_button_4", 
                    ui.output_image("hazardous4"), 
                    class_="circular-button"),
                ui.input_action_button("hazardous_button_5", 
                    ui.output_image("hazardous5"), 
                    class_="circular-button"),
            ),
            class_="button-container"
        ),
        class_="hazardous-button"
    ),
    ui.hr(),

    #NASA colab in simulations
    ui.div(
        ui.h2("NASA", class_="centered"),
        ui.h3("You can have a better view of the objects we preseted here in the NASA."
              " 3D visualization applications that allows everyone to explore and understand real NASA data and imagery in a fun and interactive way.", class_="intros"),
        ui.tags.a(" ",
              href=url_ess,
              target='_blank'),
        ui.HTML(f'<a href="{url_ess}" target="_blank">Eyes on Solar System</a>'),
        ui.p("\n"),
        ui.tags.a(" ",
              href=url_ea,
              target='_blank'),
        ui.HTML(f'<a href="{url_ea}" target="_blank">Eyes on Asteroids</a>'),
        ui.p("\n"),
        ui.tags.a(" ",
              href=url_et,
              target='_blank'),
        ui.HTML(f'<a href="{url_et}" target="_blank">Eyes on the Earth</a>'),
        ui.p("\n"),
        ui.tags.a(" ",
              href=url_ee,
              target='_blank'),
        ui.HTML(f'<a href="{url_ee}" target="_blank">Eyes on Exoplanets</a>'),
        ui.p("\n"),
        ui.tags.a(" ",
              href=url_dnsn,
              target='_blank'),
        ui.HTML(f'<a href="{url_dnsn}" target="_blank">DSN Now</a>'),
        ui.p("\n"),
        ui.tags.a(" ",
              href=url_mrn,
              target='_blank'),
        ui.HTML(f'<a href="{url_mrn}" target="_blank">Mars Relay Now</a>'),
        ui.p("\n"),
        ui.tags.a(" ",
              href=url_medl,
              target='_blank'),
        ui.HTML(f'<a href="{url_medl}" target="_blank">Mars 2020 EDL</a>'),
        ui.p("\n"),
        class_="nasa"
    ),
    ui.hr(),


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

    # Hero Image
    @render.image
    def orrery():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/orrery.jpg"), "width": "100px"}
        return img
    
    # Planets Image button
    @render.image
    def planet1():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/planet1.png"), "width": "100px"}
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
        img: ImgData = {"src": str(dir / "www/planet3.png"), "width": "100px"}
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
        img: ImgData = {"src": str(dir / "www/planet6.png"), "width": "100px"}
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
    
    # Dwarf Planets Image
    @render.image
    def dwarf1():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/dwarf1.png"), "width": "180px"}
        return img
    
    @render.image
    def dwarf2():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/dwarf2.png"), "width": "100px"}
        return img
    
    @render.image
    def dwarf3():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/dwarf3.png"), "width": "100px"}
        return img
    
    @render.image
    def dwarf4():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/dwarf4.png"), "width": "100px"}
        return img
    
    @render.image
    def dwarf5():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/dwarf5.png"), "width": "100px"}
        return img
    
    # Near-Earth Asteroids Image
    @render.image
    def asteroid1():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/asteroid1.png"), "width": "180px"}
        return img
    
    @render.image
    def asteroid2():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/asteroid2.png"), "width": "100px"}
        return img
    
    @render.image
    def asteroid3():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/asteroid3.png"), "width": "100px"}
        return img
    
    @render.image
    def asteroid4():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/asteroid4.png"), "width": "100px"}
        return img
    
    @render.image
    def asteroid5():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/asteroid5.png"), "width": "100px"}
        return img
    

    # Near-Earth Comets Image
    @render.image
    def comet1():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/comet1.png"), "width": "180px"}
        return img
    
    @render.image
    def comet2():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/comet2.png"), "width": "100px"}
        return img
    
    @render.image
    def comet3():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/comet3.png"), "width": "100px"}
        return img
    
    @render.image
    def comet4():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/comet4.png"), "width": "100px"}
        return img
    
    @render.image
    def comet5():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/comet5.png"), "width": "100px"}
        return img
    
    # Potentially Hazardous Asteroids Image
    @render.image
    def hazardous1():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/hazardous1.png"), "width": "180px"}
        return img
    
    @render.image
    def hazardous2():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/hazardous2.png"), "width": "100px"}
        return img
    
    @render.image
    def hazardous3():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/hazardous3.png"), "width": "100px"}
        return img
    
    @render.image
    def hazardous4():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/hazardous4.png"), "width": "100px"}
        return img
    
    @render.image
    def hazardous5():
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/hazardous5.png"), "width": "100px"}
        return img
    

    
    # Set up button click reactions - PLANETS
    @reactive.Effect
    @reactive.event(input.button_1)
    def _():
        show_modal("The smallest planet in our solar system and the closest planet to the Sun, it "
                    "has an equatorial diameter of about 4,880 kilometers. Mercury has "
                    "an orbital period of 88 days and orbital velocity of 47.4km/s; it has a rotation "
                    "period of 1407.6 hours, resulting in a length of day of 4222.6 hours", "Mercury")


    @reactive.Effect
    @reactive.event(input.button_2)
    def _():
        show_modal("Venus is about the same width as Earth and the second closest planet to the Sun, it "
                   "has an equatorial diameter of about 12,104 kilometers. This planet has "
                   "an orbital period of 224.7 days and orbital velocity of 35 km/s. Venus rotates slowly "
                   "with a rotation period of -5832.5 hours, giving it a length of day of 2802.0 hours", "Venus")

    @reactive.Effect
    @reactive.event(input.button_3)
    def _():
        show_modal("Our planet Venus is the third closest planet to the Sun, it "
                   "has an equatorial diameter of about 12,756 kilometers. Earth has a rotation "
                   "period of 23.9 hours, corresponding to a length of day of 24.0 hours. This "
                   "consistent rotation supports life and creates the familiar cycle of day and night.", "Earth")

    @reactive.Effect
    @reactive.event(input.button_4)
    def _():
        show_modal("Mars is the fourth planet in our Solar System. Mars has a rotation period of 24.6 hours and a "
                   "length of day of 24.7 hours, making its days slightly longer than those on Earth. Its similar "
                   "rotation allows for comparable seasonal changes. This planet as an equatorial diameter of about "
                   "6,792 kilometers.", "Mars")

    @reactive.Effect
    @reactive.event(input.button_5)
    def _():
        show_modal("Jupiter, one of the most popular planets, is the largest and most massive planet in our "
                   " Solar System. It has an equatorial diameter of about 142,984 kilometers."
                   "Jupiter rotates rapidly, with a rotation period of 9.9 hours and a orbital period of"
                   " 4331 days.", "Jupiter")

    @reactive.Effect
    @reactive.event(input.button_6)
    def _():
        show_modal("The sixth planet in our Solar System and the second largest is Saturn. This planet is "
                   " well-known for its spectacular icy rings. It has rotation period of 10.7 hours and a "
                   "length of day of 10.7 hours. Some impressive fact about this planet is the number of moons."
                   " Saturn has 146 moons!", "Saturn")

    @reactive.Effect
    @reactive.event(input.button_7)
    def _():
        show_modal("Uranus is the third largest planet in our solar system with a 51,118km diameter "
                   "It has an equatorial diameter of about 51,118 kilometers. Uranus has "
                   "a unique rotation period of -17.2 hours and a length of day of 17.2 hours, "
                   "indicating retrograde rotation. ", "Uranus")

    @reactive.Effect
    @reactive.event(input.button_8)
    def _():
        show_modal("The most distant planet from the Sun is Neptune, however, is the fourth largest planet"
                   " with a diameter of 49,528 kilometers. This planet has a ring system and a global magnetic "
                   "field. It has 16 moons and a -200C mean temperature. Neptune's rotation period "
                   "is 16.1 hours, and its length of day is also 16.1 hours.", "Neptune")
        
    # Set up button click reactions - DWARF PLANETS
    @reactive.Effect
    @reactive.event(input.dwarf_button_1)
    def _():
        show_modal("It is the only dwarf planet located in the inner solar system and is the smallest"
                   " dwarf planet. It is impressive that this dwarf planet is about 2.8 times farther "
                   "from the Sun than Earth. Like Pluto, Ceres also was once classified as a planet.", "Ceres")

    @reactive.Effect
    @reactive.event(input.dwarf_button_2)
    def _():
        show_modal("It was long considered as a solar system planet. Pluto has a rotation period of"
                   "-153.3 hours, leading to a length of day of 153.3 hours. Now, Pluto is "
                   "the largest dwarf planet", "Pluto")

    @reactive.Effect
    @reactive.event(input.dwarf_button_3)
    def _():
        show_modal("Haumea is one of the fastest rotating objects, it is extremely cold and "
                   "has an equatorial diameter of about about 1,740 kilometers. It has two known moons and "
                   "this dwarf planet takes 285 Earth years to make one trip around the Sun. ", "Haumea")

    @reactive.Effect
    @reactive.event(input.dwarf_button_4)
    def _():
        show_modal("This dwarf planet is located in the Kuiper Belt; slightly smaller than Pluto, "
                   "this planet takes 305 Earth years to make one trip around the Sun."
                   "Surprisingly, scientists know very little about Makemake's structure.", "Makemake")

    @reactive.Effect
    @reactive.event(input.dwarf_button_5)
    def _():
        show_modal("Eris was discovered on Jan. 5, 2005 as the second largest dwarf planet. It "
                   "is about 68 times farther from the Sun than Earth and has an equatorial diameter "
                   "of about 2,400 kilometers. Although it may seem surprising, Eris has a very small "
                   "moon called Dysnomia.", "Eris")

    # Set up button click reactions - Near-Earth Asteroids
    @reactive.Effect
    @reactive.event(input.asteroid_button_1)
    def _():
        show_modal("The asteroid (2022 SU21) is set to make a close approach on October 6, 2024, "
                   " is has a nominal distance of 0.04488 AU and a relative velocity of 21.10 km/s; "
                   " also an infinity velocity of 21.10 km/s. The object has a diameter ranging between "
                   " 33 m and 74 m. ", "(2022 SU21)")

    @reactive.Effect
    @reactive.event(input.asteroid_button_2)
    def _():
        show_modal("Asteroid (2024 TD) will approach Earth on October 6, 2024, with a nominal distance of "
                   "0.02480 AU (minimum distance of 0.02471 AU). Its relative velocity is 10.92 km/s, "
                   "with an infinity velocity of 10.91 km/s. ", "(2024 TD)")

    @reactive.Effect
    @reactive.event(input.asteroid_button_3)
    def _():
        show_modal("(2024 TL2) is scheduled to make a close approach on October 6, 2024, with an incredibly "
                   "close nominal distance of 0.00071 AU. It has a relative velocity of 9.12 km/s and "
                   " a diameter of approximately 1.9 m to 4.2 m", "(2024 TL2)")

    @reactive.Effect
    @reactive.event(input.asteroid_button_4)
    def _():
        show_modal("2024 SD6) will have its close approach on October 6, 2024, with a nominal distance of "
                   " 0.01236 AU and a minimum distance of 0.01231 AU. With an absolute magnitude "
                    "of 27.5, its estimated diameter ranges from 8.2 m to 18 m ", "(2024 SD6)")

    @reactive.Effect
    @reactive.event(input.asteroid_button_5)
    def _():
        show_modal("With a nominal distance of 0.04152 AU and a minimum distance of 0.04151 AU. "
                   "Its relative velocity is 19.32 km/s and a diameter between 29 m and 66 m.", "(2022 FC5)")

    # Set up button click reactions - Near-Earth Comets
    @reactive.Effect
    @reactive.event(input.comet_button_1)
    def _():
        show_modal("Lexell's Comet, designated D/1770 L1, was observed on July 1, 1770, "
                   "and made a close approach to Earth, with a miss distance of 0.0151 AU", "Lexell")

    @reactive.Effect
    @reactive.event(input.comet_button_2)
    def _():
        show_modal("Designated as 55P/1366 U1, this comet was observed on October 26, 1366, and came within a "
                   "miss distance of 0.0229 AU ", "Tempell-tuttle")

    @reactive.Effect
    @reactive.event(input.comet_button_3)
    def _():
        show_modal("Halley's Comet, designated 1P/837 F1, was observed on April 10, 837,"
                   " with a miss distance of 0.0334 AU. THis is one of the most famous comets and it "
                    " is known for its periodic returns every 76 years", "Halley")

    @reactive.Effect
    @reactive.event(input.comet_button_4)
    def _():
        show_modal("Biela's Comet, designated 3D/1805 V1, was observed on December 9, 1805, "
                   "and approached Earth with a miss distance of 0.0366 AU", "Biela")

    @reactive.Effect
    @reactive.event(input.comet_button_5)
    def _():
        show_modal("Designated as C/1743 C1, this comet was observed on February 8, 1743, with a miss distance "
                   "of 0.0390 AU ", "Comet of 1743")

    # Set up button click reactions - Potentially Hazardous Asteroids
    @reactive.Effect
    @reactive.event(input.hazardous_button_1)
    def _():
        show_modal("On October 6, 2024, the asteroid 2025 FC5 will be observed. It has an "
                   "estimated diameter of 39.3 meters. By october 6 this celestial body is "
                   "currently situated at a distance of approximately 6,210,669 kilometers "
                   "from Earth.", "2022 FC5")

    @reactive.Effect
    @reactive.event(input.hazardous_button_2)
    def _():
        show_modal("As of October 6, 2024, the asteroid 2014 FP47 has been noted for its "
                   "impressive estimated diameter of 120 meters. Positioned around "
                   "4,908,075 kilometers away from Earth.", "2014 FP47")

    @reactive.Effect
    @reactive.event(input.hazardous_button_3)
    def _():
        show_modal("The asteroid 2014 FP47 boasts an average estimated diameter of 120.37 meters, "
                   "making it a significant size among near-Earth objects. Currently, it is situated "
                   "at a distance of approximately 0.03AU from Earth", "671076(2014 FP47)")

    @reactive.Effect
    @reactive.event(input.hazardous_button_4)
    def _():
        show_modal("With an average estimated diameter of 21.9 meters, the asteroid 2024 SU3 is "
                   "relatively smaller compared to other near-Earth objects. As of now, it is located "
                   "approximately 2,162,634 kilometers away. ", "2024 SU3")

    @reactive.Effect
    @reactive.event(input.hazardous_button_5)
    def _():
        show_modal("The asteroid 2024 TY has an average estimated diameter of 20.83 meters. "
                   "Currently, it is located around 0.01 AU from Earth,", "2024 TY")

# Run app
app = App(app_ui, server=server)