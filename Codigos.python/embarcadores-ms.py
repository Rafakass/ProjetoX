import folium
from geopy.geocoders import Nominatim
import time

# Dados dos embarcadores e suas respectivas filiais
embarcadores = {
    "JACKSON": "MUNDO NOVO",
    "REBEKA": "MUNDO NOVO",
    "ANA": "CAMPO GRANDE",
    "ADRIANO G": "CAMPO GRANDE",
    "FERNANDO": "CAMPO GRANDE",
    "ADEILDO": "CAMPO GRANDE",
    "EMERSON": "CAMPO GRANDE",
    "GUILHERME": "CAMPO GRANDE",
    "MURILO": "CAMPO GRANDE",
    "ANDRE": "DOURADOS",
    "LUIZ FERNANDO": "DOURADOS",
    "MARCIO": "DOURADOS",
    "PEDROSO": "DOURADOS",
    "MARCO PEROBELI": "DOURADOS",
    "MATHEUS": "DOURADOS",
    "RAFAEL": "DOURADOS",
    "REINALDO": "DOURADOS",
    "ADRIANO JESUS": "PONTA PORA",
    "JADERSON": "MUNDO NOVO",
    "CAMILA": "MUNDO NOVO",
    "RENAN": "PONTA PORA"
}

# Cidades principais por filial
filiais = {
    "MUNDO NOVO": ["Mundo Novo", "Eldorado", "Iguatemi", "Itaquiraí", "Naviraí", "Sete Quedas", "Tacuru"],
    "PONTA PORA": ["Ponta Porã", "Amambai", "Antônio João", "Aral Moreira", "Bela Vista", "Caarapó", "Coronel Sapucaia", "Laguna Carapã"],
    "DOURADOS": ["Dourados", "Anaurilândia", "Angélica", "Batayporã", "Deodápolis", "Fátima do Sul", "Guia Lopes da Laguna", "Itaporã", "Ivinhema", "Jardim", "Maracaju", "Nioaque", "Nova Alvorada do Sul", "Nova Andradina", "Novo Horizonte do Sul", "Porto Murtinho", "Rio Brilhante"],
    "CAMPO GRANDE": ["Campo Grande", "Aparecida do Taboado", "Aquidauana", "Bandeirantes", "Bataguassu", "Bodoquena", "Bonito", "Brasilândia", "Camapuã", "Chapadão do Sul", "Corumbá", "Costa Rica", "Coxim", "Miranda", "Ribas do Rio Pardo", "São Gabriel do Oeste", "Sidrolândia", "Sonora", "Terenos", "Três Lagoas"]
}

# Inicializar o geolocalizador
geolocator = Nominatim(user_agent="geoapiExercises")

# Função para obter coordenadas com cache
coordenadas_cache = {}

def obter_coordenadas(cidade):
    if cidade in coordenadas_cache:
        return coordenadas_cache[cidade]
    try:
        location = geolocator.geocode(cidade + ", Mato Grosso do Sul, Brazil")
        if location:
            coordenadas_cache[cidade] = (location.latitude, location.longitude)
            return coordenadas_cache[cidade]
    except Exception as e:
        print(f"Erro ao buscar coordenadas para {cidade}: {e}")
    return None

# Configurações de cores para cada filial
cores_filiais = {
    "MUNDO NOVO": "blue",
    "PONTA PORA": "red",
    "DOURADOS": "green",
    "CAMPO GRANDE": "orange"
}

# Criar mapa centrado no Mato Grosso do Sul
mapa = folium.Map(location=[-20.4428, -54.6461], zoom_start=6)

# Adicionar pontos de embarque ao mapa para cada embarcador
total_cidades = sum(len(filiais[filial]) for filial in filiais)
cidade_atual = 0

for embarcador, filial in embarcadores.items():
    for cidade in filiais[filial]:
        cidade_atual += 1
        print(f"Processando {cidade} ({cidade_atual}/{total_cidades})")
        coordenadas = obter_coordenadas(cidade)
        if coordenadas:
            folium.Marker(
                location=coordenadas,
                popup=f"{cidade} - {embarcador} ({filial})",
                icon=folium.Icon(color=cores_filiais[filial])
            ).add_to(mapa)
        time.sleep(1)  # Atraso para evitar sobrecarga na API de geocodificação

# Salvar o mapa
mapa.save('mapa_embarcadores_analise_performance.html')

print("Mapa de análise de performance gerado e salvo como 'mapa_embarcadores_analise_performance.html'")
