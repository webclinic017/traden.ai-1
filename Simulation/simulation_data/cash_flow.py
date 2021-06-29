from dataclasses import dataclass, field


@dataclass(frozen=True)
class CashFlow:
    """class for representing fundamental data regarding cash flows"""

    fiscalDateEnding: str = field(default=None)
    reportedCurrency: str = field(default=None)
    operatingCashFlow: float = field(default=None)
    paymentsForOperatingActivities: float = field(default=None)
    proceedsFromOperatingActivities: float = field(default=None)
    changeInOperatingLiabilities: float = field(default=None)
    changeInOperatingAssets: float = field(default=None)
    depreciationDepletionAndAmortization: float = field(default=None)
    capitalExpenditures: float = field(default=None)
    changeInReceivables: float = field(default=None)
    changeInInventory: float = field(default=None)
    profitLoss: float = field(default=None)
    cashFlowFromInvestment: float = field(default=None)
    cashFlowFromFinancing: float = field(default=None)
    proceedsFromRepaymentsOfShortTermDebt: float = field(default=None)
    paymentsForRepurchaseOfCommonStock: float = field(default=None)
    paymentsForRepurchaseOfEquity: float = field(default=None)
    paymentsForRepurchaseOfPreferredStock: float = field(default=None)
    dividendPayout: float = field(default=None)
    dividendPayoutCommonStock: float = field(default=None)
    dividendPayoutPreferredStock: float = field(default=None)
    proceedsFromIssuanceOfCommonStock: float = field(default=None)
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet: float = field(default=None)
    proceedsFromIssuanceOfPreferredStock: float = field(default=None)
    proceedsFromRepurchaseOfEquity: float = field(default=None)
    proceedsFromSaleOfTreasuryStock: float = field(default=None)
    changeInCashAndCashEquivalents: float = field(default=None)
    changeInExchangeRate: float = field(default=None)
    netIncome: float = field(default=None)
