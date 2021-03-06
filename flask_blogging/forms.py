from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from flask.ext.babel import gettext


class BlogEditor(Form):
    title = StringField( "title" , validators=[DataRequired()])
    text = TextAreaField( "text" , validators=[DataRequired()])
    tags = StringField( "tags" , validators=[DataRequired()])
    draft = BooleanField("draft" , default=False)
    submit = SubmitField(gettext(u"submit"))
