#!/usr/bin/python3
""" Review Class That Inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Constructor """
    place_id = ""
    user_id = ""
    text = ""
