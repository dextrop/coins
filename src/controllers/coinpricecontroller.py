import requests, json, os
from django.core.exceptions import ValidationError
file = "/root/coins/coins.json"
avb = ["ETH", "LTC", "BNB", "NEO", "QTUM", "EOS", "SNT", "BNT", "BCC", "GAS", "BTC", "HSR", "OAX", "DNT", "MCO", "ICN", "WTC", "LRC", "YOYO", "OMG", "ZRX", "STRAT", "SNGLS", "BQX", "KNC", "FUN", "SNM", "IOTA", "LINK", "XVG", "SALT", "MDA", "MTL", "SUB", "ETC", "MTH", "ENG", "ZEC", "AST", "DASH", "BTG", "EVX", "REQ", "VIB", "TRX", "POWR", "ARK", "XRP", "MOD", "ENJ", "STORJ", "VEN", "KMD", "NULS", "RCN", "RDN", "XMR", "DLT", "AMB", "BAT", "BCPT", "ARN", "GVT", "CDT", "GXS", "POE", "QSP", "BTS", "XZC", "LSK", "TNT", "FUEL", "MANA", "BCD", "DGD", "ADX", "ADA", "PPT", "CMT", "XLM", "CND", "LEND", "WABI", "TNB", "WAVES", "GTO", "ICX", "OST", "ELF", "AION", "NEBL", "BRD", "EDO", "WINGS", "NAV", "LUN", "TRIG", "APPC", "VIBE", "RLC", "INS", "PIVX", "IOST", "CHAT", "STEEM", "NANO", "VIA", "BLZ", "AE", "RPX", "NCASH", "POA", "ZIL", "ONT", "STORM", "XEM", "WAN", "WPR", "QLC", "SYS", "GRS", "CLOAK", "GNT", "LOOM", "BCN", "REP", "TUSD", "ZEN", "SKY", "CVC", "THETA", "IOTX", "QKC", "AGI", "NXS", "DATA", "SC", "NPXS", "KEY", "NAS", "MFT", "DENT", "ARDR", "HOT", "VET", "DOCK", "POLY", "PHX", "HC", "GO", "PAX", "RVN", "DCR", "USDC", "MITH", "BCHABC", "BCHSV", "REN", "BTT", "USDS", "ONG", "FET", "CELR", "MATIC", "ATOM", "PHB", "TFUEL", "ONE", "FTM", "B", "ALGO", "USDSB", "ERD", "DOGE", "DUSK", "BGBP", "ANKR", "WIN", "COS", "COCOS", "TOMO", "PERL", "CHZ", "BAND", "BUSD", "BEAM", "XTZ", "HBAR", "NKN", "STX", "KAVA", "ARPA", "CTXC", "BCH", "TROY", "VITE", "FTT", "USDT", "EUR", "OGN", "DREP", "BULL", "BEAR", "ETHBULL", "ETHBEAR", "TCT", "WRX", "LTO", "EOSBULL", "EOSBEAR", "XRPBULL", "XRPBEAR", "MBL", "COTI", "BNBBULL", "BNBBEAR", "STPT", "SOL", "CTSI", "HIVE", "CHR", "BTCUP", "BTCDOWN", "MDT", "STMX", "IQ", "PNT", "GBP", "DGB", "COMP", "BKRW", "SXP", "SNX", "ETHUP", "ETHDOWN", "ADAUP", "ADADOWN", "LINKUP", "LINKDOWN", "VTHO", "IRIS", "MKR", "DAI", "RUNE", "AUD", "FIO", "BNBUP", "BNBDOWN", "XTZUP", "XTZDOWN", "AVA", "BAL", "YFI", "JST", "SRM", "ANT", "CRV", "SAND", "OCEAN", "NMR", "DOT", "LUNA", "IDEX", "RSR", "PAXG", "WNXM", "TRB", "BZRX", "W", "WBTC", "SUSHI", "YFII", "KSM", "EGLD", "DIA", "UMA", "EOSUP", "EOSDOWN", "TRXUP", "TRXDOWN", "XRPUP", "XRPDOWN", "DOTUP", "DOTDOWN", "BEL", "WING", "SWRV", "LTCUP", "LTCDOWN", "CREAM", "UNI", "NBS", "OXT", "SUN", "AVAX", "HNT", "BAKE", "BURGER", "FLM", "SCRT", "CAKE", "SPARTA", "UNIUP", "UNIDOWN", "ORN", "UTK", "XVS", "ALPHA", "VIDT", "AAVE", "NEAR", "SXPUP", "SXPDOWN", "FIL", "FILUP", "FILDOWN", "YFIUP", "YFIDOWN", "INJ", "AERGO", "EASY", "AUDIO", "CTK", "BCHUP", "BCHDOWN", "BOT", "AKRO", "KP3R", "AXS", "HARD", "RENBTC", "SLP", "CVP", "STRAX", "FOR", "UNFI", "FRONT", "BCHA", "ROSE", "HEGIC", "AAVEUP", "AAVEDOWN", "PROM", "SKL", "SUSD", "COVER", "GLM", "GHST", "SUSHIUP", "SUSHIDOWN", "XLMUP", "XLMDOWN", "DF", "GRT", "JUV", "PSG", "1INCH", "REEF", "OG", "ATM", "ASR", "CELO", "RIF", "ST", "BTCST", "TRU", "DEXE", "CKB", "TWT", "FIRO", "PROS", "LIT", "SFP", "FXS", "DODO", "UFT", "ACM", "AUCTION", "PHA", "TVK", "BADGER", "FIS", "OM", "POND", "DEGO", "ALICE", "BIFI", "LINA", "PERP", "RAMP", "SUPER", "CFX", "EPS", "AUTO", "TKO", "PUNDIX", "TLM", "1INCHUP", "1INCHDOWN", "MIR", "BAR", "FORTH", "EZ", "SHIB", "ICP", "AR", "POLS", "MDX", "MASK", "LPT", "AGIX", "NU", "ATA", "GTC", "TORN", "KEEP", "ERN", "KLAY", "BOND", "MLN", "QUICK", "C98", "CLV", "QNT", "FLOW", "XEC", "MINA", "RAY", "FARM", "ALPACA", "MBOX", "VGX", "WAXP", "TRIBE", "GNO", "DYDX", "USDP", "GALA", "ILV", "YGG", "FIDA", "AGLD", "RAD", "BETA", "RARE", "SSV", "LAZIO", "CHESS", "DAR", "BNX", "RGT", "MOVR", "CITY", "ENS", "QI", "PORTO"]
class CoinPriceController():

    def update_price(self):
        resp = requests.get("https://dev-api.shrimpy.io/v1/exchanges/kucoin/ticker")
        prices = {}
        try:
            for element in resp.json():
                curr = {
                    "prices": [round(float(element["priceUsd"]), 5)],
                    "name": element["name"],
                    "symbol": element["symbol"]
                }
                prices[curr["symbol"]] = curr
        except Exception as e:
            f = open(file, "r")
            data = json.load(f)
            return data

        resp = {
            "coins": []
        }

        if not os.path.exists(file):
            for element in prices:
                resp["coins"].append(prices[element])
        else:
            f = open(file, "r")
            data = json.load(f)
            for element in data["coins"]:
                element["prices"].append(prices[element["symbol"]]["prices"][0])
            resp = data

        with open(file, 'w') as json_file:
            json.dump(resp, json_file)

        return resp

    def get_avg_price_change_window(self, prices):
        try:
            avg_change = 0
            for i in range(1, len(prices)):
                avg_change += prices[i] - prices[i-1]
            return ( avg_change / prices[0] ) * 100
        except Exception as e:
            return 0

    def get_coin_price(self):
        if not os.path.exists(file):
            raise ValidationError("Updates not available")
        else:
            f = open(file, "r")
            data = json.load(f)
            resp = {
                "coins": []
            }
            for element in data["coins"]:
                element["prices"] = element["prices"][(len( element["prices"]) - 10 ):len( element["prices"])]
                element["price_change"] = self.get_avg_price_change_window(element["prices"])
                if element["price_change"] > 1:
                    element["price_change"] = round(element["price_change"], 2)
                else:
                    element["price_change"] = round(element["price_change"], 4)

                if element["symbol"] in avb:
                    resp["coins"].append(element)
            return resp

    def update_coin_price(self):
        return self.update_price()