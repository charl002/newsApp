import os
from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Placeholder for the API URL
API_TOKEN = os.environ.get('API_KEY')
BASE_URL = "https://api.thenewsapi.com/v1/news/top?"

@app.route('/fetch-news', methods=['GET'])
def fetch_news():
    # Get query parameters from the client
    locale = request.args.get('locale', '')  # Default to empty (all countries)
    domains = request.args.get('domains', '')  # Default to empty
    exclude_domains = request.args.get('exclude_domains', '')
    source_ids = request.args.get('source_ids', '')
    exclude_source_ids = request.args.get('exclude_source_ids', '')
    language = request.args.get('language', '')
    published_on = request.args.get('published_on', '')
    headlines_per_category = request.args.get('headlines_per_category', '6')  # Default to 6
    include_similar = request.args.get('include_similar', 'true')  # Default to true

    # Set up the parameters for the API request
    params = {
        'api_token': API_TOKEN,
        'locale': request.args.get('locale', ''),
        'language': request.args.get('language', '')
    }

    # Send the GET request to the API
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('data', [])  # Extract articles from the response
        else:
            articles = []  # Fallback in case of an error
        return render_template('news.html', articles=articles)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)