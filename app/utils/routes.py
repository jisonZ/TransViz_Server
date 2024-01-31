from flask import Blueprint, render_template, request, jsonify


utils = Blueprint('utils', __name__)

@utils.route('/api/v1/ip', methods=['GET'])
def get_ip():
  return jsonify({'ip': request.remote_addr}), 200
