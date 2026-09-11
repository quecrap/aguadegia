import math
import os

output_dir = r"C:\Users\PEPITO\Downloads\aguadegia\docs\img"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. GRÁFICO DE DONA: DESGLOSE FASE 1 ($39,710 MXN)
# -------------------------------------------------------------
fase1_data = [
    {"label": "Laboratorio EMA (NOM-127)", "amount": 13500.00, "color": "#00e5ff"},
    {"label": "Mano de Obra Cuadrilla", "amount": 7000.00, "color": "#3b82f6"},
    {"label": "Tren Purificación RO + UV", "amount": 5850.00, "color": "#10b981"},
    {"label": "Almacenamiento & Plomería", "amount": 4816.80, "color": "#f59e0b"},
    {"label": "Equipo Activo Cuadrilla", "amount": 4300.00, "color": "#8b5cf6"},
    {"label": "Materiales Micro-pozo", "amount": 3120.00, "color": "#ec4899"},
    {"label": "Telemetría IoT (ESP32)", "amount": 1123.20, "color": "#06b6d4"},
]

total_fase1 = sum(d["amount"] for d in fase1_data)

cx, cy, r_out, r_in = 220, 240, 160, 95
start_angle = -math.pi / 2

svg_paths = []
current_angle = start_angle

for item in fase1_data:
    item["pct"] = (item["amount"] / total_fase1) * 100
    angle_span = (item["amount"] / total_fase1) * 2 * math.pi
    end_angle = current_angle + angle_span
    
    x1_out = cx + r_out * math.cos(current_angle)
    y1_out = cy + r_out * math.sin(current_angle)
    x2_out = cx + r_out * math.cos(end_angle)
    y2_out = cy + r_out * math.sin(end_angle)
    
    x1_in = cx + r_in * math.cos(end_angle)
    y1_in = cy + r_in * math.sin(end_angle)
    x2_in = cx + r_in * math.cos(current_angle)
    y2_in = cy + r_in * math.sin(current_angle)
    
    large_arc = 1 if angle_span > math.pi else 0
    
    d = f"M {x1_out:.2f} {y1_out:.2f} A {r_out} {r_out} 0 {large_arc} 1 {x2_out:.2f} {y2_out:.2f} L {x1_in:.2f} {y1_in:.2f} A {r_in} {r_in} 0 {large_arc} 0 {x2_in:.2f} {y2_in:.2f} Z"
    svg_paths.append((d, item["color"], item["label"], item["amount"], item["pct"]))
    current_angle = end_angle

legend_svg = []
ly = 110
for item in fase1_data:
    legend_svg.append(f'''
    <g transform="translate(430, {ly})">
      <rect x="0" y="0" width="16" height="16" rx="4" fill="{item['color']}"/>
      <text x="26" y="13" fill="#f8fafc" font-size="13" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-weight="600">{item['label']}</text>
      <text x="350" y="13" text-anchor="end" fill="#94a3b8" font-size="12" font-family="'JetBrains Mono', monospace">${item['amount']:,.2f} ({item['pct']:.1f}%)</text>
    </g>''')
    ly += 38

donut_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d18"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  
  <!-- Background Card -->
  <rect x="2" y="2" width="816" height="476" rx="16" fill="url(#bgGrad)" stroke="#1e293b" stroke-width="2"/>
  
  <!-- Header -->
  <text x="36" y="44" fill="#00e5ff" font-size="18" font-family="'Outfit', system-ui, sans-serif" font-weight="700" letter-spacing="1">DISTRIBUCIÓN FINANCIERA — FASE 1: CONSOLIDACIÓN PILOTO</text>
  <text x="36" y="68" fill="#64748b" font-size="13" font-family="'Plus Jakarta Sans', system-ui, sans-serif">Presupuesto auditado con precios de mercado y proveedores verificados (Tijuana, B.C.)</text>
  <line x1="36" y1="84" x2="784" y2="84" stroke="#1e293b" stroke-width="1"/>
  
  <!-- Donut Chart Segments -->
  <g id="donut-segments">
'''
for d, color, label, amt, pct in svg_paths:
    donut_svg += f'    <path d="{d}" fill="{color}" stroke="#070d18" stroke-width="2.5" opacity="0.95"/>\n'

donut_svg += f'''  </g>
  
  <!-- Center Text -->
  <circle cx="{cx}" cy="{cy}" r="{r_in - 5}" fill="#0b1120" stroke="#1e293b" stroke-width="1"/>
  <text x="{cx}" y="{cy - 12}" text-anchor="middle" fill="#94a3b8" font-size="11" font-family="'Outfit', sans-serif" letter-spacing="1.5">TOTAL FASE 1</text>
  <text x="{cx}" y="{cy + 16}" text-anchor="middle" fill="#00e5ff" font-size="22" font-family="'JetBrains Mono', monospace" font-weight="700">${total_fase1:,.2f}</text>
  <text x="{cx}" y="{cy + 34}" text-anchor="middle" fill="#64748b" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">MXN (~$2,206 USD)</text>
  
  <!-- Legend -->
  <g id="legend">
{''.join(legend_svg)}
  </g>
</svg>'''

donut_path = os.path.join(output_dir, "grafico_presupuesto_fase1.svg")
with open(donut_path, "w", encoding="utf-8") as f:
    f.write(donut_svg)
print("Donut chart created:", donut_path)

# -------------------------------------------------------------
# 2. GRÁFICO DE BARRAS: COMPARATIVA DE FASES E HITOS ACUMULADOS
# -------------------------------------------------------------
fases_data = [
    {
        "fase": "Fase 1: Consolidación Piloto",
        "monto": 39710.00,
        "usd": "~$2,206 USD",
        "hitos": "Lab EMA NOM-127, RO Rotoplas 300100, Kit IoT ESP32, activo cuadrilla",
        "color": "#00e5ff",
        "max_bar": 148500.00
    },
    {
        "fase": "Fase 2: Red Centinela (3 Nodos)",
        "monto": 89120.00,
        "usd": "~$4,951 USD",
        "hitos": "3 pozos de alivio, energía solar off-grid, módem celular NB-IoT, lab multicuenca",
        "color": "#10b981",
        "max_bar": 148500.00
    },
    {
        "fase": "Fase 3: Integración Científica & CONAGUA",
        "monto": 148500.00,
        "usd": "~$8,250 USD",
        "hitos": "Convenio modelación CICESE, portal API datos abiertos, registro piezométrico",
        "color": "#3b82f6",
        "max_bar": 148500.00
    }
]

total_global = sum(f["monto"] for f in fases_data)

bars_svg = []
by = 120
max_val = 160000.00
max_w = 420

for f in fases_data:
    bw = (f["monto"] / max_val) * max_w
    bars_svg.append(f'''
    <g transform="translate(40, {by})">
      <text x="0" y="0" fill="#f8fafc" font-size="14" font-family="'Outfit', sans-serif" font-weight="600">{f['fase']}</text>
      <text x="740" y="0" text-anchor="end" fill="{f['color']}" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700">${f['monto']:,.2f} MXN <tspan fill="#64748b" font-size="12">({f['usd']})</tspan></text>
      
      <!-- Background track -->
      <rect x="0" y="10" width="{max_w + 140}" height="22" rx="6" fill="#1e293b" opacity="0.6"/>
      <!-- Progress Bar -->
      <rect x="0" y="10" width="{bw + 100}" height="22" rx="6" fill="{f['color']}" opacity="0.9"/>
      
      <!-- Detail line -->
      <text x="0" y="48" fill="#94a3b8" font-size="12" font-family="'Plus Jakarta Sans', sans-serif">🔑 {f['hitos']}</text>
    </g>''')
    by += 95

bars_chart_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d18"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  
  <!-- Background Card -->
  <rect x="2" y="2" width="816" height="476" rx="16" fill="url(#bgGrad2)" stroke="#1e293b" stroke-width="2"/>
  
  <!-- Header -->
  <text x="40" y="44" fill="#00e5ff" font-size="18" font-family="'Outfit', system-ui, sans-serif" font-weight="700" letter-spacing="1">ESCALABILIDAD Y METAS DE FINANCIAMIENTO POR FASES</text>
  <text x="40" y="68" fill="#64748b" font-size="13" font-family="'Plus Jakarta Sans', system-ui, sans-serif">Presupuesto total programado para consolidar la Red Centinela Comunitaria</text>
  <line x1="40" y1="84" x2="780" y2="84" stroke="#1e293b" stroke-width="1"/>
  
  <!-- Bars -->
{''.join(bars_svg)}
  
  <!-- Bottom Total Card -->
  <g transform="translate(40, 400)">
    <rect x="0" y="0" width="740" height="54" rx="10" fill="#0b1120" stroke="#334155" stroke-width="1"/>
    <text x="24" y="32" fill="#f8fafc" font-size="14" font-family="'Outfit', sans-serif" font-weight="700">INVERSIÓN TOTAL ACUMULADA (3 FASES):</text>
    <text x="716" y="34" text-anchor="end" fill="#00e5ff" font-size="20" font-family="'JetBrains Mono', monospace" font-weight="800">${total_global:,.2f} MXN <tspan fill="#64748b" font-size="13">(~$15,407 USD)</tspan></text>
  </g>
</svg>'''

bars_path = os.path.join(output_dir, "grafico_metas_acumuladas.svg")
with open(bars_path, "w", encoding="utf-8") as f:
    f.write(bars_chart_svg)
print("Bars chart created:", bars_path)
