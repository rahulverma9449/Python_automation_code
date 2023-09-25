import os


folders = os.listdir("rverma")

print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())

# for i in range(0,10):
#     os.rename(f"data/Tutorial{i+1}", f"data/rverma{i+1}")