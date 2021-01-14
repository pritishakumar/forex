from converter import converting
from app import app
from unittest import TestCase
from forex_python.converter import CurrencyRates, CurrencyCodes

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class RenderingHomepage(TestCase):
    def test_homepage_render(self):
        """ ensures home page renders correctly """
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Convert Currency</h1>', html)

class RenderingConvertedpage(TestCase):
    def test_converted_render(self):
        """ ensures conversion is performed and rendered correctly """
        with app.test_client() as client:
            resp = client.get('/converted?convert1=USD&convert2=EUR&amount=50')
            html = resp.get_data(as_text=True)

            cr = CurrencyRates()
            proper_amount = round(cr.convert('USD', 'EUR', 50), 2)
            cc = CurrencyCodes()
            symbol = cc.get_symbol('EUR')
            span = '<span>'+ str(symbol) +' '+ str(proper_amount)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Converted Currency</h1>', html)
            self.assertIn(span, html)

class ErrorChecking(TestCase):
    def test_invalid_code(self):
        """ Unittest ensuring invalid country code errors are handled """
        self.assertEqual(converting('USD',50, 50), {'messages': ['Not a valid Code: 50']})
        self.assertEqual(converting('AAA','ZZZ',50), {'messages': ['Not a valid Code: AAA', 'Not a valid Code: ZZZ']})

    def test_invalid_amount(self):
        """ Unittest ensuring invalid amounts are handled """
        self.assertEqual(converting('CAD','USD', 0), {'messages': ['Not a valid Amount']})
        self.assertEqual(converting('CAD','USD', -50), {'messages': ['Not a valid Amount']})

