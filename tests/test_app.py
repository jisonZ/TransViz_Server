import json
from app.entities.models import modelflow


def test_modelflow(client, app):
  #TODO: add more testing!!!
  # response = client.get('/api/v1/modelflow')
  testdata1 = {
      "name": "test1",
      "deployed": False,
      "isPublic": False,
      "flowData": '{"nodes":[{"width":300,"height":277,"id":"aiPlugin…ges":[],"viewport":{"x":-1008,"y":-727,"zoom":2}}',
  }

  testdata2 = {
      "name": "test2",
      "deployed": False,
      "isPublic": False,
      "flowData": '{"nodes":[{"width":300,"height":277,"id":"aiPlugin…ges":[],"viewport":{"x":-1008,"y":-727,"zoom":2}}',
  }
  response = client.post("http://localhost:3000/api/v1/chatflows", json=testdata1)
  response = client.post("http://localhost:3000/api/v1/chatflows", json=testdata2)
  print(response.data)

  # with app.app_context():
  #     print(modelflow.query.all())

  response = client.get('http://localhost:3000/api/v1/chatflows')
  # print(response.data)
