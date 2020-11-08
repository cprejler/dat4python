import requests
import bs4
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('job', __name__)


def get_job_data():
    html = requests.get('https://www.jobindex.dk/jobsoegning?q=Datamatiker')
    txt = html.text
    soup = bs4.BeautifulSoup(txt, 'html.parser')
    mydivs = soup.findAll("div", {"class": "jobsearch-result"})

    result = []
    jobs = []
    for item in mydivs:
        result.extend(item.findAll("b"))

    for res in result:
        jobs.append(res.getText())

    return jobs


@bp.route('/create', methods=('GET', 'POST'))
def insert_job():
    if request.method == 'GET':
        jobs = get_job_data()
        print(jobs)
        
        db = get_db() 
        for job in jobs:
            db.execute(
            'INSERT INTO jobs (title)'
            ' VALUES (?)',
            (job)
        )
        db.commit()


