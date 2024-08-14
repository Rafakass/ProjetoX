import pandas as pd
import folium
import ipywidgets as widgets
from IPython.display import display, HTML

# Dados das rotas e cotas
data = {
    "Origem": ["Rio Brilhante", "Rio Brilhante", "Sidrolândia", "Sidrolândia", "Caarapó"],
    "Destino": ["Chapecó", "Toledo", "Joaçaba", "Xanxerê", "Arroio do Meio"],
    "Cotas Liberadas": [3, 2, 1, 3, 5],  # Quantidade de cotas liberadas
    "Cotas Utilizadas": [3, 2, 1, 3, 5],  # Quantidade de cotas utilizadas (editável)
}

df = pd.DataFrame(data)

# Função para atualizar a tabela
def atualizar_tabela(origem, destino, cotas_liberadas, cotas_utilizadas):
    df.loc[(df['Origem'] == origem) & (df['Destino'] == destino), 'Cotas Liberadas'] = cotas_liberadas
    df.loc[(df['Origem'] == origem) & (df['Destino'] == destino), 'Cotas Utilizadas'] = cotas_utilizadas
    display(HTML(df.to_html()))

# Widgets para edição
origem_widget = widgets.Dropdown(options=df["Origem"].unique(), description="Origem:")
destino_widget = widgets.Dropdown(options=df["Destino"].unique(), description="Destino:")
cotas_liberadas_widget = widgets.IntText(description="Cotas Liberadas:")
cotas_utilizadas_widget = widgets.IntText(description="Cotas Utilizadas:")
atualizar_button = widgets.Button(description="Atualizar")

# Ação do botão
def on_button_click(b):
    atualizar_tabela(origem_widget.value, destino_widget.value, cotas_liberadas_widget.value, cotas_utilizadas_widget.value)

atualizar_button.on_click(on_button_click)

# Interface para edição
editor = widgets.VBox([origem_widget, destino_widget, cotas_liberadas_widget, cotas_utilizadas_widget, atualizar_button])

# Mapa Interativo
mapa = folium.Map(location=[-20.4697, -54.6201], zoom_start=7)

# Filiais no MS
filiais = {
    "Campo Grande": [-20.4697, -54.6201],
    "Amambai": [-23.1047, -55.2259],
    "Batayporã": [-22.2942, -53.2701],
    "Caarapó": [-22.6368, -54.8206],
    "Chapadão do Sul": [-18.7889, -52.6267],
    "Corumbá": [-19.0098, -57.6536],
    "Dourados": [-22.2231, -54.812],
    "Guaíra": [-20.3176, -54.1037],
    "Maracaju": [-21.6105, -55.1674],
    "Mundo Novo": [-23.9355, -54.2817],
    "Naviraí": [-23.0617, -54.1992],
    "Nova Alvorada do Sul": [-21.4653, -54.3821],
    "São Gabriel do Oeste": [-19.3888, -54.5504],
    "Sidrolândia": [-20.9308, -54.9692],
}

for filial, coords in filiais.items():
    folium.Marker(location=coords, popup=filial).add_to(mapa)

# Adicionando rotas
rotas = [
    {"origem": [-21.8031, -54.5454], "destino": [-27.0963, -52.6188]},  # Rio Brilhante -> Chapecó
    {"origem": [-21.8031, -54.5454], "destino": [-24.7247, -53.7412]},  # Rio Brilhante -> Toledo
    {"origem": filiais["Sidrolândia"], "destino": [-27.1713, -51.5107]},  # Sidrolândia -> Joaçaba
    {"origem": filiais["Sidrolândia"], "destino": [-26.8744, -52.4038]},  # Sidrolândia -> Xanxerê
    {"origem": filiais["Caarapó"], "destino": [-29.3641, -51.9166]},  # Caarapó -> Arroio do Meio
]

for rota in rotas:
    folium.PolyLine([rota["origem"], rota["destino"]], color="blue", weight=2.5, opacity=1).add_to(mapa)

# Salvando o mapa em HTML
mapa_html = 'mapa_interativo.html'
mapa.save(mapa_html)

# Exibição dos elementos
display(HTML(f"<h2>Análise de Performance - Filiais MS</h2><p>Editável, sem armazenamento de dados.</p>"))
display(editor)
display(HTML(f"<p><a href='{mapa_html}' target='_blank'>Ver Mapa Interativo</a></p>"))
display(HTML(df.to_html()))
