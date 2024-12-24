from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def home():
    return render_template('Website.html')

# Hakkımızda sayfası
@app.route('/hakkimizda')
def hakkimizda():
    return render_template('Hakkımızda.html')

# Hizmetlerimiz sayfası
@app.route('/hizmetlerimiz')
def hizmetlerimiz():
    return render_template('Hizmetlerimiz.html')

# Galeri sayfası
@app.route('/galeri')
def galeri():
    return render_template('Galeri.html')

# İletişim sayfası
@app.route('/iletisim')
def iletisim():
    return render_template('İletişim.html')

@app.route('/loginsignup')
def loginsignup():
    return render_template('loginsignup.html')


if __name__ == '__main__':
    app.run(debug=True)
