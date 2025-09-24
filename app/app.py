from flask import Flask, render_template, jsonify
import os
import logging
from datetime import datetime

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': os.environ.get('APP_VERSION', '1.0.0')
    })

@app.route('/metrics')
def metrics():
    
    return jsonify({
        'requests_total': 100,
        'response_time_seconds': 0.05,
        'memory_usage_mb': 45
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False) 
