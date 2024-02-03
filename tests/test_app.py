import json 

def test_modelflow_post(client, app):
  print("test_modelflow_post")
  # response = client.get('/api/v1/modelflow')
  f = open('/home/haochenz/TransVizServer/tests/chatflow_post.json')
  chatflowData = json.load(f)
  f.close()
  print(chatflowData)
  response = client.post('http://localhost:3000/api/v1/chatflows', data=chatflowData)
  print(response.data)
  # assert response.status_code == 201
  # with app.app_context():
  #   assert User.query.count() == 1
  #   assert User.query.first().username == 'test'

# def test_modelflow_get(client, app):
#   response = client.get('http://localhost:3000/api/v1/chatflows')
#   # print(response.data)
 


