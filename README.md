# FinalProject-Spotify
This project was designed as a machine learning exercise using the spotify "hit predictor" dataset, created by Farooq Ansari.
Original dataset available at: https://www.kaggle.com/theoverman/the-spotify-hit-predictor-dataset

![Original image from Luxemburg Times](https://luwo-ldocs-prod.imgix.net/2017/12/11/2e0270cd-2d6b-4ca7-bbc4-b1b8e0f998a0.jpeg)

## Project collaborators
* Purvi P. Patel
* Cristina Bardan
* Grecia Villarreal
* Heidy Guzman

## Contents
* original data
* models (& variations) tested
* deployment of the best model (Random Forest)
* Final prodect webpage

## Project Scope
The dataset by Farooq Ansari has features for tracks fetched using Spotify's Web API, base on the tracks labeled `hit` or `flop` by the author, which can be used to make a classification model to predicts whether any given track would be a 'Hit' or not.

## Metadata Summary
The original data, retrieved through Spotify's Web API, includes 40,000+ songs with release dates ranging from 1960-2019. Each track is identified by the track's name, the artist's name, and a unique resource identifier for the track (uri).

Each of the following features are defined and measured by Spotify for each track:
```
1. danceability
2. energy
3. key
4. loudness
5. mode
6. speechiness
7. acousticness
8. instrumentalness
9. liveness
10. valence
11. tempo
12 duration (in milliseconds)
13. time signature
14. target (a boolean variable describing whether the track ever appeared in the Billboard Weekly Hot-100 list)
```

Two additional features were extracted from the data recieved by the API call for Audio Analysis of each particular track:
```
15. chorus hit (an estimation of when the chorus of the track would first appear, i.e. "hit")
16. number of sections
```

Further detail about each of the features and what they measure can be found on Kaggle (link to the dataset ocated above), and through Spotify's documentation: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/.  Ansari's original cource code can be found at: https://github.com/fortytwo102/the-spotify-hit-predictor-dataset


## Methodology

## Results

## Copyright
As stated before, the original dataset was retrived from Kaggle and it was created by Farooq Ansari, as a team we developed the data and created our own model to analize the songs. The first image was retrive from Luxemburg Times site on 06/23/2020.
