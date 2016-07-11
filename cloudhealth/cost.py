# https://chapi.cloudhealthtech.com/olap_reports?api_key=<your api key>

from . import accounts

class CostsClient(object):
    CURRENT_COST_URL = '/olap_reports/cost/current'
    HISTORY_COST_URL = '/olap_reports/cost/history'

    def __init__(self, client):
        self.client = client

    def get_current(self, account_name=None):
        response = self.client.get(self.CURRENT_COST_URL)

        accounts_total_cost = []

        accounts_client = accounts.AccountsClient(self.client)
        list_of_aws_accounts = accounts_client.list("AWS-Account")

        prices = response['data']
        for accounts_total in prices:
            accounts_total_cost.append(accounts_total[0][0])

        cost_by_account = dict(zip(list_of_aws_accounts, accounts_total_cost))

        if account_name:
           return cost_by_account[account_name]
        else:
           return cost_by_account['Total']
