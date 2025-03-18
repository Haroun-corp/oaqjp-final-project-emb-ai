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

    # Check if the dominant emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotions, scores and dominant_emotion
    output_1 = f"For the given statement, the system response is 'anger': {anger_score}"
    output_2 = f", 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}"
    output_3 = f", and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    return output_1 + output_2 + output_3

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
