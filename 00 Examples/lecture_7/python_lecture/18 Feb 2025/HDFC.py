class bank:
    def __init__(self,amount,tds):
        self.amount = amount
        self.tds = tds
    def get_amount(self,credit):
        self.credit = credit
        self.final_amount = credit + self.amount
        print(f'Credit  Amount  {credit}')

    def Final_Amount(self):
        tds_amount = self.final_amount*self.tds/100
        F_amount = self.final_amount - tds_amount
        print(f'Bank final amount {F_amount}')
        print(f'TDS Amount  {tds_amount}')