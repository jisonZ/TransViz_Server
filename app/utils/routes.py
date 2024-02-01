from flask import Blueprint, render_template, request, jsonify
from flask import current_app as app

utils = Blueprint('utils', __name__)

@utils.route('/api/v1/ip', methods=['GET'])
def get_ip():
  # app.logger.info("Getting IP")
  return jsonify({'ip': request.remote_addr}), 200
