import boto3
from datetime import datetime, timedelta

def fetch_logs():
    client = boto3.client('logs', region_name='your-region')

    log_group_name = '/aws/ecs/your-log-group'
    start_time = int((datetime.now() - timedelta(hours=1)).timestamp() * 1000)
    end_time = int(datetime.now().timestamp() * 1000)

    logs = []
    response = client.filter_log_events(
        logGroupName=log_group_name,
        startTime=start_time,
        endTime=end_time,
        filterPattern='',
    )

    for event in response['events']:
        logs.append(event['message'])

    return '\n'.join(logs)
