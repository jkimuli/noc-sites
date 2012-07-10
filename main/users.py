

'''
Created on May 31, 2012

@author: jkimuli Julius Kimuli
'''

from google.appengine.ext import db
from utilities import make_pw_hash,valid_pw

class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def by_id(cls,uid):
        return User.get_by_id(uid)
    
    @classmethod
    def by_name(cls,name):
        u=User.all().filter('username',name).get()
        return u
    
    @classmethod
    def register(cls,name,pw,email=None):
        pw_hash = make_pw_hash(name,pw)
        
        return User(username=name,password=pw_hash,email=email)
    
    @classmethod
    def login(cls,name,pw):
        u = cls.by_name(name)
        if u and valid_pw(name,pw,u.password):
            return u
        