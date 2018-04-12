# spy-vs-spy
This project simulates a man-in-the-middle (MITM) attack. It takes place in a ficitonal world, where the Orzhov Syndicate and Azorius Senate are locked in conflict, and consists of three parties:

    * The government of the Orzhov Syndicate,
    * Syndicate Spies,
    * Senate Spies.
    

In this simulation, the Orzhov Syndicate attempts to send instructions to its spies using a web server. When Syndicate spies authenticate with the server, they receive instructions from the government. However, the spies of the Azorius Senate use a MITM attack to discover these instructions, and, in some cases, alter them. The decision of whether or not to alter instructions is based on a blacklist of spy usernames.
