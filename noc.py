import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
import jinja2
import os
from main.users import  User
from main.site import  Site
from main.regions import Region
from main.utilities import escape_html,valid_username,valid_email,valid_password,compare_pass
from main.utilities import make_secure_val,check_secure_val,make_pw_hash,valid_pw
from main.distance import distance_on_unit_sphere,kla_lat,kla_long,msk_lat,msk_long,mbr_lat,mbr_long
from main.distance import jja_lat,jja_long,fort_lat,fort_long,hom_lat,hom_long,mbl_lat,mbl_long,gul_lat,gul_long


template_dir = os.path.join(os.path.dirname(__file__),'templates')
env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)
        
    def render_str(self,template,**params):
        t = env.get_template(template)
        return t.render(params)
    
    def render(self,template,**kw):
        self.write(self.render_str(template,**kw))
        
    def set_secure_cookie(self,name,val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header('Set-Cookie','%s=%s;Path=/' %(name,cookie_val))
        
    def read_secure_cookie(self,name):
        cookie_val = self.request.cookies.get(name)
        
        return cookie_val and check_secure_val(cookie_val)
    
    def login(self,user):
        self.set_secure_cookie('user_id', str(user.key().id()))
        
    def logout(self):
        #unset cookie
        
        self.response.headers.add_header('Set-Cookie','user_id=;Path=/')
        
    def initialize(self,*a,**kw):
        webapp2.RequestHandler.initialize(self,*a,**kw)
        uid = self.read_secure_cookie('user_id')
        
        #get current user
        
        self.user = uid and User.by_id(int(uid))
        
class MainPage(Handler):
    def get(self):
        self.render('index.html')
        
    def post(self):
        site = self.request.get('site')
        

class SignUpHandler(Handler):
    def get(self):
        self.render('signup_form.html')
        
       
    def post(self):
        self.username = escape_html(self.request.get('username'))
        self.email = escape_html(self.request.get('email'))
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        
        username_error=""
        verify_error=""
        password_error=""
        email_error = ""
        
        
        #Form Validation
       
            
        #test password and verify password equality
            
        password_equal = compare_pass(self.password,self.verify)
        
        #make sure the user doen't exist
        if  valid_username(self.username) and password_equal and valid_email(self.email):
            user = User.by_name(self.username)
                   
                   
            if user==None:
                u= User.register(self.username,self.password, self.email)
                u.put()
            
                self.login(u)
                
                self.redirect('/welcome')
            
            else:
                username_error = "User already exists"
                self.render('signup_form.html',username=self.username,email=self.email,username_error=username_error,password_error=password_error,verify_error=verify_error,email_error=email_error)
                
                      
                       
            
        else:
            if not valid_username(self.username):
                username_error = "This is an invalid username"
                
                
            if not valid_password(self.password) :
                password_error = "This is an invalid password"
                
                
                
            if valid_password(self.password) and not password_equal:
                verify_error = "Your passwords don't match"
                
                
            if  not valid_email(self.email):
                email_error = "invalid email"
                
            
                 
            self.render('signup_form.html',username=self.username,email=self.email,username_error=username_error,password_error=password_error,verify_error=verify_error,email_error=email_error)
                
      
                    
                
class WelcomeHandler(Handler):
    def get(self):
        if self.user:
            self.render('welcome.html',username = self.user.username)
        else:
            self.redirect('/signup')
            
class LoginHandler(Handler):
    def get(self):
        self.render('login-form.html')
        
    def post(self):
        username = escape_html(self.request.get('username'))
        password = escape_html(self.request.get('password'))
        
        error_msg = ""
        
        u = User.login(username,password)
        
        if u:
            self.login(u)
            #refer = self.request.get('referer')
            #val = self.request.cookies.get('page')
            self.redirect('/post_region')
        else:
            msg = "Invalid login"
            self.render('login-form.html',error_msg=msg)
        
        
class LogoutHandler(Handler):
    def get(self):
        self.logout()
        self.redirect('/')
        
class RegionHandler(Handler):
    def get(self):
        if not self.user:
            self.redirect('/login')
        self.render('region_form.html')
    
    def post(self):
        name = self.request.get('name')
        
        if name:
            region = Region(name=name)
            
            region.put()
            
            #redirect to main_page
            
            self.redirect('/')
        else:
            error = "Unable to save the region"
            self.render('region_form.html',error=error)
            

class SiteHandler(Handler):
    def get(self):
        if not self.user:
            self.redirect('/login')
            
        self.render('site_form.html')
        
    def post(self):
        site_id = self.request.get('site_id')
        location = self.request.get('location')
        lat = float(self.request.get('latitude'))
        lng = float(self.request.get('longitude'))
        region = self.request.get('region')
        
        if site_id and location and lat and lng and region:
            #try to save site into database
            
            #save region
            
            region = Region(name=region)
            region.put()
            
            dis_kla = distance_on_unit_sphere(lat,lng,kla_lat,kla_long) * 6373
            dis_jja = distance_on_unit_sphere(lat,lng,jja_lat,jja_long) * 6373
            dis_msk = distance_on_unit_sphere(lat,lng,msk_lat,msk_long) * 6373
            dis_mbr= distance_on_unit_sphere(lat,lng,mbr_lat,mbr_long) * 6373
            dis_mbl = distance_on_unit_sphere(lat,lng,mbl_lat,mbl_long) * 6373
            dis_glu = distance_on_unit_sphere(lat,lng,gul_lat,gul_long) * 6373
            dis_hom = distance_on_unit_sphere(lat,lng,hom_lat,hom_long) * 6373
            dis_fort = distance_on_unit_sphere(lat,lng,fort_lat,fort_long) * 6373
                
            site = Site(site_id=site_id,
                        location=location,
                        lat=lat,
                        lng=lng,
                        region=region,
                        dis_kla=dis_kla,
                        dis_jja=dis_jja,
                        dis_msk=dis_msk,
                        dis_mbr=dis_mbr,
                        dis_mbl=dis_mbl,
                        dis_glu=dis_glu,
                        dis_hom=dis_hom,
                        dis_fort=dis_fort,
                        )
            
            site.put()
            
            
            
            
        else:
            error = "Unable to save the site"
            self.render('site_form.html',error=error)
            
class SearchHandler(Handler):
    def post(self):
        id = self.request.get('site')
        
            

application = webapp2.WSGIApplication([('/', MainPage),('/login',LoginHandler),('/signup',SignUpHandler),('/logout',LogoutHandler),('/post_region',RegionHandler),('/post_site',SiteHandler),('/welcome',WelcomeHandler),('/search',SearchHandler)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
