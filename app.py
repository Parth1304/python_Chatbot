from flask import Flask, render_template, request, jsonify
from chat import get_response
import logging
import traceback

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.get("/")
def index_get():
    return render_template('base.html')

@app.post("/predict")
def predict():
    try:
      
        data = request.get_json()
        app.logger.debug("Received data: %s", data)

        text = data.get("message")
        if not text:
            return jsonify({"error": "No message provided"}), 400
        
        response = get_response(text)
        message = {"answer": response}

        # Log the response
        app.logger.debug("Response: %s", message)
        return jsonify(message)

    except Exception as e:
        
        app.logger.error("Error occurred: %s", str(e))
        app.logger.error(traceback.format_exc())
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500

if __name__ == "__main__":
    app.run(debug=True)
