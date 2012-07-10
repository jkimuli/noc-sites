'''
Created on Jul 8, 2012

@author: jkimuli
'''

from google.appengine.ext import db

class Region(db.Model):
    name = db.StringProperty(required=True)