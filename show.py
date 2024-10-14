from nuscenes.nuscenes import NuScenes
from nuscenes.utils.splits import create_splits_scenes

import os
from PIL import Image
import pickle

root = "/volsparse1/wxd/data/nuscenes"

file_path = "/workspace/wxd/PGP/data/ffffae497b0d4fb1947864f7210a237f_393a377273b3401a9f69c64e795f89ed.pickle"

with open(file_path, "rb") as f:
    data = pickle.load(f)

sample_token = data["inputs"]["sample_token"]


nusc = NuScenes(version='v1.0-trainval', dataroot=root, verbose=True)

splits = create_splits_scenes()

my_sample = nusc.get('sample', sample_token)

import pdb; pdb.set_trace()

sensor = "CAM_FRONT"
cam_front_data = nusc.get('sample_data', my_sample['data'][sensor])
file_name = cam_front_data["filename"]

img = Image.open(os.path.join(root, file_name))
img.save(f"{sample_token}.jpg")