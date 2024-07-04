from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

# Определение класса формы
class SettingsForm(FlaskForm):
    access_key = StringField('Access Key', validators=[DataRequired()])
    speaker = SelectField('Speaker', validators=[DataRequired()],choices=['tatyana_abramova','voicesearch','anton_samokhvalov','ermil'])
    emotion = SelectField('Emotion', validators=[DataRequired()], choices=['good','evil', 'neutral'])
    submit = SubmitField('Submit')