import yfinance as yf
import matplotlib.pyplot as plt

def fetch_and_plot(ticker):
    # Adatok lekérése
    data = yf.download(ticker, period="1y")

    # Ábrázolás
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Záróár')
    plt.title(f'{ticker} Záróárának Alakulása Az Utóbbi Egy Évben')
    plt.xlabel('Dátum')
    plt.ylabel('Ár (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ticker = input("Kérlek add meg a ticker nevét: ")
    fetch_and_plot(ticker)
