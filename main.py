from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
    return {"Message": "Creating a FastAPI application with Docker."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}