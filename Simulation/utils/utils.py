from Simulation.simulation_data.SimulationData import SimulationData
from Simulation.simulation_data.stock_time_series.DailyAdjusted import DailyAdjusted
from Simulation.simulation_data.technical_indicators.EMA import EMA
from Simulation.simulation_data.technical_indicators.SMA import SMA
from Simulation.simulation_data.technical_indicators.MACD import MACD
from Simulation.simulation_data.technical_indicators.RSI import RSI
from Simulation.simulation_data.technical_indicators.VWAP import VWAP
from Simulation.simulation_data.technical_indicators.CCI import CCI
from Simulation.simulation_data.technical_indicators.ADX import ADX
from Simulation.simulation_data.technical_indicators.STOCH import STOCH
from Simulation.simulation_data.technical_indicators.AROON import AROON
from Simulation.simulation_data.technical_indicators.BBANDS import BBANDS
from Simulation.simulation_data.technical_indicators.AD import AD
from Simulation.simulation_data.technical_indicators.OBV import OBV
from Simulation.simulation_data.fundamental_data.CompanyOverview import CompanyOverview
from Simulation.simulation_data.fundamental_data.Earnings import Earnings
from Simulation.simulation_data.fundamental_data.BalanceSheet import BalanceSheet
from Simulation.simulation_data.fundamental_data.CashFlow import CashFlow
from Simulation.simulation_data.fundamental_data.IncomeStatement import IncomeStatement


def profit_percentage_by_year(initial_value, current_value, time_in_days):
    return (((((current_value - initial_value) / initial_value) + 1) ** (365 / time_in_days)) - 1) * 100


def time_between_days(start_date, end_date):
    from datetime import date
    year0, month0, day0 = get_year_month_day(start_date)
    year1, month1, day1 = get_year_month_day(end_date)
    d0 = date(int(year0), int(month0), int(day0))
    d1 = date(int(year1), int(month1), int(day1))
    delta = d1 - d0
    return delta.days


def get_year_month_day(date):
    date_parts = date.split("-")
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]
    return year, month, day


def get_year(date):
    date_parts = date.split("-")
    year = date_parts[0]
    return year


def get_month(date):
    date_parts = date.split("-")
    month = date_parts[1]
    return month


def update_today_data(yesterday_data: dict, today_data: dict):
    """ This method updates the SimulationData dataclass instances from 'yesterday'
        with the provided data from 'today'
    """
    for ticker in today_data:
        aux_data = {}
        for indicator in today_data[ticker]:
            aux_data[indicator] = SimulationDataClasses[indicator](**today_data[ticker][indicator])
        yesterday_data[ticker].__init__(**aux_data)

    return yesterday_data


def data_load(data_provider_data):
    """ This method processes the raw data provided by the data_provided
    and transforms it into clean data for a simulation execution
    """

    def daily_data_load(indicators_to_values):
        typed_data = {trading_data: {} for trading_data in SimulationDataClasses}

        for indicator in indicators_to_values:
            components_to_values = indicators_to_values[indicator].components_to_values
            for component in components_to_values:
                # FIXME DB
                if component == " close":
                    typed_data[indicator]["close"] =\
                        type(getattr(SimulationDataClasses[indicator], "close"))(components_to_values[component])
                else:
                    typed_data[indicator][component] =\
                        type(getattr(SimulationDataClasses[indicator], component))(components_to_values[component])

        return typed_data

    dates = []
    data = {}
    prices = []

    for day_data in data_provider_data:
        dates.append(day_data.date)
        data[day_data.date] = {}
        prices.append({})
        for ticker_data in day_data.ticker_data:
            data[day_data.date][ticker_data.ticker] = daily_data_load(ticker_data.indicators_to_values)
            prices[-1][ticker_data.ticker] = float(ticker_data.indicators_to_values["dailyAdjusted"]
                                                   .components_to_values["adjustedClose"])

    return dates, data, prices


SimulationDataClasses = {
    "dailyAdjusted": DailyAdjusted, "sma": SMA, "ema": EMA, "macd": MACD, "rsi": RSI, "vwap": VWAP, "cci": CCI,
    "adx": ADX, "stoch": STOCH, "aroon": AROON, "bbands": BBANDS, "ad": AD, "obv": OBV,
    "companyOverview": CompanyOverview, "earnings": Earnings, "cashFlow": CashFlow, "incomeStatement": IncomeStatement,
    "balanceSheet": BalanceSheet
}
