from flask import current_app, jsonify, request
from app import app
from app.dowloader.json_downloader import JsonDownloader

@app.route('/')
def home():
    return "Hello, Jai Sai Ram!"

@app.route('/download-json', methods=['GET'])
def download_json():
    """
    Endpoint to download JSON data from a given URL.
    Expects a JSON payload with 'url' and 'destination' keys.
    """
    url = current_app.config.get('DOWNLOAD_URL')
    destination = current_app.config.get('DOWNLOAD_DESTINATION')
    if not url or not destination:
        return jsonify({"error": "URL and destination are required"}), 400

    downloader = JsonDownloader()
    result = downloader.download(url, destination)

    if result is None:
        return jsonify({"error": "Failed to download JSON data"}), 500
    else: 
        return jsonify(result), 200



    return jsonify({"message": "Download initiated"}), 200