# -*- encoding: utf-8 -*-
import os
RUTA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField,\
            BAND_WIDTH, Label,Image,Line
from reportlab.lib.pagesizes import A5,A4,letter
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.colors import navy, yellow, red, purple, orange,\
    green, white, blue


class lista_alumnos(Report):
    title = 'Instituto Politécnico Nacional'

    #materia_grupo.profesor.cve_usuario
    page_size = landscape(letter)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm
        bandera=True

        elements=(
            ObjectValue(attribute_name='alumno.cve_usuario',top=3*cm, left=0.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
            
            ObjectValue(attribute_name='alumno.cve_usuario.get_full_name'
                , top=3*cm,left=3*cm ,style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
            
                #ObjectValue(attribute_name='materia_grupo.profesor.cve_usuario.get_full_name_prof'
                #, top=0*cm,left=0,style={'fontName': 'Helvetica-Bold', 'fontSize':8, 'alignment': TA_LEFT}),
                

            Label(text="|_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_",
                top=3*cm, left=8*cm,width=BAND_WIDTH,
             style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
            
        )

    class band_page_header(ReportBand):
        height = 1.3*cm
        elements = [ Image(left=0.4*cm, top=0, width=4*cm, height=5.12*cm,
                    filename= os.path.join(RUTA_PROYECTO,'../media/img/escom.gif')),


                    SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                    Label(text="Escuela Superior de Cómputo", top=0.8*cm, left=0,width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 10, 'alignment': TA_CENTER}),

                    Label(text="Nombre", top=4.5*cm, left=3*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8 ,'borderWidth': 1, 'borderColor': navy,
                    'borderPadding': 1, 'borderRadius': 2}),
                    Label(text="Boleta", top=4.5*cm, left=0.5*cm,width=1.5*cm,style={'fontName': 'Helvetica-Bold', 'fontSize':8,'borderWidth': 1, 'borderColor': navy,
                    'borderPadding': 1, 'borderRadius': 2}),
                    SystemField(expression=u'Pagina %(page_number)d de %(page_count)d', top=0.1*cm,
                        width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                    ]
        borders = {'bottom': Line(stroke_width=5)}
    
    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
                Label(text='Documento sin validez oficial', top=0.1*cm),
                SystemField(expression=u'Fecha Elaboración %(now:%Y, %b %d)s', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}

    class band_begin(ReportBand):
        height = 1*cm
        elements = [
            Label(text='Lista de Alumnos', top=0.1*cm,width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 10, 'alignment': TA_CENTER} ),
        ]

    class band_summary(ReportBand):
         elements = [
            ObjectValue(attribute_name='materia_grupo.profesor.cve_usuario.get_full_name_prof'
              , top= 0*cm,left=0,style={'fontName': 'Helvetica-Bold', 'fontSize':8, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='materia_grupo.materia.get_full_name_mate'
              , top= 0.4*cm,left=0*cm,style={'fontName': 'Helvetica-Bold', 'fontSize':8, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='materia_grupo.grupo.get_full_name_gpo'
              , top= 0.8*cm,left=0*cm,style={'fontName': 'Helvetica-Bold', 'fontSize':8, 'alignment': TA_LEFT}),
            ]

#*********************************************************************************************************
class lista_evaluaciones(Report):
    title = 'Instituto Politécnico Nacional'

    #materia_grupo.profesor.cve_usuario
    page_size = landscape(A5)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm

        bandera=True

        elements=(
            ObjectValue(attribute_name='alumno.cve_usuario',top=3*cm, left=0.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
            
            ObjectValue(attribute_name='alumno.cve_usuario.get_full_name'
                , top=3*cm,left=3*cm ,style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
            ObjectValue(attribute_name='calificacion'
                , top=3*cm,left=8*cm ,style={'fontName': 'Helvetica-Bold', 'fontSize':8}),
            
                #ObjectValue(attribute_name='materia_grupo.profesor.cve_usuario.get_full_name_prof'
                #, top=0*cm,left=0,style={'fontName': 'Helvetica-Bold', 'fontSize':8, 'alignment': TA_LEFT}),
            
        )

    class band_page_header(ReportBand):
        height = 1.3*cm
        elements = [ Image(left=0.4*cm, top=0, width=4*cm, height=5.12*cm,
                    filename= os.path.join(RUTA_PROYECTO,'../media/img/escom.gif')),


                    SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                    Label(text="Escuela Superior de Cómputo", top=0.8*cm, left=0,width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 10, 'alignment': TA_CENTER}),

                    Label(text="Nombre", top=4.5*cm, left=3*cm, width=1.5*cm, style={'fontName': 'Helvetica-Bold', 'fontSize':8 ,'borderWidth': 1, 'borderColor': navy,
                    'borderPadding': 1, 'borderRadius': 2}),
                    Label(text="Boleta", top=4.5*cm, left=0.5*cm,width=1.5*cm,style={'fontName': 'Helvetica-Bold', 'fontSize':8,'borderWidth': 1, 'borderColor': navy,
                    'borderPadding': 1, 'borderRadius': 2}),
                    Label(text="Calificación", top=4.5*cm, left=8*cm,width=1.5*cm,style={'fontName': 'Helvetica-Bold', 'fontSize':8,'borderWidth': 1, 'borderColor': navy,
                    'borderPadding': 1, 'borderRadius': 2}),
                    SystemField(expression=u'Pagina %(page_number)d de %(page_count)d', top=0.1*cm,
                        width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                    ]
        borders = {'bottom': Line(stroke_width=5)}
    
    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
                Label(text='Documento sin validez oficial', top=0.1*cm),
                SystemField(expression=u'Fecha Elaboración %(now:%Y, %b %d)s', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}

    class band_begin(ReportBand):
        height = 1*cm
        elements = [
            Label(text='Evaluaciones de Alumnos', top=0.1*cm,
                left=8*cm),
        ]

    class band_summary(ReportBand):
         elements = [
            ObjectValue(attribute_name='materia_grupo.profesor.cve_usuario.get_full_name_prof'
              , top= 0*cm,left=0,style={'fontName': 'Helvetica-Bold', 'fontSize':8, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='materia_grupo.materia.get_full_name_mate'
              , top= 0.4*cm,left=0*cm,style={'fontName': 'Helvetica-Bold', 'fontSize':8, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='materia_grupo.grupo.get_full_name_gpo'
              , top= 0.8*cm,left=0*cm,style={'fontName': 'Helvetica-Bold', 'fontSize':8, 'alignment': TA_LEFT}),
            ]