# FinalProject-Spotify
This project was designed as a machine learning exercise using the spotify "hit predictor" dataset, created by Farooq Ansari.
Original dataset available [here](https://www.kaggle.com/theoverman/the-spotify-hit-predictor-dataset).

![Original image from Luxemburg Times](https://luwo-ldocs-prod.imgix.net/2017/12/11/2e0270cd-2d6b-4ca7-bbc4-b1b8e0f998a0.jpeg)
  
## Go to the final [Hit or Flop?](https://spotify-hitpredictor.herokuapp.com/) page!
 
## Project collaborators
* [Purvi P. Patel](https://www.linkedin.com/in/purvippatel/)
* [Cristina Bardan](https://www.linkedin.com/in/cristinabardan/)
* [Grecia Villarreal](www.linkedin.com/in/greciavillarreal/)
* [Heidy Guzman](https://www.linkedin.com/in/heidyloreley/)
  
  
## Contents inside this repository
* Original data
* Models (& variations) tested
* Deployed program
  
  
## Project Scope
The dataset by Farooq Ansari has features for tracks fetched using Spotify's Web API, base on the tracks labeled `hit` or `flop` by the author, which can be used to make a classification model to predicts whether any given track would be a 'Hit' or not. Base on this the team used this data to do a retroactive analysis of features for songs from each decade (1960s - 2010s).


## Metadata Summary
The original data, retrieved through Spotify's Web API (accesed though the Python library Spotipy), includes 40,000+ songs with release dates ranging from 1960-2019. Each track is identified by the track's name, the artist's name, and a unique resource identifier for the track (uri).

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

    
    from sklearn.svm import SVC 
    model_SVM = SVC(kernel='linear')
    model_SVM.fit(x_train_scaled, y_train)
    
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

    from sklearn.linear_model import LogisticRegression
    model_LR = LogisticRegression()
    model_LR.fit(x_train_scaled, y_train)

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

    #Create a sequential model with 3 hidden layers
    from tensorflow.keras.models import Sequential
    model = Sequential() 

    from tensorflow.keras.layers import Dense
    number_inputs = 15  
    number_classes = 2

    model.add(Dense(units=14,activation='relu', input_dim=number_inputs))
    model.add(Dense(units=120,activation='relu'))
    model.add(Dense(units=80,activation='relu'))
    model.add(Dense(units=number_classes, activation='softmax')) 

    #Compile the Model
    import tensorflow as tf
    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

    #Training the Model
    history = model.fit(X_train_scaled, y_train_categorical, epochs=500, batch_size=2000, shuffle=True, verbose=2)

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
|0.24652884971769662|instrumentalness|
|0.10647688218070937|danceability|
|0.10021253875816241|loudness|
|0.09385057415725137|acousticness|
|0.08341099244265467|duration_ms|
|0.08323171690224049|energy|
|0.06260221928220147|valence|
|0.046057546266831645|speechiness|
|0.03927362630575717|tempo|
|0.037828883345652195|liveness|
|0.037804710879875365|chorus_hit|
|0.027115992403401484|sections|
|0.023221514930213242|key|
|0.006420602303837413|mode|
|0.0059633501235151045|time_signature|

Individually, each feature was quite weak as a predictor of whether or not a song would be a hit. However, with all the features included, this was actually the best performing model.

    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=200, max_depth=25) 
    model = model.fit(x_train_scaled, y_train)

```  
Training Data Score: 0.9993836971682507
Testing Data Score: 0.7883623625571665
```

We saw that the adjustments we were making resulted in only slight improvements or variations in the results of each model. This led us to believe that any real improvement to the results required taking a closer look at the data we were using to train the model. We theorized that, since music tastes change relatively less from one decade to the next, but is much more pronouced over 30-40 years, perhaps limiting the data to a block of twenty years would improve the accuracy. We decided to use the songs from the 2000s since that is the most recent period of 20 years, and thus might more accurately predict what would be considered a hit today. With these adjustments, the accuracy of the model did in fact improve. The final adjustments made to the model, which maximized the results, were number of trees (200), and the max depth (25).

```  
Train score: 0.9967398391653989
Test score: 0.8464797913950456
```
  

## Results
After running the 4 models and the variations described above, we chose the Random Forest model with adjusted settings as the final model, given that it had produced the best results with the highest levels of accuracy.


## Deployment of the Model & Analysis of Historical "hit" data
We designed a public webpage for final publication of the machine learning model, deployed on [Heroku](https://spotify-hitpredictor.herokuapp.com/).

Visitors to the site can input a recently released song (or their favorite past song) to see how the model would determine whether it might be a "hit" or not. A second page provides interactives graphs to analyze the preferences in different song features accross all decades in the full dataset (1960s-2010s), and provides a bit more background as to how each feature is defined.

With graph analysis, we noticed consistency in some audio features for hits throughout the decades, meaning that hits have higher quantities of these features and they seems to retain the same influence as to whether a song is popular.  These feature include: danceability, energy, loudness and valence. Other features have increasingly fluctuated in their importance from one decade to the next, characteristics like chorus hits, duration, liveness, mode, sections and speechiness.  That is to say that maybe in the 60's these features were more prominent in hits of that era, but in recent decades songs with higher levels of these features are more likely to be flops.


## Copyright
* The original dataset was retrived from Kaggle and created by Farooq Ansari. As a team, we created our own machine learning model to analize the songs, and further analyzed the features for a breakdown by decade. 
* The template for the website deploying the model was designed by [HTML Codex](https://htmlcodex.com/)
* Graphcs were generated through [Tableau](https://public.tableau.com/profile/grecia.villarreal#!/vizhome/Spotify_15936539551520/Spotify?publish=yes
)
* The first image above was retrive from Luxemburg Times site on 06/23/2020.
