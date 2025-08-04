from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_ckeditor import CKEditorField

# Utility function to add Bootstrap classes
def style_fields(fields):
    for field in fields:
        field.render_kw = {"class": "form-control mb-3"}

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Up", render_kw={"class": "btn btn-success w-100"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields([self.email, self.password, self.name])

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In", render_kw={"class": "btn btn-primary w-100"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields([self.email, self.password])

class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post", render_kw={"class": "btn btn-success mt-3 w-100"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields([self.title, self.subtitle, self.img_url])

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment", render_kw={"class": "btn btn-outline-info mt-3"})
