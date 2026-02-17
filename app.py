from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

app = Flask(__name__)

def generate_btc_data():
    """Generuje dane BTC dla API"""
    data = []
    base_price = 45000
    current_time = datetime.now()
    
    for i in range(200):
        timestamp = int((current_time - timedelta(minutes=200-i)).timestamp())
        
        volatility = np.random.uniform(0.995, 1.005)
        open_price = base_price * volatility
        
        change = np.random.uniform(-0.015, 0.015)
        close_price = open_price * (1 + change)
        
        high_price = max(open_price, close_price) * np.random.uniform(1.001, 1.008)
        low_price = min(open_price, close_price) * np.random.uniform(0.992, 0.999)
        
        volume = np.random.uniform(500, 2000)
        
        data.append({
            'time': timestamp,
            'open': round(open_price, 2),
            'high': round(high_price, 2),
            'low': round(low_price, 2),
            'close': round(close_price, 2),
            'volume': round(volume, 2)
        })
        
        base_price = close_price
    
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/crypto-data')
def get_crypto_data():
    """API zwracające dane krypto"""
    data = generate_btc_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
