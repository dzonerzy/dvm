__author__ = 'dzonerzy'

class Opcodes:

    ops = dict({
        "INCP": 0xa0,  # incrementa base pointer
        "DECP": 0xa1,  # decrementa base pointer
        "INCSP": 0xb0,  # incrementa stack pointer
        "DECSP": 0xb1,  # decrementa stack pointer
        "INCBSP": 0xdd,  # incrementa byte al puntatore
        "DECBSP": 0xde,  # decrementa byte al puntatore

        "CSTRSP": 0x7e,  # carica stringa nello stack pointer


        "MMSP": 0x50,  # muove la memoria nello stack pointer buff,dest,size

        "AGSP": 0xba,  # aggiunge x al byte puntato dallo SP
        "TOSP": 0xbb,  # rimuove x al byte puntato dallo SP

        "SSU": 0xc0,  # salta se uguale
        "SSUMM": 0xc1,  # salta se uguale o maggiore
        "SSUM": 0xc2,  # salta se uguale o minore
        "SSM": 0xc3,  # salta se minore
        "SSMM": 0xc4,  # salta se maggiore
        "SSD": 0xc5,  # salta se diverso

        "SSUD": 0xca,  # salta se uguale (dietro)
        "SSUMMD": 0xcb,  # salta se uguale o maggiore (dietro)
        "SSUMD": 0xcc,  # salta se uguale o minore (dietro)
        "SSMD": 0xcd,  # salta se minore (dietro)
        "SSMMD": 0xce,  # salta se maggiore (dietro)
        "SSDD": 0xcf,  # salta se diverso (dietro)


        "SSP": 0x60,  # stampa puntatore SP
        "EXT": 0xff,  # exit

        "CB": 0xfa,  # Controllo booleano

        "SA": 0x1a,  # salta vanti
        "SD": 0x1b,  # salta dietro

        "LICSP": 0x90  # leggi input copia stack pointer
    })

    ops_size = dict({
        0xa0: 0,  # INCP
        0xa1: 0,  # DECP
        0xb0: 0,  # INCSP
        0xb1: 0,  # DECSP
        0xdd: 1,  # INCBSP
        0xde: 1,  # DECBSP

        0x7e: 1,  # CSTRSP

        0x50: 3,  # MMSP

        0xba: 1,  # AGSP
        0xbb: 1,  # TOSP

        0xc0: 1,  # SSU
        0xc1: 1,  # SSUMM
        0xc2: 1,  # SSUM
        0xc3: 1,  # SSM
        0xc4: 1,  # SSMM
        0xc5: 1,  # SSD

        0xca: 1,  # SSUD
        0xcb: 1,  # SSUMMD
        0xcc: 1,  # SSUMD
        0xcd: 1,  # SSMD
        0xce: 1,  # SSMMD
        0xcf: 1,  # SSDD

        0x60: 0,  # SSP
        0xff: 0,  # EXT

        0xfa: 1,  # CB

        0x1a: 1,  # SA
        0x1b: 1,  # SD

        0x90: 0,  # LICSP

    })

    ops_reservation = dict({
        0x7e: 0xffff,
        0x60: 0xffff,
    })


class ReserverdBytes:

    reserved = dict({
        0xffff: 0x01,
        0xfff1: 0x0f
    })
