from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_address', methods=['GET'])
def get_address():
    cep = request.args.get('cep')
    if not cep:
        return jsonify({"error": "CEP é obrigatório"}), 400
    
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    if response.status_code != 200:
        return jsonify({"error": "Falha ao buscar o endereço"}), 500
    
    address_data = response.json()
    
    if 'erro' in address_data:
        return jsonify({"error": "CEP inválido"}), 400
    
    return jsonify(address_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
