from tinkoff.invest import Client
import datetime

Account_id=''
TOKEN = ''

def cast_money(v):
    return v.units + v.nano / 1e9 # nano - 9 нулей


def main():
    with Client(TOKEN) as client:
#        print(client.users.get_accounts())
        r = client.operations.get_portfolio(account_id=Account_id)
        print(r.total_amount_bonds, cast_money(r.total_amount_bonds))
        print(r.total_amount_shares, cast_money(r.total_amount_shares))
        print(r.total_amount_currencies, cast_money(r.total_amount_currencies))
        print(r.total_amount_futures, cast_money(r.total_amount_futures))
        total_money = cast_money(r.total_amount_bonds) + cast_money(r.total_amount_shares) + cast_money(r.total_amount_currencies)
        print(total_money)

#        r = client.operations.get_withdraw_limits(account_id=Account_id)
#        print(r)
        print('----------------------')
#        r = client.operations.get_operations(
#            account_id=Account_id,
#            from_=datetime.datetime(2024,2,1),
#            to=datetime.datetime.now()
#        )
#        print(r)


if __name__ == "__main__":
    main()