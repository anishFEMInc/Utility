from mixpanelutils.getData import *
import keen 
# TODO: make loops to read from a list of clients and timeframes.....

mp = WidgetReport('2015-01-01', '2015-01-31')
report = mp.getMainMetrics('www.inc.com')

keen.project_id="54d274a2c1e0ab5f40acd879" 
keen.write_key="c7e7365b485e60fe9846d147851933b0b9edd39aad8c00db1771848c719d2964c682331aac18fa0701d356dba50186c1185531dd8fb885dc19ccccc429ad8c2dcc68e77e816fb7b48d15d92084508e4c40432a9500f0a876115cb5e2e560cbd63c44c5aa9ef04a04212eca1e26dc8fcc"
keen.add_event("inc",report)
