CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/apps',
    # 'python': '/usr/bin/python3',
    'args': (
        '--bind=:8080',
        '--workers=4',
        '--timeout=60',
        '--log-file=/home/box/logs/unicorn.log',
        'apps.hello:app',
    ),
}
