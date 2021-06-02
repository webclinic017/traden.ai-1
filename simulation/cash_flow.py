class CashFlow:
    """class for representing fundamental data regarding cash_flows"""

    def __init__(self, data):
        self.fiscalDateEnding = data["fiscalDateEnding"]
        self.reportedCurrency = data["reportedCurrency"]
        self.operatingCashflow = data["operatingCashflow"]
        self.paymentsForOperatingActivities = data["paymentsForOperatingActivities"]
        self.proceedsFromOperatingActivities = data["proceedsFromOperatingActivities"]
        self.changeInOperatingLiabilities = data["changeInOperatingLiabilities"]
        self.changeInOperatingAssets = data["changeInOperatingAssets"]
        self.depreciationDepletionAndAmortization = data["depreciationDepletionAndAmortization"]
        self.capitalExpenditures = data["capitalExpenditures"]
        self.changeInReceivables = data["changeInReceivables"]
        self.changeInInventory = data["changeInInventory"]
        self.profitLoss = data["profitLoss"]
        self.cashflowFromInvestment = data["cashflowFromInvestment"]
        self.cashflowFromFinancing = data["cashflowFromFinancing"]
        self.proceedsFromRepaymentsOfShortTermDebt = data["proceedsFromRepaymentsOfShortTermDebt"]
        self.paymentsForRepurchaseOfCommonStock = data["paymentsForRepurchaseOfCommonStock"]
        self.paymentsForRepurchaseOfEquity = data["paymentsForRepurchaseOfEquity"]
        self.paymentsForRepurchaseOfPreferredStock = data["paymentsForRepurchaseOfPreferredStock"]
        self.dividendPayout = data["dividendPayout"]
        self.dividendPayoutCommonStock = data["dividendPayoutCommonStock"]
        self.dividendPayoutPreferredStock = data["dividendPayoutPreferredStock"]
        self.proceedsFromIssuanceOfCommonStock = data["proceedsFromIssuanceOfCommonStock"]
        self.proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = data[
            "proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"]
        self.proceedsFromIssuanceOfPreferredStock = data["proceedsFromIssuanceOfPreferredStock"]
        self.proceedsFromRepurchaseOfEquity = data["proceedsFromRepurchaseOfEquity"]
        self.proceedsFromSaleOfTreasuryStock = data["proceedsFromSaleOfTreasuryStock"]
        self.changeInCashAndCashEquivalents = data["changeInCashAndCashEquivalents"]
        self.changeInExchangeRate = data["changeInExchangeRate"]
        self.netIncome = data["netIncome"]

