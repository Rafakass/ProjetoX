import folium
import time

# Dados de exemplo
data = [
    {'latitude': -20.0, 'longitude': -54.0, 'filial': 'Filial A', 'embarcador': 'Embarcador A', 'viagens': 10},
    {'latitude': -20.5, 'longitude': -54.5, 'filial': 'Filial B', 'embarcador': 'Embarcador B', 'viagens': 20}
]

# Inicialize o mapa
print("Inicializando o mapa...")
m = folium.Map(location=[-20.25, -54.25], zoom_start=7)  # Ajustado para melhor visualização

# Adicione marcadores com campos editáveis
total_markers = len(data)
for i, item in enumerate(data):
    popup_html = f"""
    <strong>Filial:</strong> {item['filial']}<br>
    <strong>Embarcador:</strong> {item['embarcador']}<br>
    <strong>Viagens:</strong> <input type="text" id="viagens_{item['filial']}" value="{item['viagens']}" />
    <button onclick="updateDisplay()">Atualizar</button>
    <script>
    function updateDisplay() {{
        var inputs = document.querySelectorAll('input[type="text"]');
        var display = 'Viagens atualizadas:<br>';
        inputs.forEach(function(input) {{
            display += input.id + ': ' + input.value + '<br>';
        }});
        document.getElementById('display').innerHTML = display;
    }}
    </script>
    """
    folium.Marker(
        location=[item['latitude'], item['longitude']],
        popup=folium.Popup(folium.Html(popup_html, script=True), max_width=300)
    ).add_to(m)

    # Indicador de progresso
    progress = (i + 1) / total_markers * 100
    print(f"Adicionando marcadores: {progress:.2f}% concluído")
    time.sleep(0.5)  # Simula um atraso para visualização do progresso

# Adicionar um lugar para exibir as atualizações
m.get_root().html.add_child(folium.Element('<div id="display" style="position:fixed; bottom:0; left:0; background: white; padding: 10px; width: 100%;"></div>'))

# Salvar o mapa em um arquivo HTML
print("Salvando o mapa...")
m.save('mapa_interativo.html')
print("Mapa salvo como mapa_interativo.html")
