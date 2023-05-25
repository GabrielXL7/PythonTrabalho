import pandas
jogosEsportePagos = [
    {'Nome': 'FIFA 22', 'Preços': 199.99, 'Avaliação': '7.2/10'},
    {'Nome': 'eFootball PES 2022', 'Preços': 199.99, 'Avaliação': '6.8/10'},
    {'Nome': 'NBA 2K22', 'Preços': 199.99, 'Avaliação': '8.0/10'},
    {'Nome': 'Madden NFL 22', 'Preços': 199.99, 'Avaliação': '7.5/10'},
    {'Nome': 'NHL 22', 'Preços': 199.99, 'Avaliação': '7.0/10'},
    {'Nome': 'Tony Hawks Pro Skater 1 + 2', 'Preços': 124.99, 'Avaliação': '9.1/10'},
    {'Nome': 'WRC 10 FIA World Rally Championship', 'Preços': 129.99, 'Avaliação': '8.3/10'},
    {'Nome': 'F1 2021', 'Preços': 199.99, 'Avaliação': '8.7/10'},
    {'Nome': 'Tennis World Tour 2', 'Preços': 119.99, 'Avaliação': '6.5/10'},
    {'Nome': 'Pro Cycling Manager 2021', 'Preços': 129.99, 'Avaliação': '7.8/10'},
    {'Nome': 'PGA TOUR 2K21', 'Preços': 119.99, 'Avaliação': '8.2/10'},
    {'Nome': 'Cricket 19', 'Preços': 99.99, 'Avaliação': '7.1/10'},
    {'Nome': 'Ride 4', 'Preços': 129.99, 'Avaliação': '7.6/10'},
    {'Nome': 'Rugby 22', 'Preços': 149.99, 'Avaliação': '6.7/10'},
    {'Nome': 'Hunting Simulator 2', 'Preços': 79.99, 'Avaliação': '6.4/10'}
]

jogosEsporteGratuito = [
    {'Nome': 'Neverwinter', 'Preços': '[Gratuito]', 'Avaliação': '7.9/10'},
    {'Nome': 'Brawlhalla', 'Preços': '[Gratuito]', 'Avaliação': '8.1/10'},
    {'Nome': 'Dota 2', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Path of Exile', 'Preços': '[Gratuito]', 'Avaliação': '9.2/10'},
    {'Nome': 'World of Tanks', 'Preços': '[Gratuito]', 'Avaliação': '8.4/10'},
    {'Nome': 'AdventureQuest 3D', 'Preços': '[Gratuito]', 'Avaliação': '7.8/10'},
    {'Nome': 'Apex Legends', 'Preços': '[Gratuito]', 'Avaliação': '8.7/10'},
    {'Nome': 'War Thunder', 'Preços': '[Gratuito]', 'Avaliação': '8.6/10'},
    {'Nome': 'Golf With Your Friends', 'Preços': '[Gratuito]', 'Avaliação': '7.7/10'},
    {'Nome': 'Ball 3D: Soccer Online', 'Preços': '[Gratuito]', 'Avaliação': '7.9/10'},
    {'Nome': 'Frozen Free Fall: Snowball Fight', 'Preços': '[Gratuito]', 'Avaliação': '7.6/10'},
    {'Nome': 'Rec Room', 'Preços': '[Gratuito]', 'Avaliação': '8.2/10'},
    {'Nome': 'The Lord of the Rings Online™', 'Preços': '[Gratuito]', 'Avaliação': '8.0/10'},
    {'Nome': 'TrackMania Nations Forever', 'Preços': '[Gratuito]', 'Avaliação': '8.7/10'},
    {'Nome': 'Fishing Planet: Bottom Power Pack', 'Preços': '[Gratuito]', 'Avaliação': '7.4/10'}
]

jogosEsportePagoGratuito = [
    {'Nome': 'FIFA 22', 'Preços': 199.99, 'Avaliação': '7.9/10'},
    {'Nome': 'Fishing Planet: Bottom Power Pack', 'Preços': '[Gratuito]', 'Avaliação': '7.4/10'},
    {'Nome': 'Madden NFL 22', 'Preços': 199.99, 'Avaliação': '7.5/10'},
    {'Nome': 'Golf With Your Friends', 'Preços': '[Gratuito]', 'Avaliação': '7.7/10'},
    {'Nome': 'Tony Hawks Pro Skater 1 + 2', 'Preços': 124.99, 'Avaliação': '9.1/10'},
    {'Nome': 'WRC 10 FIA World Rally Championship', 'Preços': 129.99, 'Avaliação': '9.5/10'},
    {'Nome': 'War Thunder', 'Preços': '[Gratuito]', 'Avaliação': '8.6/10'},
    {'Nome': 'Ball 3D: Soccer Online', 'Preços': '[Gratuito]', 'Avaliação': '7.9/10'},
    {'Nome': 'Frozen Free Fall: Snowball Fight', 'Preços': '[Gratuito]', 'Avaliação': '7.6/10'},
    {'Nome': 'NHL 22', 'Preços': 199.99, 'Avaliação': '7.0/10'},
    {'Nome': 'Rec Room', 'Preços': '[Gratuito]', 'Avaliação': '8.2/10'},
    {'Nome': 'NBA 2K22', 'Preços': 199.99, 'Avaliação': '8.0/10'},
    {'Nome': 'eFootball PES 2022', 'Preços': 199.99, 'Avaliação': '6.8/10'},
    {'Nome': 'The Lord of the Rings Online™', 'Preços': '[Gratuito]', 'Avaliação': '8.0/10'},
    {'Nome': 'TrackMania Nations Forever', 'Preços': '[Gratuito]', 'Avaliação': '8.7/10'},
]

dataEsportePago = pandas.DataFrame(jogosEsportePagos)
dataEsporteGratuito = pandas.DataFrame(jogosEsporteGratuito)
dataEsportePagoGratuito = pandas.DataFrame(jogosEsportePagoGratuito)
