from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class SongForm(FlaskForm):
    song = StringField('Song', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    choice = RadioField('Has the artist had a billboard hit before this?',
                        choices=[
                            ('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe?')])
    submit = SubmitField('Predict!')
