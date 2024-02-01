from flask import Blueprint, render_template, request
from random import randint
import json 
from flask import current_app as app

components = Blueprint('components', __name__)

def component_init():
  # load nodes data 
  f = open('app/components/nodes.json')
  global nodesData
  nodesData = json.load(f)
  f.close()

  # load credentials
  f = open('app/components/components-credentials.json')
  global credentials
  credentials = json.load(f)
  f.close()

@components.route('/api/v1/nodes', methods=['GET'])
def get_nodes():
  return json.dumps(nodesData), 200

@components.route('/api/v1/components-credentials', methods=['GET'])
def get_credentials():
  return json.dumps(credentials), 200

@components.route('/api/v1/nodes/<string:name>', methods=['GET'])
def get_node(name):
  for node in nodesData:
    if node['name'] == name:
      return json.dumps(node), 200

@components.route('/api/v1/components-credentials/<string:name>', methods=['GET'])
def get_credential(name):
  for credential in credentials:
    if credential['name'] == name:
      return json.dumps(credential), 200
    

# @home.route('/home')
# @home.route('/', methods=['GET', 'POST'])
# def homepage():
#     return render_template('home.html', title='Home')


# @home.route('/about')
# def about():
#     return render_template('about.html', title='About')