import re

file_path = r'C:\Users\felip\OneDrive\Documents\Proyectos\Pagina Web HTML Pasteleria\producto_quequevariedades.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add the select HTML before the button
html_to_insert = '''
<div style="margin-bottom: 20px;">
    <label for="flavor-select" style="display:block; font-weight:600; color:var(--texto); margin-bottom:8px;">Sabor:</label>
    <select id="flavor-select" style="width:100%; padding:10px; border:1px solid var(--borde); border-radius:4px; font-size:1rem; color:var(--texto); background:#fff;">
        <option value="Vainilla">Vainilla</option>
        <option value="Naranja">Naranja</option>
        <option value="Marmoleado">Marmoleado</option>
    </select>
</div>
'''

content = re.sub(
    r'(<p style="[^"]*">Queque Vainilla - Queque Naranja - Queque Marmoleado</p>\s*)',
    r'\g<1>' + html_to_insert,
    content
)

# Replace 'Aadir al carrito' or 'Aadir al carrito' with 'Añadir al carrito'
content = re.sub(r'A.adir al carrito', 'Añadir al carrito', content)

# Modify the script block
script_replacement = '''
    var h1 = document.querySelector('h1').textContent.trim();
    var size = document.getElementById('size-select') ? document.getElementById('size-select').value + " porciones" : "";
    var design = document.getElementById('design-select') ? document.getElementById('design-select').value : "";
    var flavor = document.getElementById('flavor-select') ? document.getElementById('flavor-select').value : "";
    
    var fullName = h1;
    var extras = [];
    if (size) extras.push(size);
    if (design) extras.push(design);
    if (flavor) extras.push(flavor);
'''

content = re.sub(
    r'\s*var h1 = document.querySelector\(\'h1\'\)\.textContent\.trim\(\);\s*var size = document\.getElementById\(\'size-select\'\) \? document\.getElementById\(\'size-select\'\)\.value \+ " porciones" : "";\s*var design = document\.getElementById\(\'design-select\'\) \? document\.getElementById\(\'design-select\'\)\.value : "";\s*var fullName = h1;\s*var extras = \[\];\s*if \(size\) extras\.push\(size\);\s*if \(design\) extras\.push\(design\);',
    script_replacement,
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modifications applied successfully.")
