from flask import Flask, render_template

app = Flask(__name__)

# Portfolio data - updated with actual LinkedIn information
portfolio_data = {
    "name": "Manjunath T",
    "title": "Software Engineer II at Cisco",
    "email": "4682ssbj@gmail.com",
    "phone": "+91 7899643162",
    "location": "Bengaluru, Karnataka, India",
    "about": "Experienced Software Engineer with 3+ years at Cisco, specializing in service automation and network configuration compliance. Passionate about automation solutions, Infrastructure as Code (IaC), and enhancing efficiency through innovative technology solutions. Strong background in cross-team collaboration and continuous integration.",
    "skills": [
        "Python", "JavaScript", "Camunda", "Git", "CI/CD", 
        "Infrastructure as Code (IaC)", "Automation", "Agile Methodologies",
        "Cross-team Collaboration", "Network Services", "Flask", "HTML/CSS"
    ],
    "experience": [
        {
            "title": "Software Engineer II",
            "company": "Cisco",
            "duration": "Nov 2023 - Present",
            "description": "Leading advanced automation projects and service automation solutions for Network Services Team. Continuing to deliver robust automation using Infrastructure as Code (IaC) model and enhancing team efficiency."
        },
        {
            "title": "Software Engineer",
            "company": "Cisco",
            "duration": "Aug 2022 - Oct 2023",
            "description": "Delivered automated network configuration compliance project for Network Services Team. Utilized Camunda, JavaScript, Python, Git and CI/CD for robust automation using Infrastructure as Code (IaC) model. Led the project to successful implementation and collaborated with network services team to enhance efficiency and security through automation solutions."
        },
        {
            "title": "Technical Undergraduate Intern",
            "company": "Cisco",
            "duration": "Jan 2022 - Jul 2022",
            "description": "Implemented automation solutions using Camunda-based in-house platforms like BPA and NSO. Utilized JavaScript and Python for scripting and automation tasks. Contributed to enhancing efficiency within the network services team through process automation and optimization."
        }
    ],
    "education": [
        {
            "degree": "Bachelor's degree, Computer Science",
            "school": "JSS Science and Technology University",
            "year": "2018 - 2022"
        },
        {
            "degree": "Primary and Secondary Education, Science (10+2)",
            "school": "Sainik School, Bijapur",
            "year": "2011 - 2018"
        }
    ],
    "certifications": [
        {
            "name": "Technical Support Fundamentals",
            "issuer": "Coursera",
            "date": "Aug 2020",
            "credential": "MHDY827SB3PU"
        },
        {
            "name": "The Bits and Bytes of Computer Networking",
            "issuer": "Coursera",
            "date": "Aug 2020",
            "credential": "MMVAJNFP9V4R"
        }
    ],
    "volunteering": [
        {
            "role": "Cadet",
            "organization": "National Cadet Corps - India",
            "duration": "Jun 2011 - Mar 2018",
            "category": "Education"
        },
        {
            "role": "Editor",
            "organization": "IEEE SJCE",
            "duration": "Jun 2020 - Jun 2022",
            "category": "Science and Technology"
        }
    ],
    "projects": [
        {
            "name": "Network Configuration Compliance Automation",
            "description": "Automated network configuration compliance system for Cisco's Network Services Team using Camunda workflow engine and Infrastructure as Code principles",
            "technologies": ["Python", "JavaScript", "Camunda", "Git", "CI/CD", "IaC"],
            "status": "Completed",
            "impact": "Enhanced security and efficiency for network services"
        },
        {
            "name": "Service Automation Platform",
            "description": "Implemented automation solutions using Camunda-based in-house platforms (BPA and NSO) to enhance network services efficiency",
            "technologies": ["Python", "JavaScript", "Camunda", "BPA", "NSO"],
            "status": "Completed",
            "impact": "Streamlined network service operations"
        },
        {
            "name": "Personal Portfolio Website",
            "description": "A responsive personal portfolio website built with Flask and Bootstrap, featuring modern UI/UX and deployed on GitHub",
            "technologies": ["Python", "Flask", "HTML", "CSS", "Bootstrap", "Git"],
            "status": "Live",
            "impact": "Professional online presence"
        }
    ],
    "achievements": [
        "Led successful implementation of network configuration compliance automation",
        "3+ years of continuous service at Cisco with promotions",
        "Strong background in cross-team collaboration and project leadership",
        "Active contributor to automation and efficiency improvements"
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