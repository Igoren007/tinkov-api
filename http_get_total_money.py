import http.server
from tinkoff.invest import Client
import json

Account_id=''
TOKEN = ''

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/total":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(get_money().encode())


def cast_money(v):
    return v.units + v.nano / 1e9 # nano - 9 нулей


def get_money():
    with Client(TOKEN) as client:
        dct = {}
        r = client.operations.get_portfolio(account_id=Account_id)
#        print(r.total_amount_bonds, cast_money(r.total_amount_bonds))
#        print(r.total_amount_shares, cast_money(r.total_amount_shares))
#        print(r.total_amount_currencies, cast_money(r.total_amount_currencies))
#        print(r.total_amount_futures, cast_money(r.total_amount_futures))
        total_money = cast_money(r.total_amount_bonds) + cast_money(r.total_amount_shares) + cast_money(r.total_amount_currencies)
        dct['total'] = round(total_money,2)
        resp = json.dumps(dct)
#        return str(total_money)
        return resp




if __name__ == "__main__":
    server_address = ('', 8888)
    httpd = http.server.HTTPServer(server_address, MyRequestHandler)
    httpd.serve_forever()