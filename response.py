from flask import Flask, request, jsonify
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()  # loads API_KEY and CSE_ID
API_KEY = os.getenv("API_KEY")
CSE_ID = os.getenv("CSE_ID")

app = Flask(__name__)

def google_search(query, num=5):
    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=query, cx=CSE_ID, num=num).execute()
    items = res.get("items", [])
    return [{"title": i.get("title"), "link": i.get("link")} for i in items]

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    q = data.get("query", "")
    results = google_search(q)
    return jsonify({"results": results})

if __name__=="__main__":
    app.run(debug=True)
