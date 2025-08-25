from fastapi import FastAPI
from titiler.application.main import app as titiler_app
from titiler.xarray.factory import TilerFactory as XarrayTilerFactory

# Start with titiler.application app
app = titiler_app

# Add xarray endpoints
xarray = XarrayTilerFactory(router_prefix="/xarray")
app.include_router(xarray.router, prefix="/xarray", tags=["Xarray Datasets"])

@app.get("/", tags=["Meta"])
def root():
    return {
        "message": "Welcome to the Meta TiTiler App 🚀",
        "available_endpoints": {
            "COG": "/cog",
            "Mosaic": "/mosaic",
            "STAC": "/stac",
            "Xarray": "/xarray",
        },
        "docs": "/docs",
        "redoc": "/redoc",
    }
