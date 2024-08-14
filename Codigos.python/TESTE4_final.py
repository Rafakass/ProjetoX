import folium
import pandas as pd

# Coordenadas já definidas manualmente
coords = {
    'Amambai': (-23.1058, -55.2253),
    'Bataypora': (-22.2950, -53.2700),
    'Caarapo': (-22.6375, -54.8203),
    'Campo Grande': (-20.4697, -54.6201),
    'Chapadão do Sul': (-18.7886, -52.6269),
    'Corumbá': (-19.0077, -57.6514),
    'Dourados': (-22.2231, -54.8054),
    'Guaira': (-24.0857, -54.1371),
    'Maracaju': (-21.6109, -55.1678),
    'Mundo Novo': (-23.9358, -54.2814),
    'Navirai': (-23.0651, -54.1909),
    'Nova Alvorada do Sul': (-21.4653, -54.3825),
    'São Gabriel do Oeste': (-19.3900, -54.5500),
    'Sidrolandia': (-20.9301, -54.9706),
    'Ponta Porã': (-22.52155, -55.71368)  # Nova filial incluída
}

# Dados das filiais e embarcadores
data = {
    'Filial': ['Amambai', 'Bataypora', 'Caarapo', 'Campo Grande', 'Campo Grande', 'Campo Grande', 'Campo Grande', 'Chapadão do Sul', 'Corumbá', 'Dourados', 'Dourados', 'Dourados', 'Dourados', 'Guaira', 'Maracaju', 'Maracaju', 'Mundo Novo', 'Mundo Novo', 'Navirai', 'Nova Alvorada do Sul', 'Nova Alvorada do Sul', 'São Gabriel do Oeste', 'Sidrolandia', 'Ponta Porã'],
    'Embarcador': ['Renan', 'Rafael', 'Camila', 'Ana', 'Adriano G', 'Adeildo', 'Emerson', 'Murilo', 'Fernando', 'Marcio', 'Matheus', 'Reinaldo', 'Jacob', 'Adriano Jesus', 'Andre', 'Luiz Fernando', 'Jackson', 'Rebeka', 'Jaderson', 'Pedroso', 'Marco Perobeli', 'Guilherme', 'Eduardo', 'Novo Embarcador'],
    'Quantidade de Viagens': [120, 90, 75, 100, 80, 90, 60, 75, 85, 120, 90, 60, 100, 40, 45, 55, 20, 25, 30, 10, 15, 35, 50, 10]
}

# Criar DataFrame
df = pd.DataFrame(data)
df['Latitude'] = df['Filial'].map(lambda x: coords[x][0])
df['Longitude'] = df['Filial'].map(lambda x: coords[x][1])

# Criar o mapa
m = folium.Map(location=[-20.4697, -54.6201], zoom_start=6)

# Filiais emissoras de documentos
emissoras = ['Campo Grande', 'Mundo Novo', 'Ponta Porã', 'Dourados']

# Função para formatar o popup
def format_popup(filial, embarcadores_info):
    return folium.Popup(f"""
    <div style="font-size:14px;">
        <b>Filial:</b> {filial}<br><br>
        {embarcadores_info}
    </div>
    """, max_width=300)

# Adicionar marcadores para as filiais
for filial in df['Filial'].unique():
    filial_data = df[df['Filial'] == filial]
    
    if len(filial_data) > 0:
        # Agrupar os embarcadores e suas quantidades de viagens
        embarcadores_info = "<br>".join(
            [f"<b style='font-size:14px;'>{row['Embarcador']}:</b> <span style='color:blue; font-size:14px;'>{row['Quantidade de Viagens']}</span>" for index, row in filial_data.iterrows()]
        )
        
        # Escolher a cor do pin
        pin_color = 'red' if filial in emissoras else 'blue'
        
        # Criar marcador com popup
        marker = folium.Marker(
            location=[filial_data['Latitude'].iloc[0], filial_data['Longitude'].iloc[0]],
            icon=folium.Icon(color=pin_color, icon='info-sign')
        )
        marker.add_to(m)
        
        # Formatando o popup
        popup = format_popup(filial, embarcadores_info)
        popup.add_to(marker)
        
        # Abrir todos os popups automaticamente
        marker.add_child(popup)
        marker.get_root().html.add_child(folium.Element('<script>setTimeout(function() { $(\'div.leaflet-popup\').each(function() { this.openPopup(); }); }, 100);</script>'))

# Criar a legenda personalizada como uma tabela
legend_html = """
<div style='position: fixed; bottom: 50px; left: 50px; width: auto; height: auto; background-color: white; border:2px solid grey; z-index:9999; font-size:12px; padding: 10px;'>
    <img src='logo.png' alt='Logo Empresa' style='width: 100%; height: auto;'><br>
    <b>Legenda de Viagens</b><br>
    <table style='width:100%; font-size:10px;'>
"""

# Agrupar os dados por filial e adicionar à legenda
for filial in df['Filial'].unique():
    color = 'red' if filial in emissoras else 'black'
    legend_html += f"<tr><td colspan='2'><b style='color:{color};'>{filial}</b></td></tr>"
    filial_data = df[df['Filial'] == filial]
    for index, row in filial_data.iterrows():
        legend_html += f"<tr><td>{row['Embarcador']}</td><td>{row['Quantidade de Viagens']} viagens</td></tr>"
    legend_html += "<tr><td colspan='2'>&nbsp;</td></tr>"  # Espaçamento entre filiais

legend_html += """
    </table>
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))

# Salvar o mapa em um arquivo HTML
map_html = 'mapa_filiais_embarcadores3.html'
m.save(map_html)

print(f"Mapeamento salvo em {map_html}")


import folium
import pandas as pd

# Coordenadas já definidas manualmente
coords = {
    'Amambai': (-23.1058, -55.2253),
    'Bataypora': (-22.2950, -53.2700),
    'Caarapo': (-22.6375, -54.8203),
    'Campo Grande': (-20.4697, -54.6201),
    'Chapadão do Sul': (-18.7886, -52.6269),
    'Corumbá': (-19.0077, -57.6514),
    'Dourados': (-22.2231, -54.8054),
    'Guaira': (-24.0857, -54.1371),
    'Maracaju': (-21.6109, -55.1678),
    'Mundo Novo': (-23.9358, -54.2814),
    'Navirai': (-23.0651, -54.1909),
    'Nova Alvorada do Sul': (-21.4653, -54.3825),
    'São Gabriel do Oeste': (-19.3900, -54.5500),
    'Sidrolandia': (-20.9301, -54.9706),
    'Ponta Porã': (-22.52155, -55.71368)  # Nova filial incluída
}

# Dados das filiais e embarcadores
data = {
    'Filial': ['Amambai', 'Bataypora', 'Caarapo', 'Campo Grande', 'Campo Grande', 'Campo Grande', 'Campo Grande', 'Chapadão do Sul', 'Corumbá', 'Dourados', 'Dourados', 'Dourados', 'Dourados', 'Guaira', 'Maracaju', 'Maracaju', 'Mundo Novo', 'Mundo Novo', 'Navirai', 'Nova Alvorada do Sul', 'Nova Alvorada do Sul', 'São Gabriel do Oeste', 'Sidrolandia', 'Ponta Porã'],
    'Embarcador': ['Renan', 'Rafael', 'Camila', 'Ana', 'Adriano G', 'Adeildo', 'Emerson', 'Murilo', 'Fernando', 'Marcio', 'Matheus', 'Reinaldo', 'Jacob', 'Adriano Jesus', 'Andre', 'Luiz Fernando', 'Jackson', 'Rebeka', 'Jaderson', 'Pedroso', 'Marco Perobeli', 'Guilherme', 'Eduardo', 'Novo Embarcador'],
    'Quantidade de Viagens': [120, 90, 75, 100, 80, 90, 60, 75, 85, 120, 90, 60, 100, 40, 45, 55, 20, 25, 30, 10, 15, 35, 50, 10]
}

# Criar DataFrame
df = pd.DataFrame(data)
df['Latitude'] = df['Filial'].map(lambda x: coords[x][0])
df['Longitude'] = df['Filial'].map(lambda x: coords[x][1])

# Criar o mapa
m = folium.Map(location=[-20.4697, -54.6201], zoom_start=6)

# Filiais emissoras de documentos
emissoras = ['Campo Grande', 'Mundo Novo', 'Ponta Porã', 'Dourados']

# Função para formatar o popup
def format_popup(filial, embarcadores_info):
    return folium.Popup(f"""
    <div style="font-size:14px;">
        <b>Filial:</b> {filial}<br><br>
        {embarcadores_info}
    </div>
    """, max_width=300)

# Adicionar marcadores para as filiais
for filial in df['Filial'].unique():
    filial_data = df[df['Filial'] == filial]
    
    if len(filial_data) > 0:
        # Agrupar os embarcadores e suas quantidades de viagens
        embarcadores_info = "<br>".join(
            [f"<b style='font-size:14px;'>{row['Embarcador']}:</b> <span style='color:blue; font-size:14px;'>{row['Quantidade de Viagens']}</span>" for index, row in filial_data.iterrows()]
        )
        
        # Escolher a cor do pin
        pin_color = 'red' if filial in emissoras else 'blue'
        
        # Criar marcador com popup
        marker = folium.Marker(
            location=[filial_data['Latitude'].iloc[0], filial_data['Longitude'].iloc[0]],
            icon=folium.Icon(color=pin_color, icon='info-sign')
        )
        marker.add_to(m)
        
        # Formatando o popup
        popup = format_popup(filial, embarcadores_info)
        popup.add_to(marker)
        
        # Abrir todos os popups automaticamente
        marker.add_child(popup)
        marker.get_root().html.add_child(folium.Element('<script>setTimeout(function() { $(\'div.leaflet-popup\').each(function() { this.openPopup(); }); }, 100);</script>'))

# Criar a legenda personalizada como uma tabela
legend_html = """
<div style='position: fixed; bottom: 50px; left: 50px; width: auto; height: auto; background-color: white; border:2px solid grey; z-index:9999; font-size:12px; padding: 10px;'>
    <img src='logo.png' alt='Logo Empresa' style='width: 100%; height: auto;'><br>
    <b>Legenda de Viagens</b><br>
    <table style='width:100%; font-size:10px;'>
"""

# Agrupar os dados por filial e adicionar à legenda
for filial in df['Filial'].unique():
    color = 'red' if filial in emissoras else 'black'
    legend_html += f"<tr><td colspan='2'><b style='color:{color};'>{filial}</b></td></tr>"
    filial_data = df[df['Filial'] == filial]
    for index, row in filial_data.iterrows():
        legend_html += f"<tr><td>{row['Embarcador']}</td><td>{row['Quantidade de Viagens']} viagens</td></tr>"
    legend_html += "<tr><td colspan='2'>&nbsp;</td></tr>"  # Espaçamento entre filiais

legend_html += """
    </table>
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))

# Salvar o mapa em um arquivo HTML
map_html = 'mapa_filiais_embarcadores3.html'
m.save(map_html)

print(f"Mapeamento salvo em {map_html}")



# Ajustando o código para exibir todos os embarcadores por filial no popup e adicionar a rota sinalizada em azul.

# Adicionando a cidade de Rio Brilhante nas coordenadas
coords['Rio Brilhante'] = (-21.8039, -54.5427)

# Função para formatar o popup com todos os embarcadores e suas respectivas viagens
def format_popup(filial):
    embarcadores_info = df[df['Filial'] == filial][['Embarcador', 'Quantidade de Viagens']]
    popup_text = "<b>{}</b><br>".format(filial)
    popup_text += "<br>".join([f"{row['Embarcador']}: {row['Quantidade de Viagens']} viagens" for _, row in embarcadores_info.iterrows()])
    return folium.Popup(popup_text, max_width=300)

# Criar o mapa com as alterações
m = folium.Map(location=[-20.4697, -54.6201], zoom_start=6)

# Adicionando os marcadores com popups atualizados
for i, row in df.iterrows():
    popup = format_popup(row['Filial'])
    folium.Marker(location=[row['Latitude'], row['Longitude']],
                  popup=popup,
                  icon=folium.Icon(color='red' if row['Filial'] in emissoras else 'blue')).add_to(m)

# Adicionando uma rota sinalizada em azul de Ponta Porã, Maracaju e Rio Brilhante para Santa Catarina
rota_coords = [
    coords['Ponta Porã'], 
    coords['Maracaju'], 
    coords['Rio Brilhante'], 
    (-27.2423, -50.2189)  # Coordenada geral representando Santa Catarina
]

# Adicionando a rota no mapa
folium.PolyLine(rota_coords, color="blue", weight=5, opacity=0.7).add_to(m)

# Salvando o mapa como arquivo HTML para visualização
output_file = "/mnt/data/mapa_legenda_popup_rotas.html"
m.save(output_file)
