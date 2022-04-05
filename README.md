## Table of Contents
[About](#about-the-project)  
[Tools Used](#tools-used)  
[Getting Started](#getting-started-on-windows)  
[License](#license)  

# About The Project
## Spotify Sorter
This application sorts user's Spotify playlist based on any of the following attributes:
* Name of the Song
* Name of the Artist
* Duration of the Song
* Popularity
[Click to visit deployed version](https://playlistsorter.herokuapp.com/)

# Tools Used
* [Flask (python)](https://flask.palletsprojects.com/en/2.1.x/)
* HTML
* CSS
* [Spotipy/Spotify API](https://spotipy.readthedocs.io/en/2.19.0/)

# Getting Started On Windows
### Creating Repo and Installing Dependencies (Part 1)
1. Clone the repository.
``git clone https://github.com/SinghxRaj/PlaylistSorter.git``

2. Install virtualenv so that you can create your virtual environment (If not installed yet).
``pip install virtualenv``

3. Create your virtual environment. Make sure your inside your PlaylistSorter.
``virtualenv venv``

4. Activate your virtual environment.
``venv/Scripts/activate``

5. Install dependencies which are stored in requirements.txt:
``pip install -r requirements.txt``

### Creating a Spotify App (Part 2)
1. Go to [Spotify Dashboard](https://developer.spotify.com/dashboard/login)
2. Login in and click ``Create An App``
3. Give it any name and description and then click create.
4. Click on ``Edit Settings``
5. Go under ``Redirect URIs`` and add ``http://127.0.0.1:5000/callback``
6. Optionally, under ``Redirect URIs`` you can add the following:
   * ``http://127.0.0.1:5000/callback/``
   * ``http://localhost:5000/callback/``
   * ``http://localhost:5000/callback``
7. Save settings and copy the ``Client ID`` and ``Client Secret`` which are needed to   set the environment variables.

### Setting Environment Variables (Part 3)
1. Set the following environment variables in the terminal.
``set SPOTIFY_CLIENT_ID=<client_id>``
``set SPOTIFY_CLIENT_SECRET=<client_secret>``
``set SECRET_KEY=<any_string>``

### Run Application (Final Part)
1. To run the application.
``python run.py``

# License
Distributed under the MIT license. See ``LICENSE`` for more information.
