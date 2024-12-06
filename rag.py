from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import JinaEmbeddings

api_key = "jina_e01f12a794f14a409806a73ed3020d209hmgkX0oQz2KICmm_fQV47F34fBp"

# embedding 
embeddings = JinaEmbeddings(jina_api_key=api_key, model_name='jina-embeddings-v2-base-en')

def intialize():
    db = Chroma.from_texts(["hello"], embeddings, persist_directory="db")
    return db

# Load a PDF document
def add_query_to_db(query,db):

    # Create or load the vector store
    db.add_texts([query])
    return "added to db"

def search_query_in_db(query,db):
    # Create or load the vector store
    retrived = db.similarity_search(query)
    return retrived
db=intialize()
#print(add_query_to_db(" my name is raghav",db))
#print(search_query_in_db("my name is raghav"))