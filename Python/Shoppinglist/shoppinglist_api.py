from item_db_context import ItemDBContext as idc
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add-item", methods=["POST"])
def add():
    item = request.get_json()
    db = idc()
    db.create_item((item["name"], item["price"], item["amount"]))
    return jsonify(item)

@app.route("/get-items", methods=["GET"])
def get_all():
    db = idc()
    result = db.get_all_items()
    items = []
    for r in result:
        items.append({"id": r[0], "name": r[1], "amount": r[2], "price": r[3]})
    return jsonify(items)

@app.route("/get-item/<item_id>", methods=["GET"])
def get(item_id):
    db = idc()
    r = db.get_item_by_id(item_id)
    return jsonify({"id": r[0][0], "name": r[0][1], "amount": r[0][2], "price": r[0][3]})

@app.route("/update-item", methods=["PUT"])
def update():
    item = request.get_json()
    db = idc()
    db.update_item(item["id"], item["name"], item["price"], item["amount"])
    return jsonify(item)

@app.route("/delete-item/<item_id>", methods=["DELETE"])
def delete(item_id):
    db = idc()
    db.delete_item(item_id)
    return jsonify({})
    
def run():
    app.run(debug=False)
        