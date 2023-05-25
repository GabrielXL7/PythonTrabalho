import pandas
jogosAcaoPagos = [
    {'Nome': 'Gta V', 'Preços': 82.41,'Avaliação': '09/10'},
    {'Nome': 'PlayerUnknowns Battlegrounds', 'Preços': 55.99,'Avaliação': '10/10'},
    {'Nome': 'Tom Clancys Rainbow Six Siege ', 'Preços': 59.99, 'Avaliação': '10/10'},
    {'Nome': 'ARK: Survival Evolved ', 'Preços': 37.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Rust', 'Preços': 103.49, 'Avaliação': '10/10'},
    {'Nome': 'Monster Hunter: World', 'Preços': 99.90, 'Avaliação': '9.5/10'},
    {'Nome': 'Dying Light', 'Preços': 74.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Borderlands 3', 'Preços': 17.98, 'Avaliação': '9.5/10'},
    {'Nome': 'DOOM Eternal', 'Preços': 37.25, 'Avaliação': '9.5/10'},
    {'Nome': 'Hunt: Showdown', 'Preços': 35.60, 'Avaliação': '9.5/10'},
    {'Nome': 'Far Cry 5', 'Preços': 179.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Resident Evil 2', 'Preços': 139.90, 'Avaliação': '9.5/10'},
    {'Nome': 'Metro Exodus', 'Preços': 12.88, 'Avaliação': '9.5/10'},
    {'Nome': 'Mortal Kombat 11', 'Preços': 22.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Sekiro: Shadows Die Twice', 'Preços': 199.90, 'Avaliação': '9.5/10'}
]

jogosAcaoGratuito = [
    {'Nome': 'Dota 2', 'Preços': '[Gratuito]','Avaliação': '9.0/10'},
    {'Nome': 'Team Fortress 2', 'Preços': '[Gratuito]','Avaliação': '10/10'},
    {'Nome': 'Warframe', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Path of Exile', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Paladins', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Counter-Strike: Global Offensive (CS:GO)', 'Preços':'[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Apex Legends', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Destiny 2', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'War Thunder', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Brawlhalla', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Unturned', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Warface', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Path of Exile', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Alien Swarm: Reactive Drop', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Fortnite', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'}
]

jogosAcaoPagoGratuito = [
    {'Nome': 'Gta V', 'Preços': 82.41,'Avaliação': '09/10'},
    {'Nome': 'Warface: Shadows Die Twice', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'PlayerUnknowns Battlegrounds', 'Preços': 55.99,'Avaliação': '10/10'},
    {'Nome': 'Tom Clancys Rainbow Six Siege ', 'Preços': 59.99, 'Avaliação': '10/10'},
    {'Nome': 'Dota 2', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'ARK: Survival Evolved ', 'Preços': 37.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Warframe', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Rust', 'Preços': 103.49, 'Avaliação': '10/10'},
    {'Nome': 'Team Fortress 2 ', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Monster Hunter: World', 'Preços': 99.90, 'Avaliação': '9.5/10'},
    {'Nome': 'Apex Legends', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Destiny 2', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Unturned', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Dying Light', 'Preços': 74.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Planetside 2', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
]

dataAcaoPago = pandas.DataFrame(jogosAcaoPagos)
dataAcaoGratuito = pandas.DataFrame(jogosAcaoGratuito)
dataAcaoPagoGratuito = pandas.DataFrame(jogosAcaoPagoGratuito)
