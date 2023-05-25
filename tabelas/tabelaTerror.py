import pandas

jogosTerrorPagos = [
    {'Nome': 'Resident Evil Village', 'Preços': 199.99,'Avaliação': '8.7/10'},
    {'Nome': 'Outlast 2', 'Preços': 44.99,'Avaliação': '8.2/10'},
    {'Nome': 'Amnesia: Rebirth', 'Preços': 69.99, 'Avaliação': '7.9/10'},
    {'Nome': 'Alien: Isolation', 'Preços': 74.99, 'Avaliação': '9.0/10'},
    {'Nome': 'The Evil Within 2', 'Preços': 149.99, 'Avaliação': '8.4/10'},
    {'Nome': 'Little Nightmares II', 'Preços': 99.90, 'Avaliação': '8.6/10'},
    {'Nome': 'Layers of Fear 2', 'Preços': 54.99, 'Avaliação': '7.8/10'},
    {'Nome': 'Blair Witch', 'Preços': 54.99, 'Avaliação': '7.2/10'},
    {'Nome': 'Phasmophobia', 'Preços': 37.99, 'Avaliação': '9.1/10'},
    {'Nome': 'Observer: System Redux', 'Preços': 89.99, 'Avaliação': '8.5/10'},
    {'Nome': 'SOMA', 'Preços': 39.99, 'Avaliação': '8.9/10'},
    {'Nome': 'The Forest', 'Preços': 36.99, 'Avaliação': '9.3/10'},
    {'Nome': 'Dead Space', 'Preços': 29.99, 'Avaliação': '9.2/10'},
    {'Nome': 'Visage', 'Preços': 47.99, 'Avaliação': '8.0/10'},
    {'Nome': 'Darkwood', 'Preços': 36.99, 'Avaliação': '8.3/10'}
]

jogosTerrorGratuito = [
    {'Nome': 'Dead Frontier 2', 'Preços': '[Gratuito]','Avaliação': '8.5/10'},
    {'Nome': 'Cry of Fear', 'Preços': '[Gratuito]','Avaliação': '9.2/10'},
    {'Nome': 'SCP - Containment Breach', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Doki Doki Literature Club!', 'Preços': '[Gratuito]', 'Avaliação': '9.7/10'},
    {'Nome': 'Spookys Jump Scare Mansion', 'Preços': '[Gratuito]', 'Avaliação': '9.1/10'},
    {'Nome': 'The Joy of Creation: Reborn', 'Preços':'[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'No More Room in Hell', 'Preços': '[Gratuito]', 'Avaliação': '9.3/10'},
    {'Nome': 'Deceit', 'Preços': '[Gratuito]', 'Avaliação': '8.0/10'},
    {'Nome': 'Unturned', 'Preços': '[Gratuito]', 'Avaliação': '9.3/10'},
    {'Nome': 'The Expendabros', 'Preços': '[Gratuito]', 'Avaliação': '9.1/10'},
    {'Nome': 'Hide and Shriek', 'Preços': '[Gratuito]', 'Avaliação': '7.5/10'},
    {'Nome': 'Emily Wants to Play', 'Preços': '[Gratuito]', 'Avaliação': '7.6/10'},
    {'Nome': 'The Witchs House', 'Preços': '[Gratuito]', 'Avaliação': '9.2/10'},
    {'Nome': 'One Late Night', 'Preços': '[Gratuito]', 'Avaliação': '8.4/10'},
    {'Nome': 'IMSCARED', 'Preços': '[Gratuito]', 'Avaliação': '8.8/10'}
]

jogosTerrorPagoGratuito = [
    {'Nome': 'Resident Evil Village', 'Preços': 199.99, 'Avaliação': '8.7/10'},
    {'Nome': 'Outlast 2', 'Preços': 44.99, 'Avaliação': '8.2/10'},
    {'Nome': 'Little Nightmares II', 'Preços': 99.90, 'Avaliação': '8.6/10'},
    {'Nome': 'Cry of Fear', 'Preços': '[Gratuito]', 'Avaliação': '9.2/10'},
    {'Nome': 'The Evil Within 2', 'Preços': 149.99, 'Avaliação': '8.4/10'},
    {'Nome': 'SCP - Containment Breach', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'Doki Doki Literature Club!', 'Preços': '[Gratuito]', 'Avaliação': '9.7/10'},
    {'Nome': 'Layers of Fear 2', 'Preços': 54.99, 'Avaliação': '7.8/10'},
    {'Nome': 'Spookys Jump Scare Mansion', 'Preços': '[Gratuito]', 'Avaliação': '9.1/10'},
    {'Nome': 'Alien: Isolation', 'Preços': 74.99, 'Avaliação': '9.0/10'},
    {'Nome': 'The Joy of Creation: Reborn', 'Preços': '[Gratuito]', 'Avaliação': '9.0/10'},
    {'Nome': 'No More Room in Hell', 'Preços': '[Gratuito]', 'Avaliação': '9.3/10'},
    {'Nome': 'Amnesia: Rebirth', 'Preços': 69.99, 'Avaliação': '7.9/10'},
    {'Nome': 'Blair Witch', 'Preços': 54.99, 'Avaliação': '7.2/10'},
]

dataTerrorPago = pandas.DataFrame(jogosTerrorPagos)
dataTerrorGratuito = pandas.DataFrame(jogosTerrorGratuito)
dataTerrorPagoGratuito = pandas.DataFrame(jogosTerrorPagoGratuito)
