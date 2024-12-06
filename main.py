from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from chat import chato
from controll import controll
from rag import intialize , add_query_to_db , search_query_in_db
import uvicorn

app = FastAPI()
db = intialize()
origins = "[*]"
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(query: str):
    controll_response = controll(query)
    emotion = controll_response['Emotion']
    easters = controll_response['Easter']
    history = search_query_in_db(query,db)
    print(add_query_to_db(query,db))
    response = chato(str(emotion), query, history)
    output = {
        "easters": easters,
        "response": response
    }

    return JSONResponse(content=output) 

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
