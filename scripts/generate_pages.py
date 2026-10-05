import os
import re

tortas = [
    {"name": "Manjar Nuez", "desc": "Bizcocho de vainilla con manjar y nueces.", "price": ""},
    {"name": "Manjar Piña", "desc": "Bizcocho vainilla con manjar y trozos de piña en almíbar.", "price": ""},
    {"name": "Francisca", "desc": "Bizcocho de vainilla con manjar y trozos de chocolate, mermelada de frambuesa y frambuesas naturales.", "price": ""},
    {"name": "Torta Mixta", "desc": "Bizcocho de vainilla y de chocolate, manjar, crema pastelera, crema moka y trozos de chocolate.", "price": ""},
    {"name": "Chocolate", "desc": "Bizcocho de chocolate, ganache de chocolate con trozos de chocolate, manjar, cubierta de ganache.", "price": ""},
    {"name": "Torta de Manjarate", "desc": "Bizcocho con mousse de manjar.", "price": ""},
    {"name": "Turrón De Nuez", "desc": "Bizcocho de nuez, manjar con trozos de chocolate, disco de merengue cubierta en merengue.", "price": ""},
    {"name": "Torta Oreo", "desc": "Bizcocho de galleta oreo, manjar, trozos de chocolate, crema de oreo.", "price": ""},
    {"name": "Tres leches", "desc": "Bizcocho de vainilla remojada en 3 leches, cubierta en merengue.", "price": ""},
    {"name": "Pompadour", "desc": "Plátano, frambuesa, lúcuma, vainilla o chocolate, cubierta en crema o merengue.", "price": ""},
    {"name": "Dulce Margarita (amor-amor)", "desc": "Hojarascas, rellenos de manjar con crema chantilly, mermelada de frambuesa y frambuesas naturales con crema pastelera.", "price": ""},
    {"name": "Cuatro leches", "desc": "Bizcocho de vainilla remojada en 3 leches, crema pastelera, cubierta en merengue.", "price": ""},
    {"name": "Danesa", "desc": "Torta de hoja, manjar, trozos de chocolate o nuez, crema pastelera.", "price": ""},
    {"name": "Cielo", "desc": "Bizcocho de vainilla y hojarascas, manjar, trozos de chocolate, frambuesas naturales, disco de merengue, crema pastelera.", "price": ""},
    {"name": "Chifón", "desc": "Bizcocho de naranja, manjar, confitura de naranja, crema de naranja cubierta en merengue.", "price": ""},
    {"name": "Torta helada", "desc": "Frambuesa, lúcuma, chocolate o vainilla.", "price": ""},
    {"name": "Papaya a la crema", "desc": "Bizcocho de vainilla, con un mousse de papaya, manjar, papayas en almíbar, cubierta en crema de papaya.", "price": ""},
    {"name": "Torta de durazno", "desc": "Bizcocho de vainilla, manjar con duraznos en almíbar, cubierta con merengue o crema.", "price": ""}
]

premium = [
    {"name": "Tentación", "desc": "Deliciosos y húmedos bizcocho de chocolate, crema frambuesas natural, un sabroso galletón crocante de nuez, manjar, disco de merengue y una cobertura de el mismo manjar acompañado de praline de nuez.", "price": ""},
    {"name": "Caluga (vainilla o chocolate)", "desc": "Masa de galleta con nueces, deliciosa caluga artesanal junto con frambuesas naturales con manjar, además de un crocante praline de nuez.", "price": ""},
    {"name": "Alejandra", "desc": "Bizcocho de nuez con manjar discos de hojarasca rellenos de manjar y pastelera, discos de merengue con crema y frambuesa y bizcocho de vainilla.", "price": ""},
    {"name": "Amapola", "desc": "Biscocho de amapola relleno con manjar, frambuesas naturales o crema de chocolate.", "price": ""},
    {"name": "Encanto", "desc": "Bizcocho de chocolate con crema de chocolate, hojarascas con crema y frambuesas naturales y manjar.", "price": ""},
    {"name": "Torta panqueques", "desc": "Chocolate, trufa, frambuesa, lúcuma, chocolate menta, naranja, manjar nuez.", "price": ""},
    {"name": "Cinco leches", "desc": "Bizcocho de vainilla remojada en 3 leches, crema pastelera, manjar, cubierta en merengue.", "price": ""},
    {"name": "Silvia", "desc": "Bizcocho de amapola, manjar con trozos de chocolate, acompañado de hojarascas con crema de chocolate y frambuesas naturales, crema pastelera casera y disco de merengue.", "price": ""},
    {"name": "Oreo frambuesa", "desc": "Bizcocho de oreo, manjar con trozos de chocolate, crema de frambuesas naturales, manjar con galletas de oreo.", "price": ""},
    {"name": "Crocante de Nuez", "desc": "Crocante de nuez con relleno de manjar y frambuesa.", "price": ""},
    {"name": "Torta Amapola", "desc": "Exquisita torta de bizcocho de amapola, rellena con manjar, trozos de chocolate y frambuesas naturales.", "price": ""},
    {"name": "Torta Tres Leches Pastelera Frambuesa", "desc": "Torta tres leches, acompañada de crema pastelera y frambuesas naturales.", "price": ""}
]

dulces = [
    {"name": "Pastelitos para coctel", "desc": "Ciento de pastelitos de coctel surtidos.", "price": ""},
    {"name": "Tartaletas Variedades", "desc": "Tartaleta de Durazno - Tartaleta Nuez - Tartaleta de frutos Rojos.", "price": ""},
    {"name": "Queque Variedades", "desc": "Queque Vainilla - Queque Naranja - Queque Marmoleado", "price": ""},
    {"name": "Pie Variedades", "desc": "Pie de limón - Pie de Frambuesa", "price": ""}
]

def format_card(item):
    return f'''            <div class="pastel-card" style="display:flex; flex-direction:column; justify-content:space-between; height: 100%;">
                <img src="img/Logo%20Tentaciones%20lore%20Horizontal.png" alt="{item['name']}" style="object-fit:cover; height:200px; width:100%;">
                <div style="padding:15px; flex-grow:1; display:flex; flex-direction:column;">
                    <h3 style="margin-bottom:10px;">{item['name']}</h3>
                    <p style="font-size: 0.9em; flex-grow:1;">{item['desc']}</p>
                    <button class="btn-oscuro" style="margin-top:15px;">Comprar Ahora</button>
                </div>
            </div>'''

def generate_catalogo(items):
    cards = [format_card(item) for item in items]
    return '<div class="catalogo" style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; padding: 20px;">\\n' + '\\n'.join(cards) + '\\n        </div>'

with open('pasteles.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Replace Nav
nav_regex = re.compile(r'<ul class="enlaces">.*?</ul>', re.DOTALL)
new_nav = '''<ul class="enlaces">
            <li><a href="index.html">Novedades</a></li>
            <li><a href="pasteles.html">Tortas</a></li>
            <li><a href="premium.html">Tortas Premium</a></li>
            <li><a href="dulces.html">Variedades Dulces</a></li>
            <li><a href="contacto.html">Contacto</a></li>
        </ul>'''

footer_nav_regex = re.compile(r'<ul>\\s*<li><a href="index\.html">Novedades</a></li>\\s*<li><a href="pasteles\.html">Tortas</a></li>\\s*<li><a href="contacto\.html">Contacto</a></li>\\s*</ul>', re.DOTALL)
new_footer = '''<ul>
                    <li><a href="index.html">Novedades</a></li>
                    <li><a href="pasteles.html">Tortas</a></li>
                    <li><a href="premium.html">Tortas Premium</a></li>
                    <li><a href="dulces.html">Variedades Dulces</a></li>
                    <li><a href="contacto.html">Contacto</a></li>
                </ul>'''

html = nav_regex.sub(new_nav, html)
html = footer_nav_regex.sub(new_footer, html)

# Function to replace catalogo div and title
def create_page(title, items, output_file):
    page_html = html.replace('Coleccin de Tortas', title)
    page_html = page_html.replace('Colección de Tortas', title) 
    
    catalogo_regex = re.compile(r'<div class="catalogo".*?</div>\\s*</section>', re.DOTALL)
    new_catalogo = generate_catalogo(items) + '\\n    </section>'
    
    page_html = catalogo_regex.sub(new_catalogo, page_html)
    
    # update title tag
    page_html = re.sub(r'<title>.*?</title>', f'<title>{title} - Tortas de Autor</title>', page_html)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(page_html)

create_page('Colección de Tortas', tortas, 'pasteles.html')
create_page('Tortas Premium', premium, 'premium.html')
create_page('Variedades Dulces', dulces, 'dulces.html')

print("Pages generated successfully.")
