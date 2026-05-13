import base64

with open('dashboard_template.html', encoding='utf-8') as f:
    template = f.read()
with open('preloaded_adimark.json', encoding='utf-8') as f:
    adimark_js = f.read()
with open('preloaded_reporte.json', encoding='utf-8') as f:
    reporte_js = f.read()
with open('preloaded_comunas.json', encoding='utf-8') as f:
    comunas_js = f.read()

with open('Logo situ_vd.png', 'rb') as f:
    situ_b64 = base64.b64encode(f.read()).decode()
with open('Logo aspen_vd.png', 'rb') as f:
    aspen_b64 = base64.b64encode(f.read()).decode()

html = template
html = html.replace('__SITU_LOGO__', 'data:image/png;base64,' + situ_b64)
html = html.replace('__ASPEN_LOGO__', 'data:image/png;base64,' + aspen_b64)
html = html.replace('__ADIMARK__', adimark_js)
html = html.replace('__REPORTE__', reporte_js)
html = html.replace('__COMUNAS__', comunas_js)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'dashboard.html: {round(len(html)/1024)} KB')
