# To ignore numpy errors:
#     pylint: disable=E1101
import os
import os.path as op
import configmail
import requests
import json
import smtplib
from email import encoders
from email.utils import COMMASPACE, formatdate
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from time import sleep
from datetime import datetime
from binance.client import Client
from numpy import array
import talib


os.system("clear")


# KLINE RECORD
OPEN_TIME = 0
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = int(4)
VOLUME = 5
CLOSE_TIME = 6
QUOTE_ASSET_VOLUME = 7
NUMBER_OF_TRADES = 8
TAKER_BUY_BASE_ASSET_VOLUME = 9
TAKER_BUY_QUOTE_ASSET_VOLUME = 10
IGNORE = 11

# Valores a modificar
activo = 'BTC'       # Símbolo de la criptomoneda ej: BTC. ETH, LTC, BCHSV, etc
CompraCripto = 0.05       # Cantidad de moneDas a comprar
Balance = 1         # Dinero depositado
# Tomar ganancias al superar el valor en moneda (contra)
Tomar_Ganancia = 0.005
# Porcentaje de Stop Loss, dispuesto a perder si cae el precio abruptamente
Porc_StopLoss = 5.0
# Toma ganancias mayores al porcentaje especificado y finaliza trading
Ganancia_Porc = 5.0
Refresh_seg = 30       # Muestreo en segundos
Num_operaciones = 0


# Variables
broker = 'BINANCE'
candle = 1  # Represented in minutes
contra = 'USDT'
symbol = activo + contra
market = symbol

if contra != 'USDT':
    dml = 8
else:
    dml = 2

registro = -1  # Primero = 0, último = -1


def get_signal(market, candle, broker):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://scanner.tradingview.com/crypto/scan"

    payload = {
        "symbols": {
            "tickers": ["{}:{}".format(broker, market)],
            "query": {"types": []}
        },
        "columns": [
            "Recommend.Other|{}".format(candle),
            "Recommend.All|{}".format(candle),
            "Recommend.MA|{}".format(candle),
            "RSI|{}".format(candle),
            "RSI[1]|{}".format(candle),
            "Stoch.K|{}".format(candle),
            "Stoch.D|{}".format(candle),
            "Stoch.K[1]|{}".format(candle),
            "Stoch.D[1]|{}".format(candle),
            "CCI20|{}".format(candle),
            "CCI20[1]|{}".format(candle),
            "ADX|{}".format(candle),
            "ADX+DI|{}".format(candle),
            "ADX-DI|{}".format(candle),
            "ADX+DI[1]|{}".format(candle),
            "ADX-DI[1]|{}".format(candle),
            "AO|{}".format(candle),
            "AO[1]|{}".format(candle),
            "Mom|{}".format(candle),
            "Mom[1]|{}".format(candle),
            "MACD.macd|{}".format(candle),
            "MACD.signal|{}".format(candle),
            "Rec.Stoch.RSI|{}".format(candle),
            "Stoch.RSI.K|{}".format(candle),
            "Rec.WR|{}".format(candle),
            "W.R|{}".format(candle),
            "Rec.BBPower|{}".format(candle),
            "BBPower|{}".format(candle),
            "Rec.UO|{}".format(candle),
            "UO|{}".format(candle),
            "EMA10|{}".format(candle),
            "close|{}".format(candle),
            "SMA10|{}".format(candle),
            "EMA20|{}".format(candle),
            "SMA20|{}".format(candle),
            "EMA30|{}".format(candle),
            "SMA30|{}".format(candle),
            "EMA50|{}".format(candle),
            "SMA50|{}".format(candle),
            "EMA100|{}".format(candle),
            "SMA100|{}".format(candle),
            "EMA200|{}".format(candle),
            "SMA200|{}".format(candle),
            "Rec.Ichimoku|{}".format(candle),
            "Ichimoku.BLine|{}".format(candle),
            "Rec.VWMA|{}".format(candle),
            "VWMA|{}".format(candle),
            "Rec.HullMA9|{}".format(candle),
            "HullMA9|{}".format(candle),
            "Pivot.M.Classic.S3|{}".format(candle),
            "Pivot.M.Classic.S2|{}".format(candle),
            "Pivot.M.Classic.S1|{}".format(candle),
            "Pivot.M.Classic.Middle|{}".format(candle),
            "Pivot.M.Classic.R1|{}".format(candle),
            "Pivot.M.Classic.R2|{}".format(candle),
            "Pivot.M.Classic.R3|{}".format(candle),
            "Pivot.M.Fibonacci.S3|{}".format(candle),
            "Pivot.M.Fibonacci.S2|{}".format(candle),
            "Pivot.M.Fibonacci.S1|{}".format(candle),
            "Pivot.M.Fibonacci.Middle|{}".format(candle),
            "Pivot.M.Fibonacci.R1|{}".format(candle),
            "Pivot.M.Fibonacci.R2|{}".format(candle),
            "Pivot.M.Fibonacci.R3|{}".format(candle),
            "Pivot.M.Camarilla.S3|{}".format(candle),
            "Pivot.M.Camarilla.S2|{}".format(candle),
            "Pivot.M.Camarilla.S1|{}".format(candle),
            "Pivot.M.Camarilla.Middle|{}".format(candle),
            "Pivot.M.Camarilla.R1|{}".format(candle),
            "Pivot.M.Camarilla.R2|{}".format(candle),
            "Pivot.M.Camarilla.R3|{}".format(candle),
            "Pivot.M.Woodie.S3|{}".format(candle),
            "Pivot.M.Woodie.S2|{}".format(candle),
            "Pivot.M.Woodie.S1|{}".format(candle),
            "Pivot.M.Woodie.Middle|{}".format(candle),
            "Pivot.M.Woodie.R1|{}".format(candle),
            "Pivot.M.Woodie.R2|{}".format(candle),
            "Pivot.M.Woodie.R3|{}".format(candle),
            "Pivot.M.Demark.S1|{}".format(candle),
            "Pivot.M.Demark.Middle|{}".format(candle),
            "Pivot.M.Demark.R1|{}".format(candle)
        ]
    }

    resp = requests.post(url, headers=headers, data=json.dumps(payload)).json()
    signal = resp["data"][0]["d"][1]
    return signal


def signal():
    ms = ''
    signal = get_signal(market, candle, broker)
    if signal is None:
        signal = 0
    if signal > 0 and signal < 0.4:
        ms = 'Comprar'
    elif signal > 0.4:
        ms = 'Compra Fuerte'
    elif signal == 0:
        ms = 'Neutral'
    elif signal < 0 and signal > -0.4:
        ms = 'Vender'
    elif signal < -0.4:
        ms = 'Venta Fuerte'
    return ms


def send_mail_withattach(send_from, send_to, subject, message, files=[],
                         server="localhost", port=587, username='', password='',
                         use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (str): to name
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    try:

        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(message))

        for path in files:
            part = MIMEBase('application', "octet-stream")
            with open(path, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="{}"'.format(op.basename(path)))
            msg.attach(part)

        smtp = smtplib.SMTP(server, port)
        if use_tls:
            smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.quit()
        print("Success: Email sent!")
    except Exception as e:
        print("Email failed to send. Causa:\n{}").format(e)

# Envío de correo electrónico a través de gmail server autenticado
# Para que funcione debe activar la opcion en el siguiente link:
# https://myaccount.google.com/lesssecureapps


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(configmail.EMAIL_ADDRESS, configmail.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(configmail.EMAIL_ADDRESS,
                        configmail.TO_EMAIL_ADDRESS, message.encode('utf-8'))
        server.quit()
        print("Success: Email sent!")
    except Exception as e:
        print("Email failed to send. Causa:\n{}").format(e)


def mensaje(Balance, Ganancia, CompraCripto, activo, Precio_Actual_Cripto, promedio, tiempo):
    texto = """\n{}\nSe vendieron {} {} por {} Precio venta: {}\nPrecio Promedio {}: {}\nValoración: {}\nBeneficio/Pérdida: {}\n""".format(
        tiempo,
        CompraCripto,
        activo,
        round(CompraCripto * Precio_Actual_Cripto, dml),
        round(Precio_Actual_Cripto, dml),
        activo,
        round(promedio, dml),
        round(Balance + Precio_Compra + Ganancia, dml),
        round(Ganancia, dml)
    )
    return texto


def Display(SIGNAL, tiempo, Balance, valoracion, Precio_Compra, Ganancia, CompraCripto, activo, Precio_Actual_Cripto, promedio, Porcentaje, SMA, RSI, Total_GP, Total_GN):
    """Imprime resultado de los indicadores en pantalla.

    Args:
        Balance (float): Balance en estado de cuenta
        Valoración (float): Resultado de suma entre balance, compra cripto y Beneficio/Pérdida
        Precio_Compra (float): Precio compra del activo. ej: BTC, ETH, LTC, etc
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """

    texto = ("="*100) + "\n{}\nBalance = {}\nValoración: {}\nÚltima Compra: {} {} / {} {} PrecioCompra({}): {} Fecha/Hora Compra: {}\nPrecio {}: {}\nÚltimo Beneficio/Pérdida:({}%) {}\nPrecio Promedio {}(1hora): {} SMA: {} RSI:{} Señal: {}\nTotal Beneficio: {} Total Perdida: {}\nTotal Operaciones(compra/venta): {}".format(
        tiempo,
        round(Balance, dml),
        valoracion,
        CompraCripto,
        activo,
        round(Precio_Compra, dml),
        contra,
        activo,
        round(Precio_Compra_Cripto, dml),
        tiempocompra,
        activo,
        Precio_Actual_Cripto,
        round(Porcentaje, 2),
        round(Ganancia, dml),
        activo,
        round(promedio, dml),
        round(SMA, dml),
        round(RSI, 2),
        SIGNAL,
        round(Total_GP, dml),
        round(Total_GN, dml),
        Num_operaciones
    )
    return texto


try:

    # Escribir el log de compras y ventas
    def write_log(texto):
        with open("trading_log.txt", "a") as f:
            f.write(texto)
        f.close()

    # Convierte segundos BINANCE a Fecha con Hora

    def seconds_to_time(seconds_T):
        # .strftime("%A, %B %d, %Y %I:%M:%S")
        return datetime.fromtimestamp(int(seconds_T)/1000)

    client = Client("", "", {"verify": True, "timeout": 20})

    while True:

        Precio_Compra = 0
        Precio_Compra_Cripto = 0
        Porcentaje = 0
        Ganancia = 0
        Total_GP = 0
        Total_GN = 0
        tiempocompra = None
        Se_Compro = False
        Ope_Ganadas_Seg = 0     # Flag operaciones ganadas seguidas
        order = False
        seg = 0
        Saldo_Inicial = Balance
        valoracion = 0

        while order == False:
            try:
                CRIPTO = client.get_historical_klines(
                    symbol=symbol, interval=client.KLINE_INTERVAL_1MINUTE, start_str='1 hour ago UTC')

                SMA = talib.SMA(array([float(i[CLOSE]) for i in CRIPTO]))[-1]
                RSI = talib.RSI(array([float(i[CLOSE]) for i in CRIPTO]))[-1]
                SIGNAL = signal()

                # Calcula el promedio del precio de cierre de los datos en klines binance de la lista CRIPTO
                promedio = sum([float(i[CLOSE]) for i in CRIPTO]) / len(CRIPTO)
                # Calcula la media movil simple

                tiempo = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())

                Precio_Actual_Cripto = float(CRIPTO[registro][CLOSE])
                if Se_Compro:
                    valoracion = round(Balance + Precio_Compra + Ganancia, dml)
                    Porcentaje = (
                        (Precio_Actual_Cripto/Precio_Compra_Cripto) * 100)-100
                    Ganancia = Precio_Actual_Cripto * \
                        CompraCripto - float(Precio_Compra)

                texto = Display(SIGNAL,
                                tiempo,
                                Balance,
                                valoracion,
                                Precio_Compra,
                                Ganancia,
                                CompraCripto,
                                activo,
                                Precio_Actual_Cripto,
                                promedio,
                                Porcentaje,
                                SMA,
                                RSI,
                                Total_GP,
                                Total_GN)

                print(texto)

                # Ganancia = Precio_Actual_Cripto * \
                #    CompraCripto - float(Precio_Compra)
                # if Precio_Compra > 0:
                #    Porcentaje = ((Precio_Actual_Cripto/Precio_Compra_Cripto)*100)-100

                # Compra
                if (float(CRIPTO[registro][CLOSE]) <= promedio + promedio * (5/100)) and (not Se_Compro) and (SIGNAL in ['Vender', 'Comprar', 'Compra Fuerte']):
                    print('Buyyy')
                    # client.order_market_buy(symbol=symbol, quantity=quantity)
                    Precio_Compra = CompraCripto * \
                        float(CRIPTO[registro][CLOSE])
                    print(Precio_Compra, Balance)
                    if Precio_Compra > Balance:
                        print('No posee suficiente balance para comprar {} {} por valor de: {} USD'.format(
                            CompraCripto,
                            activo,
                            Precio_Compra
                        ))
                        break
                    Precio_Compra_Cripto = float(CRIPTO[registro][CLOSE])
                    Balance = Balance - Precio_Compra
                    Ganancia = Precio_Actual_Cripto * \
                        CompraCripto - float(Precio_Compra)
                    tiempocompra = tiempo
                    texto = """\n{}\nSe compraron {} {} por {} Precio compra:{}\nPrecio Promedio {}: {}\nValoración: {}\n{}""".format(
                        tiempo,
                        CompraCripto,
                        activo,
                        round(Precio_Compra, dml),
                        round(Precio_Actual_Cripto, dml),
                        activo,
                        round(promedio, dml),
                        round(Balance + Precio_Compra + Ganancia, dml),
                        38*"="
                    )
                    write_log(texto)
                    Num_operaciones += 1
                    Se_Compro = True

                # Venta si sube abruptamente
                if Porcentaje > 2 and Se_Compro:
                    # client.order_market_buy(symbol=symbol, quantity=quantity)
                    print('Sellll')
                    print(Porcentaje)
                    texto = mensaje(Balance,
                                    Ganancia,
                                    CompraCripto,
                                    activo,
                                    Precio_Actual_Cripto,
                                    promedio,
                                    tiempo) + 'Venta por Porcentaje > 2.0%\n' + 38*"="

                    Balance = Balance + Precio_Compra + Ganancia
                    Total_GP += Ganancia
                    Ope_Ganadas_Seg += 1
                    write_log(texto)
                    Num_operaciones += 1
                    Se_Compro = False
                    # order = True

                # Venta si se supera o pierde límite para tomar ganancias
                if ((Ganancia > Tomar_Ganancia) or (Ganancia <= -1 * Tomar_Ganancia)) and Se_Compro:
                    print('Sellll')
                    print(Ganancia)
                    if Ganancia > 0:
                        ms = 'Venta por Ganancia > ' + str(Tomar_Ganancia)
                    else:
                        ms = 'Venta por Ganancia <= - ' + str(Tomar_Ganancia)

                    texto = mensaje(Balance,
                                    Ganancia,
                                    CompraCripto,
                                    activo,
                                    Precio_Actual_Cripto,
                                    promedio,
                                    tiempo) + ms + '\n' + 38*"="

                    Balance = Balance + Precio_Compra + Ganancia
                    if Ganancia > 0:
                        Total_GP += Ganancia
                        Ope_Ganadas_Seg += 1
                    else:
                        Total_GN += Ganancia
                        Ope_Ganadas_Seg = 0
                    write_log(texto)
                    Num_operaciones += 1
                    Se_Compro = False
                    if Ope_Ganadas_Seg >= 5:
                        print(
                            'Se registraron mas de 5 operaciones en ganancia continuas')
                        subject = "Trading Bot. Mas de 5 operacioens en Ganancia continua."
                        write_log('\n' + subject + '\n' + 38*"=")
                        texto = Display(SIGNAL, tiempo, Balance,
                                        Balance, Precio_Compra,
                                        Ganancia, CompraCripto, activo,
                                        Precio_Actual_Cripto, promedio, Porcentaje,
                                        SMA, RSI, Total_GP, Total_GN)
                        send_mail_withattach(configmail.EMAIL_ADDRESS,
                                             configmail.TO_EMAIL_ADDRESS,
                                             subject,
                                             texto,
                                             ['trading_log.txt'],
                                             'smtp.gmail.com',
                                             587,
                                             configmail.EMAIL_ADDRESS,
                                             configmail.PASSWORD,
                                             True
                                             )
                        break
                    # order = True

                # Venta si se pierde por porcentaje Stop Loss fijado
                if ((float(Porcentaje) <= -float(Porc_StopLoss)) or (((Total_GP + Total_GN)/Saldo_Inicial)*100 <= -float(Porc_StopLoss))) and Se_Compro:  # Stop Loss %
                    print('Sellll')
                    print(Porcentaje)
                    texto = mensaje(Balance,
                                    Ganancia,
                                    CompraCripto,
                                    activo,
                                    Precio_Actual_Cripto,
                                    promedio,
                                    tiempo) + 'Venta por Porcentaje <= -{}%\n'.format(round(Porc_StopLoss, 2)) + 38*"="

                    valoracion = round(Balance + Precio_Compra + Ganancia, 2)
                    Total_GN += Ganancia
                    Num_operaciones += 1
                    write_log(texto)
                    subject = "Trading Bot. Stop Loss del {}% en pérdidas".format(
                        Porc_StopLoss)
                    write_log('\n' + subject + '\n' + 38*"=")
                    texto = Display(SIGNAL, tiempo, Balance,
                                    valoracion, Precio_Compra, Ganancia,
                                    CompraCripto, activo, Precio_Actual_Cripto,
                                    promedio, Porcentaje, SMA,
                                    RSI, Total_GP, Total_GN)
                    send_mail_withattach(configmail.EMAIL_ADDRESS,
                                         configmail.TO_EMAIL_ADDRESS,
                                         subject,
                                         texto,
                                         ['trading_log.txt'],
                                         'smtp.gmail.com',
                                         587,
                                         configmail.EMAIL_ADDRESS,
                                         configmail.PASSWORD,
                                         True
                                         )
                    Se_Compro = False
                    Ope_Ganadas_Seg = 0
                    break

                # Venta si se supera el porcentaje de ganancia respecto al saldo inicial al comenzar el trading
                if (round(Balance, 2) >= (Saldo_Inicial + Saldo_Inicial * (Ganancia_Porc/100))) and Se_Compro:
                    print('Sellll')
                    print(round(Balance, 2), (Saldo_Inicial +
                                              Saldo_Inicial * (Ganancia_Porc/100)))
                    texto = mensaje(Balance,
                                    Ganancia,
                                    CompraCripto,
                                    activo,
                                    Precio_Actual_Cripto,
                                    promedio,
                                    tiempo) + 'Se ha ganado más del {}% en todas las operaciones\n'.format(Ganancia_Porc) + 38*"="

                    # Balance = Balance + Precio_Compra + Ganancia
                    Total_GP += Ganancia
                    Num_operaciones += 1
                    write_log(texto)
                    subject = "Trading Bot. Ganancia del {} %".format(
                        Ganancia_Porc)
                    write_log('\n' + subject + '\n' + 38*"=")
                    texto = Display(SIGNAL, tiempo, Balance,
                                    Balance, Precio_Compra,
                                    Ganancia, CompraCripto, activo,
                                    Precio_Actual_Cripto, promedio, Porcentaje,
                                    SMA, RSI, Total_GP, Total_GN)
                    send_mail_withattach(configmail.EMAIL_ADDRESS,
                                         configmail.TO_EMAIL_ADDRESS,
                                         subject,
                                         texto,
                                         ['trading_log.txt'],
                                         'smtp.gmail.com',
                                         587,
                                         configmail.EMAIL_ADDRESS,
                                         configmail.PASSWORD,
                                         True
                                         )
                    Se_Compro = False
                    Ope_Ganadas_Seg = 0
                    break

                else:
                    print('*** Presione CTRL + C para salir del programa ***')
                sleep(Refresh_seg)

            except KeyboardInterrupt:
                print('\nHa interrumpido el sistema!')
                break
            except Exception as e:
                sleep(Refresh_seg)
                print('Ocurrio un error conectándose al API Binance:\n{}'.format(e))


except Exception as e:
    print('Ocurrió el siguiente error:\n{}'.format(e))
