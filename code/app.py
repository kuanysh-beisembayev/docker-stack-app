from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def index():
    return 'index'


@app.get('/error')
async def error():
    return 1 / 0


if __name__ == '__main__':
    uvicorn.run('code.app:app', host='0.0.0.0')
