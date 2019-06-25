# Rest-ex
Get Rotten Tomatoes ratings from http://www.omdbapi.com/ OMDB API.

## Environment
- python3
- tested on Linux Ubuntu 16.04
- it can be run stand-alone or in a Docker container

### Clone
- `git clone https://github.com/micpez/rest-ex`

## OMDB API Key
- Get an API key from http://www.omdbapi.com/apikey.aspx and add it to ```config.py```.

## Usage
### from CLI
- dependency: install "requests" library with ```pip install requests```, if not available
```
$ python3 get_ratings.py -h
usage: get_ratings.py [-h] title

Fetch Rotten Tomatoes rating from www.omdbapi.com

positional arguments:
  title       title of the movie

optional arguments:
  -h, --help  show this help message and exit
```

### from Docker
- run the program in a container
- Docker shall be installed in your system
- build the container image:
```sudo docker build -t film_rating .```
- run the program from command line:
```sudo docker run --rm film_rating "<title>"```
