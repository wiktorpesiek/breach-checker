import os
import re

from flask import Flask, jsonify, request
from flask_cors import CORS

DATA_FILE = "/app/data/leaked-sha1.txt"

app = Flask(__name__)
CORS(app, origins=["http://localhost:8080"])


def load_hashes(path):
    with open(path, encoding="utf-8") as f:
        hashes = {
            line.strip().lower()
            for line in f
            if line.strip() and not line.startswith("#")
        }
    print(f"Wczytano {len(hashes)} hashy z {path}", flush=True)
    return hashes


KNOWN_HASHES = load_hashes(DATA_FILE)


@app.post("/check")
def check():
    data = request.get_json(silent=True) or {}
    h = data.get("hash")
    if not isinstance(h, str):
        return jsonify({"error": "Brak pola 'hash'"}), 400
    h = h.strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", h):
        return jsonify({"error": "Pole 'hash' musi byc skrotem SHA-1"}), 400
    print(f"Sprawdzam skrot {h[:5]}...", flush=True)
    found = h in KNOWN_HASHES
    return jsonify({"found": found})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
