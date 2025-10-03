# Personal Portfolio Website

A simple and elegant personal portfolio website built with Flask and Bootstrap.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean and professional design with smooth animations
- **Multiple Pages**: Home, About, Projects, and Contact pages
- **Easy to Customize**: Simple Python dictionary structure for easy content updates
- **Bootstrap Integration**: Uses Bootstrap 5 for responsive components
- **Font Awesome Icons**: Beautiful icons throughout the site

## Project Structure

```
portfolio/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── templates/            # HTML templates
│   ├── base.html        # Base template with navigation and footer
│   ├── index.html       # Home page
│   ├── about.html       # About page
│   ├── projects.html    # Projects page
│   └── contact.html     # Contact page
│
└── static/              # Static files
    └── css/
        └── style.css    # Custom CSS styles
```

## Installation

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv portfolio_env
   source portfolio_env/bin/activate  # On Windows: portfolio_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask development server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

The application will be running in development mode with debug enabled.

## Customization

### Personal Information

Edit the `portfolio_data` dictionary in `app.py` to add your personal information:

```python
portfolio_data = {
    "name": "Your Name",
    "title": "Your Title",
    "email": "your.email@example.com",
    "phone": "+1 (555) 123-4567",
    "location": "Your City, Country",
    "about": "Your description...",
    # ... add your skills, experience, education, projects
}
```

### Styling

- Modify `static/css/style.css` to change colors, fonts, and layout
- The CSS uses CSS custom properties (variables) for easy color customization
- Bootstrap classes can be customized or overridden

### Adding New Pages

1. Add a new route in `app.py`
2. Create a new HTML template in the `templates/` folder
3. Add navigation links in `base.html`

### Social Media Links

Update the social media links in the footer and contact page by replacing the `#` placeholders with your actual profiles.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Fonts**: System fonts (Segoe UI, etc.)

## Deployment

For production deployment, consider:

1. **Set Flask to production mode**:
   ```python
   app.run(debug=False)
   ```

2. **Use a production WSGI server** like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. **Deploy to platforms** like:
   - Heroku
   - Vercel
   - PythonAnywhere
   - DigitalOcean
   - AWS

## Future Enhancements

- Add a blog section
- Implement contact form functionality
- Add project filtering and search
- Include a resume download feature
- Add analytics tracking
- Implement dark/light theme toggle
- Add animation libraries (AOS, etc.)

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to fork this project and customize it for your own use. If you have suggestions for improvements, please feel free to submit a pull request or open an issue.

---

**Happy coding!** 🚀