let navbar=document.querySelector('.navbar')
//contact
let contact=document.querySelector('.contact')
let cont=document.getElementById('cont')
cont.addEventListener('mouseenter',()=>{
    contact.style.display='block'
    search.style.display='none'
})
contact.addEventListener('mouseleave',()=>{
    contact.style.display='none'
})


//li1
let li1=document.getElementById('li1')
let mobile=document.querySelector('.mobile')
let overlay=document.querySelector('.overlay')

//li2
let li2=document.getElementById('li2')
let Wearables=document.querySelector('.Wearables')

//li3
let li3=document.getElementById('li3')
let smart=document.querySelector('.smart')

//li4
let li4=document.getElementById('li4')
let life_Style=document.querySelector('.life_Style')

//li5
let li5=document.getElementById('li5')
let POCO= document.querySelector('.POCO')

//li6
let li6=document.getElementById('li6')

//search
let search=document.querySelector('.search')
let seaa=document.getElementById('seaa')
seaa.addEventListener('mouseenter',()=>{
    search.style.display='block'
    contact.style.display='none'
    overlay.style.display='block'
})
search.addEventListener('mouseleave',()=>{
    search.style.display='none'
    overlay.style.display='none'
})


//block - 1
li1.addEventListener('mouseenter',()=>{
    mobile.style.display='block'
    overlay.style.display='block'
    Wearables.style.display='none'
    POCO.style.display='none'
    smart.style.display='none'
    life_Style.style.display='none'
    li1.style.color= '#FF6900'
    li1.style.textDecorationLine='underline'
    navbar.style.boxShadow='none'
    li2.style.color= 'black'
    li2.style.textDecorationLine='none'
    li5.style.color= 'black'
    li5.style.textDecorationLine='none'
    li4.style.color= 'black'
    li4.style.textDecorationLine='none'
    li3.style.color= 'black'
    li3.style.textDecorationLine='none'
})
mobile.addEventListener('mouseleave',()=>{
    mobile.style.display='none'
    overlay.style.display='none'
    navbar.style.boxShadow=' 0px 10px 10px 1px #F7F7F7'
    li1.style.color= 'black'
    li1.style.textDecorationLine='none'
})

//block - 2
li2.addEventListener('mouseenter',()=>{
    Wearables.style.display='block'
    overlay.style.display='block'
    mobile.style.display='none'
    POCO.style.display='none'
    smart.style.display='none'
    life_Style.style.display='none'
    li2.style.color='#FF6900'
    li2.style.textDecorationLine='underline'
    li1.style.color= 'black'
    li1.style.textDecorationLine='none'
    li5.style.color= 'black'
    li5.style.textDecorationLine='none'
    li4.style.color= 'black'
    li4.style.textDecorationLine='none'
    li3.style.color= 'black'
    li3.style.textDecorationLine='none'
    navbar.style.boxShadow='none'
})
Wearables.addEventListener('mouseleave',()=>{
    Wearables.style.display='none'
    overlay.style.display='none'
    navbar.style.boxShadow=' 0px 10px 10px 1px #F7F7F7'
    li2.style.color= 'black'
    li2.style.textDecorationLine='none'
})

//block - 3
li3.addEventListener('mouseenter',()=>{
    smart.style.display='block'
    overlay.style.display='block'
    mobile.style.display='none'
    Wearables.style.display='none'
    POCO.style.display='none'
    life_Style.style.display='none'
    li3.style.color= '#FF6900'
    li3.style.textDecorationLine='underline'
    li5.style.color= 'black'
    li5.style.textDecorationLine='none'
    li1.style.color= 'black'
    li1.style.textDecorationLine='none'
    li2.style.color= 'black'
    li2.style.textDecorationLine='none'
    li4.style.color= 'black'
    li4.style.textDecorationLine='none'
    navbar.style.boxShadow='none'
})
smart.addEventListener('mouseleave',()=>{
    smart.style.display='none'
    overlay.style.display='none'
    navbar.style.boxShadow=' 0px 10px 10px 1px #F7F7F7'
    li3.style.color= 'black'
    li3.style.textDecorationLine='none'
})
//block4
li4.addEventListener('mouseenter',()=>{
    life_Style.style.display='block'
    overlay.style.display='block'
    mobile.style.display='none'
    Wearables.style.display='none'
    POCO.style.display='none'
    smart.style.display='none'
    li4.style.color= '#FF6900'
    li4.style.textDecorationLine='underline'
    li1.style.color= 'black'
    li1.style.textDecorationLine='none'
    li2.style.color= 'black'
    li2.style.textDecorationLine='none'
    li3.style.color= 'black'
    li3.style.textDecorationLine='none'
    li5.style.color= 'black'
    li5.style.textDecorationLine='none'
    navbar.style.boxShadow='none'
})
life_Style.addEventListener('mouseleave',()=>{
    life_Style.style.display='none'
    overlay.style.display='none'
    navbar.style.boxShadow=' 0px 10px 10px 1px #F7F7F7'
    li4.style.color= 'black'
    li4.style.textDecorationLine='none'
})
//block5
li5.addEventListener('mouseenter',()=>{
    POCO.style.display='block'
    overlay.style.display='block'
    mobile.style.display='none'
    Wearables.style.display='none'
    life_Style.style.display='none'
    li5.style.color= '#FF6900'
    li5.style.textDecorationLine='underline'
    navbar.style.boxShadow='none'
    li2.style.color= 'black'
    li2.style.textDecorationLine='none'
    li3.style.color= 'black'
    li3.style.textDecorationLine='none'
    li1.style.color= 'black'
    li1.style.textDecorationLine='none'
    li4.style.color= 'black'
    li4.style.textDecorationLine='none'

})
POCO.addEventListener('mouseleave',()=>{
    POCO.style.display='none'
    overlay.style.display='none'
    navbar.style.boxShadow=' 0px 10px 10px 1px #F7F7F7'
    li5.style.color= 'black'
    li5.style.textDecorationLine='none'
})
li6.addEventListener('mouseenter',()=>{
    POCO.style.display='none'
    overlay.style.display='none'
    navbar.style.boxShadow=' 0px 10px 10px 1px #F7F7F7'
    li5.style.color= 'black'
    li5.style.textDecorationLine='none'
})

//block - 1
let imgblockXiomi=document.querySelector('.imgblockXiomi')
let xio=document.querySelector('.xio')

let imgblockREDMI_Series=document.querySelector('.imgblockREDMI_Series')
let red = document.querySelector('.red')

let imgblockPOCO_Series = document.querySelector('.imgblockPOCO_Series')
let poco = document.querySelector('.poco')

let imgblockTABLETS = document.querySelector('.imgblockTABLETS')
let table = document.querySelector('.table')

let imgblockLaptop = document.querySelector('.imgblockLaptop')
let laptop = document.querySelector('.laptop')

xio.addEventListener('mouseenter',()=>{
    imgblockXiomi.style.display='block'
    imgblockREDMI_Series.style.display='none'
    imgblockPOCO_Series.style.display='none'
    imgblockTABLETS.style.display='none'
    imgblockLaptop.style.display='none'
    xio.style.color= '#FF6900'
    xio.style.textDecorationLine='underline'
    red.style.color= '#898989'
    red.style.textDecorationLine='none'
    table.style.color= 'black'
    table.style.textDecorationLine ='none'
})

red.addEventListener('mouseenter',()=>{
    imgblockREDMI_Series.style.display='block'
    imgblockXiomi.style.display='none'
    imgblockPOCO_Series.style.display='none'
    imgblockTABLETS.style.display='none'
    imgblockLaptop.style.display='none'
    red.style.color= '#FF6900'
    red.style.textDecorationLine='underline'
    xio.style.color= '#898989'
    xio.style.textDecorationLine='none'
    table.style.color= 'black'
    table.style.textDecorationLine='none'
    poco.style.color= '#898989'
    poco.style.textDecorationLine='none'
    laptop.style.color= 'black'
    laptop.style.textDecorationLine='none'
})
poco.addEventListener('mouseenter',()=>{
    imgblockPOCO_Series.style.display='block'
    imgblockREDMI_Series.style.display='none'
    imgblockXiomi.style.display='none'
    imgblockTABLETS.style.display='none'
    imgblockLaptop.style.display='none'
    poco.style.color= '#FF6900'
    poco.style.textDecorationLine='underline'
    red.style.color= '#898989'
    red.style.textDecorationLine='none'
    xio.style.color= '#898989'
    xio.style.textDecorationLine='none'
    table.style.color= 'black'
    table.style.textDecorationLine='none'
    laptop.style.color= 'black'
    laptop.style.textDecorationLine='none'
})
table.addEventListener('mouseenter',()=>{
    imgblockTABLETS.style.display='block'
    imgblockPOCO_Series.style.display='none'
    imgblockREDMI_Series.style.display='none'
    imgblockXiomi.style.display='none'
    imgblockLaptop.style.display='none'
    table.style.color= '#FF6900'
    table.style.textDecorationLine='underline'
    poco.style.color= '#898989'
    poco.style.textDecorationLine='none'
    xio.style.color= '#898989'
    xio.style.textDecorationLine='none'
    laptop.style.color= 'black'
    laptop.style.textDecorationLine='none'
    red.style.color= '#898989'
    red.style.textDecorationLine='none'
})
laptop.addEventListener('mouseenter',()=>{
    imgblockLaptop.style.display='block'
    imgblockPOCO_Series.style.display='none'
    imgblockREDMI_Series.style.display='none'
    imgblockXiomi.style.display='none'
    imgblockTABLETS.style.display='none'
    laptop.style.color= '#FF6900'
    laptop.style.textDecorationLine='underline'
    table.style.color= 'black'
    table.style.textDecorationLine='none'
    poco.style.color= '#898989'
    poco.style.textDecorationLine='none'
    red.style.color= '#898989'
    red.style.textDecorationLine='none'
    xio.style.color= '#898989'
    xio.style.textDecorationLine='none'
})

//block - 2
let imgblockSmart_Watches = document.querySelector('.imgblockSmart_Watches')
let sm=document.querySelector('.sm')

let imgblockSmart_Brands = document.querySelector('.imgblockSmart_Brands')
let bran=document.querySelector('.bran')

let imgblockTWS = document.querySelector('.imgblockTWS')
let tw_s=document.querySelector('.tw_s')

sm.addEventListener('mouseenter',()=>{
    imgblockSmart_Watches.style.display='block'
    imgblockSmart_Brands.style.display='none'
    imgblockTWS.style.display='none'
    sm.style.color= '#FF6900'
    sm.style.textDecorationLine='underline'
    bran.style.color= 'black'
    bran.style.textDecorationLine='none'
    tw_s.style.color= 'black'
    tw_s.style.textDecorationLine='none'
})

bran.addEventListener('mouseenter',()=>{
    imgblockSmart_Brands.style.display='block'
    imgblockSmart_Watches.style.display='none'
    imgblockTWS.style.display='none'
    bran.style.color= '#FF6900'
    bran.style.textDecorationLine='underline'
    tw_s.style.color= 'black'
    tw_s.style.textDecorationLine='none'
    sm.style.color= 'black'
    sm.style.textDecorationLine='none'
})
tw_s.addEventListener('mouseenter',()=>{
    imgblockTWS.style.display='block'
    imgblockSmart_Brands.style.display='none'
    imgblockSmart_Watches.style.display='none'
    tw_s.style.color= '#FF6900'
    tw_s.style.textDecorationLine='underline'
    sm.style.color= 'black'
    sm.style.textDecorationLine='none'
    bran.style.color= 'black'
    bran.style.textDecorationLine='none'
})

//block5
let imgblock_F_Series = document.querySelector('.imgblock_F_Series')
let F=document.querySelector('.F')

let imgblock_X_Series = document.querySelector('.imgblock_X_Series')
let X=document.querySelector('.X')

let imgblock_M_Series = document.querySelector('.imgblock_M_Series')
let M=document.querySelector('.M')

let imgblock_C_Series = document.querySelector('.imgblock_C_Series')
let C=document.querySelector('.C')

F.addEventListener('mouseenter',()=>{
    imgblock_F_Series.style.display='block'
    imgblock_X_Series.style.display='none'
    imgblock_M_Series.style.display='none'
    imgblock_C_Series.style.display='none'
    F.style.color= '#FF6900'
    F.style.textDecorationLine='underline'
    X.style.color= 'black'
    X.style.textDecorationLine='none'
    M.style.color= 'black'
    M.style.textDecorationLine='none'
    C.style.color= 'black'
    C.style.textDecorationLine='none'
})
X.addEventListener('mouseenter',()=>{
    imgblock_X_Series.style.display='block'
    imgblock_F_Series.style.display='none'
    imgblock_M_Series.style.display='none'
    imgblock_C_Series.style.display='none'
    F.style.color= 'black'
    F.style.textDecorationLine='none'
    X.style.color= '#FF6900'
    X.style.textDecorationLine='underline'
    M.style.color= 'black'
    M.style.textDecorationLine='none'
    C.style.color= 'black'
    C.style.textDecorationLine='none'
})
M.addEventListener('mouseenter',()=>{
    imgblock_M_Series.style.display='block'
    imgblock_F_Series.style.display='none'
    imgblock_X_Series.style.display='none'
    imgblock_C_Series.style.display='none'
    F.style.color= 'black'
    F.style.textDecorationLine='none'
    X.style.color= 'black'
    X.style.textDecorationLine='none'
    M.style.color= '#FF6900'
    M.style.textDecorationLine='underline'
    C.style.color= 'black'
    C.style.textDecorationLine='none'
})
C.addEventListener('mouseenter',()=>{
    imgblock_C_Series.style.display='block'
    imgblock_F_Series.style.display='none'
    imgblock_X_Series.style.display='none'
    imgblock_M_Series.style.display='none'
    F.style.color= 'black'
    F.style.textDecorationLine='none'
    X.style.color= 'black'
    X.style.textDecorationLine='none'
    M.style.color= 'black'
    M.style.textDecorationLine='none'
    C.style.color= '#FF6900'
    C.style.textDecorationLine='underline'
})













