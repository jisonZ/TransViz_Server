from flask import Blueprint, render_template, request
import json 
from flask import current_app as app

components = Blueprint('components', __name__)

def component_init():
  '''
  load pesudo data for nodes and credentials
  '''
  f = open('/home/haochenz/TransVizServer/app/components/nodes.json')
  global nodesData
  nodesData = json.load(f)
  f.close()

  f = open('/home/haochenz/TransVizServer/app/components/components-credentials.json')
  global credentials
  credentials = json.load(f)
  f.close()

@components.route('/api/v1/nodes', methods=['GET'])
def get_nodes():
  '''
  return a list of nodes
  '''
  return json.dumps(nodesData), 200

@components.route('/api/v1/components-credentials', methods=['GET'])
def get_credentials():
  '''
  return a list of credentials
  '''
  return json.dumps(credentials), 200

@components.route('/api/v1/nodes/<string:name>', methods=['GET'])
def get_node(name):
  '''
  return node by name
  '''
  for node in nodesData:
    if node['name'] == name:
      return json.dumps(node), 200

@components.route('/api/v1/components-credentials/<string:name>', methods=['GET'])
def get_credential(name):
  '''
  return credential by name
  '''
  for credential in credentials:
    if credential['name'] == name:
      return json.dumps(credential), 200
    