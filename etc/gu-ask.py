CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask/',
    # 'python': '/usr/bin/python3',
    'args': (
        '--bind=:8000',
        '--workers=1',
        '--timeout=60',
        '--log-file=/home/box/web/logs/unicorn.log',
        'ask.wsgi',
    ),
}
