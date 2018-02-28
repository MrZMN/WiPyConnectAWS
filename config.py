# wifi configuration
WIFI_SSID = 'MIIphone'
WIFI_PASS = '12345678'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'a1x71kn62lp0hu.iot.us-west-2.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/root-CA.crt'
AWS_CLIENT_CERT = '/flash/cert/WiPy.cert.pem'
AWS_PRIVATE_KEY = '/flash/cert/WiPy.private.key'

################## Subscribe / Publish client #################
CLIENT_ID = 'PycomPublishClient'
TOPIC = 'PublishTopic'
OFFLINE_QUEUE_SIZE = -1
DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'PublishTopic'
LAST_WILL_MSG = 'To All: Last will message'

####################### Shadow updater ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "ShadowUpdater"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Delta Listener ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "DeltaListener"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Shadow Echo ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "ShadowEcho"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5