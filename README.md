# spy-vs-spy
This project simulates a man-in-the-middle (MITM) attack. It takes place in a ficitonal world, where the Orzhov Syndicate and Azorius Senate are locked in conflict, and consists of three parties:

    * The government of the Orzhov Syndicate,
    * Syndicate Spies,
    * Senate Spies.
    

In this simulation, the Orzhov Syndicate attempts to send instructions to its spies using a web server. When Syndicate spies authenticate with the server, they receive instructions from the government. However, the spies of the Azorius Senate use a MITM attack to discover these instructions, and, in some cases, alter them. The decision of whether or not to alter instructions is based on a blacklist of spy usernames.


# Instructions

Install the required python packages
```
pip install -r requirements.txt
```

Set your Flask app path environment variable
```
export FLASK_APP = path/to/senate_server.py
```

Run the Flask app on the command line
```
flask run
```

Navigate to the server (which is still the default Flask testing path) and can be found at `127.0.0.1:5000`

# Current Spies
| Username        | password           |
| ------------- |-------------  |
| ghostwing      | hazoret |
| carnage      | tyrant      |
