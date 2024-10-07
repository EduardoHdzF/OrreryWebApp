# 2024 NASA Space Apps Challenge - Orrery Web App.

## Project: Orrery Web App that Displays Near-Earth Objects.

### Team: Esnupi coders.

#### Team members:

	- Cruz Cruz Alan Josué.
	- Floriano Hernández Eduardo.
	- López Villalba Cielo.
	- Matute Cantón Sara Lorena.
	- Mora Hernández Dulce Julieta.
	- Noriega Rodríguez Marcos Julián.

Welcome to our submission for the 2024 NASA Space Apps Challenge! 

### [Click for the Live Demo](https://eduardohdzf.github.io/OrreryWebApp/)



#### Objective 

Our project presents a unique opportunity to innovate within the educational technology space, promoting knowledge through an engaging and interactive platform. By leveraging our programming skills and a passion for education, we aim to inspire curiosity about the universe.

#### Features

	- 3D Visualization: Explore the solar system with interactive 3D models to scale.
	- Planetary Orbits: View the orbits of major planets.
	- Data Presentation: We display information about each planet and Near-Earth Objects in sections and in an engaging way.

#### How to Compile and Run

We need to create a virtual environment in Python, activate it, and then install the necessary requirements:
	- python3 -m venv .venv
	- source .venv/bin/activate
	- pip install -r requirements.txt
	
To run the Orrery Web App:
	- shiny run app.py
	
Then, open the port http://127.0.0.1:8000 in your browser, where our Orrery Web App will be accessible.

#### Technologies Used

We used the "shiny" framework for Python for the frontend, and for the 3D Orrery we used "plotly".

	- Shiny: https://shiny.posit.co/py/
	- plotly: https://plotly.com/python/

The information about the planets was obtained from official NASA sites:
	- https://nssdc.gsfc.nasa.gov/planetary/factsheet/
	- https://eyes.nasa.gov/apps/asteroids/#/watch/2022_fc5

#### Future Work

	- Track Near-Earth Objects based on real-time data.
	- Display the information in a more interactive and visually appealing way.
	- Implement additional datasets and integrate more astronomical bodies.
