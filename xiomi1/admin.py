from django.contrib import admin

# Register your models here.
from xiomi1.models import nav
class navAdmin(admin.ModelAdmin):
    list_display = ('logo_img','li1','li2','li3','li4','li5','li6','li7','li8')
admin.site.register(nav,navAdmin)    

from xiomi1.models import section1
class section1Admin(admin.ModelAdmin):
    list_display=('li9','li10','li11' , 'heading' , 'li12' , 'li13' , 'li14')
admin.site.register(section1,section1Admin)

from xiomi1.models import section2
class section2Admin(admin.ModelAdmin):
    list_display = ('box1_H1','box1_img' , 'box2_h1','box2_img' , 'box3_h1','box3_img' , 'box4_h1','box4_img','box5_h1','box5_img' , 'box6_h1','box6_img' , 'box7_h1','box7_img' , 'box8_h1','box8_img' , 'box9_h1','box9_img' , 'box10_h1','box10_img' , 'box11_h1','box11_img' , 'box12_h1','box12_img' , 'box13_h1','box13_img' , 'box14_h1','box14_img' , 'box15_h1','box15_img' , 'box16_h1','box16_img' , 'box17_h1','box17_img' , 'box18_h1','box18_img' , 'box19_h1','box19_img' , 'box20_h1','box20_img' , 'box21_h1','box21_img' , 'box22_h1','box22_img' , 'box23_h1','box23_img' , 'box24_h1','box24_img')
admin.site.register(section2,section2Admin)    

from xiomi1.models import Mobile
class MobileAdmin(admin.ModelAdmin):
    list_display=('mob_1' , 'mob_2' , 'mob_3' , 'mob_4' , 'mob_5')
admin.site.register(Mobile,MobileAdmin)    

from xiomi1.models import RedmiSeries
class RedmiSeriesAdmin(admin.ModelAdmin):
    list_display=('red_1' , 'red_2' , 'red_3' , 'red_4' ,'red_5')
admin.site.register(RedmiSeries,RedmiSeriesAdmin)    

from xiomi1.models import poco
class pocoAdmin(admin.ModelAdmin):
    list_display=('poco_1','poco_2','poco_3','poco_4','poco_5')
admin.site.register(poco,pocoAdmin)    

from xiomi1.models import tablets
class tabletsAdmin(admin.ModelAdmin):
    list_display=('tablet_1' , 'tablet_2' ,'tablet_3' ,'tablet_4' , 'tablet_5')
admin.site.register(tablets,tabletsAdmin)

from xiomi1.models import lapSeries
class lapSeriesAdmin(admin.ModelAdmin):
    list_display=('lapSeries1', 'lapSeries2' ,'lapSeries3' ,'lapSeries4' ,'lapSeries5')
admin.site.register(lapSeries,lapSeriesAdmin)    

from xiomi1.models import watches
class watchesAdmin(admin.ModelAdmin):
    list_display=('watches1','watches_h1','watches2','watches_h2','watches3','watches_h3','watches4','watches_h4','watches5','watches_h5')
admin.site.register(watches,watchesAdmin)    

from xiomi1.models import bands
class bandsAdmin(admin.ModelAdmin):
    list_display=('bands1','bands_h1','bands2','bands_h2','bands3','bands_h3','bands4','bands_h4','bands5','bands_h15')
admin.site.register(bands,bandsAdmin)

from xiomi1.models import Earphones
class EarphonesAdmin(admin.ModelAdmin):
    list_display=('Earphn1','Earphn_h1','Earphn2','Earphn_h2','Earphn3','Earphn_h3','Earphn4','Earphn_h4','Earphn5','Earphn_h5')
admin.site.register(Earphones,EarphonesAdmin)

from xiomi1.models import pocoF
class pocoF_Admin(admin.ModelAdmin):
    list_display=('pocoF1','pocoF1_h1','pocoF2','pocoF1_h2','pocoF3','pocoF1_h3','pocoF4','pocoF1_h4','pocoF5','pocoF1_h5')
admin.site.register(pocoF,pocoF_Admin)

from xiomi1.models import picX
class picX_Admin(admin.ModelAdmin):
    list_display=('POCOX1','POCOX1_h1','POCOX2','POCOX1_h2','POCOX2','POCOX1_h2','POCOX4','POCOX1_h4','POCOX5','POCOX1_h5')
admin.site.register(picX,picX_Admin)    

from xiomi1.models import picM
class picM_Admin(admin.ModelAdmin):
    list_display=('POCOM1','POCOM1_h1','POCOM2','POCOM1_h2','POCOM3','POCOM1_h3','POCOM4','POCOM1_h4')
admin.site.register(picM,picM_Admin)    

from xiomi1.models import picS
class picS_Admin(admin.ModelAdmin):
    list_display=('picS1','picS1_h1','picS2','picS1_h2','picS3','picS1_h3')
admin.site.register(picS,picS_Admin)    

from xiomi1.models import SignBackGroundImg
class SignBackGroundImg_Admin(admin.ModelAdmin):
    list_display=('SignBackGroundImg1',)
admin.site.register(SignBackGroundImg,SignBackGroundImg_Admin)    

from xiomi1.models import sign_inlogoImg
class sign_inlogoImg_Admin(admin.ModelAdmin):
    list_display=('sign_inlogoImg1',)
admin.site.register(sign_inlogoImg,sign_inlogoImg_Admin)    

from xiomi1.models import sign_upImg
class sign_upImgAdmin(admin.ModelAdmin):
    list_display=('sign_upBackground_Img','sign_up_LogoImg')
admin.site.register(sign_upImg,sign_upImgAdmin)    
