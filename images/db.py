import pyaudio
import numpy as np
import sys
import time
import tweepy
  
consumer_key = "XY9wxt3VBA6XpjH3HAFlEEe5D"
consumer_secret = "Uh1bbVVhSnmzGrUQbsGWzjqHoHfzcR5zsWgZ3EMTTDKMxshdbC"
access_token = "1225331522720288768-1Wud8hB6gboTla5PsssiwiQ0YBERU4"
access_token_secret = "iQHzvlRfNYgQfqSd5q9yjVQYTNeWwkYe9lrx178rw5lhU"
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
auth.set_access_token(access_token, access_token_secret)
  
api = tweepy.API(auth)
  
recipient_id =1225331522720288768

text = "Emergency"
  


# check args
if (len(sys.argv) < 2) or (not sys.argv[1].isdecimal()):
    print("Please specify input_device_index in integer")
    sys.exit(-1)

p = pyaudio.PyAudio()

# set prams
INPUT_DEVICE_INDEX = int(sys.argv[1])
CHUNK = 2 ** 10 # 1024
FORMAT = pyaudio.paInt16
CHANNELS = int(p.get_device_info_by_index(INPUT_DEVICE_INDEX)["maxInputChannels"])
SAMPLING_RATE = int(p.get_device_info_by_index(INPUT_DEVICE_INDEX)["defaultSampleRate"])
RECORD_SECONDS = 1


# amp to db
def to_db(x, base=1):
    y=20*np.log10(x/base)
    return y

# main loop
def main():
    while True:
        start = time.time()
        stream = p.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = SAMPLING_RATE,
                        input = True,
                        frames_per_buffer = CHUNK,
                        input_device_index = INPUT_DEVICE_INDEX
                )
        data = np.empty(0)
        for i in range(0, int(SAMPLING_RATE / CHUNK * RECORD_SECONDS)):
            elm = stream.read(CHUNK, exception_on_overflow = False)
            elm = np.frombuffer(elm, dtype="int16")/float((np.power(2,16)/2)-1)
            data = np.hstack([data, elm])
        # calc RMS
        rms = np.sqrt(np.mean([elm * elm for elm in data]))
        # RMS to db
        db = to_db(rms, 20e-6)
        stream.close()

        elapsed_time = time.time() - start
        if db > 35:
            direct_message = api.send_direct_message(recipient_id, text)
        print("elapsed_time:{:.3f}[sec], DB:{:.3f}[db]".format(elapsed_time, db))

try:
    main()
except KeyboardInterrupt:
    pass
finally:
    p.terminate()
        
    
