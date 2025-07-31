from django .shortcuts import render
from xiomi1.models import nav
from xiomi1.models import section1
from xiomi1.models import section2
from xiomi1.models import Mobile
from xiomi1.models import RedmiSeries
from xiomi1.models import poco
from xiomi1.models import tablets
from xiomi1.models import lapSeries
from xiomi1.models import watches
from xiomi1.models import bands
from xiomi1.models import Earphones
from xiomi1.models import pocoF
from xiomi1.models import picX
from xiomi1.models import picM
from xiomi1.models import picS
from xiomi1.models import SignBackGroundImg
from xiomi1.models import sign_inlogoImg
from xiomi1.models import sign_upImg

def home(request):
    data=nav.objects.all()
    sec1=section1.objects.all()
    sec2=section2.objects.all()
    mobimg=Mobile.objects.all()
    redmiImg=RedmiSeries.objects.all()
    poc_o=poco.objects.all()
    tablet=tablets.objects.all()
    lapt=lapSeries.objects.all()
    watch=watches.objects.all()
    band=bands.objects.all()
    Ear_ph=Earphones.objects.all()
    poco_F=pocoF.objects.all()
    poco_X=picX.objects.all()
    poco_M=picM.objects.all()
    poco_C=picS.objects.all()

    record1={
        'nav':data,
        'section1':sec1,
        'section2':sec2,
        'secMobile':mobimg,
        'redSeries':redmiImg,
        'pocoo':poc_o,
        'table_t':tablet,
        'l_apto':lapt,
        'Watc_h':watch,
        'ba_nd':band,
        'Ear_p':Ear_ph,
        'poc_o_F' :poco_F,
        'poc_o_X':poco_X,
        'poc_0_M':poco_M,
        'poc_o_C':poco_C
    }
    return render(request,'index.html',record1)   

def sign(request):

    SignBackGround_Img=SignBackGroundImg.objects.all()
    sign_in_logoImg=sign_inlogoImg.objects.all()

    records1={
        'Sign_BackGround_Img':SignBackGround_Img,
        'sign_in_logo_Img':sign_in_logoImg
    }
    
    return render(request,'sing_in.html',records1)

def sign_up(request):
    Sign_upImg=sign_upImg.objects.all()

    records2={
        'Sign_up_Img':Sign_upImg
    }
    return render(request,'sign_Up.html',records2)



     

