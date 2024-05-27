from tkinter import  *
from customtkinter import *
import webbrowser 
from tkinter import ttk

ventana = Tk()
ventana.config(bg="#E3F2FF")
ventana.geometry("303x520")


#0 FUNCIONES MENÚ
puntos=0

#variables Mis metas
Entry1=IntVar()
Entry2=IntVar()
Entry3=IntVar()

#variables en casa
#tuto
recicla=IntVar()
huerto=IntVar()
abono=IntVar()
reduce=IntVar()
#reducir residuos
separa=IntVar()
empaque=IntVar()
mano=IntVar()
envase=IntVar()

def MIBOSQUE():
    global puntos
    
    if recicla.get() == 1:
        puntos=puntos+30
    if huerto.get() == 1:
        puntos=puntos+50
    if abono.get()==1:
        puntos=puntos+30
    if reduce.get()==1:
        puntos=puntos+45
    if separa.get()==1:
        puntos=puntos+25
    if empaque.get()==1:
        puntos=puntos+40
    if mano.get()==1:
        puntos=puntos+30
    if envase.get()==1:
        puntos=puntos+30
    if Entry1.get()==1:
        puntos=puntos+10
    if Entry2.get()==1:
        puntos=puntos+10
    if Entry3.get()==1:
        puntos=puntos+10
        
    if puntos>=50 and puntos <250:
        lblfondobosque.config(bd=0, image=BosqueFase2)   
        
    elif puntos>=250 and puntos<550:
        lblfondobosque.config(bd=0, image=BosqueFase3)  
    
    elif puntos>=550:
        lblfondobosque.config(bd=0, image=BosqueFase4)  
    

   
    















def fnEditar():
    entObj1.config(state="normal")
    chkopcion1.config(state="disabled")
    btnenviar= Button(frmMisMetas, image=imgEnviar, command=fnEnviar)
    btnenviar.place(x=240, y=60)
    
def fnEnviar():
    entObj1.config(state="disabled")
    chkopcion1.config(state="normal")
    btnEditar=Button(frmMisMetas, image=imgEditar, command=fnEditar)
    btnEditar.place(x=240, y=60)
    
def fnEditar2():
    entObj2.config(state="normal")
    chkopcion2.config(state="disabled")
    btnenviar= Button(frmMisMetas, image=imgEnviar, command=fnEnviar2)
    btnenviar.place(x=240, y=100)
    
def fnEnviar2():
    entObj2.config(state="disabled")
    chkopcion2.config(state="normal")
    btnEditar=Button(frmMisMetas, image=imgEditar, command=fnEditar2)
    btnEditar.place(x=240, y=100)
    
def fnEditar3():
    entObj3.config(state="normal")
    chkopcion3.config(state="disabled")
    btnenviar= Button(frmMisMetas, image=imgEnviar, command=fnEnviar3)
    btnenviar.place(x=240, y=143)
    
def fnEnviar3():
    entObj3.config(state="disabled")
    chkopcion3.config(state="normal")
    btnEditar=Button(frmMisMetas, image=imgEditar, command=fnEditar3)
    btnEditar.place(x=240, y=143)
    
    

#0.1 Mi bosque Puntos-Imágen
def fnBosque():
    frmProp_Below.forget()
    frmForo_Below.forget()
    frmForoDiscu.forget()
    frmForoViaje.forget()
    frmForoPropuestas.forget()
    frmForoGracias.forget()    
    frmForoEnergia.forget()
    frmForoOrganizaciones.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras_Below.forget()
    frmContacto_Below.forget()
    frmTest_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmAcciones_Below.forget()
    frmHuellaCarbono.forget()
    frmMenu_Below.forget()
    frmMenu_Top.forget()
    frmAcciones.forget()
    frmContactanos.forget()
    frmAccionesCasa.forget()
    frmCompras.forget()
    frmComp1.forget()
    frmComp2.forget()
    frmSellosEco.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    
    
    frmBosque.pack()
    frmBosque_Below.pack()

    
    
#Informacion Bosque 2 Sara botones
def fnBosqueinfo():
    frmBosque.forget()
    frmBosque_Below.forget()
    frminfoBosque.pack()
    
def fnBosqueAyuda():
    frmBosque.forget()
    frmBosque_Below.forget()
    frmayudaBosque.pack()
    
    
#botones regresar Bosque

def fnBosqueRegresarinfo():
    frmBosque.pack()
    frmBosque_Below.pack()
    frminfoBosque.forget()

def fnBosqueRegresarAyuda():
    frmBosque.pack()
    frmBosque_Below.pack()
    frmayudaBosque.forget()

def fnAcciones():
    frmColaboradores.forget()
    frmProp_Below.forget()
    frmForo_Below.forget()
    frmForoDiscu.forget()
    frmForoViaje.forget()
    frmForoPropuestas.forget()
    frmForoGracias.forget()    
    frmForoEnergia.forget()
    frmForoOrganizaciones.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras_Below.forget()
    frmBosque_Below.forget()
    frmContacto_Below.forget()
    frmTest_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmHuellaCarbono.forget()
    frmMenu_Below.forget()
    frmAccionesCasa.forget()
    frmMenu_Top.forget()
    frmBosque.forget()
    frmContactanos.forget()
    frmCompras.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    
    
    frmAcciones.pack()
    frmAcciones_Below.pack()
    
    

def fnCasa_Pagina_Inicio():
    MIBOSQUE()
    frmColaboradores.forget()
    frmProp_Below.forget()
    frmForo_Below.forget()
    frmForoDiscu.forget()
    frmForoViaje.forget()
    frmForoPropuestas.forget()
    frmForoGracias.forget()    
    frmForoEnergia.forget()
    frmForoOrganizaciones.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras_Below.forget()
    frmBosque_Below.forget()
    frmContacto_Below.forget()
    frmTest_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmAcciones_Below.forget()
    frmHuellaCarbono.forget()
    frmBosque.forget()
    frmAcciones.forget()
    frmContactanos.forget()
    frmAccionesCasa.forget()
    frmCompras.forget()
    frmComp1.forget()
    frmComp2.forget()
    frmSellosEco.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    lblPuntos2.config(text=puntos)
    

    frmMenu_Top.pack()
    frmMenu_Below.pack()

def fnForoDD():
    frmColaboradores.forget()
    frmForo_Below.forget()
    frmProp_Below.forget()
    frmForoViaje.forget()
    frmForoPropuestas.forget()
    frmForoGracias.forget()    
    frmForoEnergia.forget()
    frmForoOrganizaciones.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras.forget()
    frmBosque_Below.forget()
    frmContacto_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmAccionesCasa.forget()
    frmCasa_Below.forget()
    frmAcciones_Below.forget()
    frmMenu_Below.forget()
    frmMenu_Top.forget()
    frmBosque.forget()
    frmAcciones.forget()
    frmContactanos.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    frmHuellaCarbono.forget()
    frmTest_Below.forget()
    
    
    frmForoDiscu.pack()
    frmForo_Below.pack()
    
    
def fnHuella_Carbono():
    frmColaboradores.forget()
    frmProp_Below.forget()
    frmForo_Below.forget()
    frmForoDiscu.forget()
    frmForoViaje.forget()
    frmForoPropuestas.forget()
    frmForoGracias.forget()    
    frmForoEnergia.forget()
    frmForoOrganizaciones.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras.forget()
    frmBosque_Below.forget()
    frmContacto_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmAccionesCasa.forget()
    frmCasa_Below.forget()
    frmAcciones_Below.forget()
    frmMenu_Below.forget()
    frmMenu_Top.forget()
    frmBosque.forget()
    frmAcciones.forget()
    frmContactanos.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    
    
    frmHuellaCarbono.pack()
    frmTest_Below.pack()

def fnContactanos():
    frmColaboradores.forget()
    frmProp_Below.forget()
    frmForo_Below.forget()
    frmForoDiscu.forget()
    frmForoViaje.forget()
    frmForoPropuestas.forget()
    frmForoGracias.forget()    
    frmForoEnergia.forget()
    frmForoOrganizaciones.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras.forget()
    frmCompras_Below.forget()
    frmBosque_Below.forget()
    frmTest_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmAccionesCasa.forget()
    frmAcciones_Below.forget()
    frmMenu_Below.forget()
    frmBosque.forget()
    frmMenu_Top.forget()
    frmAcciones.forget()
    frmHuellaCarbono.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    
    
    frmContactanos.pack()
    frmContacto_Below.pack()

    
    
#Funciones Acciones

def fnCasa():
    frmColaboradores.forget()
    frmConciencia.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmCompras_Below.forget()
    frmAcciones.forget()
    frmAcciones_Below.forget()
    frmMenu_Below.forget()
    
    frmAccionesCasa.pack()
    frmCasa_Below.pack()
    

def fnCompras():
    frmAcciones.forget()
    frmAccionesCasa.forget()
    frmAcciones_Below.forget()
    frmComp1.forget()
    frmComp2.forget()
    frmSellosEco.forget()
    frmCompras.pack()
    frmCompras_Below.pack()
    
def fnComp1():
    frmCompras_Below.forget()
    frmCompras.forget()
    frmComp1.pack()
def fnComp2():
    frmCompras_Below.forget()
    frmCompras.forget()
    frmComp2.pack()
    
    
def fnSellos():
    frmCompras_Below.forget()
    frmCompras.forget()
    frmSellosEco.pack()

def fnODS():
    frmAcciones_Below.forget()
    frmAcciones.forget()
    frmODS.pack()
    frmODS_Below.pack()
    
def fnMisMetas():
    frmAcciones_Below.forget()
    frmAcciones.forget()
    frmMisMetas.pack()
    frmMisMetas_Below.pack()
    
# Funciones en casa
def fnTutoriales():
    frmCasa_Below.forget()
    frmAcciones.forget()
    frmAccionesCasa.forget()
    frmTutoriales.pack()
    frmCompras_Below.pack()
    

def fnReduceResiduos():
    frmCasa_Below.forget()
    frmAcciones.forget()
    frmAccionesCasa.forget()
    frmReduceResiduos.pack()
    frmCompras_Below.pack()
    
      
#Funciones sistema de puntos----



    
#Informacion Bosque 2 Sara botones
def fnBosqueinfo():
    frmBosque.forget()
    frmBosque_Below.forget()
    frminfoBosque.pack()
    
def fnBosqueAyuda():
    frmBosque.forget()
    frmBosque_Below.forget()
    frmayudaBosque.pack()
    

#Comandos Externos
    
def abrir_sprLink():
    url="https://www.footprintcalculator.org/"
    webbrowser.open_new(url)
    
#TUTORIALKES
def abrir_sprLink_TUTO():
    url="https://www.youtube.com/watch?v=dWrcf1bd8-0"
    webbrowser.open_new(url)

def abrir_sprLink_TUTO1():
    url="https://www.youtube.com/watch?v=kx-tGf3CcGg0"
    webbrowser.open_new(url)

def abrir_sprLink_TUTO2():
    url="https://www.youtube.com/watch?v=lFAlXkWK9X0"
    webbrowser.open_new(url)

def abrir_sprLink_TUTO3():
    url="https://www.youtube.com/watch?v=pnHgp6R-60o"
    webbrowser.open_new(url)
    
#RESIDUOS
def abrir_sprLink_RESI():
    url="https://www.youtube.com/watch?v=vQrXFn3dcOY"
    webbrowser.open_new(url)

def abrir_sprLink_RESI1():
    url="https://www.youtube.com/watch?v=7NDtVsWv928"
    webbrowser.open_new(url)

def abrir_sprLink_RESI2():
    url="https://www.youtube.com/watch?v=f60URzqVsEo"
    webbrowser.open_new(url)

def abrir_sprLink_RESI3():
    url="https://www.tupperwarecontigo.com.mx/soluciones-practicas-tupperware-botellas-y-vasos"
    webbrowser.open_new(url)
    
def abrirBioMar():
    url="https://sites.google.com/view/biomar-microalga/"
    webbrowser.open_new(url)
#-----------------------
def fnBosque2():
    frmColaboradores.forget()
    frmProp_Below.forget()
    frmFelicidades.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras_Below.forget()
    frmContacto_Below.forget()
    frmTest_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmAcciones_Below.forget()
    frmHuellaCarbono.forget()
    frmMenu_Below.forget()
    frmMenu_Top.forget()
    frmAcciones.forget()
    frmContactanos.forget()
    frmAccionesCasa.forget()
    frmCompras.forget()
    frmComp1.forget()
    frmComp2.forget()
    frmSellosEco.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    frmBosque.pack()
    frmBosque_Below.pack()
    
    
    
    
   
#-------------
def fnPropuestas():
    frmForoDiscu.forget()
    frmForo_Below.forget()
    frmForoPropuestas.pack()
    frmProp_Below.pack()

def fnViaje():
    frmForoDiscu.forget()
    frmForo_Below.forget()
    frmForoPropuestas.forget()
    frmForoViaje.pack()
    frmProp_Below.pack()
    
def fnEnergia():
    frmForoDiscu.forget()
    frmForo_Below.forget()
    frmForoPropuestas.forget()
    frmForoEnergia.pack()
    frmProp_Below.pack()
    
def fnOrganizaciones():
    frmForoDiscu.forget()
    frmForo_Below.forget()
    frmForoPropuestas.forget()
    frmForoOrganizaciones.pack()
    frmProp_Below.pack()

def fnGraciasForo():
    frmForoDiscu.forget()
    frmForoPropuestas.forget()
    frmForoOrganizaciones.forget()
    frmProp_Below.forget()
    frmForoGracias.pack()
    frmForo_Below.pack()
    
def fnNuestrosColabs():
    frmMasBioMar.forget()
    frmProp_Below.forget()
    frmForo_Below.forget()
    frmForoDiscu.forget()
    frmForoViaje.forget()
    frmForoPropuestas.forget()
    frmForoGracias.forget()    
    frmForoEnergia.forget()
    frmForoOrganizaciones.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras_Below.forget()
    frmBosque_Below.forget()
    frmContacto_Below.forget()
    frmTest_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmHuellaCarbono.forget()
    frmMenu_Below.forget()
    frmAccionesCasa.forget()
    frmMenu_Top.forget()
    frmBosque.forget()
    frmContactanos.forget()
    frmCompras.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    frmAcciones.forget()
    frmAcciones_Below.forget()
    frmColaboradores.pack()
    frmCompras_Below.pack()
    
def fnMasDeBiomar():
    frmProp_Below.forget()
    frmForo_Below.forget()
    frmForoDiscu.forget()
    frmForoViaje.forget()
    frmForoPropuestas.forget()
    frmForoGracias.forget()    
    frmForoEnergia.forget()
    frmForoOrganizaciones.forget()
    frmTutoriales.forget()
    frmIniciaElCambio.forget()
    frmReduceResiduos.forget()
    frmConciencia.forget()
    frmCompras_Below.forget()
    frmBosque_Below.forget()
    frmContacto_Below.forget()
    frmTest_Below.forget()
    frmCompras_Below.forget()
    frmCasa_Below.forget()
    frmHuellaCarbono.forget()
    frmMenu_Below.forget()
    frmAccionesCasa.forget()
    frmMenu_Top.forget()
    frmBosque.forget()
    frmContactanos.forget()
    frmCompras.forget()
    frmODS.forget()
    frmODS_Below.forget()
    frmMisMetas.forget()
    frmMisMetas_Below.forget()
    frmAcciones.forget()
    frmAcciones_Below.forget()
    frmColaboradores.forget()
    frmCompras_Below.forget()
    
    frmMasBioMar.pack()
    
    
    
    
    
#Imágenes
    
#BIOMAR FONDO
imgfondoBiomar=PhotoImage(file="BiomarFondo.png")
    
#propuestas fondo
imgfondoTienesProp=PhotoImage(file="fondoTienesProp.png")
    
imgComparativaEj2=PhotoImage(file="imgEjemplo2.png")
imgComparativaEj1=PhotoImage(file="imgEjemplo1.png")

imgFondoAcciones=PhotoImage(file="imgAcciones.png")
imgFondoEnCasa=PhotoImage(file="NCasa(1).png")
imgFondoCarbono=PhotoImage(file="crbno.png") #(para que el conejo se vea completo: .place(x=0, y=40)
imgComprasSus=PhotoImage(file="cmrps.png") #(para que el conejo se vea completo: .place(x=0, y=40)
imgBosque=PhotoImage(file="imgBosque.png")
imgContactanos= PhotoImage(file="contactoNues.png")
imgFondoMenu= PhotoImage(file="deinicio.png")
imgEstaPasando=PhotoImage(file="imgQEP.png")
imgFondoAyuBos=PhotoImage(file="AyuBos.png")

imgsellosfondo=PhotoImage(file="sellos.png")
imgtutofondo=PhotoImage(file="tutoriales.png")
imgresiduosfondo=PhotoImage(file="residuos.png")


imgNuevoForo=PhotoImage(file="Foro++Nuevo.png")
#Botones imagen Regreso
imgVolver=PhotoImage(file="imgRegresar.png")
imgAcciones=PhotoImage(file="tab_lapiz.png")
imgInicio=PhotoImage(file="csaima.png")
imgContacto=PhotoImage(file="contactanegro.png")
imgHuella=PhotoImage(file="HuellaNegro.png")
imgForo=PhotoImage(file="ForoNegro1.png")

#imagenes extra icnonos
imgInfo=PhotoImage(file="info_Bos.png")
imgAyuBos=PhotoImage(file="imgMasN.png")
imgSellos=PhotoImage(file="imgSellosN.png")
imgAbeja=PhotoImage(file="pequeabeja.png")

#imagenes acciones 
imgODS=PhotoImage(file="imgODS.png")
imgBioMar=PhotoImage(file="BioMar.png")

#IMG FORO
FondoEnergia=PhotoImage(file="FondoEnergia.png")
FondoOrg=PhotoImage(file="FondoOrg.png")
FondoViaje=PhotoImage(file="FondoViaje.png")

#Imagenes en Mi bosque
BosqueFase1=PhotoImage(file="imgBosque.png")
BosqueFase2=PhotoImage(file="imgBosque2.png")
BosqueFase3=PhotoImage(file="imgBosque3.png")
BosqueFase4=PhotoImage(file="imgBosque4.png")


#MIS METAS
imgMisMetas=PhotoImage(file="imgMisMetas.png")

#IMG MIS METAs

imgEditar=PhotoImage(file="imgeditar.png")
imgEnviar=PhotoImage(file="enviarejemp.png")



#IMAGENES EN COLOR

imgArbolColor=PhotoImage(file="Arbol_Color.png")
imgHuellaColor=PhotoImage(file="Huellaima.png")
imgContaColor=PhotoImage(file="ContaColor.png")
imgCasaColor=PhotoImage(file="CasaColor.png")
imgTablaColor=PhotoImage(file="laPiolor.png")
imgForoColor=PhotoImage(file="Foro_Color.png")

#Imagenes última versión
imgGloboTexto=PhotoImage(file="globoTxt.png")
imgVoydeViaje=PhotoImage(file="Voy_De_Viaje.png")
imgRenovaEnergia=PhotoImage(file="energia_Renova_.png")
imgAltosJalisco=PhotoImage(file="Zapopan_Img.png")
imgNuesColabs=PhotoImage(file="nuescolabs.png")
imgDesBioMar=PhotoImage(file="DesBioMar.png")
imgGracias=PhotoImage(file="graciastierraviv.png")


#Frames de Icono-Boton de abajo
frmMenu_Below = Frame(ventana, width=303, height=40)
frmMenu_Below.config(bd=0, relief="solid", bg="#376DA0")
frmMenu_Below.pack(side="bottom")

frmAcciones_Below = Frame(ventana, width=303, height=40)
frmAcciones_Below.config(bd=0, relief="solid", bg="#376DA0")

frmCasa_Below= Frame(ventana, width=303, height=40)
frmCasa_Below.config(bd=0, relief="solid", bg="#376DA0")

frmCompras_Below= Frame(ventana, width=303, height=40)
frmCompras_Below.config(bd=0, relief="solid", bg="#376DA0")

frmTest_Below= Frame(ventana, width=303, height=40)
frmTest_Below.config(bd=0, relief="solid", bg="#376DA0")

frmContacto_Below= Frame(ventana, width=303, height=40)
frmContacto_Below.config(bd=0, relief="solid", bg="#376DA0")

frmBosque_Below= Frame(ventana, width=303, height=40)
frmBosque_Below.config(bd=0, relief="solid", bg="#376DA0")

frmCompras_Below=Frame(ventana, width=303, height=40)
frmCompras_Below.config(bd=0, relief="solid", bg="#376DA0")




#Frames de sección Acciones
frmConciencia= Frame(ventana, width=303, height=480)
frmTutoriales= Frame(ventana, width=303, height=480)
frmIniciaElCambio= Frame(ventana, width=303, height=480)
frmReduceResiduos= Frame(ventana, width=303, height=480)

#Frames de Foro de Discusión
frmForoDiscu= Frame(ventana, width=303, height=480)
frmForoPropuestas= Frame(ventana, width=303, height=480)
frmForoGracias= Frame(ventana, width=303, height=480)
frmForoViaje= Frame(ventana, width=303, height=480)
frmForoEnergia= Frame(ventana, width=303, height=480)
frmForoOrganizaciones= Frame(ventana, width=303, height=480)

#Frames Empresas Sustentables
frmColaboradores= Frame(ventana, width=303, height=480)




#1 CONFIGURACIÓN DE PÁGINA MENÚ
#1.1 Botones Below
imgArbolBosque=PhotoImage(file="imgArbolNegro.png")

btnHuella_Carbono=CTkButton(frmMenu_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmMenu_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)


Btn_Bosque=CTkButton(frmMenu_Below, fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmMenu_Below, fg_color="#376DA0",text_color="#376DA0",image=imgCasaColor, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=5)

btnAcciones_en_mcpr=CTkButton(frmMenu_Below, fg_color="#376DA0",text_color="#376DA0",image=imgAcciones, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=4.5)

btnContactanos=CTkButton(frmMenu_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)




#1.2 Estética Arriba
frmMenu_Top= Frame(ventana, width=303, height=480)
frmMenu_Top.config(bd=0, relief="solid", bg="#E3F2FF")
frmMenu_Top.pack(side="top")

lblFondoMenuimg=Label(frmMenu_Top, image=imgFondoMenu)
lblFondoMenuimg.place(x=0, y=0)

lblPuntos= Label(frmMenu_Top, text="Mis puntos: ")
lblPuntos.config(font=("Contrail One", 12), bg="#E3F2FF")
lblPuntos.place(x=20, y=20)

lblPuntos2= Label(frmMenu_Top, text=puntos)
lblPuntos2.config(font=("Contrail One", 12), bg="#E3F2FF")
lblPuntos2.place(x=100, y=20)



#2 CONFIGURACIÓN DE ACCIONES 
#2.01 CONFIGURACIÓN ACCIONES
frmAcciones= Frame(ventana, width=303, height=480)
frmAcciones.config(bd=0, relief="solid", bg="#E3F2FF")

lblFondoAcciones=Label(frmAcciones, image=imgFondoAcciones)
lblFondoAcciones.config(bd=0)
lblFondoAcciones.place(x=0, y=0)



#2.02 Botones Below ACCIONES


btnHuella_Carbono=CTkButton(frmAcciones_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmAcciones_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmAcciones_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmAcciones_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmAcciones_Below, fg_color="#376DA0",text_color="#376DA0",image=imgTablaColor, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmAcciones_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)


#2.03Botones + Acciones

btnPequeAbeja= Button(frmAcciones, image=imgAbeja , bg="#376DA0",command=fnNuestrosColabs)
btnPequeAbeja.place(x=263, y=10)


btnAcciones_main= CTkButton(frmAcciones, text="Acciones En casa" ,corner_radius=0, fg_color="#376DA0",text_color="white" ,command=fnCasa)
btnAcciones_main.place(x=85, y=170)

btnAccionesCompra= CTkButton(frmAcciones, text="Compra Sustentable" ,corner_radius=0,fg_color="#376DA0",text_color="white", command=fnCompras)
btnAccionesCompra.place(x=85, y=210)

btnODS= CTkButton(frmAcciones, text="ODS" ,fg_color="#376DA0",corner_radius=0,text_color="white", command=fnODS)
btnODS.place(x=85, y=250)


btnMisMetas= CTkButton(frmAcciones, text="Mis Metas" ,corner_radius=0,fg_color="#376DA0",text_color="white", command=fnMisMetas)
btnMisMetas.place(x=85, y=290)

#2.031 Nuestros Colaboradores

frmColaboradores.config(bg="#E3F2FF")

lblFondoColabs=Label(frmColaboradores, image=imgNuesColabs)
lblFondoColabs.place(x=0, y=0)
btn_BioMar=Button(frmColaboradores, image=imgBioMar,bd=0, command=fnMasDeBiomar)
btn_BioMar.config(bg="#E3F2FF")
btn_BioMar.place(x=100, y=156.8)
Btn_Colab_Acciones=Button(frmColaboradores,image=imgVolver, bd=0, command=fnAcciones)
Btn_Colab_Acciones.place(x=10,y=10)

#2.032 BioMar

frmMasBioMar=Frame(ventana, height=520, width=303)
frmMasBioMar.config(bg="#E3F2FF")

lblFondoODS= Label(frmMasBioMar, image=imgfondoBiomar)
lblFondoODS.config(bd=0)
lblFondoODS.place(x=0, y=0, width=303, height=520)

Btn_BioMar_Colabs=Button(frmMasBioMar,image=imgVolver, bd=0, command=fnNuestrosColabs)
Btn_BioMar_Colabs.place(x=10,y=10)




#MIS METAS FRAME
frmMisMetas= Frame(ventana, width=303, height=480)
frmMisMetas.config(bd=0, relief="solid", bg="#E3F2FF")

lblFondoMISMETAS=Label(frmMisMetas, image=imgMisMetas)
lblFondoMISMETAS.config(bd=0)
lblFondoMISMETAS.place(x=0, y=0)

Btn_Tutoriales_MISMETAS=Button(frmMisMetas,image=imgVolver, bd=0, command=fnAcciones)
Btn_Tutoriales_MISMETAS.place(x=10,y=10)

#MIS METAS ENTRYS Y CHK
chkopcion1= Checkbutton(frmMisMetas, text="", variable=Entry1)
chkopcion1.config(state="disabled")
chkopcion1.place(x=25, y=65, width=20,height=20)

entObj1= Entry(frmMisMetas)
entObj1.place(x=50, y=67, width=180, height=15)

btnenviar= Button(frmMisMetas, image=imgEnviar, command=fnEnviar)
btnenviar.place(x=240, y=60)

chkopcion2= Checkbutton(frmMisMetas, text="", variable=Entry2)
chkopcion2.config(state="disabled")
chkopcion2.place(x=25, y=107, width=20,height=20)

entObj2= Entry(frmMisMetas)
entObj2.place(x=50, y=109, width=180, height=15)

btnenviar2= Button(frmMisMetas, image=imgEnviar, command=fnEnviar2)
btnenviar2.place(x=240, y=100)

chkopcion3= Checkbutton(frmMisMetas, text="", variable=Entry3)
chkopcion3.config(state="disabled")
chkopcion3.place(x=25, y=150, width=20,height=20)

entObj3= Entry(frmMisMetas)
entObj3.place(x=50, y=153, width=180, height=15)

btnenviar3= Button(frmMisMetas, image=imgEnviar, command=fnEnviar3)
btnenviar3.place(x=240, y=143)

#BELOW
frmMisMetas_Below=Frame(ventana, width=303, height=40)
frmMisMetas_Below.config(bd=0, relief="solid", bg="#376DA0")



btnHuella_Carbono=CTkButton(frmMisMetas_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmMisMetas_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmMisMetas_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmMisMetas_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmMisMetas_Below, fg_color="#376DA0",text_color="#376DA0",image=imgTablaColor, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmMisMetas_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)




#CONFIG FRAME ODS
frmODS= Frame(ventana, width=303, height=480)
frmODS.config(bd=0, relief="solid", bg="#E3F2FF")

frmODS_Below=Frame(ventana, width=303, height=40)
frmODS_Below.config(bd=0, relief="solid", bg="#376DA0")


btnHuella_Carbono=CTkButton(frmODS_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmODS_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmODS_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmODS_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmODS_Below, fg_color="#376DA0",text_color="#376DA0",image=imgTablaColor, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmODS_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)
#ADENTRO ODS

lblFondoODS= Label(frmODS, image=imgODS)
lblFondoODS.config(bd=0)
lblFondoODS.place(x=0, y=0, width=303, height=480)

Btn_ODSreg=Button(frmODS,image=imgVolver, bd=0, command=fnAcciones)
Btn_ODSreg.place(x=10,y=10)





#2.1 configuración En casa

frmAccionesCasa= Frame(ventana, width=303, height=480)
frmAccionesCasa.config(bd=0, relief="solid", bg="#E3F2FF")


lblFondoCasa= Label(frmAccionesCasa, image=imgFondoEnCasa)
lblFondoCasa.config(bd=0)
lblFondoCasa.place(x=0, y=0)


BtnTuto= CTkButton(frmAccionesCasa, text="Tutoriales", corner_radius=0,fg_color="#376DA0",text_color="white",command=fnTutoriales)
BtnTuto.place(x=85, y=190)

BtnReduceResiduos=CTkButton(frmAccionesCasa, text="Reducir residuos",corner_radius=0,fg_color="#376DA0",text_color="white", command=fnReduceResiduos)
BtnReduceResiduos.place(x=85, y=230)

Btn_Casa_Acciones=Button(frmAccionesCasa,image=imgVolver, bd=0, command=fnAcciones)
Btn_Casa_Acciones.place(x=10,y=10)


#2.1102 Tutoriales
frmTutoriales.config(relief="solid", bg="#E3F2FF")

lblFondoTUTO= Label(frmTutoriales, image=imgtutofondo, width=303, height=480)
lblFondoTUTO.config(bd=0)
lblFondoTUTO.place(x=0, y=0)


Btn_Tutoriales_Casa=Button(frmTutoriales,image=imgVolver, bd=0, command=fnCasa)
Btn_Tutoriales_Casa.place(x=10,y=10)

BtnRecicla=CTkButton(frmTutoriales, text="Reciclaje Inteligente",corner_radius=0, fg_color="#376DA0",text_color="white",command=abrir_sprLink_TUTO)
BtnRecicla.place(x=5,y=160)

BtnHuerto=CTkButton(frmTutoriales, text="Haz tu Huerto", corner_radius=0,fg_color="#376DA0",text_color="white", command=abrir_sprLink_TUTO1)
BtnHuerto.place(x=155,y=160)

Btnabono=CTkButton(frmTutoriales, text="Haz tu Abono", corner_radius=0,fg_color="#376DA0",text_color="white",command=abrir_sprLink_TUTO2)
Btnabono.place(x=5,y=290)

Btnreduce=CTkButton(frmTutoriales, text="Reducir huella de CO2", corner_radius=0,fg_color="#376DA0",text_color="white",command=abrir_sprLink_TUTO3)
Btnreduce.place(x=150,y=290)


#CHEKBUTTONS
chkReciclaje=ttk.Checkbutton(frmTutoriales, text="Completado", variable=recicla)
chkReciclaje.place(x=25, y=190)

chkHuerto=ttk.Checkbutton(frmTutoriales, text="Completado", variable=huerto)
chkHuerto.place(x=180, y=190)


chkabono=ttk.Checkbutton(frmTutoriales, text="Completado", variable=abono)
chkabono.place(x=25, y=320)


chkreduce=ttk.Checkbutton(frmTutoriales, text="Completado", variable=reduce)
chkreduce.place(x=180, y=320)




#2.1104 Reduce Residuos

Btn_ReduceResiduos_Casa=Button(frmReduceResiduos,image=imgVolver, bd=0, command=fnCasa)
Btn_ReduceResiduos_Casa.place(x=30,y=20)

lblFondoRESI= Label(frmReduceResiduos, image=imgresiduosfondo, width=303, height=480)
lblFondoRESI.config(bd=0)
lblFondoRESI.place(x=0, y=0)


#BOTONES LBL
BtnSeparar_Basura=CTkButton(frmReduceResiduos, text="Separar Basura",corner_radius=0, fg_color="#376DA0",text_color="white",command=abrir_sprLink_RESI)
BtnSeparar_Basura.place(x=5,y=165)

Btnempaque=CTkButton(frmReduceResiduos, text="Elige Menos Empaque",corner_radius=0, fg_color="#376DA0",text_color="white",command=abrir_sprLink_RESI1)
Btnempaque.place(x=150,y=165)

BtnHuerto=CTkButton(frmReduceResiduos, text="Compra Segunda Mano", corner_radius=0,fg_color="#376DA0",text_color="white",command=abrir_sprLink_RESI2)
BtnHuerto.place(x=2,y=295)

BtnReusable=CTkButton(frmReduceResiduos, text="Envases Reusables", corner_radius=0,fg_color="#376DA0",text_color="white",command=abrir_sprLink_RESI3)
BtnReusable.place(x=160,y=295)

Btn_Tutoriales_Casa=Button(frmReduceResiduos,image=imgVolver, bd=0, command=fnCasa)
Btn_Tutoriales_Casa.place(x=10,y=10)



#CHECKBUTTONS

chksepara=ttk.Checkbutton(frmReduceResiduos, text="Completado",  variable=separa)
chksepara.place(x=25, y=195)

chkempaque=ttk.Checkbutton(frmReduceResiduos, text="Completado",  variable=empaque)
chkempaque.place(x=180, y=195)

chk2mano=ttk.Checkbutton(frmReduceResiduos, text="Completado",  variable=mano)
chk2mano.place(x=25, y=325)

chkenvase=ttk.Checkbutton(frmReduceResiduos, text="Completado",  variable=envase)
chkenvase.place(x=180, y=325)


#2.12 Botones abajo de Casa

btnHuella_Carbono=CTkButton(frmCasa_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmCasa_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmCasa_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmCasa_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmCasa_Below, fg_color="#376DA0",text_color="#376DA0",image=imgTablaColor, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmCasa_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)



#2.2 configuración Compras Sustentables

frmCompras= Frame(ventana, width=303, height=480)
frmCompras.config(bd=0, relief="solid", bg="#E3F2FF")

lblFondoCompras= Label(frmCompras, image=imgComprasSus)
lblFondoCompras.config(bd=0)
lblFondoCompras.place(x=0, y=0)




btnSellos= Button(frmCompras, image=imgSellos, bd=0, command=fnSellos)
btnSellos.place(x=270, y=10)

#____________________



btnDesBioMar=CTkButton(frmCompras, image=imgDesBioMar, fg_color="#376DA0",text_color="White", command=abrirBioMar)
btnDesBioMar.place(x=0, y=78.3)

btn_comp1=CTkButton(frmCompras, text="Pasta Dental",corner_radius=0, fg_color="#376DA0",text_color="White", command=fnComp1)
btn_comp1.place(x=155, y=287)


btn_comp2=CTkButton(frmCompras,fg_color="#376DA0",text_color="White", corner_radius=0,text="Protector Solar",command=fnComp2)
btn_comp2.place(x=5, y=287)





#___________________

Btn_Casa_Compras=Button(frmCompras,image=imgVolver, bd=0, command=fnAcciones)
Btn_Casa_Compras.place(x=10,y=10)





#2.21 CONFIGURACIÓN COMPARATIVA COMPRAS
#2.201 Botones Abajo Compras
btnHuella_Carbono=CTkButton(frmCompras_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmCompras_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmCompras_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)



btnAcciones_Menu=CTkButton(frmCompras_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmCompras_Below, fg_color="#376DA0",text_color="#376DA0",image=imgTablaColor, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmCompras_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)



#2.211 Producto 1
frmComp1= Frame(ventana, width=303, height=580)
frmComp1.config(bd=0, relief="solid", bg="#E3F2FF")
lbl_Ej_Comparativa= Label(frmComp1, image=imgComparativaEj1)
lbl_Ej_Comparativa.place(x=0, y=0)


Btn_Cmp_Cmprs1=Button(frmComp1,image=imgVolver, bd=0, command=fnCompras)
Btn_Cmp_Cmprs1.place(x=10,y=10)

#2.212 Producto 2
frmComp2= Frame(ventana, width=303, height=580)
frmComp2.config(bd=0, relief="solid", bg="#E3F2FF")
lbl_Ej_Comparativa2= Label(frmComp2, image=imgComparativaEj2)
lbl_Ej_Comparativa2.place(x=0, y=0)


Btn_Cmp_Cmprs2=Button(frmComp2,image=imgVolver, bd=0, command=fnCompras)
Btn_Cmp_Cmprs2.place(x=10,y=10)


#2.3 Sellos

frmSellosEco= Frame(ventana, width=303, height=580)
frmSellosEco.config(bd=0, relief="solid", bg="#E3F2FF")
Btn_sello_Accion=Button(frmSellosEco,image=imgVolver, bd=0, command=fnCompras)
Btn_sello_Accion.place(x=10,y=10)

lblfondosellos=Label(frmSellosEco, image=imgsellosfondo)
lblfondosellos.config(bd=0)
lblfondosellos.place(x=0, y=0)

Btn_sellosV=Button(frmSellosEco,image=imgVolver, bd=0, command=fnCompras)
Btn_sellosV.config(relief="solid")
Btn_sellosV.place(x=10,y=10)










#3 HUELLA DE CARBONO

#3.1Configuración Huella de Carbono
frmHuellaCarbono= Frame(ventana, width=303, height=480)
frmHuellaCarbono.config(bd=0, relief="solid", bg="#E3F2FF")

lblFondoCarbono= Label(frmHuellaCarbono, image=imgFondoCarbono)
lblFondoCarbono.config(bd=0)
lblFondoCarbono.place(x=0, y=0)

btnCarbonoLink=CTkButton(frmHuellaCarbono, text="Huella ecológica",corner_radius=0,fg_color="#376DA0",text_color="white", command=abrir_sprLink)
btnCarbonoLink.place(x=80, y=170)



#3.2 Botones Below Huella de Carbono


btnHuella_Carbono=CTkButton(frmTest_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuellaColor, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmTest_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmTest_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmTest_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmTest_Below, fg_color="#376DA0",text_color="#376DA0",image=imgAcciones, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmTest_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)







#4 CONTÁCTANOS

#4.1Configuración Contáctanos
frmContactanos= Frame(ventana, width=303, height=480)
frmContactanos.config(bd=0, relief="solid", bg="#E3F2FF")

Titulo_Contactanos=Label(frmContactanos, text="CONTÁCTANOS")
Titulo_Contactanos.config(font=("Contrail One", 20), bg="#E3F2FF")
Titulo_Contactanos.place(x=70, y=40)

lblFondoContact= Label(frmContactanos, image=imgContactanos)
lblFondoContact.place(x=0, y=0)

#4.2 Botones abajo Contacto


btnHuella_Carbono=CTkButton(frmContacto_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmContacto_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmContacto_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmContacto_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmContacto_Below, fg_color="#376DA0",text_color="#376DA0",image=imgAcciones, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmContacto_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContaColor, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)










#5 MI BOSQUE

#5.0Configuración de Mi bosque
frmBosque= Frame(ventana, width=303, height=480)
frmBosque.config(bd=0, relief="solid", bg="#E3F2FF")












 #5.01 Imagenes de mi Bosque

lblfondobosque=Label(frmBosque, image=BosqueFase1)
lblfondobosque.config(bd=0)
lblfondobosque.place(x=0, y=0)

#5.2 Botones abajo Mi Bosque

btnHuella_Carbono=CTkButton(frmBosque_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmBosque_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForo, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmBosque_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolColor, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmBosque_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmBosque_Below, fg_color="#376DA0",text_color="#376DA0",image=imgAcciones, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmBosque_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)

#5.3 Mi bosque Informacion

btnBosqueP=Button(frmBosque,image=imgInfo, bd=0, command=fnBosqueinfo)
btnBosqueP.place(x=270,y=10)

btninfoBosque=Button(frmBosque ,image=imgAyuBos, bd=0, command=fnBosqueAyuda)
btninfoBosque.place(x=5,y=10)



#5.3.1 Explicación Bosque 

frminfoBosque= Frame(ventana, width=303, height=520)
frminfoBosque.config(bd=0, relief="solid", bg="#E3F2FF")

FondoAyudaBos= Label(frminfoBosque, image=imgFondoAyuBos)
FondoAyudaBos.place(x=0, y=0)

Btn_info_regresar=Button(frminfoBosque,image=imgVolver, bd=0, command=fnBosqueRegresarinfo)
Btn_info_regresar.place(x=10,y=10)


#5.3.2 Ayuda Bosque +

frmayudaBosque= Frame(ventana, width=303, height=520)
frmayudaBosque.config(bd=0, relief="solid", bg="#E3F2FF")

lblFondoPasando=Label(frmayudaBosque, image=imgEstaPasando)
lblFondoPasando.place(x=0, y=0)

Btn_info_regresar=Button(frmayudaBosque,image=imgVolver, bd=0, command=fnBosqueRegresarAyuda)
Btn_info_regresar.place(x=10,y=10)












#6 FORO DE DISCUSIÓN

frmForoDiscu.config(bd=0, relief="solid", bg="#E3F2FF")


lblFondoForo=Label(frmForoDiscu, bd=0, image=imgNuevoForo)
lblFondoForo.place(x=0, y=0)

btnGloboTxt=CTkButton(frmForoDiscu, fg_color="#E3F2FF",text_color="#E3F2FF",image=imgGloboTexto, command=fnPropuestas)
btnGloboTxt.place(x=241.9, y=12.6)


#6.1 Below Foro Discu

frmForo_Below=Frame(ventana, width=303, height=40)
frmForo_Below.config(bd=0, relief="solid", bg="#376DA0")

btnHuella_Carbono=CTkButton(frmForo_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmForo_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForoColor, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmForo_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)


btnAcciones_Menu=CTkButton(frmForo_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmForo_Below, fg_color="#376DA0",text_color="#376DA0",image=imgAcciones, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmForo_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)

#6.12 Adentro de Foro de Discusión
btnForoUno=CTkButton(frmForoDiscu,fg_color="transparent",text_color="",
                     width=237.4, height=69.6,
                     image=imgVoydeViaje, text="", command=fnViaje)
btnForoUno.place(x=30.3,y=190.4)

btnForoDos=CTkButton(frmForoDiscu,fg_color="transparent",width=237.4, height=69.6
                     , text="", image=imgRenovaEnergia, command=fnEnergia)

btnForoDos.place(x=30.3,y=271.2)

btnForoTres=CTkButton(frmForoDiscu,fg_color="transparent",width=237.4, height=69.6,
                      text="", image=imgAltosJalisco, command=fnOrganizaciones)

btnForoTres.place(x=30.3,y=352.8)







#6.2 Mis Propuestas
frmForoPropuestas.config(bg="#E3F2FF")


lblFondoProp= Label(frmForoPropuestas, image=imgfondoTienesProp)
lblFondoProp.config(bd=0)
lblFondoProp.place(x=0, y=0, width=303, height=520)


Btn_Propuestas_Foro=Button(frmForoPropuestas,image=imgVolver, bd=0, command=fnForoDD)
Btn_Propuestas_Foro.place(x=10,y=10)

entPropuesta= Entry(frmForoPropuestas)
entPropuesta.place(x=115.2, y=247.2, width=150)


btnEnviarProp=CTkButton(frmForoPropuestas,fg_color="#376DA0", width=40, height=20,
                      text="Enviar", command=fnGraciasForo)
btnEnviarProp.place(x=216.2, y=280.6)


#6.201 Mis Propuestas Below

frmProp_Below=Frame(ventana, width=303, height=40)
frmProp_Below.config(bd=0, relief="solid", bg="#376DA0")

btnHuella_Carbono=CTkButton(frmProp_Below, fg_color="#376DA0",text_color="#376DA0",image=imgHuella, command=fnHuella_Carbono)
btnHuella_Carbono.place(x=0,y=5)

btnForoDD=CTkButton(frmProp_Below,fg_color="#376DA0",text_color="#376DA0", image=imgForoColor, command=fnForoDD)
btnForoDD.place(x=45.16,y=5)

Btn_Bosque=CTkButton(frmProp_Below,fg_color="#376DA0",text_color="#376DA0", image=imgArbolBosque, command=fnBosque)
Btn_Bosque.place(x=94.3,y=5)

btnAcciones_Menu=CTkButton(frmProp_Below, fg_color="#376DA0",text_color="#376DA0",image=imgInicio, command=fnCasa_Pagina_Inicio)
btnAcciones_Menu.place(x=141.5,y=4.5)

btnAcciones_en_mcpr=CTkButton(frmProp_Below, fg_color="#376DA0",text_color="#376DA0",image=imgAcciones, command=fnAcciones)
btnAcciones_en_mcpr.place(x=188.6,y=5)

btnContactanos=CTkButton(frmProp_Below,fg_color="#376DA0",text_color="#376DA0", image=imgContacto, command=fnContactanos)
btnContactanos.place(x=235.83,y=5)


#6.21 Gracias
frmForoGracias.config(bg="#E3F2FF")
lblGracias=Label(frmForoGracias, image=imgGracias)
lblGracias.place(x=0, y=0)
Btn_Gracias_Foro=Button(frmForoGracias,image=imgVolver, bd=0, command=fnForoDD)
Btn_Gracias_Foro.place(x=10,y=10)

#6.3 Foro de Viaje
frmForoViaje.config(bg="#E3F2FF")


lblFondoviaje=Label(frmForoViaje, image=FondoViaje)
lblFondoviaje.config(bd=0)
lblFondoviaje.place(x=0, y=0)

Btn_Viaje_Foro=Button(frmForoViaje,image=imgVolver, bd=0, command=fnForoDD)
Btn_Viaje_Foro.place(x=10,y=10)


#6.4 Foro deEnergia
frmForoEnergia.config(bg="#E3F2FF")


lblFondoenergia=Label(frmForoEnergia, image=FondoEnergia)
lblFondoenergia.config(bd=0)
lblFondoenergia.place(x=0, y=0)


Btn_Energia_Foro=Button(frmForoEnergia,image=imgVolver, bd=0, command=fnForoDD)
Btn_Energia_Foro.place(x=10,y=10)

#6.5 Foro Organizaciones
frmForoOrganizaciones.config(bg="#E3F2FF")

lblFondoorg=Label(frmForoOrganizaciones, image=FondoOrg)
lblFondoorg.config(bd=0)
lblFondoorg.place(x=0, y=0)

Btn_Organizaciones_Foro=Button(frmForoOrganizaciones,image=imgVolver, bd=0, command=fnForoDD)
Btn_Organizaciones_Foro.place(x=10,y=10)





ventana.mainloop()
