import time


exact = time.time()
inttime = int(exact)
sod = inttime - (inttime % 86400)

print("Exact: " + str(exact))
print("Integer Time: " + str(inttime))
print("Start of Day: " + str(sod))
