from tkinter.tix import InputOnly
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')


class CreateBlog(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    content = TextAreaField('Blog Content',validators=[InputRequired()])
    submit = SubmitField('Post')