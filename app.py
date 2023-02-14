from flask import Flask, render_template, session, jsonify, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, RatesNotAvailableError

import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

currency_codes = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF",
    "CLF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF",
    "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP",
    "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL",
    "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK",
    "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW",
    "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD",
    "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK",
    "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR",
    "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD",
    "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL",
    "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND",
    "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS",
    "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XDR", "XOF",
    "XPD", "XPF", "XPT", "YER", "ZAR", "ZMW", "ZWL"
]

@app.route('/')
def index():
    return render_template ("app.html")



@app.route('/check_currency', methods=["POST"])
def check_currency():
    convertFrom = request.form["convertFrom"].upper()
    convertTo = request.form["convertTo"].upper()
    amount = request.form["numberValue"]
    
    if convertFrom in currency_codes and convertTo in currency_codes:
                return redirect(f"/conversion/{convertFrom}/{convertTo}/{amount}")
              

    else: 
        flash("Invalid currency codes. Please try again.")
        return redirect("/")

        
  

@app.route('/conversion/<convertFrom>/<convertTo>/<amount>')
def conversion(convertFrom, convertTo, amount):


    exchange_rate_url = f'https://api.exchangerate.host/convert?from={convertFrom}&to={convertTo}'
    response = requests.get(exchange_rate_url)

    if response.status_code == 200:
        exchange_rate = response.json()['result']

        converted_amount = exchange_rate * float(amount)
        rounded_amount = round(converted_amount,2)
        return (f"{convertTo} {str(rounded_amount)} <br><br> <a href='/'>Home</a>")


    else:
        return jsonify({'error': 'Unable to retrieve exchange rate'}), 500

