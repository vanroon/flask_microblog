from app import app

@app.route('/dutch')
def index():
    return "Hallo wereld"
