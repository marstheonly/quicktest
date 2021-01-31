from flask import Flask, json, jsonify

names = [{'id': 0, 'name': 'Marius', 'city': 'T-dot'}, {'id': 1, 'name': 'Sorin', 'city': 'Tel Aviv'}]


api = Flask(__name__)

@api.route('/names', methods=['GET'])
def get_names():
#  return json.dumps(names)
   return jsonify(names)


@api.route('/names/<int:id>', methods=['GET'])
def get_names_id(id):
   return jsonify(names[id])


if __name__ == '__main__':
    api.run(host='0.0.0.0',port=4999)

