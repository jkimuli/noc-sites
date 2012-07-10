'''
Created on Jul 9, 2012

@author: jkimuli


'''

import math

mbr_lat = -0.61137

mbr_long = 30.65830

kla_lat =  0.31917

kla_long = 32.59010

msk_lat = -0.32053

msk_long = 31.74193

jja_lat = 0.42969

jja_long = 33.20969

mbl_lat = 1.07348

mbl_long = 34.17663

gul_lat = 2.76835

gul_long = 32.30153

hom_lat =  1.42950

hom_long  =  31.35047

fort_lat = 0.66796

fort_long= 30.2887




def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc

