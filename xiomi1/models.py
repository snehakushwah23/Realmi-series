from django.db import models

# Create your models here.
class nav(models.Model):
    logo_img = models.ImageField(upload_to='images')
    li1 = models.CharField(max_length=30)
    li2 = models.CharField(max_length=30)
    li3 = models.CharField(max_length=30)
    li4 = models.CharField(max_length=30)
    li5 = models.CharField(max_length=30)
    li6 = models.CharField(max_length=30)
    li7 = models.CharField(max_length=30)
    li8 = models.CharField(max_length=30)

class section1(models.Model):
    li9 = models.CharField(max_length=30)
    li10 = models.CharField(max_length=30)
    li11 = models.CharField(max_length=30)
    heading = models.CharField(max_length=30)
    li12 = models.CharField(max_length=30)
    li13 = models.CharField(max_length=30)
    li14 = models.CharField(max_length=30)

class section2(models.Model):
    box1_H1 = models.CharField(max_length=30)
    box1_img= models.ImageField(upload_to='images')

    box2_h1 = models.CharField(max_length=30)
    box2_img= models.ImageField(upload_to='images')

    box3_h1 = models.CharField(max_length=30)
    box3_img = models.ImageField(upload_to='images')

    box4_h1 = models.CharField(max_length=30)
    box4_img = models.ImageField(upload_to='images')

    box5_h1 = models.CharField(max_length=30)
    box5_img = models.ImageField(upload_to='images')

    box6_h1 = models.CharField(max_length=30)
    box6_img = models.ImageField(upload_to='images')

    box7_h1 = models.CharField(max_length=30)
    box7_img = models.ImageField(upload_to='images')

    box8_h1 = models.CharField(max_length=30)
    box8_img = models.ImageField(upload_to='images')

    box9_h1 = models.CharField(max_length=30)
    box9_img = models.ImageField(upload_to='images')

    box10_h1 = models.CharField(max_length=30)
    box10_img = models.ImageField(upload_to='images')

    box11_h1 = models.CharField(max_length=30)
    box11_img = models.ImageField(upload_to='images')

    box12_h1 = models.CharField(max_length=30)
    box12_img = models.ImageField(upload_to='images')

    box13_h1 = models.CharField(max_length=30)
    box13_img = models.ImageField(upload_to='images')

    box14_h1 = models.CharField(max_length=30)
    box14_img = models.ImageField(upload_to='images')

    box15_h1 = models.CharField(max_length=30)
    box15_img = models.ImageField(upload_to='images')

    box16_h1 = models.CharField(max_length=30)
    box16_img = models.ImageField(upload_to='images')

    box17_h1 = models.CharField(max_length=30)
    box17_img = models.ImageField(upload_to='images')

    box18_h1 = models.CharField(max_length=30)
    box18_img = models.ImageField(upload_to='images')

    box19_h1 = models.CharField(max_length=30)
    box19_img = models.ImageField(upload_to='images')

    box19_h1 = models.CharField(max_length=30)
    box19_img = models.ImageField(upload_to='images')

    box20_h1 = models.CharField(max_length=30)
    box20_img = models.ImageField(upload_to='images')

    box21_h1 = models.CharField(max_length=30)
    box21_img = models.ImageField(upload_to='images')

    box22_h1 = models.CharField(max_length=30)
    box22_img = models.ImageField(upload_to='images')

    box23_h1 = models.CharField(max_length=30)
    box23_img = models.ImageField(upload_to='images')

    box24_h1 = models.CharField(max_length=30)
    box24_img = models.ImageField(upload_to='images')

class Mobile(models.Model): 
    mob_1 = models.ImageField(upload_to='images')
    mob_2 = models.ImageField(upload_to='images')
    mob_3 = models.ImageField(upload_to='images')
    mob_4 = models.ImageField(upload_to='images')
    mob_5 = models.ImageField(upload_to='images')

class RedmiSeries(models.Model):
    red_1 = models.ImageField(upload_to='images')
    red_2 = models.ImageField(upload_to='images')
    red_3 = models.ImageField(upload_to='images')
    red_4 = models.ImageField(upload_to='images')
    red_5 = models.ImageField(upload_to='images')

class poco(models.Model):
    poco_1 = models.ImageField(upload_to='images')
    poco_2 = models.ImageField(upload_to='images')
    poco_3 = models.ImageField(upload_to='images')
    poco_4 = models.ImageField(upload_to='images')
    poco_5 = models.ImageField(upload_to='images')

class tablets(models.Model):
    tablet_1 = models.ImageField(upload_to='images')
    tablet_2 = models.ImageField(upload_to='images')
    tablet_3 = models.ImageField(upload_to='images')
    tablet_4 = models.ImageField(upload_to='images')
    tablet_5 = models.ImageField(upload_to='images')

class lapSeries(models.Model):
   lapSeries1 = models.ImageField(upload_to='images')
   lapSeries2 = models.ImageField(upload_to='images')
   lapSeries3 = models.ImageField(upload_to='images')
   lapSeries4 = models.ImageField(upload_to='images')
   lapSeries5 = models.ImageField(upload_to='images')

class watches(models.Model):
    watches1 = models.ImageField(upload_to='images')
    watches_h1 = models.CharField(max_length=30)
    watches2 = models.ImageField(upload_to='images')
    watches_h2 = models.CharField(max_length=30)
    watches3 = models.ImageField(upload_to='images')
    watches_h3 = models.CharField(max_length=30)
    watches4 = models.ImageField(upload_to='images')
    watches_h4 = models.CharField(max_length=30)
    watches5 = models.ImageField(upload_to='images')
    watches_h5 = models.CharField(max_length=30)
    
class bands(models.Model):
    bands1 = models.ImageField(upload_to='images')
    bands_h1 = models.CharField(max_length=30)
    bands2 = models.ImageField(upload_to='images')
    bands_h2 = models.CharField(max_length=30)
    bands3 = models.ImageField(upload_to='images')
    bands_h3 = models.CharField(max_length=30)
    bands4 = models.ImageField(upload_to='images')
    bands_h4 = models.CharField(max_length=30)
    bands5 = models.ImageField(upload_to='images')
    bands_h15 = models.CharField(max_length=30)

class Earphones(models.Model):
    Earphn1  = models.ImageField(upload_to='images')
    Earphn_h1 = models.CharField(max_length=30)
    Earphn2  = models.ImageField(upload_to='images')
    Earphn_h2 = models.CharField(max_length=30)
    Earphn3  = models.ImageField(upload_to='images')
    Earphn_h3 = models.CharField(max_length=30)
    Earphn4  = models.ImageField(upload_to='images')
    Earphn_h4 = models.CharField(max_length=30)
    Earphn5  = models.ImageField(upload_to='images')
    Earphn_h5 = models.CharField(max_length=30)


class pocoF(models.Model):
    pocoF1  = models.ImageField(upload_to='images')
    pocoF1_h1 = models.CharField(max_length=30)
    pocoF2  = models.ImageField(upload_to='images')
    pocoF1_h2 = models.CharField(max_length=30)
    pocoF3  = models.ImageField(upload_to='images')
    pocoF1_h3 = models.CharField(max_length=30)
    pocoF4  = models.ImageField(upload_to='images')
    pocoF1_h4 = models.CharField(max_length=30)
    pocoF5  = models.ImageField(upload_to='images')
    pocoF1_h5 = models.CharField(max_length=30)

class pocox(models.Model):
    pocox1 = models.ImageField(upload_to='images')
    pocox1_h1 = models.CharField(max_length=30)
    pocox2 = models.ImageField(upload_to='images')
    pocox1_h2 = models.CharField(max_length=30)
    pocox3 = models.ImageField(upload_to='images')
    pocox1_h3 = models.CharField(max_length=30)
    pocox4 = models.ImageField(upload_to='images')
    pocox1_h4 = models.CharField(max_length=30)
    pocox5 = models.ImageField(upload_to='images')
    pocox1_h5 = models.CharField(max_length=30)

class New(models.Model):
    New1 = models.ImageField(upload_to='images')
    New1_h1 = models.CharField(max_length=30)

class picX(models.Model):
    POCOX1 = models.ImageField(upload_to='images')
    POCOX1_h1 = models.CharField(max_length=30)
    POCOX2 = models.ImageField(upload_to='images')
    POCOX1_h2 = models.CharField(max_length=30)
    POCOX3 = models.ImageField(upload_to='images')
    POCOX1_h3 = models.CharField(max_length=30)
    POCOX4 = models.ImageField(upload_to='images')
    POCOX1_h4 = models.CharField(max_length=30)
    POCOX5 = models.ImageField(upload_to='images')
    POCOX1_h5 = models.CharField(max_length=30)

class picM(models.Model):
    POCOM1 = models.ImageField(upload_to='images')
    POCOM1_h1 = models.CharField(max_length=30)
    POCOM2 = models.ImageField(upload_to='images')
    POCOM1_h2 = models.CharField(max_length=30)
    POCOM3 = models.ImageField(upload_to='images')
    POCOM1_h3 = models.CharField(max_length=30)
    POCOM4 = models.ImageField(upload_to='images')
    POCOM1_h4 = models.CharField(max_length=30)

class picS(models.Model):
    picS1 = models.ImageField(upload_to='images')
    picS1_h1 = models.CharField(max_length=30)
    picS2 = models.ImageField(upload_to='images')
    picS1_h2 =models.CharField(max_length=30)
    picS3 = models.ImageField(upload_to='images')
    picS1_h3 = models.CharField(max_length=30)

class SignBackGroundImg(models.Model):
    SignBackGroundImg1 = models.ImageField(upload_to='images')

class sign_inlogoImg(models.Model):
    sign_inlogoImg1 = models.ImageField(upload_to='images')

class sign_upImg(models.Model):
    sign_upBackground_Img = models.ImageField(upload_to='images')
    sign_up_LogoImg = models.ImageField(upload_to='images')


   