from flask import render_template, flash, redirect, url_for, request, g, current_app, json
from flask_login import login_user, logout_user, current_user, login_required
from app.main import bp
from app.main.forms import ConsultForm



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])

def index():

	form=ConsultForm()

	return render_template('index.html' ,form=form)






@bp.route('/container_explain', methods=['GET', 'POST'])

def container_explain():



	return render_template('explain.html')



@bp.route('/howitworks', methods=['GET', 'POST'])

def howitworks():

	

	return render_template('howitworks.html')





@bp.route('/packages', methods=['GET', 'POST'])

def packages():

	

	return render_template('packages.html')




@bp.route('/aspackage', methods=['GET', 'POST'])

def aspackage():

	

	return render_template('aspackage.html')



@bp.route('/transparent', methods=['GET', 'POST'])

def transparent():

	

	return render_template('transparent.html')


@bp.route('/lego', methods=['GET', 'POST'])

def lego():

	

	return render_template('lego.html')


@bp.route('/scalable', methods=['GET', 'POST'])

def scalable():

	

	return render_template('scalable.html')


@bp.route('/footer', methods=['GET', 'POST'])

def footer():

	

	return render_template('footer.html')




