from flask import Blueprint, render_template, request, jsonify
from flask import current_app as app
from ..extensions import db
from ..entities.models import modelflow
import json 

model = Blueprint('model', __name__)

@model.route('/api/v1/chatflows', methods=['POST', 'GET'])
def save_chatflow():
  '''
  save chatflow
  '''
  if request.method == 'POST':
    # TODO: is there a way to match the request data to the model?
    # TODO: why it's request.form?
    app.logger.info("chatflow post")
    app.logger.info(request.json)

    newModelFlow = modelflow(
      name=request.json['name'],
      deployed=request.json['deployed'],
      isPublic=request.json['isPublic'],
      flowData=request.json['flowData']
    )

    db.session.add(newModelFlow)
    db.session.commit()

    # TODO: use json maybe?
    return jsonify(newModelFlow), 201
    # return {"status": "success"}
    
  if request.method == 'GET':
    allmodel = modelflow.query.all()
    return jsonify(allmodel)
