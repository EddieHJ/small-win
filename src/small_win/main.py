from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pathlib

from small_win.api.chat import router as chat_router

# --- 路径计算修正 ---
# main.py 在 src/small_win/ 里面, 所以需要向上跳3级才能到项目根目录
PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent
STATIC_ROOT = PROJECT_ROOT / "static"

app = FastAPI(
    title="Small Win AI",
    description="一个将模糊目标拆解为具体步骤的AI助手",
    version="0.1.0"
)

# --- CORS 中间件 ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API 路由 ---
# 将 API 路由挂载到 /api 前缀下，避免与静态文件冲突
app.include_router(chat_router, prefix="/api")

# --- 挂载静态文件 ---
# 检查一下目录是否存在，如果不存在就给一个更友好的提示
if not STATIC_ROOT.is_dir():
    raise RuntimeError(f"静态文件目录未找到，请确保它在项目根目录: {STATIC_ROOT}")

# 将 static 文件夹挂载到根路径 "/"
app.mount("/", StaticFiles(directory=STATIC_ROOT, html=True), name="static")

