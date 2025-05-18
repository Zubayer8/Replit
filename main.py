from flask import Flask, request, jsonify
from scraper import search_anime

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Anime Scraper API is running!"

@app.route("/search")
def search():
    anime = request.args.get("anime", "")
    if not anime:
        return jsonify({"error": "Missing anime name"}), 400
    try:
        results = search_anime(anime)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
