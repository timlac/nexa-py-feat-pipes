from feat import Detector
from feat.utils.io import get_test_data_path
import os
import matplotlib.pyplot as plt

test_video_path = "../data/test/sentimotion/A67_pea_v_3.mov"

detector = Detector()

print(detector)

video_prediction = detector.detect_video(test_video_path, skip_frames=24)

axes = video_prediction.emotions.plot()
plt.show()
