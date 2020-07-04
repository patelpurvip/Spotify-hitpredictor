from flask import Flask, render_template, redirect, jsonify, request
import spotify

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html
@app.route("/")
def home():
    return render_template("index.html", item='home')

@app.route("/home")
def home2():
    return render_template("index.html", item='home')

# Route for hit_flop
@app.route('/hit_flop', methods = ['POST'])
def hit_flop():
    track = request.form["song"]
    artist = request.form["artist"]
    print(track, artist)
    
    try:
        response = spotify.hit_flop(track, artist)
        # hit_predict, hit_score = spotify.hit_flop(track, artist)
        if len(response) == 3:
            hit_predict = response[0]
            hit_score = response[1]
            feature_table = response[2]
            track = f'{track} by {artist}'

            if hit_predict[0] == 1:
                result = 'Looks like a hit!'
                score = f"There's a {round(hit_score[0][1]*100,0)}% chance it'll be a hit"

            else:
                result = 'It could be a flop'
                score = f"There's a {round(hit_score[0][0]*100,0)}% chance it'll be a flop =("
            
            return render_template("index.html", result=result, score=score, feature_table=feature_table, song=track)
        else:
            error = response[0]
            return render_template("index.html", score=error, item='home')
    except:
        return '=('   

@app.route("/about/")
def about():
    return render_template("aboutv2.html", item='about')

@app.route("/historical/")
def historical():
    return render_template("historical.html", item='historical')

if __name__ == "__main__":
    app.run(debug=True)