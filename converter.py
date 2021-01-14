from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal


def converting(convert1, convert2, amount):
    """ Receives the values, converts the amount and 
    assembles the response along with error messages.
    Returns a dictionary response """
    cr = CurrencyRates(force_decimal= True)
    cc = CurrencyCodes()
    resp = {'messages': list()}

    try:
        new_amount = cr.convert(convert1, convert2, Decimal(amount))

        # if error not thrown, country codes are valid, validate amount
        if validateAmount(new_amount):
            # if amount valid, form proper response
            resp['symbol'] = cc.get_symbol(convert2)
            resp['amount'] = round(new_amount, 2)  
        else:
            resp['messages'].append(f'Not a valid Amount')       

    except:
        # country codes not valid, append necessary error messages
        if not cc.get_symbol(convert1):
            resp['messages'].append(f'Not a valid Code: {convert1}')
        if not cc.get_symbol(convert2):
            resp['messages'].append(f'Not a valid Code: {convert2}')
        if not validateAmount(amount):
            resp['messages'].append(f'Not a valid Amount')

    return resp

        

def validateAmount(amount):
    """ ensure dollar value is valid, returns Boolean """
    try:
        if float(amount) > 0.00:
            return True
    except:
        return False
