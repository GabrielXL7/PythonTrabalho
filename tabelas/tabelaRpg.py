import pandas
jogosRpgPagos = [
    {'Nome': 'The Witcher 3: Wild Hunt', 'Preços': 119.99,'Avaliação': '9.8/10'},
    {'Nome': 'Divinity: Original Sin 2', 'Preços': 129.99,'Avaliação': '9.6/10'},
    {'Nome': 'Disco Elysium', 'Preços': 79.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Skyrim', 'Preços': 39.99, 'Avaliação': '9.3/10'},
    {'Nome': 'Fallout: New Vegas', 'Preços': 39.99, 'Avaliação': '9.2/10'},
    {'Nome': 'Dark Souls III', 'Preços': 69.99, 'Avaliação': '9.1/10'},
    {'Nome': 'Final Fantasy XIV Online', 'Preços': 39.99, 'Avaliação': '9.0/10'},
    {'Nome': 'Pillars of Eternity II: Deadfire', 'Preços': 119.99, 'Avaliação': '8.9/10'},
    {'Nome': 'Monster Hunter: World', 'Preços': 119.99, 'Avaliação': '8.8/10'},
    {'Nome': 'Dragon Age: Origins', 'Preços': 39.99, 'Avaliação': '8.7/10'},
    {'Nome': 'Baldurs Gate II: Enhanced Edition', 'Preços': 34.99, 'Avaliação': '8.6/10'},
    {'Nome': 'Kingdom Come: Deliverance', 'Preços': 39.99, 'Avaliação': '8.5/10'},
    {'Nome': 'The Elder Scrolls Online', 'Preços': 39.99, 'Avaliação': '8.4/10'},
    {'Nome': 'NieR: Automata', 'Preços': 159.99, 'Avaliação': '8.3/10'},
    {'Nome': 'Torchlight II', 'Preços': 37.99, 'Avaliação': '8.2/10'}
]

jogosRpgGratuito = [
    {'Nome': 'Path of Exile', 'Preços': '[Gratuito]','Avaliação': '9.2/10'},
    {'Nome': 'Warframe', 'Preços': '[Gratuito]','Avaliação': '9.0/10'},
    {'Nome': 'Destiny 2', 'Preços': '[Gratuito]', 'Avaliação': '8.3/10'},
    {'Nome': 'Dauntless', 'Preços': '[Gratuito]', 'Avaliação': '8.1/10'},
    {'Nome': 'Genshin Impact', 'Preços': '[Gratuito]', 'Avaliação': '8.1/10'},
    {'Nome': 'Star Trek Online', 'Preços':'[Gratuito]', 'Avaliação': '7.4/10'},
    {'Nome': 'Neverwinter', 'Preços': '[Gratuito]', 'Avaliação': '8.0/10'},
    {'Nome': 'Paladins', 'Preços': '[Gratuito]', 'Avaliação': '8.3/10'},
    {'Nome': 'The Lord of the Rings Online™', 'Preços': '[Gratuito]', 'Avaliação': '8.0/10'},
    {'Nome': 'Dungeon Defenders II', 'Preços': '[Gratuito]', 'Avaliação': '7.7/10'},
    {'Nome': 'Kingdoms of Amalur: Reckoning - FATE Edition', 'Preços': '[Gratuito]', 'Avaliação': '9.1/10'},
    {'Nome': 'Tree of Savior (English Ver.)', 'Preços': '[Gratuito]', 'Avaliação': '7.9/10'},
    {'Nome': 'Trove', 'Preços': '[Gratuito]', 'Avaliação': '8.2/10'},
    {'Nome': 'Albion Online', 'Preços': '[Gratuito]', 'Avaliação': '7.9/10'},
    {'Nome': 'Secret World Legends', 'Preços': '[Gratuito]', 'Avaliação': '8.1/10'}
]

jogosRpgPagoGratuito = [
    {'Nome': 'Path of Exile', 'Preços': '[Gratuito]', 'Avaliação': '9.2/10'},
    {'Nome': 'Warframe', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Destiny 2', 'Preços': '[Gratuito]', 'Avaliação': '8.3/10'},
    {'Nome': 'Dauntless', 'Preços': '[Gratuito]', 'Avaliação': '8.1/10'},
    {'Nome': 'Genshin Impact', 'Preços': '[Gratuito]', 'Avaliação': '8.1/10'},
    {'Nome': 'Star Trek Online', 'Preços': '[Gratuito]', 'Avaliação': '7.4/10'},
    {'Nome': 'Neverwinter', 'Preços': '[Gratuito]', 'Avaliação': '8.0/10'},
    {'Nome': 'Paladins', 'Preços': '[Gratuito]', 'Avaliação': '8.3/10'},
    {'Nome': 'Team Fortress 2 ', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Monster Hunter: World', 'Preços': 99.90, 'Avaliação': '9.5/10'},
    {'Nome': 'Apex Legends', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Destiny 2', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Unturned', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Dying Light', 'Preços': 74.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Planetside 2', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
]

dataRpgPago = pandas.DataFrame(jogosRpgPagos)
dataRpgGratuito = pandas.DataFrame(jogosRpgGratuito)
dataRpgPagoGratuito = pandas.DataFrame(jogosRpgPagoGratuito)
