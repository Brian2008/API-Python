from flask import Flask, json,jsonify,request
app=Flask(__name__)
tasks=[
{id:1,'title':'groceries','description':'milk,cheese,fruit,pizza','done':False},
{id:2,'title':'python','description':'pythonBook','done':False}
]
@app.route("/add-data",methods=["POST"])
def AddData():
    if not request.json:
        return jsonify({"status":"error","message":"Please Provide Data."},400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({"status":"success","message":"Task Added Successfully!"},)
@app.route("/get-data")
def GetTask():
    return jsonify({"data":"tasks"})
if(__name__=="__main__"):
    app.run(debug=True)
    
