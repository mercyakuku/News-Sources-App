from flask import render_template
from . import main

@main.errorhandler(404)
def four_zero_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourzerofour.html'),404