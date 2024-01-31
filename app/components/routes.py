from flask import Blueprint, render_template, request
from random import randint


components = Blueprint('components', __name__)

@components.route('/api/v1/nodes', methods=['GET'])
def get_nodes():
    

# @home.route('/home')
# @home.route('/', methods=['GET', 'POST'])
# def homepage():
#     return render_template('home.html', title='Home')


# @home.route('/about')
# def about():
#     return render_template('about.html', title='About')
