#!/usr/bin/python3
"""
Defines the city attrib """
from models.base_model import BaseModel


class City(BaseModel):
    """defines city to look for"""
    state_id = ""
    name = ""
