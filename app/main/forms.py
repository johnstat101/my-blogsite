from tkinter.tix import InputOnly
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')


class CreateBlog(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    content = TextAreaField('Blog Content',validators=[InputRequired()])
    submit = SubmitField('Post')