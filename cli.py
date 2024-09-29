import argparse
import subprocess
from fetch_logs import fetch_logs

def analyze_logs():
    logs = fetch_logs()
    process = subprocess.Popen(
        ['goaccess', '-', '-o', 'report.html', '--log-format=%^ %dT%t.%^ %v %h:%^ %^ %^ %T %^ %s %^ %^ %b "%r" "%u" %k %K %^', '--date-format=%Y-%m-%d', '--time-format=%H:%M:%S'],
        stdin=subprocess.PIPE,
        text=True
    )
    process.communicate(logs)

def main():
    parser = argparse.ArgumentParser(description="Analyze CloudWatch logs using GoAccess.")
    parser.add
