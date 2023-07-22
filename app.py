import os
from fastapi import FastAPI, UploadFile, File, Request
from pydantic import BaseModel
from typing import List
from embedchain import OpenSourceApp
import os
os.environ["OPENAI_API_KEY"] = "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"


app = FastAPI()
naval_chat_bot = OpenSourceApp()

class PDF(BaseModel):
    file: bytes
    filename: str

@app.post("/upload_pdf")
async def upload_pdf(pdf: UploadFile = File(...)):
    print("file addition")
    contents = await pdf.read()
    if pdf.filename.endswith('.pdf'):
        file_path = os.path.join("files", pdf.filename)
        with open(file_path, "wb") as f:
            f.write(contents)
        naval_chat_bot.add("pdf_file", file_path)
        os.remove(file_path)
        return {"message": "PDF file uploaded and added successfully."}
    else:
        return {"message": "Only PDF files are allowed."}



@app.post("/chat")
async def chat_with_files(req: Request):
    print("chat")
    rqs = await req.json()
    
    chat_input = rqs["chat_input"]
    responses = naval_chat_bot.chat(chat_input)
    return {"chat_putput" : responses}
