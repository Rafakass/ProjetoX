import folium
from folium.plugins import MarkerCluster
import geopy
from geopy.geocoders import Nominatim

# Dados das cidades de embarque por filial para o cliente específico
embarques = {
    "Filial Mundo Novo": ["Eldorado", "Iguatemi", "Itaquiraí", "Juti", "Mundo Novo", "Naviraí", "Sete Quedas", "Tacuru"],
    "Filial Ponta Porã": ["Amambai", "Antônio João", "Aral Moreira", "Bela Vista", "Caarapó", "Coronel Sapucaia", "Laguna Carapã", "Ponta Porã"],
    "Filial Dourados": ["Anaurilândia", "Angélica", "Batayporã", "Deodápolis", "Dourados", "Fátima do Sul", "Guia Lopes da Laguna", "Itaporã", "Ivinhema", "Jardim", "Maracaju", "Nioaque", "Nova Alvorada do Sul", "Nova Andradina", "Nova Casa Verde", "Novo Horizonte do Sul", "Porto Murtinho", "Rio Brilhante"],
    "Filial Campo Grande": ["Aparecida do Taboado", "Aquidauana", "Bandeirantes", "Bataguassu", "Bodoquena", "Bonito", "Brasilândia", "Camapuã", "Campo Grande", "Chapadão do Sul", "Corumbá", "Costa Rica", "Coxim", "Miranda", "Ribas do Rio Pardo", "São Gabriel do Oeste", "Sidrolândia", "Sonora", "Terenos", "Três Lagoas"]
}

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

# Configurações de cores para cada filial
cores_filiais = {
    "Filial Mundo Novo": "blue",
    "Filial Ponta Porã": "red",
    "Filial Dourados": "green",
    "Filial Campo Grande": "orange"
}

# Criar mapa centrado no Mato Grosso do Sul
mapa = folium.Map(location=[-20.4428, -54.6461], zoom_start=6)

# Adicionar pontos de embarque ao mapa
for filial, cidades in embarques.items():
    for cidade in cidades:
        coordenadas = obter_coordenadas(cidade)
        if coordenadas:
            folium.Marker(
                location=coordenadas,
                popup=f"{cidade} ({filial})",
                icon=folium.Icon(color=cores_filiais[filial])
            ).add_to(mapa)

# Salvar o mapa
mapa.save('mapa_pontos_embarque_cliente.html')

print("Mapa de pontos de embarque gerado e salvo como 'mapa_pontos_embarque_cliente.html'")
