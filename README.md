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

The team also used the data to do a retroactive analysis of features for songs from each decade (1960s - 2010s).


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
14. target (a boolean variable describing if the track ever appeared on Billboard's Weekly Hot-100 list)
```

Two additional features were defined by Ansari and extracted from the data recieved by the API call for Audio Analysis of each particular track:
```
15. chorus hit (an estimation of when the chorus of the track would first appear, i.e. "hit")
16. number of sections
```

Further detail about each of the features and what they measure can be found on Kaggle (link to the dataset located above), and through Spotify's documentation: 
https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/.  

Ansari's original cource code can be found at: 
https://github.com/fortytwo102/the-spotify-hit-predictor-dataset


## Methodology (CRIS, HEIDY -- SI PUEDEN AGREGAR DETALLES....)
The team trained and tested 4 different models to evaluate the dataset, in addition to variations within some of the models.  The models were run on local systems as well as through Google's Collaboratory:
1. SVM (Support Vector Machine) Model
2. Logistic Regression
3. Neural Network/Deep Learning Model
4. Random Forest Model

### 1) SVM
We ran an SVM models with all 16 features, in two different variations: one with the StandardScaler for x, and one using the MinMax Scaler.  The LabelEncoder was used for y in both cases, with the following results:

* StandardScaler: 
    Training Data Score: 0.7257776768626942
    Testing Data Score: 0.7308553079692517
* MinMaxScaler:
    Training Data Score: 0.7256479288981154
    Testing Data Score: 0.7306606986474652


### 2) Logistic Regression
This was the worst performing model of the four. Similar to the SVM Model, we ran Logistic regression with all 16 features suing both Standar and MinMax Scaler variations:

*  StandardScaler:
    Training Data Score: 0.7280158292516786
    Testing Data Score: 0.7288119100904933
* MinMaxScaler:
    Training Data Score: 0.7280482662428233
    Testing Data Score: 0.7283253867860271


### 3) Neural Network/Deep Learning
We originally designed the archetecture of our deep learning model to have 4 layers, while measuring the loss and accuracy levels while training and testing the model.  In the process of training and testing the model, we discovered that the addition of the final layer was essentially overtraining the model, leading to decreased accuracy.  As such, we elimated the last layer from the final version of the model. The best variation model was with 500 epochs and a batch size of 2000.

    TRAINING DATA --> Loss: 0.4263421893119812, Accuracy: 0.7969444394111633
    TESTING DATA --> Loss: 0.4867408275604248, Accuracy: 0.7762965559959412


The initial test of the Neural Network , with all 16 features, performed than the SVM or Logistic Regression Models.  For this reason, we decided to run sevveral variations to see if eliminating and one of the features, or some features in combination, would improve the model's accuracy.  The results can be seen in the table below.

    [INSERT TABLE]

Overall, these tests showed that eliminating any features did not improve accuracy and the best results came from including all 16 features. 


### 4) Random Forest
One thing we were able to see immediately with this model is that no one feature seemed to have a particularly strong weight or influence on the overall results, and the individually, each feature was quite weak as a predictor of whether or not a song would be a hit.  However, with all the features included, this was actually the best performing model. 

* via local 
    Training Data Score: 0.9993836971682507
    Testing Data Score: 0.7848593947650092

At first it seemed that while the training score improved, the testing scrore only improved slightly over prior models.  We thought at first that this meant that we might be overtraining the model, or that the results reflected limits to the dataset itself and the data's abilty to actually predict hit songs. However, we decided to see if part of the reason for the results were due to the power of the local computers we were using to run the models.  To test this idea, we decided to run the same model through Google Collab, which did improve the result.  Lastly, the key difference in improving accuracy for the last variation of the model were final adjustments made to the number of trees (200), and the max depth (25).

* via Google Collab, with adjustments :
    Training Data Score: 0.9957346048427642
    Testing Data Score: 0.9388410451029047


## Results
After running the 4 models and the variations described above, we chose the Random Forest model with adjusted settings as the final model, given that it had produced by far the best results with the highest levels of accuracy.


## Copyright
The original dataset was retrived from Kaggle and created by Farooq Ansari. As a team, we created our own machine learning model to analize the songs, and further analyzed the features for a breakdown by decade. The first image above was retrive from Luxemburg Times site on 06/23/2020.
