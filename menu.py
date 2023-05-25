import util
from tabelas import tabelaAcao, tabelaAventura, tabelaEsporte, tabelaTerror, tabelaRpg

repeticao = True
while repeticao:
        numCategoria = ['Ação', 'Aventura', 'Esporte', 'RPG', 'Terror']
        util.cabecalho()
        categoria = int(input())
        iSelecionado = categoria - 1
        if categoria == 1:

                print('\nVocê escolheu [{}]'.format(numCategoria[iSelecionado]))
                util.menu()
                tipoJogo = int(input())
                if tipoJogo == 1:
                        print('Aqui estar a tabela de jogos [PAGOS] : ')
                        print(util.style(tabelaAcao.dataAcaoPago))
                elif tipoJogo == 2:
                        print('Aqui estar a tabela de jogos [GRATUITO]: ')
                        print(util.style(tabelaAcao.dataAcaoGratuito))
                elif tipoJogo == 3:
                        print('Aqui estar a tabela de jogos [PAGOS/GRATUITO]: ')
                        print(util.style(tabelaAcao.dataAcaoPagoGratuito))
                else:
                        print('Enter para voltar')
                        input()

        elif categoria == 2:
                print('\nVocê escolheu [{}]'.format(numCategoria[iSelecionado]))
                util.menu()
                tipoJogo = int(input())
                if tipoJogo == 1:
                        print('Aqui estar a tabela de jogos [PAGOS] : ')
                        print(util.style(tabelaAventura.dataAventuraPago))
                elif tipoJogo == 2:
                        print('Aqui estar a tabela de jogos [GRATUITO]: ')
                        print(util.style(tabelaAventura.dataAventuraGratuito))
                elif tipoJogo == 3:
                        print('Aqui estar a tabela de jogos [PAGOS/GRATUITO]: ')
                        print(util.style(tabelaAventura.dataAventuraPagoGratuito))
                else:
                        print('Enter para voltar')
                        input()
        elif categoria == 4:
                print('\nVocê escolheu [{}]'.format(numCategoria[iSelecionado]))
                util.menu()
                tipoJogo = int(input())
                if tipoJogo == 1:
                        print('Aqui estar a tabela de jogos [PAGOS] : ')
                        print(util.style(tabelaRpg.dataRpgPago))
                elif tipoJogo == 2:
                        print('Aqui estar a tabela de jogos [GRATUITO]: ')
                        print(util.style(tabelaRpg.dataRpgGratuito))
                elif tipoJogo == 3:
                        print('Aqui estar a tabela de jogos [PAGOS/GRATUITO]: ')
                        print(util.style(tabelaRpg.dataRpgPagoGratuito))
                else:
                        print('Enter para voltar')
                        input()
        elif categoria == 3:
                print('\nVocê escolheu [{}]'.format(numCategoria[iSelecionado]))
                util.menu()
                tipoJogo = int(input())
                if tipoJogo == 1:
                        print('Aqui estar a tabela de jogos [PAGOS] : ')
                        print(util.style(tabelaEsporte.dataEsportePago))
                elif tipoJogo == 2:
                        print('Aqui estar a tabela de jogos [GRATUITO]: ')
                        print(util.style(tabelaEsporte.dataEsporteGratuito))
                elif tipoJogo == 3:
                        print('Aqui estar a tabela de jogos [PAGOS/GRATUITO]: ')
                        print(util.style(tabelaEsporte.dataEsportePagoGratuito))
                else:
                        print('Enter para voltar')
                        input()
        elif categoria == 5:
                print('\nVocê escolheu [{}]'.format(numCategoria[iSelecionado]))
                util.menu()
                tipoJogo = int(input())
                if tipoJogo == 1:
                        print('Aqui estar a tabela de jogos [PAGOS] : ')
                        print(util.style(tabelaTerror.dataTerrorPago))
                elif tipoJogo == 2:
                        print('Aqui estar a tabela de jogos [GRATUITO]: ')
                        print(util.style(tabelaTerror.dataTerrorGratuito))
                elif tipoJogo == 3:
                        print('Aqui estar a tabela de jogos [PAGOS/GRATUITO]: ')
                        print(util.style(tabelaTerror.dataTerrorPagoGratuito))
                else:
                        print('Enter para voltar')
                        input()
        else:
                repeticao = False

