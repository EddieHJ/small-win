from fastapi import FastAPI
import small_win
app = FastAPI(title="TEST")

@app.get("/")
def test():
    return {"package name test": small_win.__name__,}