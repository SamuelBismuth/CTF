import subprocess


def is_good():
    with open("out.txt", 'r') as f:
        try:
            print(f.readline())
        except:
            pass


for i in range(0, 7):
    for j in range(0,  10):
        for l in ['+', '-']:
            for r in ['+', '-']:
                proc = subprocess.Popen(
                    ['bash', 'run-pinball.sh', str(j), str(i), l, r], stdout=subprocess.PIPE)
                # for line in proc.stdout:
                #     line = line.decode('utf-8').strip()
                #     print(line)
                proc.wait()
                is_good()
