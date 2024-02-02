from flask import Blueprint, render_template, request
from flask import current_app as app

modelflow = Blueprint('modelflow', __name__)

@modelflow.route('/api/v1/chatflows', methods=['POST', 'GET'])
def save_chatflow():
  '''
  save chatflow
  '''
  if request.method == 'POST':
    print("post chatflow")

  if request.method == 'GET':
    print("get chatflow")
