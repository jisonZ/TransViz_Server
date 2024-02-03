from flask import Blueprint, render_template, request, jsonify
from flask import current_app as app
from ..extensions import db
from ..entities.models import modelflow, User
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
    print(request.form['isPublic'])
    print(request.form['deployed'])
    print(str(request.form['flowData']))
    # newModelFlow = modelflow(
    #   id=str('tedtttttttt'),
    #   name=str(request.form['name']),
    #   deployed=request.form['deployed'].title() == 'True',
    #   isPublic=request.form['isPublic'].title() == 'True',
    #   flowData=str(request.form['flowData'])
    # )
    user = User(
            username="tesrsfssdfdrsdfssdfdteest ",
            email="smail",
        )
    db.session.add(user)
    db.session.commit()
    # newModelFlow = modelflow(
    #   id='testest',
    #   name='name',
    #   deployed=True,
    #   isPublic=True,
    #   flowData='flowlflow'
    # )
    # db.session.add(newModelFlow)
    # db.session.commit()
    return "saved", 201
    return jsonify(newModelFlow)
    

  if request.method == 'GET':
    app.logger.info(request)
    return "chatflow", 200
