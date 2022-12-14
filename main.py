from http.client import responses
from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse

from generatepdf import generatePdf
from member import Member

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to the APC ID Card Generator"}


@app.post("/pdfgen")
def create_pdf():
    generatePdf(
         name="Iyanu Gbenga", 
        email="kpelenge@gmail.com", 
        state_code="KB/BRN/ZAR/0902", 
        state="KEBBI",
        lga="ZAURO", 
        ward="Ambursa" ,
    )
    return {"msg": "Created a card"}
    # return FileResponse("idcard.pdf", filename="membership_card")
    
@app.get("/pdf", )
def create_pdf(member: Member):
    # print(member)
    generatePdf(
        name=member.name ,
        email=member.email, 
        state_code=member.state_code, 
        state=member.state,
        lga=member.lga, 
        ward=member.ward, 
    )
    return FileResponse("idcard.pdf", filename="membership_card")



