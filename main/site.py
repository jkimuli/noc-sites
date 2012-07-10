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
    
    dis_kla = db.FloatProperty()
    dis_jja = db.FloatProperty()
    dis_msk = db.FloatProperty()
    dis_mbr = db.FloatProperty()
    dis_mbl = db.FloatProperty()
    dis_glu = db.FloatProperty()
    dis_hom = db.FloatProperty()
    dis_fort = db.FloatProperty()
    
 
        
        
        
        
    
    
    
    
