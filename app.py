import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- API Credentials from Azure AI Foundry ---
# DeepSeek AI Model Interference Endpoint
DEEPSEEK_ENDPOINT = "https://hoteldeepseek2853572667.services.ai.azure.com/models"
# (Note: Use the specific endpoint path required by your model if different)

# API Key for DeepSeek AI (keep it secure)
API_KEY = "B1EpkVjxJvBcF9nxf7SKl2obAAkJQ65ai7Ac7dGovU1Ast6sy8NdJQQJ99BBACHrzpqXJ3w3AAAAACOGzMk6"

# --- Function to Call the DeepSeek AI Model ---
def call_deepseek_ai(user_query):
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY  # some services require the header name "api-key"
    }
    
    # Payload for the AI model. Adjust parameters as needed.
    payload = {
        "prompt": user_query,    # The user input is sent as the prompt.
        "max_tokens": 150        # Set maximum tokens for the response.
        # You can add other parameters as required by your model.
    }
    
    # Make the POST request to the DeepSeek AI model endpoint.
    response = requests.post(DEEPSEEK_ENDPOINT, json=payload, headers=headers)
    
    if response.status_code == 200:
        # Adjust the parsing based on your model’s response structure.
        result = response.json()
        # Example: assuming the model returns an "output" field.
        return result.get("output", "Sorry, I didn't understand that.")
    else:
        return f"Error: {response.status_code} - {response.text}"

# --- Flask Route to Handle Chatbot Requests ---
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    # Here you can also add custom logic to handle intents (like booking, pricing, etc.)
    ai_response = call_deepseek_ai(user_message)
    
    return jsonify({"response": ai_response})

# --- Run the Flask App ---
if __name__ == "__main__":
    # For local testing on port 5000
    app.run(host="0.0.0.0", port=5000)
