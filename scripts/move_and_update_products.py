import os
import glob
import re

base_dir = r'C:\Users\felip\OneDrive\Documents\Proyectos\Pagina Web HTML Pasteleria'
productos_dir = os.path.join(base_dir, 'productos')

if not os.path.exists(productos_dir):
    os.makedirs(productos_dir)

# 1. Update root files to point to productos/...
root_files = ['index.html', 'pasteles.html', 'premium.html', 'dulces.html', 'contacto.html']

for filename in root_files:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href="producto_..." with href="productos/producto_..."
    # Wait, some might already have productos/ if they run the script twice, so check carefully
    content = re.sub(r'href="(?!productos/)(producto_[^"]+\.html)"', r'href="productos/\1"', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Process all producto_*.html files
product_files = glob.glob(os.path.join(base_dir, 'producto_*.html'))

for filepath in product_files:
    filename = os.path.basename(filepath)
    new_filepath = os.path.join(productos_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update paths inside product files
    content = content.replace('href="css/', 'href="../css/')
    content = content.replace('src="js/', 'src="../js/')
    content = content.replace('src="img/', 'src="../img/')
    
    for root_file in root_files:
        content = content.replace(f'href="{root_file}"', f'href="../{root_file}"')
        
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Remove the original file
    os.remove(filepath)

print(f"Moved and updated {len(product_files)} product files.")
