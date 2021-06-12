from flask import Blueprint, flash, render_template, request, session, abort, redirect, url_for
import requests
import os

appbp = Blueprint('auth',__name__, url_prefix = '')
@appbp.route('/main')
def main():
    sender = requests.get('http://localhost:5000/apis/init')
    print(sender)
    return render_template('main.html')
