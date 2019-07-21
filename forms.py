from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, InputRequired, Email
from wtforms.fields.html5 import EmailField


class SongForm(FlaskForm):
    song = StringField('Song', validators=[DataRequired()],
                       default='Shape Of You')
    artist = StringField('Artist', validators=[DataRequired()],
                         default='Ed Sheeran')
    choice = RadioField('Has the artist had a billboard hit before this?',
                        validators=[InputRequired()],
                        choices=[
                            ('Yes', 'Yes'),
                            ('No', 'No'),
                            ('Maybe', 'Maybe?')],
                        default='Yes'
                        )
    submit = SubmitField('Predict!')


class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
