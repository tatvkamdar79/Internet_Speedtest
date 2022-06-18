import speedtest

test = speedtest.Speedtest()

print("Loading server List...")
test.get_servers() # -> Get's list of servers that are available for speedtests
print("Done ✅")

print("Choosing Best Server...")
best = test.get_best_server() # -> Choose best server

print(f"Found : {best['host']} located in {best['country']}")

print("Performing Download test...")
download_result = test.download()

print("Performing Upload test...")
upload_result = test.upload()

ping = test.results.ping

print(f"Ping -> {ping : .2f} ms")
print(f"Download speed -> {download_result / 1024 / 1024 : .2f} Mbit/s")
print(f"Upload speed -> {upload_result / 1024 / 1024 : .2f} Mbit/s")