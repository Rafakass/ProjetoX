<!DOCTYPE html>
<html>
<head>
    <title>Tabela de Embarcadores Editável</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h2>Tabela de Embarcadores por Filial</h2>
    <table id="embarcadoresTable">
        <tr>
            <th>Filial</th>
            <th>Embarcador</th>
            <th>Quantidade de Viagens</th>
        </tr>
        <tr>
            <td>Amambai</td>
            <td>Renan</td>
            <td><input type="number" value="120" onchange="updateMap()"></td>
        </tr>
        <!-- Continue with other rows... -->
    </table>

    <br>
    <button onclick="updateMap()">Atualizar Mapa</button>

    <div id="map" style="height: 500px;"></div>

    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
        // Coordenadas das filiais (exemplos, ajuste conforme necessário)
        const coords = {
            'Amambai': [-23.1047, -55.2256],
            'Bataypora': [-22.2947, -53.2703],
            // Continue with other coordinates...
        };

        // Inicializar o mapa
        const map = L.map('map').setView([-20.4697, -54.6201], 6);

        // Adicionar camada de mapa
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; OpenStreetMap contributors'
        }).addTo(map);

        // Função para atualizar o mapa conforme os dados da tabela
        function updateMap() {
            map.eachLayer(layer => {
                if (layer.options && layer.options.icon) {
                    map.removeLayer(layer);
                }
            });

            const table = document.getElementById('embarcadoresTable');
            const rows = table.getElementsByTagName('tr');

            for (let i = 1; i < rows.length; i++) {
                const cells = rows[i].getElementsByTagName('td');
                const filial = cells[0].innerText;
                const embarcador = cells[1].innerText;
                const viagens = cells[2].getElementsByTagName('input')[0].value;

                const popupContent = `<b>${embarcador}:</b> <span style="color:blue;">${viagens}</span>`;

                L.marker(coords[filial]).addTo(map)
                    .bindPopup(`<b>Filial:</b> ${filial}<br>${popupContent}`);
            }
        }

        // Chamar a função para criar o mapa inicial
        updateMap();
    </script>
</body>
</html>
