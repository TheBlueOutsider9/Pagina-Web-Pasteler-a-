import os, glob, re

base_dir = r'C:\Users\felip\OneDrive\Documents\Proyectos\Pagina Web HTML Pasteleria\productos'
html_files = glob.glob(os.path.join(base_dir, 'producto_*.html'))

new_shipping_html = '''<div style="margin-bottom: 20px;">
    <label for="shipping-select" style="display:block; font-weight:600; color:var(--texto); margin-bottom:8px;">Tipo de env&iacute;o:</label>
    <select id="shipping-select" onchange="updateShipping()" style="width:100%; padding:10px; border:1px solid var(--borde); border-radius:4px; font-size:1rem; color:var(--texto); background:#fff;">
        <option value="Retiro">Retiro</option>
        <option value="Delivery">Delivery</option>
    </select>
</div>
<div id="address-container" style="display:none; margin-bottom: 20px;">
    <label for="comuna-select" style="display:block; font-weight:600; color:var(--texto); margin-bottom:8px;">Comuna:</label>
    <select id="comuna-select" style="width:100%; padding:10px; border:1px solid var(--borde); border-radius:4px; font-size:1rem; color:var(--texto); background:#fff; margin-bottom:10px;">
        <option value="">Selecciona tu comuna</option>
        <option value="Santiago Centro">Santiago Centro (.500)</option>
        <option value="Providencia">Providencia (.000)</option>
        <option value="Nunoa">&Ntilde;u&ntilde;oa (.000)</option>
        <option value="Las Condes">Las Condes (.000)</option>
        <option value="Vitacura">Vitacura (.000)</option>
        <option value="Macul">Macul (.500)</option>
        <option value="La Florida">La Florida (.500)</option>
        <option value="Maipu">Maip&uacute; (.000)</option>
    </select>
    
    <label for="address-input" style="display:block; font-weight:600; color:var(--texto); margin-bottom:8px;">Direcci&oacute;n exacta:</label>
    <input type="text" id="address-input" placeholder="Ej: Av. Siempreviva 123, Depto 4" style="width:100%; padding:10px; border:1px solid var(--borde); border-radius:4px; font-size:1rem; color:var(--texto); background:#fff; box-sizing:border-box;">
</div>'''

old_shipping_html = r'<div style="margin-bottom: 20px;">\s*<label for="shipping-select"[^>]*>Tipo de env&iacute;o:</label>\s*<select id="shipping-select"[^>]*>\s*<option value="Retiro">Retiro</option>\s*<option value="Delivery">Delivery</option>\s*</select>\s*</div>\s*<div id="address-container"[^>]*>\s*<label for="address-input"[^>]*>Direcci&oacute;n de Delivery:</label>\s*<input type="text" id="address-input"[^>]*>\s*</div>'

old_extras_logic = r'''\s*if \(shipping === 'Delivery'\) \{\s*if \(address\) \{\s*extras\.push\("Delivery: " \+ address\);\s*\} else \{\s*extras\.push\("Delivery \(Sin direcci\\u00f3n\)"\);\s*\}\s*\} else \{\s*extras\.push\("Retiro"\);\s*\}'''

new_extras_logic = '''
        if (shipping === 'Delivery') {
            var comuna = document.getElementById('comuna-select') ? document.getElementById('comuna-select').value : "";
            if (comuna && address) {
                extras.push("Delivery: " + comuna + " (" + address + ")");
            } else if (comuna) {
                extras.push("Delivery: " + comuna + " (Sin direcci\\u00f3n)");
            } else {
                extras.push("Delivery (Falta comuna y direcci\\u00f3n)");
            }
        } else {
            extras.push("Retiro");
        }'''

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace HTML
    content = re.sub(old_shipping_html, new_shipping_html.replace('\\', '\\\\'), content, flags=re.DOTALL)
    
    # Replace Logic
    content = re.sub(old_extras_logic, new_extras_logic.replace('\\', '\\\\'), content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files with comuna logic.")
