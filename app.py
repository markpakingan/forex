from flask import Flask, render_template, session, jsonify, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, RatesNotAvailableError

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
def home_page():
    return render_template ("app.html")


from flask import Flask, request, redirect, flash

@app.route('/check_currency', methods=["POST"])
def check_currency():
    convertFrom = request.form["convertFrom"].upper()
    convertTo = request.form["convertTo"].upper()


    if convertFrom in currency_codes and convertTo in currency_codes:
        return redirect("/conversion")
    

    else: 
        flash("Invalid currency codes. Please try again.")
        return redirect("/")

        
    # for currency in currencies:
    #     if currency.alpha_3 == convertFrom.upper():
    #         return redirect ("/conversion")
    #     else: 
    #         return "this is invalid!"

@app.route("/conversion")
def conversion():

    c = CurrencyRates()
    converted_value = (c.convert('USD', 'LBP', 10))

    return str(converted_value)

# @app.route("/conversion")
# def conversion():

#     c = CurrencyRates()

#     try:
#         converted_value = c.convert("USD", "INR", 10)
#     except RatesNotAvailableError:
#         return "Currency rates are not available at this time. Please try again later."

#     return str(converted_value)


#     # print(c.get_rate('USD', 'INR'))
    