import datetime
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)


site_owner = "İbrahim Arslan"
github_url = "https://github.com/arslan1616"
linkedin_url = "https://www.linkedin.com/in/ibrahim-arslan-28b26b260/"
email_address = "ibrahimars1224@gmail.com"

common_context = {
    'site_owner': site_owner,
    'github_url': github_url,
    'linkedin_url': linkedin_url,
    'email_address': email_address,
    'current_year': datetime.datetime.now().year,
    'nav_links': [
        {'name': 'Anasayfa', 'url': 'index'},
        {'name': 'Hakkımda', 'url': 'about'},
        {'name': 'CV', 'url': 'cv_page'},
        {'name': 'Projelerim', 'url': 'projects'},
        {'name': 'İletişim', 'url': 'contact'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', **common_context)

@app.route('/about')
def about():
    tech_stack = ["Python", "C", "Java","PostgreSQL", "Flask", "HTML", "CSS", "JavaScript","Machine Learning"]
    education = [
        {"institution": "Konya Teknik Üniversitesi", "degree": "Yazılım Mühendisliği Lisans", "year": "2021-2026"},
        {"institution": "Ahmet Hamdi Gökbayrak Fen Lisesi", "year": "2016-2020"}
    ]
    context = {**common_context, 'tech_stack': tech_stack, 'education': education, 'page_title': 'Hakkımda'}
    return render_template('about.html', **context)

@app.route('/cv')
def cv_page():
    context = {**common_context, 'page_title': 'CV'}
    return render_template('cv.html', **context)

@app.route('/download_cv')
def download_cv():
    return send_from_directory('static/cv', 'ibrahim_cv.pdf', as_attachment=True)

@app.route('/projects')
def projects():

    github_projects_data = [

        {
            "name": "FinAI Web Uygulaması",
            "description": "Finans alanı ile alakalı yapmış ve yayınlamış olduğum web projem.",
            "url": f"{github_url}/finansal_tahmin_sistemi-main", # Örnek
            "image": url_for('static', filename='images/finaiWeb_resim.png'), # Farklı bir görsel
            "tags": ["Python", "Veri Analizi", "Web"]
        },
        {
            "name": "FinAI Mobil Uygulama ",
            "description": "Java kullanılarak oluşturulan finansal tahmin modeli için bir mobil uygulama.",
            "url": f"{github_url}/FinAi-Mobile", # Örnek
            "image": url_for('static', filename='images/finai_resim.png'),
            "tags": ["Java", "Machine Learning", "Mobil","Android Studio"]
        },
        {
            "name": "Veteriner Takip Sistemi ",
            "description": "Veterinerlerin takip için kullanabileceği web tabanlı bir proje.",
            "url": f"{github_url}/VeterinerTakipSistemi",
            "image": url_for('static', filename='images/Veteriner_resim.png'),
            "tags": ["Web", "JavaScript", "Docker"]
        },
        {
            "name": "Biİndirim Telegram Botu ",
            "description": "Ünlü giyim markalarının web sitelerine stok gelince telegrama bildirim gönderen bot ",
            "url": f"{github_url}/BiIndirim",
            "image": url_for('static', filename='images/biİndirim_resim.png'),
            "tags": ["Telegram", "Web scraping", "Python"]
        },
        {
            "name": "Kütüphane Otomasyonu ",
            "description": "Docker kullanılarak çalıştırılan kütüphane kitap takip sistemi ",
            "url": f"{github_url}/K-t-phaneSistemi",
            "image": url_for('static', filename='images/kutuphane_resim.png'),
            "tags": ["Docker", "Python", "Web"]
        },

    ]
    context = {**common_context, 'github_projects': github_projects_data, 'page_title': 'Projelerim'}
    return render_template('projects.html', **context)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    context = {**common_context, 'page_title': 'İletişim'}
    return render_template('contact.html', **context)

if __name__ == '__main__':
    app.run(debug=True)