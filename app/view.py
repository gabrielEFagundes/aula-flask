from app import app

@app.route('/')
def homepage():
    return 'Minha página FLASK.'