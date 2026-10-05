import os, glob, re

base_dir = r'C:\Users\felip\OneDrive\Documents\Proyectos\Pagina Web HTML Pasteleria\productos'
html_files = glob.glob(os.path.join(base_dir, 'producto_*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace the options inside the select id="comuna-select"
    # From <option value="Santiago Centro"> ... to </select>
    old_options_regex = r'<option value="Santiago Centro">.*?</select>'
    
    new_options = '''<option value="Machali">Machal&iacute; ($1.500)</option>
        <option value="Rancagua">Rancagua ($2.500)</option>
    </select>'''
    
    content = re.sub(old_options_regex, new_options, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated comunas in {len(html_files)} files.")
