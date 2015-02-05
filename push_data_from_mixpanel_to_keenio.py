##author - anish@fem-inc.com
from mixpanelutils.getData import *
import keen 
from mixpanelutils.getRaw import *
# TODO: make loops to read from a list of clients and timeframes.....

keen.project_id="54d274a2c1e0ab5f40acd879"
keen.write_key="c7e7365b485e60fe9846d147851933b0b9edd39aad8c00db1771848c719d2964c682331aac18fa0701d356dba50186c1185531dd8fb885dc19ccccc429ad8c2dcc68e77e816fb7b48d15d92084508e4c40432a9500f0a876115cb5e2e560cbd63c44c5aa9ef04a04212eca1e26dc8fcc"

## Give the Project and Event ID of the particular Project you are uploading data to

##Option -1 To get the metrices of each partner
### Hard Coded - Storing to Project- Test (anish@fem-inc.com)
partner='www.inc.com'
start_date='2014-01-01'
end_date='2015-01-31'
mp = WidgetReport(start_date,end_date)
report = mp.getMainMetrics(partner)

keen.add_event("inc",report)



##Option -2 To get Raw Data
keen.project_id="54d3cabd6f31a23e1391d111"
keen.write_key="4992555d11b0f296c79bee765a9f06b94e4842c2b2fb9e01bf230a2dee8baa6a08a92a57d86f70e34417f4e16e5b5df2a329335c20b005a34ab19bc2537bd4f6ad87cee85dbe60a88fdf88533b300c9801edb094a1b068e33d04672de37c2caaded31ff47061895df2f5a30e8c8165d8"

start_date='2014-02-01'
end_date='2014-02-02'
raw = GetRaw(start_date, end_date)
raw.getRawData(['Impressions', 'UnitInView', 'Click', 'Start', 'FirstWatch'])
file_name ="raw" #set to whatever you like
# now data is in the list raw.raw_data
keen.add_event(file_name,raw.raw_data)
