from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from flask_babel import _, lazy_gettext as _l








class ConsultForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    email= StringField(_l('Email'), validators=[DataRequired(),Email()])
    telefon = StringField(_l('Telefonnummer'), validators=[DataRequired()])
    question = TextAreaField(_l('Ihre Nachricht (Branche, Terminvorschlag, Frage, etc.)'), validators=[DataRequired()])
    send = SubmitField(_l('Senden'))
