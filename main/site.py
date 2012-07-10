'''
Created on Jul 8, 2012

@author: jkimuli


'''


from google.appengine.ext import db
from main.regions import Region





class Site(db.Model):
    site_id = db.StringProperty(required=True)
    location = db.StringProperty(required=True)
    region = db.ReferenceProperty(Region)
    lat = db.FloatProperty(required=True)
    lng = db.FloatProperty(required=True)
    
    
    #distance parameters to be calculated in a custom model save method
    
    dis_kla = db.IntegerProperty()
    dis_jja = db.IntegerProperty()
    dis_msk = db.IntegerProperty()
    dis_mbr = db.IntegerProperty()
    dis_mbl = db.IntegerProperty()
    dis_glu = db.IntegerProperty()
    dis_hom = db.IntegerProperty()
    dis_fort = db.IntegerProperty()
    
 
        
        
        
        
    
    
    
    
