from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Dados de exemplo (em produção, usaríamos um banco de dados)
alunos = [
    {"id": 1, "nome": "Lucas", "idade": 20},
    {"id": 2, "nome": "Kelly", "idade": 22},  # Adicionada vírgula aqui
    {"id": 3, "nome": "Kim", "idade": 21}
]

# Rota para listar todos os alunos
@app.route('/alunos', methods=['GET'])
def obter_alunos():
    return jsonify(alunos)

# Rota para obter um aluno específico
@app.route('/alunos/<int:aluno_id>', methods=['GET'])
def obter_aluno(aluno_id):

    #Analiza linha por linha para encontrar o aluno pelo id
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)


