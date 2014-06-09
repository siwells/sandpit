import json
from uuid import uuid4

from stompest.config import StompConfig
from stompest.protocol import StompSpec
from stompest.sync import Stomp




def call_route(request_queue, response_queue, request):
    """
    """
    config = {
        "stomp": {
            "server": '192.168.0.3',
            "port": 61613,
            "timeout": 15,
        }
    }

    stomp_config = StompConfig("tcp://%s:%d" % (config['stomp']['server'], config['stomp']['port']), version=StompSpec.VERSION_1_0)
    stomp = Stomp(stomp_config)
    stomp.connect()
  
    jms_id = str(uuid4())
    token = stomp.subscribe(response_queue, {'JMSCorrelationID': jms_id})
    stomp.send(request_queue, json.dumps(request), {'JMSCorrelationID': jms_id})

    response = None
    if stomp.canRead(config['stomp']['timeout']):
        response = stomp.receiveFrame()
    
    stomp.unsubscribe(token)
    return response


if __name__ == "__main__":

    request = {"clientType":"TEST","city":"HELSINKI","destination":{"lonE6":25264279,"latE6":60376863},"origin":{"lonE6":24938702,"latE6":60169908},"userID":"b8eb7ae6-8366-46e3-8b3c-98fa531a2997","description":"CarC1S2OffPRobSun","requirements":{"allowedModesOfTransports":["CAR"],"maxWalkingDistance":0,"maxNumberOfInterchanges":0},"departureDateTime":"2014-04-29T14:00:00.000+03:00"}

    request_queue =  "/queue/wp5.JourneyPlanning.planJourney.Helsinki"

    response_queue = "/topic/wp5.JourneyPlanning.planJourney.Helsinki.wiretap.reply"

    response = call_route(request_queue, response_queue, request)

    if response is None:
	print "No Response Received"
    else:
        payload = json.loads(response.body)
        print payload

