# Practice_Python_with_Angela
This Git repository has projects base on Dr. Angela Yu course from Udemy 🐍

## API practice folder
### Kanye West Quote Generator
In the `Kanye folder` you can find `Kanye West Quote Generator`. This Python script `main.py` creates a simple graphical user interface (GUI) application using the `tkinter` library that displays random Kanye West quotes fetched from the [Kanye REST API](https://api.kanye.rest/). The application features an image of Kanye West and a canvas to display the quotes. When you click the provided button, a new random quote from Kanye West will replace the existing one on the canvas.

### Features:
- Fetches random Kanye West quotes from the API.
- Dynamically updates and displays the fetched quote on the canvas.
- Provides a visually appealing GUI with background and image.

### Usage:
1. Clone this repository to your local machine.
2. Make sure you have the required Python libraries (`requests`, `tkinter`) installed.
3. Place your custom background image as "background.png" and an image of Kanye West as "kanye.png" in the same directory as the script.
4. Run the script using a Python interpreter.
5. Click the Kanye West image button to fetch and display a new quote.


### ISS Tracker and Notification System

In the `ISS_Overhead_Notifier folder` you can find `ISS Tracker and Notification System`. This Python script `ISS.py` continuously monitors the International Space Station (ISS) position and sends an email notification when the ISS is overhead during nighttime hours. The script utilizes two main functions:

- `is_iss_overhead()`: Checks if the ISS is within a specified proximity to your coordinates on Earth.
- `is_night()`: Determines if it's nighttime at your location based on sunrise and sunset times.

When both conditions are met (the ISS is overhead and it's nighttime), the script sends an email notification to a specified recipient using Gmail's SMTP server.

### Configuration:
- Set your email and password in the `MY_EMAIL` and `MY_PASSWORD` variables.
- Configure the recipient's email address in the `OKS_EMAIL` variable.
- Adjust your latitude and longitude coordinates in the `MY_LAT` and `MY_LONG` variables to match your location.

### Usage:
1. Clone this repository to your local machine.
2. Install the required Python libraries (`requests`, `datetime`, `smtplib`, `time`) if not already installed.
3. Customize your email, password, recipient's email, and location coordinates in the script.
4. Run the script using a Python interpreter.
5. Keep the script running to monitor the ISS position and receive notifications when it passes overhead during nighttime.


