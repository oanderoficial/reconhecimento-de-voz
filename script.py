import pyttsx3
import speech_recognition as sr
import webbrowser

# Inicia motor de voz
ia = pyttsx3.init()
ia.setProperty('rate', 135)
ia.setProperty('volume', 1)

voices = ia.getProperty('voices')
for voice in voices:
    if "brazil" in voice.id.lower() or "portuguese" in voice.name.lower():
        ia.setProperty('voice', voice.id)
        break

def falar(texto):
    ia.say(texto)
    ia.runAndWait()

falar("Olá senhor, o que você deseja buscar?")

# Reconhecimento de voz
reconhecimento = sr.Recognizer()
with sr.Microphone() as source:
    audio = reconhecimento.listen(source)

try:
    resposta = reconhecimento.recognize_google(audio, language='pt-BR')
    print("Você disse:", resposta)

    if "bitcoin" in resposta.lower():
        falar("Ok, abrindo a cotação atual do Bitcoin")
        webbrowser.open('https://dolarhoje.com/bitcoin-hoje/')
    elif "mempool" in resposta.lower():
        falar("Ok, abrindo o mempool.space")
        webbrowser.open('https://mempool.space/pt/')
    elif "arbitragem" in resposta.lower():
        falar("Ok, abrindo Arbitragem")
        webbrowser.open('https://cointradermonitor.com/arbitragem')
    elif "criptomoeda" in resposta.lower() or "coinmarketcap" in resposta.lower():
        falar("Ok, abrindo CoinMarketCap")
        webbrowser.open('https://coinmarketcap.com/pt-br/')
    elif "binance" in resposta.lower():
        falar("Ok, abrindo Binance")
        webbrowser.open('https://www.binance.com/pt-BR/')
    else:
        falar("Desculpe, não entendi o que foi falado")

except sr.UnknownValueError:
    falar("Desculpe, não entendi o que foi falado")
except sr.RequestError:
    falar("Erro ao se conectar com o serviço de reconhecimento")
