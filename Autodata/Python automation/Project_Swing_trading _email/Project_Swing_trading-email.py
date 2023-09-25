
import pdb
#import modulefinder
all_trades_raw = """

Dell short $ 374.43
stop Loss $397.4
Target $400.00

Team short $ 377.43
stop Loss $397.4
Target $400.00

HCL $ 376.43
stop Loss $397.4
Target $400.00

wipro $ 378.43
stop Loss $397.4
Target $400.00

cisco $ 379.43
stop Loss $397.4
Target $400.00

delta $ 371.43
stop Loss $397.4
Target $400.00
"""

def raw_string_to_Dictionary(input_string):

    input_as_list = input_string.split('\n\n')
    print(input_as_list)
    all_tardes = []
    for trade in input_as_list:
        print(trade)
        trade_split = trade.split()
        symbol = trade_split[0]
        trade_type = trade_split[1]
        entry_price = trade_split[2]
        stop_loss_price = trade_split[5]
        target = trade_split[7]

        trade_dictionary = {

            'symbol': symbol,
            'trade_type': trade_type,
            'entry_price': entry_price,
            'stop_loss_price': stop_loss_price,
            'target': target
        }
        all_tardes.append(trade_dictionary)

        print(all_tardes)
raw_string_to_Dictionary(all_trades_raw)
