
import logging
from fastapi import FastAPI

logger = logging.getLogger("app")

from src.ctff import FeatureFlaggerMiddleware, featureflag

app = FastAPI(
  title="CTFF python example"
)

# app.add_middleware(FeatureFlaggerMiddleware, settings={})

@app.on_event("startup")
async def startup():
  logger.info("Application startup")

@app.on_event("shutdown")
async def shutdown():
  logger.info("Application shutdown")


@app.get("/")
async def root():
  return {"message": "Hello World", "app_color": get_app_color()}


@featureflag("use_new_color")
def get_app_color(use_new_color = False):
  if use_new_color:
    return "Orange"
  else:
    return "Pink"
