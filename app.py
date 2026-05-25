from flask import Flask, render_template, request, jsonify
from analyzer import analyze_protocol
from ai_engine import explain
from attack_simulator import get_attack_data

app = Flask(__name__)


# ================= HOME =================
@app.route('/')
def home():
    return render_template('index.html')


# ================= PROTOCOL ANALYSIS =================
@app.route('/analyze', methods=['POST'])
def analyze():
    protocol = request.form.get('protocol')

    if not protocol:
        return "No protocol selected"

    result = analyze_protocol(protocol)

    return render_template(
        'protocol.html',
        protocol=protocol,
        result=result
    )


# ================= ATTACK PAGE =================
@app.route('/attack')
def attack():
    return render_template('attack.html')


# ================= ATTACK DATA API =================
@app.route('/get_attack', methods=['POST'])
def get_attack():
    layer = request.form.get('layer')

    if not layer:
        return jsonify({"error": "No layer provided"})

    data = get_attack_data(layer)

    return jsonify(data)


# ================= AI CHAT =================
@app.route('/ai_chat', methods=['POST'])
def ai_chat():
    protocol = request.form.get('protocol')
    question = request.form.get('question')

    if not protocol:
        return jsonify({"response": "Protocol missing"})

    data = analyze_protocol(protocol)["data"]

    if not data:
        return jsonify({"response": "No data found for protocol"})

    response = explain(protocol, data, question)

    return jsonify({"response": response})


# ================= ERROR HANDLER =================
@app.errorhandler(404)
def not_found(e):
    return "Page not found", 404


# ================= RUN APP =================
if __name__ == '__main__':
    app.run(debug=True)