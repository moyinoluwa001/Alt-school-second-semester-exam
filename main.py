from fastapi import FastAPI
from routes import user_routes, course_routes, enrollment_routes

app = FastAPI(title="EduTrack Lite API")


@app.get("/", tags=["Home"])
def read_root():
    return {"message": "Welcome to the EduTrack Lite API!"}


app.include_router(user_routes.router)
app.include_router(course_routes.router)
app.include_router(enrollment_routes.router)