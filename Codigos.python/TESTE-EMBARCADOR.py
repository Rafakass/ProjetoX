import folium
import pandas as pd
from geopy.geocoders import Nominatim

# Função para obter coordenadas usando geopy
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name + ", Mato Grosso do Sul, Brazil")
    if location:
        return location.latitude, location.longitude
    return None, None

# Dados das filiais e embarcadores
data = {
    'Filial': ['Amambai', 'Bataypora', 'Caarapo', 'Campo Grande', 'Campo Grande', 'Campo Grande', 'Campo Grande', 'Chapadão do Sul', 'Corumbá', 'Dourados', 'Dourados', 'Dourados', 'Dourados', 'Guaira', 'Maracaju', 'Maracaju', 'Mundo Novo', 'Mundo Novo', 'Navirai', 'Nova Alvorada do Sul', 'Nova Alvorada do Sul', 'São Gabriel do Oeste', 'Sidrolandia'],
    'Embarcador': ['Renan', 'Rafael', 'Camila', 'Ana', 'Adriano G', 'Adeildo', 'Emerson', 'Murilo', 'Fernando', 'Marcio', 'Matheus', 'Reinaldo', 'Jacob', 'Adriano Jesus', 'Andre', 'Luiz Fernando', 'Jackson', 'Rebeka', 'Jaderson', 'Pedroso', 'Marco Perobeli', 'Guilherme', 'Eduardo'],
    'Quantidade de Viagens': [120, 90, 75, 100, 80, 90, 60, 75, 85, 120, 90, 60, 100, 40, 45, 55, 20, 25, 30, 10, 15, 35, 50]
}

# Coordenadas
coords = {
    'Amambai': get_coordinates('Amambai'),
    'Bataypora': get_coordinates('Bataypora'),
    'Caarapo': get_coordinates('Caarapo'),
    'Campo Grande': get_coordinates('Campo Grande'),
    'Chapadão do Sul': get_coordinates('Chapadão do Sul'),
    'Corumbá': get_coordinates('Corumbá'),
    'Dourados': get_coordinates('Dourados'),
    'Guaira': (-24.0857, -54.1371),  # Correção para Guaíra
    'Maracaju': get_coordinates('Maracaju'),
    'Mundo Novo': get_coordinates('Mundo Novo'),
    'Navirai': get_coordinates('Navirai'),
    'Nova Alvorada do Sul': get_coordinates('Nova Alvorada do Sul'),
    'São Gabriel do Oeste': get_coordinates('São Gabriel do Oeste'),
    'Sidrolandia': get_coordinates('Sidrolandia')
}

# Filiais emissoras de documentos
emissoras = ['Campo Grande', 'Mundo Novo', 'Ponta Porã', 'Dourados']

# Criar DataFrame
df = pd.DataFrame(data)
df['Latitude'] = df['Filial'].map(lambda x: coords[x][0])
df['Longitude'] = df['Filial'].map(lambda x: coords[x][1])

# Criar o mapa
m = folium.Map(location=[-20.4697, -54.6201], zoom_start=6)

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
        marker.get_root().html.add_child(folium.Element('<script>setTimeout(function() { $(''div.leaflet-popup'').each(function() { this.openPopup(); }); }, 100);</script>'))

# Criar a legenda personalizada com todos os embarcadores e viagens
legend_html = "<div style='position: fixed; bottom: 50px; left: 50px; width: 350px; height: auto; background-color: white; border:2px solid grey; z-index:9999; font-size:12px; padding: 10px;'>"
legend_html += "<img src='logo.png' alt='Logo Empresa' style='width: 100%; height: auto;'><br>"
legend_html += "<b>Legenda de Viagens</b><br>"

# Agrupar os dados por filial e adicionar à legenda
for filial in df['Filial'].unique():
    color = 'red' if filial in emissoras else 'black'
    legend_html += f"<b style='color:{color};'>{filial}</b><br>"
    filial_data = df[df['Filial'] == filial]
    for index, row in filial_data.iterrows():
        legend_html += f"&nbsp;&nbsp;<b>{row['Embarcador']}:</b> {row['Quantidade de Viagens']} viagens<br>"
    legend_html += "<br>"

legend_html += "</div>"

m.get_root().html.add_child(folium.Element(legend_html))

# Salvar o mapa em um arquivo HTML
map_html = 'mapa_filiais_embarcadores.html'
m.save(map_html)

print(f"Mapeamento salvo em {map_html}.")
