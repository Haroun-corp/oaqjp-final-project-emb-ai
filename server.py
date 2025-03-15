"""Import Flask module and emotion detection module."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """Return the index of page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """Return the emotions score and the dominant emotion."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotion and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the emotion, score and dominant_emotion 
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
