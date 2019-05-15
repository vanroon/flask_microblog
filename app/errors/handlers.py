from flask import render_template
from app import db
from app.errors import bp

@bp.app.errorhandler(404)
def not_found_error(error):
    return render_template('error/404.html'), 404

@bp.app.errorhandler(500)
def internal_error(error):
    # rollback any changes 
    db.session.rollback()
    return render_template('error/500.html'), 500
