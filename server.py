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
    """Return the emotions scores and the dominant emotion."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions scores and dominant emotion from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the emotion scores is None and dominant emotion , indicating an error or invalid input
    if anger_score is None and disgust_score is None and fear_score is None and joy_score is None and sadness_score is None and dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotions, scores and dominant_emotion 
    return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
