from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify

Tybe_of_persone=(
     ('Male','male'),
     ('Female','female'),
)
Doctor_In=(
     ('Obesity and endoscopic surgery','Obesity and endoscopic surgery'),
     ('Heart and blood vessels','Heart and blood vessels'),
     ('Blood diseases','Blood diseases'),
     ('Bones','Bones'),
     ('Gynecology and Obstetrics','Gynecology and Obstetrics'),
     ('Newborn babies','Newborn babies'),
     ('teeth','teeth'),
     ('Newborn babies','Newborn babies'),
     ('Nose, Ear and Throat','Nose, Ear and Throat'),
     ('Tumors','Tumors'),
)
class Profile(models.Model):
    user=models.OneToOneField( User,verbose_name=_("user"), on_delete=models.CASCADE)
    name=models.CharField(_("name"), max_length=50)
    subtitle=models.CharField(_("about you"), max_length=1000,null=True,blank=True)
    infor=models.TextField(_("information about you"), max_length=500,null=True,blank=True)
    adrees=models.CharField(_("adress"), max_length=50)
    adrees_detail=models.CharField(_("adrees_detail"), max_length=80)
    number_phone=models.IntegerField(_("number_phone"),null=True,blank=True)
    working_hour=models.CharField(_("working houre"), max_length=100)
    working_time=models.CharField(_("working time"), max_length=100,null=True,blank=True)
    doctor_in=models.CharField(_("doctor_in?"),choices=Doctor_In, max_length=50,null=True,blank=True)
    price=models.IntegerField(_("Detection price:"),null=True,blank=True)
    facebook=models.CharField(_("facebook"), max_length=50,null=True,blank=True)
    google=models.CharField(_("google"), max_length=50,null=True,blank=True)
    twitter=models.CharField(_("twitter"), max_length=50,null=True,blank=True)
    img=models.ImageField(_("youre picture:"),null=True,blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    slug=models.SlugField(_("slug"),null=True,blank=True)
    tybe=models.CharField(_("tybe:"),choices=Tybe_of_persone, max_length=50,null=True,blank=True)
    img_medical_one=models.ImageField(_("youre picture medical one:"),null=True,blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    img_medical_two=models.ImageField(_("youre picture medical two:"),null=True,blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    img_medical_three=models.ImageField(_("youre picture medical three:"),null=True,blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    
    class Meta:
        verbose_name = _("Profil")
        verbose_name_plural = _("Profile")




    def __str__(self):
            return' %s '%( self.user.username)
        





    def creat_profile(sender,**kwargs):
        if kwargs ['created']:
            Profile.objects.create(user=kwargs["instance"])

    post_save.connect(creat_profile,sender=User)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)



class LOGIN(models.Model):
    
    name1=models.CharField( max_length=100)
    number=models.IntegerField()
    doctor=models.CharField( max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    data=models.DateField()
    
class Comments(models.Model):
     Name=models.CharField(_("name"), max_length=100)
     email=models.CharField(_("email"), max_length=100)
     comment=models.CharField(_("comment"), max_length=500)
    
     
     def __str__(self):
          return f"{self.Name}the write comment:-{ self.comment}"
     
class Callus(models.Model):
    firstname=models.CharField( max_length=50)
    lastname=models.CharField( max_length=50)
    youremail=models.CharField( max_length=100)
    numberphone=models.IntegerField()
    masseg=models.TextField( max_length=500)
    def __str__(self) :
        return self.firstname
    
class Blogs(models.Model):
    img=models.ImageField( upload_to='photo')
    name=models.CharField( max_length=50)
    title=models.CharField( max_length=50)
    discribtion=models.CharField( max_length=500)
    date=models.DateField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _("blogs")
        verbose_name_plural = _("blogs")




class ExpertDoctor(models.Model):
    img=models.ImageField(_("img"), upload_to='photo', height_field=None, width_field=None, max_length=None)
    nameDoctor=models.CharField(max_length=40)
    aboutDoctor=models.CharField(_("about you"), max_length=50)
    adressDoctor=models.CharField(_("adress"), max_length=50)
    ExpertIn=models.CharField(_("doctor_in?"),choices=Doctor_In, max_length=50,null=True,blank=True)
    facebook=models.CharField(_("facebook"), max_length=50,null=True,blank=True)
    google=models.CharField(_("google"), max_length=50,null=True,blank=True)
    twitter=models.CharField(_("twitter"), max_length=50,null=True,blank=True)
    price=models.IntegerField()