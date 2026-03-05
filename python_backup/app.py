from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def hitung_silinder(jari_jari, tinggi):
    keliling = 2 * math.pi * jari_jari
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    volume = math.pi * (jari_jari ** 2) * tinggi
    return keliling, luas_permukaan, volume

def hitung_kerucut(jari_jari, tinggi):
    keliling = 2 * math.pi * jari_jari
    garis_pelukis = math.sqrt((jari_jari ** 2) + (tinggi ** 2))
    luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)
    volume = (1 / 3) * math.pi * (jari_jari ** 2) * tinggi
    return keliling, luas_permukaan, volume

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    shape = data.get('shape')
    try:
        r = float(str(data.get('radius')).replace(',', '.'))
        t = float(str(data.get('height')).replace(',', '.'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Harap masukkan angka yang valid.'}), 400

    if r < 0 or t < 0:
        return jsonify({'error': 'Jari-jari dan tinggi tidak boleh negatif.'}), 400

    if shape == 'silinder':
        k, l, v = hitung_silinder(r, t)
    elif shape == 'kerucut':
        k, l, v = hitung_kerucut(r, t)
    else:
        return jsonify({'error': 'Bentuk tidak valid.'}), 400
        
    return jsonify({
        'keliling': round(k, 2),
        'luas': round(l, 2),
        'volume': round(v, 2)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
