#!/usr/bin/python3
""" City Class That Inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class Constructor """
    state_id = ""
    name = ""
