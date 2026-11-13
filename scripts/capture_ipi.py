import os, sys, termios, time

port = '/dev/ttyUSB0'
baud = termios.B115200

print(f"Waiting for {port} to become accessible (read/write)...", flush=True)
while True:
    if os.path.exists(port):
        try:
            fd = os.open(port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
            break
        except PermissionError:
            time.sleep(0.5)
        except Exception as e:
            time.sleep(0.5)
    else:
        time.sleep(0.5)

print(f"{port} opened successfully! Configuring 115200 8N1...", flush=True)
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

print("Listening for incoming Pi 4 boot and PMU trace (up to 30 seconds)...", flush=True)
captured = []
start = time.time()
last_data_time = None

while time.time() - start < 30.0:
    try:
        chunk = os.read(fd, 2048)
        if chunk:
            s = chunk.decode('utf-8', errors='ignore')
            captured.append(s)
            sys.stdout.write(s)
            sys.stdout.flush()
            last_data_time = time.time()
    except BlockingIOError:
        pass
    time.sleep(0.02)
    # Stop early if we received data and then 2.5 seconds of silence
    if last_data_time and (time.time() - last_data_time > 2.5) and len("".join(captured)) > 50:
        break

os.close(fd)
text = "".join(captured)
out_path = '/home/mourya/projects/Major_Project/evaluation_graphs/clean_hardware_ipi_pmu_run.txt'
with open(out_path, 'w') as f:
    f.write(text)

print("\n--- CAPTURE COMPLETE ---")
print(f"Captured {len(text)} bytes, saved to {out_path}")
