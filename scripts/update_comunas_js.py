import os, re

carrito_path = r"C:\Users\felip\OneDrive\Documents\Proyectos\Pagina Web HTML Pasteleria\js\carrito.js"

with open(carrito_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the tarifasDelivery dictionary
old_dict_regex = r'const tarifasDelivery = \{[^}]+\};'
new_dict = '''const tarifasDelivery = {
                "Machali": 1500,
                "Rancagua": 2500
            };'''
content = re.sub(old_dict_regex, new_dict, content)

# Replace the match regex
old_match_regex = r'/Delivery: \(Santiago Centro\|Providencia\|Nunoa\|Las Condes\|Vitacura\|Macul\|La Florida\|Maipu\)/'
new_match = r'/Delivery: (Machali|Rancagua)/'
content = re.sub(old_match_regex, new_match, content)

with open(carrito_path, "w", encoding="utf-8") as f:
    f.write(content)

print("carrito.js comunas updated.")
