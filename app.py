from flask import Flask, render_template

app = Flask(__name__)

# Portfolio data - you can modify this with your actual details
portfolio_data = {
    "name": "Your Name",
    "title": "Software Developer",
    "email": "your.email@example.com",
    "phone": "+1 (555) 123-4567",
    "location": "Your City, Country",
    "about": "Passionate software developer with experience in web development, data analysis, and problem-solving. Always eager to learn new technologies and take on challenging projects.",
    "skills": [
        "Python", "JavaScript", "Flask", "HTML/CSS", 
        "Git", "SQL", "React", "Node.js"
    ],
    "experience": [
        {
            "title": "Software Developer",
            "company": "Tech Company",
            "duration": "2022 - Present",
            "description": "Developed web applications using Python and JavaScript frameworks."
        },
        {
            "title": "Junior Developer",
            "company": "Startup Inc",
            "duration": "2021 - 2022",
            "description": "Worked on various projects involving database design and API development."
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Computer Science",
            "school": "University Name",
            "year": "2021"
        }
    ],
    "projects": [
        {
            "name": "Portfolio Website",
            "description": "A personal portfolio website built with Flask and Bootstrap",
            "technologies": ["Python", "Flask", "HTML", "CSS", "Bootstrap"]
        },
        {
            "name": "Data Analysis Tool",
            "description": "A tool for analyzing and visualizing data using Python",
            "technologies": ["Python", "Pandas", "Matplotlib", "Jupyter"]
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)