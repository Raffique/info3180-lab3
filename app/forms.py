from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message= StringField('Message', validators=[DataRequired()], widget=TextArea())