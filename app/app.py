# app/app.py
from flask import Flask, request, jsonify
from services.tts_service import TTSService

app = Flask(__name__)
tts_service = TTSService(model_path="path/to/your/model")

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    audio = tts_service.synthesize_text(text)
    if audio is None:
        return jsonify({"error": "Synthesis failed"}), 500

    # 音声データをレスポンスとして返す
    # 注意: この例では音声データをそのまま返していますが、実際には適切な形式（例: WAVファイル）に変換してから返すことが多いです。
    return audio, 200, {'Content-Type': 'audio/wav'}

if __name__ == '__main__':
    app.run(debug=True)
