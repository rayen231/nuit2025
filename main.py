from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from chat import chato
from controll import controll

app = FastAPI()
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
    response = chato(str(emotion), query)
    output = {
        "easters": easters,
        "response": response
    }

    return JSONResponse(content=output) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
