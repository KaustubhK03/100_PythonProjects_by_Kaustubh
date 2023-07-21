from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import time

PROMISED_UP = 360
PROMISED_DOWN = 350

complaint = InternetSpeedTwitterBot()
up_down_speed = complaint.get_internet_speed()
print(f"Download Speed: {up_down_speed[0]}\nUpload Speed: {up_down_speed[1]}")
tweet = complaint.tweet_at_provider()
time.sleep(5)
