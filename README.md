### International Space Station (ISS) Real-Time Tracker

This project provides a simple visualisation of the International Space Station's (ISS) current position in real-time using Python and the Turtle graphics module. The core functionality relies on fetching real-time location data of the ISS from a public API and plotting its movement onto a world map.

#### Key Features:

- **Real-Time ISS Positioning**: The project utilises the Open Notify API to retrieve the ISS's current latitude and longitude coordinates. These coordinates are refreshed every two seconds to ensure the position is updated continuously on the map.

- **Map Display**: Using the Turtle graphics module, a world map background (`world.gif`) is displayed, with the ISS's position plotted on it. The ISS is represented as a custom turtle icon (`iss.gif`), which moves across the map as new positional data is received.

- **Crew Onboard Display**: A text file (`crew.txt`) is updated dynamically to show the names of the astronauts currently onboard the ISS. This provides an additional real-time feature that offers insight into the station’s crew, pulled directly from the API.

- **Error Handling**: To ensure stability, basic error handling has been implemented to catch potential issues when fetching data from the API.

- **Longitude Wrapping**: Since longitude values can exceed the bounds of the map, a wrapping mechanism ensures smooth transitions when the ISS crosses the map’s edges.

---

### Setup Instructions:

To run this project, follow these steps to set up the environment:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ISS_where
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install any necessary dependencies (if applicable in the future)**: If you use additional libraries, create a `requirements.txt` file and include the dependencies. For now, no additional packages are required.

5. **Run the programme**:
   ```bash
   python main.py
   ```

---

### Important Notes:

- **Virtual Environment**: Using a virtual environment (`venv`) is highly recommended to manage project-specific dependencies and avoid conflicts with other projects. The instructions above will help you set up and activate the virtual environment.

By following these steps, you’ll ensure that the project is set up correctly and ready to run.
