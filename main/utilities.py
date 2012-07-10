'''
Created on May 10, 2012

@author: jkimuli
'''
import cgi
import re
import hmac
import random
import string
import hashlib

SECRET = 'imsosecret'

def escape_html(s):
    return cgi.escape(s, quote=True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_email(email):
    if len(email) > 0:
        return EMAIL_RE.match(email)
    else:
        return True
        
   

def valid_password(password):
    return PASSWORD_RE.match(password)

def compare_pass(password,verify):
    password_valid = valid_password(password)
    verify_valid = valid_password(verify)
    
    if password_valid and verify_valid:
        return (password==verify)
    
def hash_str(s):
    return hmac.new(SECRET,s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

# -----------------
# User Instructions
# 
# Implement the function check_secure_val, which takes a string of the format 
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None 

def check_secure_val(h):
    ###Your code here
    
    val = h.split('|')[0]
    
    if h == make_secure_val(val):
        return val
    
def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# implement the function make_pw_hash(name, pw) that returns a hashed password 
# of the format: 
# HASH(name + pw + salt),salt
# use sha256

def make_pw_hash(name, pw,salt=None):
    ###Your code here
    
    if not salt:
        salt = make_salt()
    
    h = hashlib.sha256(name+pw+salt).hexdigest()
    
    return "%s,%s" % (h,salt)

def valid_pw(name,pw,h):
    salt = h.split(',')[1]
    
    return h == make_pw_hash(name,pw,salt)




if __name__ == '__main__':
    escape_html()