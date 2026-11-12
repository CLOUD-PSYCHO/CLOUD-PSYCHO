import os, platform, psutil
print("Cloud PC Started!")
print(f"OS: {platform.system()} {platform.release()}")
print(f"CPU Cores: {os.cpu_count()}")
print(f"Total RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
