import pickle

file_path = "/workspace/wxd/PGP/data/ffffae497b0d4fb1947864f7210a237f_393a377273b3401a9f69c64e795f89ed.pickle"

with open(file_path, "r", encoding="utf-8") as f:
    data = pickle.load(f)

print(data)