#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sqla
from sqlalchemy_i18n import (
    make_translatable,
    translation_base,
    Translatable,
)
from sqlalchemy.ext.declarative import declarative_base
from flask import g

make_translatable( options = {'locales': ['en' , 'fr' , 'es']})
Base = declarative_base()

class Post(Translatable,Base):
    __tablename__ = 'post'
    __translatable__ = {
          'locales': ['en' , 'fr', 'es']
         ,'dynamic_source_locale': True
    }

    locale = 'en'  # this defines the default locale

    id = sqla.Column(sqla.Integer, primary_key=True)
    post_date = sqla.Column(sqla.DateTime)
    last_modified_date = sqla.Column(sqla.DateTime)
    draft = sqla.Column(sqla.SmallInteger, default=0)

    def get_locale(self):
        return self.locale

class PostTranslation(translation_base(Post)):
    __tablename__ = 'post_translation'

    title = sqla.Column(sqla.String(256 ))
    text = sqla.Column(sqla.Text())
