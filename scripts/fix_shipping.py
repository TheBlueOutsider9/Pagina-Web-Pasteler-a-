import os, glob, re

base_dir = r'C:\Users\felip\OneDrive\Documents\Proyectos\Pagina Web HTML Pasteleria\productos'
html_files = glob.glob(os.path.join(base_dir, 'producto_*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the fallback logic
    content = content.replace(
        '''        if (shipping === 'Delivery' && address) {
            extras.push("Delivery: " + address);
        } else {
            extras.push("Retiro");
        }''',
        '''        if (shipping === 'Delivery') {
            if (address) {
                extras.push("Delivery: " + address);
            } else {
                extras.push("Delivery (Sin direcci\u00f3n)");
            }
        } else {
            extras.push("Retiro");
        }'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed {len(html_files)} files.")
