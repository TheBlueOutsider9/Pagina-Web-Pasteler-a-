import os, glob, re

base_dir = r'C:\Users\felip\OneDrive\Documents\Proyectos\Pagina Web HTML Pasteleria\productos'
html_files = glob.glob(os.path.join(base_dir, 'producto_*.html'))

shipping_html = '''<div style="margin-bottom: 20px;">
    <label for="shipping-select" style="display:block; font-weight:600; color:var(--texto); margin-bottom:8px;">Tipo de env&iacute;o:</label>
    <select id="shipping-select" onchange="updateShipping()" style="width:100%; padding:10px; border:1px solid var(--borde); border-radius:4px; font-size:1rem; color:var(--texto); background:#fff;">
        <option value="Retiro">Retiro</option>
        <option value="Delivery">Delivery</option>
    </select>
</div>
<div id="address-container" style="display:none; margin-bottom: 20px;">
    <label for="address-input" style="display:block; font-weight:600; color:var(--texto); margin-bottom:8px;">Direcci&oacute;n de Delivery:</label>
    <input type="text" id="address-input" placeholder="Ingresa tu direcci&oacute;n" style="width:100%; padding:10px; border:1px solid var(--borde); border-radius:4px; font-size:1rem; color:var(--texto); background:#fff; box-sizing:border-box;">
</div>
'''

update_shipping_script = '''
function updateShipping() {
    var shipping = document.getElementById('shipping-select');
    var addressContainer = document.getElementById('address-container');
    if (shipping && shipping.value === 'Delivery') {
        addressContainer.style.display = 'block';
    } else {
        addressContainer.style.display = 'none';
    }
}
'''

extras_injection = '''    var extras = [];
    var shipping = document.getElementById('shipping-select') ? document.getElementById('shipping-select').value : "";
    var address = document.getElementById('address-input') ? document.getElementById('address-input').value.trim() : "";
    if (shipping) {
        if (shipping === 'Delivery' && address) {
            extras.push("Delivery: " + address);
        } else {
            extras.push("Retiro");
        }
    }'''

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid double injection
    if 'id="shipping-select"' in content:
        continue

    # 1. Insert shipping_html before the button
    content = re.sub(
        r'(<button class="btn-oscuro"[^>]*onclick="agregarAlCarroPersonalizado\(event\)")',
        shipping_html + r'\1',
        content
    )

    # 2. Insert updateShipping() script before agregarAlCarroPersonalizado
    content = re.sub(
        r'(function agregarAlCarroPersonalizado\(e\) \{)',
        update_shipping_script + r'\n\1',
        content
    )

    # 3. Inject extras logic
    content = re.sub(
        r'(\s*var extras = \[\];)',
        '\n' + extras_injection,
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed {len(html_files)} files.")
