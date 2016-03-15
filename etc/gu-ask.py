CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/ask/',
    # 'python': '/usr/bin/python3',
    'args': (
        '--bind=:8000',
        '--workers=1',
        '--timeout=60',
        '--log-file=/home/box/logs/unicorn.log',
        'ask.wsgi',
    ),
}
