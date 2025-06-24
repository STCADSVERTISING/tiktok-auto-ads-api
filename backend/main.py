
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/targeting', methods=['POST'])
def analyze_target():
    data = request.json
    keywords = data.get('keywords', '')
    return jsonify({
        'audience': 'หญิง อายุ 18-24 สนใจแฟชั่น',
        'keyword_used': keywords
    })

@app.route('/api/launch_ad', methods=['POST'])
def launch_ad():
    return jsonify({'status': 'success', 'message': 'ยิงแอดแล้ว (mock)'})

@app.route('/api/launch_multi_ads', methods=['POST'])
def launch_multi_ads():
    with open('accounts.json', 'r') as f:
        accounts = json.load(f)

    results = []
    for acc in accounts:
        results.append({
            'brand': acc['name'],
            'pixel_id': acc['pixel_id'],
            'ad_account_id': acc['ad_account_id'],
            'status': 'success (mock)'
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
