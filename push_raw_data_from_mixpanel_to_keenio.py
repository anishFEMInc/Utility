from mixpanelutils.getData import *
import keen
from mixpanelutils.getRaw import *
from datetime import datetime
import calendar
# TODO: make loops to read from a list of clients and timeframes.....


keen.project_id="54c6fadfc2266c4333d21f84"
keen.write_key="ef3fed154a91cad9130a9d18f233d99d2d5314855e590e97ba70d23a84d8d46d447f15196c4c760d4248391661e66022185c71ec33cfda1a85e7d3b20267a18703aa329f40623ab5b1045e5190571d991f8de4bc64b38faf17e2efa22b761684d44d2d34a00b361fdab28f981eb61b38"


## Give the Project and Event ID of the particular Project you are uploading data to


#print 'In raw'

start_date='2015-02-01'
end_date='2015-02-02'


raw = GetRaw(start_date, end_date)
raw.getRawData(['Impression', 'Click', 'Start', 'FirstWatch', 'Watch', 'Complete'])

file_name ="raw"
#set to whatever you like
# now data is in the list raw.raw_data

i=0
length=len(raw.raw_data)

EVENT_PROPERTIES_MAP ={
                'unit_url': 'unit_url',
                'unit_domain': 'unit_domain',
                'unit_title': 'unit_title',
                'unit_description': 'unit_description',
                'VideoId': 'video_id',
                'video_id': 'video_id',
                'VideoIds': 'unit_video_list',
                'title': 'video_title',
                'unit_video_list': 'unit_video_list',
                'Layout': 'unit_layout',
                'unit_layout': 'unit_layout',
                'NumVideos': 'unit_num_videos',
                'unit_num_videos': 'unit_num_videos',
                'ExperimentId': 'unit_experiment_id',
                'unit_experiment_id': 'unit_experiment_id',
                'Source': 'video_source',
                'video_source': 'video_source',
                'token': 'token'
}

EVENT_NAME_MAP ={
                'UnitStartLoad': 'UnitStartLoad',
                'UnitTimedOut': 'UnitTimedOut',
                'UnitNoVideosFound': 'UnitNoVideosFound',
                'Impression': 'UnitCompleteLoad',
                'UnitCompleteLoad': 'UnitCompleteLoad',
                'UnitInView': 'UnitFirstVisible',
                'UnitFirstVisible': 'UnitFirstVisible',
                'Click': 'VideoThumbnailClick',
                'VideoThumbnailClick': 'VideoThumbnailClick',
                'Start': 'VideoPlayStarted',
                'VideoPlayStarted': 'VideoPlayStarted',
                'Complete': 'VideoCompleted',
                'VideoCompleted': 'VideoCompleted'
}


for data in raw.raw_data:
    event = data['event']
    
    if event in EVENT_NAME_MAP:
        event = EVENT_NAME_MAP[event]
    props = raw.raw_data[i]['properties']
    propsnew = {}
    for p in props:
        if p in EVENT_PROPERTIES_MAP:
            propsnew[EVENT_PROPERTIES_MAP[p]] = props[p]
        else:
            propsnew[p] = props[p]
    propsnew["keen"]={}
    propsnew["keen"]["timestamp"] = datetime.fromtimestamp(props['time']).isoformat()
    keen.add_event(EVENT_NAME_MAP[event],propsnew)

i=i+1
print i


