from fastapi import FastAPI
from small_win.api.chat import router
app = FastAPI(title="small win v0.1")
app.include_router(router)