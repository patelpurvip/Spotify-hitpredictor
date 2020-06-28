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
* final prodect webpage


## Project Scope
The dataset by Farooq Ansari has features for tracks fetched using Spotify's Web API, base on the tracks labeled `hit` or `flop` by the author, which can be used to make a classification model to predicts whether any given track would be a 'Hit' or not. 

The collaboration team also used the data to do a retroactive analysis of features for songs from each decade (1960s - 2010s).


## Metadata Summary
The original data, retrieved through Spotify's Web API, includes 40,000+ songs with release dates ranging from 1960-2019. Each track is identified by the track's name, the artist's name, and a unique resource identifier for the track (uri).

The dataset includes measurements for the following features, defined and measured by Spotify for each track:
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
12. duration (in milliseconds)
13. time signature
14. target (a boolean variable describing whether the track ever appeared in the Billboard Weekly Hot-100 list)
```

Two additional features were defined by Ansari and extracted from the data recieved by the API call for Audio Analysis of each particular track:
```
15. chorus hit (an estimation of when the chorus of the track would first appear, i.e. "hit")
16. number of sections
```

Further detail about each of the features and what they measure can be found on Kaggle (link to the dataset located above), and through Spotify's documentation: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/.  Ansari's original cource code can be found at: https://github.com/fortytwo102/the-spotify-hit-predictor-dataset


## Methodology
The team trained and tested 4 different models to evaluate the dataset, in additiona to variations within some of the models:
1. Logistic Regression
2. SVM (Support Vector Machine) Model
3. Neural Network/Deep Learning Model
4. Random Forest Model

#### 1) Logistic Regression
#### 2) SVM
#### 3) Neural Network/Deep Learning
We originally designed the archetecture of our deep learnign model to have 4 layers, while measuring the loss and accuracy levels while training and testing the model.  In the process of training and testing the model, we discovered that the addition of the final layer was essentially overtraining the model, leading to decreased accuracy.  As such, we elimated the last layer from the final version of the model. z


#### 4) Random Forest

The models were run on local systems as well as through Google's Collaboratory.

## Results


## Copyright
The original dataset was retrived from Kaggle and created by Farooq Ansari. As a team, we created our own machine learning model to analize the songs, and further analyzed the features for a breakdown by decade. The first image above was retrive from Luxemburg Times site on 06/23/2020.
