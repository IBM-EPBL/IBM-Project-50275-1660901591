from flask import Flask ,request,json

app=Flask(__name__)
food_items={"1":"rice","2":"dosa","3":"vada","4":"payasam","5":"rasam","6":"dal"}

@app.route("/data",methods=["GET","POST"])
def api():
    if request.method=='GET':
        return food_items
    if request.method=='POST':
        data=request.json
        food_items.update(data)
        return 'data is inserted'

@app.route('/data/<id>',methods=['PUT'])
def update(id):
    data=request.form['item']
    food_items[str(id)]=data
    return "Data updated"

@app.route('/data/<id>',methods=['DELETE'])
def deleteOp(id):
    food_items.pop(str(id))
    return "Data deleted"

if __name__=='__main__':
    app.run(debug=True)
