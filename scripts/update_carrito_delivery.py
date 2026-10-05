import os, re

carrito_path = r'C:\Users\felip\OneDrive\Documents\Proyectos\Pagina Web HTML Pasteleria\js\carrito.js'

with open(carrito_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to inject the delivery cost calculation in renderCarrito
# Specifically before updating totalElement and actual badges.

# First, find where 	otal += subtotal; happens inside the forEach.
# Wait, let's just find 	otalElement.textContent = formatPrecio(total); and insert the logic right before it.

shipping_calc = '''
            // Cálculo de costo de envío según la comuna
            let costoEnvio = 0;
            let comunaEnvio = "";
            const tarifasDelivery = {
                "Santiago Centro": 2500,
                "Providencia": 3000,
                "Nunoa": 3000,
                "Las Condes": 4000,
                "Vitacura": 4000,
                "Macul": 3500,
                "La Florida": 4500,
                "Maipu": 5000
            };

            carrito.forEach(item => {
                const match = item.nombre.match(/Delivery: (Santiago Centro|Providencia|Nunoa|Las Condes|Vitacura|Macul|La Florida|Maipu)/);
                if (match) {
                    comunaEnvio = match[1];
                    costoEnvio = tarifasDelivery[comunaEnvio];
                }
            });

            if (costoEnvio > 0) {
                total += costoEnvio;
                const divEnvio = document.createElement("div");
                divEnvio.style.display = "flex";
                divEnvio.style.alignItems = "center";
                divEnvio.style.gap = "15px";
                divEnvio.style.borderBottom = "1px solid var(--borde)";
                divEnvio.style.paddingBottom = "15px";
                
                divEnvio.innerHTML = 
                    <div style="width: 60px; height: 60px; border-radius: 4px; display: flex; align-items: center; justify-content: center; background: var(--borde);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--texto)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
                    </div>
                    <div style="flex: 1;">
                        <p style="font-weight: bold; margin: 0; font-size: 0.95rem; color: var(--texto);">Despacho a Domicilio</p>
                        <p style="margin: 3px 0 0 0; font-size: 0.85rem; color: #666;">Comuna: \</p>
                    </div>
                    <div style="font-weight: bold; color: var(--acento);">
                        \
                    </div>
                ;
                itemsContainer.appendChild(divEnvio);
            }
'''

content = re.sub(
    r'(totalElement\.textContent = formatPrecio\(total\);)',
    shipping_calc.replace('\\', '\\\\') + r'\n            \1',
    content
)

with open(carrito_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("carrito.js updated.")
