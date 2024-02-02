from flask import Blueprint, render_template, request
from flask import current_app as app

model = Blueprint('model', __name__)

@model.route('/api/v1/chatflows', methods=['POST', 'GET'])
def save_chatflow():
  '''
  save chatflow
  '''
  if request.method == 'POST':
    app.logger.info(request)

  if request.method == 'GET':
    app.logger.info(request)
    return "chatflow", 200
