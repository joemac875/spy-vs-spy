# spy-vs-spy
This project simulates a man-in-the-middle (MITM) attack. It takes place in a ficitonal world, where the Syndicate and  Senate are locked in conflict, and consists of three parties:

    * The government of the  Syndicate,
    * Syndicate Spies,
    * Senate Spies.
    

In this simulation, the  Syndicate attempts to send instructions to its spies using a web server. When Syndicate spies authenticate with the server, they receive instructions from the government. However, the spies of the Senate use a MITM attack to discover these instructions, and, in some cases, alter them. The decision of whether or not to alter instructions is based on a blacklist of spy usernames.


# Instructions

Create a new virtual environment
```
python3 -m venv mitm_env
```

Activate the environment (in bash):

```
source mitm_env/bin/activate
```


Install the required python packages
```
pip install -r requirements.txt
```


Run the senate server
```
python /path/to/senate_server.py
```

Run the syndicate server
```
python /path/to/syndicate_server.py
```

The Senate server runs on `localhost:12345`.

The Syndicate server runs on `localhost:12346`.

Any requests made on the syndicate server will be logged in the access table of the syndicate.db database. In addition, spies in the syndicate.db database table syndicate_spies will be scrubbed from any requests made on the syndicate server.

# Current Spies
| Username        | password           |
| ------------- |-------------  |
| ghostwing      | hazoret |
| carnage      | tyrant      |

