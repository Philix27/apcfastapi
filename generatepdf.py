from turtle import st, width
from fpdf import FPDF, HTML2FPDF

# create FPDF object 
# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4', 'A5', 'Letter', 'Legal', (100, 150))
#  size: [242.64, 153],

def generatePdf(name: str, email: str, state_code: str,state:str, lga:str, ward:str, ):
    card_width = 86
    card_height = 54
    card_font = 6.5
    card_spacer = 4
    
    pdf = FPDF(unit='mm',orientation='P',format=(card_width, card_height))
    # Add Page
    pdf.add_page()
    # fonts('times', "courier", "helvetica", "symbol", "")
    # fontStyles
    # "B" (bold), "U" (underline), "I" (Italics), '' (regular), combination (i.e, (BU))
    pdf.set_font('helvetica', '', 8)
    pdf.set_margin(4)
    pdf.set_author("Felix Eligbue")
    pdf.set_title("Membership Card")
     
    pdf.image("logo.png" ,alt_text="logo", h=4*1.2, w=5*1.2, title="APC LOGO", x=5, y=2) 
    pdf.set_font('helvetica', 'B', card_font)
    pdf.text(txt="ALL PROGRESSIVES CONGRESS (APC)",  x=card_width/2 - 20, y=4.3 )
    pdf.ln(card_spacer)
    pdf.set_font('helvetica', 'U', 4 )
    pdf.text(txt="JUSTICE, PEACE & UNITY",  x=card_width/2 - 5, y=6.5)
    # pdf.text(txt="Texty Texter", x=242.64/2, y=50)
    # pdf.cell(txt="JUSTICE, PEACE & UNITY", )
    pdf.ln(card_spacer)
    pdf.ln(card_spacer)
    # pdf.set_image_filter("Dodge")
    # pdf.image_filter()
    pdf.image("logo.png" ,alt_text="logo", h=4*6, w=5*6, title="APC LOGO", x=card_width/2 - 12, y=card_height/2 - 10,)
    
    pdf.set_font('helvetica', 'B', card_font)
    pdf.cell(txt=f"NAME:", align='L', )
    pdf.set_font('helvetica', '', card_font)
    pdf.cell(txt=name, align='L')
    pdf.ln(card_spacer)
    
    pdf.set_font('helvetica', 'B', card_font)
    pdf.cell(txt=f"EMAIL:", align='L', )
    pdf.set_font('helvetica', '', card_font)
    pdf.cell(txt=email, align='L')
    pdf.ln(card_spacer)
    
    pdf.set_font('helvetica', 'B', card_font)
    pdf.cell(txt=f"STATE:", align='L', )
    pdf.set_font('helvetica', '', card_font)
    pdf.cell(txt=state, align='L')
    pdf.ln(card_spacer)
    
    pdf.set_font('helvetica', 'B', card_font)
    pdf.cell(txt=f"LGA:", align='L', )
    pdf.set_font('helvetica', '', card_font)
    pdf.cell(txt=lga, align='L')
    pdf.ln(card_spacer)
    
    pdf.set_font('helvetica', 'B', card_font)
    pdf.cell(txt=f"WARD:", align='L', )
    pdf.set_font('helvetica', '', card_font)
    pdf.cell(txt=ward, align='L')
    pdf.ln(card_spacer)
    
    pdf.set_font('helvetica', 'B', card_font)
    pdf.cell(txt=f"MEMBER ID:", align='L', )
    pdf.set_font('helvetica', '', card_font)
    pdf.cell(txt=state_code, align='L')
    pdf.ln(card_spacer)
    
  

    # pdf.text(txt="Texty Texter", x=242.64/2, y=50)
    #! Footer
    
    pdf.set_font('helvetica', 'B', card_spacer)
    pdf.text(txt="APC MEMBERSHIP ID CARD",   x=card_width/2 - 7, y=card_height - 3)
    pdf.ln(10)
    
    pdf.output(name="idcard.pdf" )


