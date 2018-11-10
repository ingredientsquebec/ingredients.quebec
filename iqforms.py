from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms.validators import DataRequired

# Formulaire détaillants
class DetaillantForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    URL = StringField('URL', validators=[DataRequired()])
    code_postal = StringField('code_postal', validators=[DataRequired()])
    logo = FileField('logo')