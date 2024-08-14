import geopy
from geopy.geocoders import Nominatim
import folium
from folium.plugins import HeatMap
import pandas as pd

# Dados das cidades por filial
data = {
    "Filial 1776 (Agência Ponta Porã)": ["Amambai", "Antônio João", "Aral Moreira", "Bela Vista", "Caarapó", "Coronel Sapucaia", "Laguna Carapã", "Ponta Porã"],
    "Filial 224 (Filial Dourados)": ["Anaurilândia", "Angélica", "Batayporã", "Deodápolis", "Dourados", "Fátima do Sul", "Guia Lopes da Laguna", "Itaporã", "Ivinhema", "Jardim", "Maracaju", "Nioaque", "Nova Alvorada do Sul", "Nova Andradina", "Nova Casa Verde", "Novo Horizonte do Sul", "Porto Murtinho", "Rio Brilhante"],
    "Filial 250 (Filial Campo Grande)": ["Aparecida do Taboado", "Aquidauana", "Bandeirantes", "Bataguassu", "Bodoquena", "Bonito", "Brasilândia", "Camapuã", "Campo Grande", "Chapadão do Sul", "Corumbá", "Costa Rica", "Coxim", "Miranda", "Ribas do Rio Pardo", "São Gabriel do Oeste", "Sidrolândia", "Sonora", "Terenos", "Três Lagoas"],
    "Filial 269 (Filial Mundo Novo)": ["Eldorado", "Iguatemi", "Itaquiraí", "Juti", "Mundo Novo", "Naviraí", "Sete Quedas", "Tacuru"]
}

# Lista de todas as cidades
cidades = [cidade for sublist in data.values() for cidade in sublist]

# Inicializar o geolocalizador
geolocator = Nominatim(user_agent="geoapiExercises")

# Função para obter coordenadas
def obter_coordenadas(cidade):
    try:
        location = geolocator.geocode(cidade + ", Mato Grosso do Sul, Brazil")
        if location:
            return (location.latitude, location.longitude)
    except:
        return None

# Obter coordenadas para cada cidade
coordenadas = [obter_coordenadas(cidade) for cidade in cidades]

# Filtrar coordenadas não encontradas
coordenadas = [coord for coord in coordenadas if coord is not None]

# Criar mapa de calor
mapa = folium.Map(location=[-20.4428, -54.6461], zoom_start=6)  # Posição central aproximada de Mato Grosso do Sul
heatmap = HeatMap(coordenadas, radius=10)
mapa.add_child(heatmap)

# Salvar mapa
mapa.save('mapa_de_calor_mato_grosso_do_sul.html')

print("Mapa de calor gerado e salvo como 'mapa_de_calor_mato_grosso_do_sul.html'")
