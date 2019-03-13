from flask import render_template, flash, redirect, url_for, request, g, current_app, json
from flask_login import login_user, logout_user, current_user, login_required
from app.main import bp



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])

def index():

	return render_template('index.html')






@bp.route('/container_explain', methods=['GET', 'POST'])

def container_explain():



	return render_template('explain.html')



@bp.route('/howitworks', methods=['GET', 'POST'])

def howitworks():

	

	return render_template('howitworks.html')

