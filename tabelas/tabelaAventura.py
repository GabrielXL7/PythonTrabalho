import pandas
jogosAventuraPagos = [
    {'Nome': 'Red Dead Redemption 2', 'Preços': 299.90, 'Avaliação': '09/10'},
    {'Nome': 'The Witcher 3: Wild Hunt', 'Preços': 79.99, 'Avaliação': '10/10'},
    {'Nome': 'Assassins Creed Valhalla', 'Preços': 199.99, 'Avaliação': '10/10'},
    {'Nome': 'Dark Souls III', 'Preços': 257.90, 'Avaliação': '9.5/10'},
    {'Nome': 'Sekiro: Shadows Die Twice', 'Preços': 199.90, 'Avaliação': '10/10'},
    {'Nome': 'Tomb Raider', 'Preços': 34.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Subnautica', 'Preços': 57.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Hellblade: Senuas Sacrifice', 'Preços': 55.99, 'Avaliação': '9.5/10'},
    {'Nome': 'A Plague Tale: Innocence', 'Preços': 25.98, 'Avaliação': '9.5/10'},
    {'Nome': 'The Forest', 'Preços': 37.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Control', 'Preços': 129.00, 'Avaliação': '9.5/10'},
    {'Nome': 'Resident Evil 2', 'Preços': 139.90, 'Avaliação': '9.5/10'},
    {'Nome': 'Dishonored 2', 'Preços': 89.99, 'Avaliação': '9.5/10'},
    {'Nome': 'A Way Out', 'Preços': 17.80, 'Avaliação': '9.5/10'},
    {'Nome': 'Celeste', 'Preços': 36.99, 'Avaliação': '9.5/10'}
]

jogosAventuraGratuito = [
    {'Nome': 'Dota 2', 'Preços': '[Gratuito]','Avaliação': '09/10'},
    {'Nome': 'Warframe', 'Preços': '[Gratuito]','Avaliação': '10/10'},
    {'Nome': 'Path of Exile', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Apex Legends', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Paladins', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Team Fortress 2', 'Preços':'[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Unturned', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Destiny 2', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Neverwinter', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'War Thunder', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'World of Tanks', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Brawlhalla', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'AdventureQuest 3D', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'The Lord of the Rings Online™', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Star Trek Online', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'}
]

jogosAventuraPagoGratuito = [
    {'Nome': 'Resident Evil 2', 'Preços': 139.90, 'Avaliação': '9.5/10'},
    {'Nome': 'Dota 2', 'Preços': '[Gratuito]', 'Avaliação': '09/10'},
    {'Nome': 'Warframe', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Control', 'Preços': 129.00, 'Avaliação': '9.5/10'},
    {'Nome': 'Path of Exile', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Dishonored 2', 'Preços': 89.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Apex Legends', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'Rust', 'Preços': 103.49, 'Avaliação': '10/10'},
    {'Nome': 'Paladins', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'Team Fortress 2', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'A Way Out', 'Preços': 17.80, 'Avaliação': '9.5/10'},
    {'Nome': 'Unturned', 'Preços': '[Gratuito]', 'Avaliação': '10/10'},
    {'Nome': 'A Plague Tale: Innocence', 'Preços': 25.98, 'Avaliação': '9.5/10'},
    {'Nome': 'Destiny 2', 'Preços': '[Gratuito]', 'Avaliação': '9.5/10'},
    {'Nome': 'The Forest', 'Preços': 37.99, 'Avaliação': '9.5/10'},
    {'Nome': 'Celeste', 'Preços': 36.99, 'Avaliação': '9.5/10'}
]

dataAventuraPago = pandas.DataFrame(jogosAventuraPagos)
dataAventuraGratuito = pandas.DataFrame(jogosAventuraGratuito)
dataAventuraPagoGratuito = pandas.DataFrame(jogosAventuraPagoGratuito)
