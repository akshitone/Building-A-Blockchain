from crypt import methods
from packages import *

app = Flask(__name__)

blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        "message": "Block mined successfully",
        "block": block
    }

    return jsonify(response), 200


@app.route('/get_chain', methods=["GET"])
def get_chain():
    response = {
        "message": "Blockchain retrieved successfully",
        "length": blockchain.length(),
        "chain": blockchain.chain,
    }

    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    if blockchain.is_chain_valid(blockchain.chain):
        response = {"message": "Blockchain is valid"}
    else:
        response = {"message": "Blockchain is not valid"}

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
