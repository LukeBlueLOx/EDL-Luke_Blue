plt.ion()
fig = plt.figure()
x_data = []
y_data = []
start_time = time()

x_data.append(elapsed_time)
y_data.append(lightlevel)

plt.title("Light Sensor input over time")
plt.ylabel("Light Level")
plt.xlabel("Time in seconds")

plt.plot(x_data, y_data)
plt.draw()
plt.pause(0.01)