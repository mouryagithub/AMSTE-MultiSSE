import os, sys, termios, time

port = '/dev/ttyUSB0'
baud = termios.B115200

fd = os.open(port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
attrs = termios.tcgetattr(fd)
attrs[0] = 0
attrs[1] = 0
attrs[2] &= ~termios.CSIZE
attrs[2] |= (termios.CS8 | termios.CREAD | termios.CLOCAL)
attrs[3] = 0
attrs[4] = baud
attrs[5] = baud
attrs[6][termios.VMIN] = 0
attrs[6][termios.VTIME] = 1
termios.tcsetattr(fd, termios.TCSANOW, attrs)

captured = []
start = time.time()
while time.time() - start < 4.0:
    try:
        chunk = os.read(fd, 2048)
        if chunk:
            captured.append(chunk.decode('utf-8', errors='ignore'))
    except BlockingIOError:
        pass
    time.sleep(0.02)

os.close(fd)
text = "".join(captured)
with open('/home/mourya/projects/Major_Project/evaluation_graphs/clean_hardware_pmu_run.txt', 'w') as f:
    f.write(text)

print("TOTAL_BYTES:", len(text))
print("--- FULL CAPTURED TEXT ---")
print(text)
