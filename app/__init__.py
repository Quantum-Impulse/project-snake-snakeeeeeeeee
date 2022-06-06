from optparse import TitledHelpFormatter
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

work_json = {
    "David":[
        {
            "title": "Production Engineer Fellow",
            "image": '../static/img/fellowship.png',
            "company": "MLH Fellowship",
            "date": "May 2022 - Current",
            "bullets": [
                {
                    "description": "Selected from 100 students for a 12 week program sponsored by Meta learning and working on Production / Site Reliability Engineering and DevOps.",    
                },
                {
                    "description": "Working with Linux Systems, Flask, Docker, GitHub Actions, cAdvisor and other technologies to keep services and applications running and highly available."
                },
            ]
        },
        {
            "title": "Fullstack Developer",
            "image": '../static/img/AGSMAC.png',
            "company": "AGSMAC (Freelancer)",
            "date": "December 2021 - April 2022",
            "bullets": [
                {    
                    "description": "Developed a new redesign of the .org page, by creating UI designs and making an UX research of 75 persons who used to use the old version of the page.",
                },
                {
                    "description": "Reduced 60% of the technical cost of the site by building a new back end architecture and migrating the old database to Mongo Db.",
                },
                 {
                    "description": "Managed to increase the trafic of visitors to the site by 230% by building the site new front end with technologies like React, Firebase and Google Maps"
                },
            ]
        },
        {
            "title": "UX/UI Designer",
            "company": "omegaUp",
            "image": '../static/img/omega.png',
            "date": "February 2021 - June 2021",
            "bullets": [
                {    
                    "description": "Developed user-friendly design concepts for a new .org page, ensuring that all of the organization reFuirements were met and the procedures were fully followed",
                },
                {
                    "description": "Revamped website flows , reducing the freFuency of misdirected customer service Fueries by 30% and increasing traffic to previously neglected pages",
                },
                 {
                    "description": "Reduced the design cost by 40% by creating a plan to merge related pages to one design system." 
                },
            ]
        },
    ],
    "Enrique":[
        {
            
        }
    ]
}

education_json = {
 "David":[
     {
         "school": "Universidad Autónoma de Nuevo León",
         "title": "Bachelor of Science in Computer Science",
         "date":"Graduating in 2023",
         'image': '../static/img/uanl.png',
     }
 ],
 "Enrique":[
     {
         
     }
 ]   
}
@app.route('/')
def index():
    return render_template('index.html', title="David & Enrique", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('/about-us/index.html', title="+ About Us", url=os.getenv("URL"))

@app.route('/about/quicksearch')
def quick_search():
    return render_template('/about-us/quick-search.html', title="+ About Us", url=os.getenv("URL"))

@app.route('/work/david')
def work():
    return render_template('/about-us/work.html', title="Work Experience", work_id="David", data=work_json, url=os.getenv("URL"))

@app.route('/work/enrique')
def work2():
    return render_template('/about-us/work.html', title="Work Experience", work_id="Enrique", data=work_json, url=os.getenv("URL"))

@app.route('/education/david')
def education():
    return render_template('/about-us/education.html', title="Education", education_id="David", data=education_json, url=os.getenv("URL"))

@app.route('/education/enrique')
def education2():
    return render_template('/about-us/education.html', title="Education", education_id="Enrique", data=education_json, url=os.getenv("URL"))
