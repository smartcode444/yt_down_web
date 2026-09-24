import re
from handler import VideoHandler
from thumbnail import fetch_thumbnail_response
from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import JSONResponse
# from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from pathlib import Path

app = FastAPI(debug=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class App:
    def __init__(self):
        self.handler = VideoHandler()
        self.video_data = None
        self.video_id = None
        self.video_thumbnail = None
        self.video_title = None


    def validate_url(self, url: str) -> bool:
        """Basic validation for Youtube URLs."""
        pattern = re.match(
            r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)[\w-]{11}(.*)?$', 
            url, 
            re.IGNORECASE 
        )
        return bool(pattern)

    def fetch_data(self, url: str):
        """Fetching video metadata"""
        self.video_data = self.handler.fetch_metadata(url)
        self.video_id = self.handler.fetch_metadata(url)
        self.video_thumbnail = fetch_thumbnail_response(self.video_id)
        self.video_title = self.handler.title

app = App()

@app.get("/")
def read_root(request: Request):
    """home page"""
    return templates.TemplateResponse(
        request=request, name="index.html", context={"title": "home_page"}
    )

@app.get("/fetch")
def fetch_video(request:Request, url: str = Query(...)):
    """Download Youtube videos"""
    if not url:
        return JSONResponse({"ok": False, "error": "URL is required"}, status_code=400)

    if not app.validate_url(url):
        return JSONResponse({"ok": False, "error": "Invalid Youtube URL"}, status_code=400)

    app.fetch_data(url)

    return {
        "ok": True,
        "title": app.video_title,
        "thumbnail": app.video_thumbnail
    }






# @app.get("/download-pdf")
# async def get_pdf():
#     file_path = Path("files/SIWES.jpeg")
#     if not file_path.is_file():
#         raise HTTPException(status_code=404, detail="File not found")
#     return FileResponse(file_path)