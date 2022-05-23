# Recipe Microservice
A microservice Python program for a Few Devs Short of a Scrum team member Miguel.

Serves up a list of recipe URLs as a JSON object in a signal.txt file.

1. Client makes request by writing the 'run' command as a new line to the signal file.
2. Server reads signal and begins the request process.
3. Server reads the recipies csv data file into a JSON object in memory.
4. Server write the data object from memory into the recipies JSON file.
5. Client waits fomr a complete command in the signal file.
6. Client reads the JSON object from the JSON file.
