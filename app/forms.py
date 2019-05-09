from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    name = TextField('Username', validators = [DataRequired(),
        Length(min=6, max=16)])
    password = PasswordField('Password', validators = [DataRequired(),
        Length(min=6, max=16)])

#A single Form for question and answers does not allow for >2 questions
#Could use seperate Choice form as below but more difficult to create new poll

class NewPollForm(FlaskForm):
    """ For creating a Poll from /admin """
    question = TextField('Question', validators = [DataRequired(),
        Length(max=200)])
    first_choice =TextField('First choice', validators = [DataRequired(),
        Length(max=200)])
    second_choice =TextField('Second choice', validators = [DataRequired(),
        Length(max=200)])


class PollForm(FlaskForm):
    """ For editing a Poll from /admin """
    question = TextField('Question', validators = [DataRequired(),
        Length(max=200)])


class ChoiceForm(FlaskForm):
    """ For editing a Poll from /admin """
    choice =TextField('Question', validators = [DataRequired(),
        Length(max=200)])

class ChoicesForm(FlaskForm):
    """ For editing a Poll from /admin """
    choice_one =TextField('First question', validators = [DataRequired(),
        Length(max=200)])
    choice_two =TextField('Second question', validators = [DataRequired(),
        Length(max=200)])
