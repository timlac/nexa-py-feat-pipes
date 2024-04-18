from feat import Detector
from feat.utils.io import get_test_data_path

import os
import pandas as pd
from glob import glob
import argparse


from utils import get_filename



# Parse command-line arguments
parser = argparse.ArgumentParser(description='Process audio files with Py-Feat.')
parser.add_argument('input_dir', type=str, help='Input directory for video files')
parser.add_argument('output_dir', type=str, help='Output directory for CSV files')

args = parser.parse_args()

detector = Detector(device="cuda")


# Use arguments for input and output directories
input_dir = args.input_dir
output_dir = args.output_dir

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Search for audio files recursively within input_dir
file_paths = (glob(os.path.join(input_dir, '**/*.mov'), recursive=True)
              + glob(os.path.join(input_dir, "**/*.mp4"), recursive=True))


for idx, file_path in enumerate(file_paths):
    print(f"processing file {file_path}, number {idx + 1} out of {len(file_paths)}")

    df = detector.detect_video(file_path, skip_frames=24)

    filename = get_filename(file_path)
    output_path = os.path.join(output_dir, filename + ".csv")

    # Save CSV
    df.to_csv(output_path, index=False)
