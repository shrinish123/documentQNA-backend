import os

from fastapi import APIRouter,UploadFile,File
from api.models.document import Document
from api.database import database,document_table

router = APIRouter(prefix='/document')

DOCUMENTS_DIR = os.path.join(os.path.dirname(__file__), '../..', 'docs')


@router.post("/create")
async def create_doc(file: UploadFile = File(...)):

    print(f'file={file}')

    # Save file to document directory
    file_path = os.path.join(DOCUMENTS_DIR, file.filename)
    with open(file_path, 'wb') as destination:
        for chunk in file.file:
            destination.write(chunk)
    
    ## Save data to document_table and return doc_id 
    document_data = {
        'title' : file.filename,
        'path'  : file_path
    }
    query = document_table.insert().values(document_data)
    document_id = await database.execute(query)
    
    return {**document_data, "id": document_id}


@router.get('/getAll', response_model=list[Document])
async def get_all_documents():
      query = document_table.select()
      return await database.fetch_all(query)
