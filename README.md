# FinalProject-Spotify
This project was designed as a machine learning exercise using the spotify "hit predictor" dataset, created by Farooq Ansari.
Original dataset available [here](https://www.kaggle.com/theoverman/the-spotify-hit-predictor-dataset).

![Original image from Luxemburg Times](https://luwo-ldocs-prod.imgix.net/2017/12/11/2e0270cd-2d6b-4ca7-bbc4-b1b8e0f998a0.jpeg)
  
 
## Project collaborators
* [Purvi P. Patel](https://github.com/patelpurvip/)
* [Cristina Bardan](https://github.com/cckuqui)
* [Grecia Villarreal](https://github.com/greciavm)
* [Heidy Guzman](https://github.com/heidyloreley)
  
  
## Contents inside this repository
* Original data
* Models (& variations) tested
* Deployed program
  
  
## Project Scope
The dataset by Farooq Ansari has features for tracks fetched using Spotify's Web API, base on the tracks labeled `hit` or `flop` by the author, which can be used to make a classification model to predicts whether any given track would be a 'Hit' or not. Base on this the team used this data to do a retroactive analysis of features for songs from each decade (1960s - 2010s).


## Metadata Summary
The original data, retrieved through Spotify's Web API, includes 40,000+ songs with release dates ranging from 1960-2019. Each track is identified by the track's name, the artist's name, and a unique resource identifier for the track (uri).

The dataset includes measurements for the following features, defined and measured by Spotify for each track:

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

Two additional features were defined by Ansari and extracted from the data recieved by the API call for Audio Analysis of each particular track:

15. chorus hit (an estimation of when the chorus of the track would first appear, i.e. "hit")
16. sections (number of sections inside the song)


Details about each of the features and what they measure can be found on [Kaggle](https://www.kaggle.com/theoverman/the-spotify-hit-predictor-dataset), and through [Spotify's documentation](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/). Ansari's original source code can be found [here](https://github.com/fortytwo102/the-spotify-hit-predictor-dataset).

  
  
## Methodology
The team trained and tested 4 different models to evaluate the dataset, in addition to variations within some of the models.
1. SVM (Support Vector Machine) Model
2. Logistic Regression
3. Neural Network/Deep Learning Model
4. Random Forest Model

> Note: The models were run in local servers and the ones with the best results were run through Google's Collaboratory to maximize their score.

----
### 1) SVM with two normalization variations
We ran an SVM models with all 16 features, in two different functions for the normalization: with Standard Scaler and the other with MinMax Scaler, both for x values with the following results:

* Standard Scaler:
``` 
Training Score: 0.7257776768626942
Testing Score: 0.7308553079692517
```
* MinMax Scaler:
```
Training Score: 0.7256479288981154
Testing Score: 0.7306606986474652
```
  
----
### 2) Logistic Regression with two normalization variations
Same as SVM, we ran it with all 16 features and with the same normalization variations:

* Standard Scaler:
```
Training Data Score: 0.7280158292516786
Testing Data Score: 0.7288119100904933
```
* MinMax Scaler:
```
Training Data Score: 0.7280482662428233
Testing Data Score: 0.7283253867860271
```

> With further analysis of the data, we decided to normalize each feature independently and ran the same models to see if the results improved. 


----
### 1) & 2) with independent normalization for features with values greater than 1 or with negative values.
The features included in this process were: 
* Loudness (also adjusted to positive values by adding 50)
* Duration (modified from microseconds to seconds)
* Key
* Tempo
* Time_signature
* Chorus_hit
* Sections

The results for each model were:
* SVM
```
Training Data Score: 0.765026436147783
Testing Data Score: 0.7634523693684927
```
* Logistic Regression
```
Training Data Score: 0.7280482662428233
Testing Data Score: 0.7286173007687068
```

> None of these adjustments produced improvements high enough where it seemed worth it to develop the models furhter. Therefore, we decide to test other types of models altogether.
  
----
### 3) Neural Network/Deep Learning
We originally designed the archetecture of our deep learning model to have 4 layers, while measuring the loss and accuracy levels while training and testing the model. In the process of training and testing the model, we discovered that the addition of the final layer was essentially overtraining the model, leading to decreased accuracy. As such, we elimated the last layer from the final version of the model. The best variation model was with 500 epochs, a batch size of 2000, and with MinMax Scaler normalization.

```
Training Score: 0.7969444394111633
Testing Score: 0.7762965559959412
```
  
The initial test of the Neural Network, with all 16 features, performed than the SVM or Logistic Regression Models. For this reason, we decided to run several variations to see if eliminating and one of the features, or some features in combination, would improve the model's accuracy. The results can be seen in the table below.

|Features Missing|Training Score|Testing Score|
|:---:|:---:|:---:|
|Key|0.7884783744812012|0.7758100628852844|
|Key & tempo|0.7861429452896118|0.7703610062599182|
|Key, tempo & speechiness|0.7821207046508789|0.7650092244148254|
|Key, tempo, speechiness & chorus_hit|0.7844237685203552|0.7752262353897095|
|Tempo|0.7880242466926575|0.7751289010047913|
|Tempo & speechiness|0.7824126482009888|0.7678310871124268|
|Chorus_hit|0.7875052690505981|0.7728909254074097|
|Chorus_hit & speechiness|0.7880891561508179|0.7698744535446167|
|Speechiness|0.7906516790390015|0.76938796043396|

Overall, these tests showed that eliminating any features did not improve accuracy and the best results came from including all 16 features.
  
----
### 4) Random Forest
In this case, the best variation model was with Standar Scaler normalization. With it we were able to see immediately with this model is that no one feature seemed to have a particularly strong weight or influence on the overall results:
|Importance|Feature|
|:---:|:---:|
|0.1616016100025217|instrumentalness|
|0.1070654609190537|acousticness|
|0.10271071047704178|danceability|
|0.08363844200055588|energy|
|0.08230679984020853|loudness|
|0.07510012135816571|duration_ms|
|0.07410242758962575|speechiness|
|0.07215948844632883|valence|
|0.05429002409144878|tempo|
|0.05138273046462514|liveness|
|0.050923230770768046|chorus_hit|
|0.03794584582792825|sections|
|0.029724932619056243|key|
|0.010268775607701109|mode|
|0.006779399984970517|time_signature|

Individually, each feature was quite weak as a predictor of whether or not a song would be a hit. However, with all the features included, this was actually the best performing model.

* via local
```  
Training Data Score: 0.9993836971682507
Testing Data Score: 0.7883623625571665
```

At first it seemed that while the training score improved, the testing score only improved slightly over prior models.  We thought at first that this meant that we might be overtraining the model, or that the results reflected limits to the dataset itself and the data's abilty to actually predict hit songs. However, we decided to see if part of the reason for the results were due to the power of the local computers we were using to run the models. To test this idea, we decided to run the same model through Google Collab, which did improve the result.  Lastly, the key difference in improving accuracy for the last variation of the model were final adjustments made to the number of trees (200), and the max depth (25).

* via Google Collab, with adjustments:
```  
Training Data Score: 0.9964482070743931
Testing Data Score: 0.9401060672407922
```
  
    
## Results
After running the 4 models and the variations described above, we chose the Random Forest model with adjusted settings as the final model, given that it had produced by far the best results with the highest levels of accuracy.
  
  
## Copyright
The original dataset was retrived from Kaggle and created by Farooq Ansari. As a team, we created our own machine learning model to analize the songs, and further analyzed the features for a breakdown by decade. The first image above was retrive from Luxemburg Times site on 06/23/2020.
