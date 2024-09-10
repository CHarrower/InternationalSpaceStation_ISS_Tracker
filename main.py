import json
import turtle
import urllib.request
import time

# Function to update ISS position on the map
def update_iss_position():
    # Load the current status of the ISS in real-time
    error = "error"
    #try catch 
    try:
        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
    except error:
        print(error)     

    # Extract the ISS location
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])

    # Check and adjust the ISS's longitude to wrap around the map edges
    if lon > 180:
        lon = -180 + (lon - 180)
    elif lon < -180:
        lon = 180 - (-180 - lon)

    # Output lon and lat to the terminal
    print("\nLatitude: " + str(lat))
    print("Longitude: " + str(lon))



    # Update the ISS location on the map
    iss.goto(lon, lat)


# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("world.gif")  # Make sure you have a world.gif file in the current directory
screen.register_shape("iss.gif")  # Make sure you have an iss.gif file in the current directory

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

# Fetch and display the initial position of the ISS
update_iss_position()

# Continuous update loop
while True:
    update_iss_position()
    # Refresh every 2 seconds
    time.sleep(2)
    
