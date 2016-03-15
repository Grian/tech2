CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/',
    # 'python': '/usr/bin/python3',
    'args': (
        '--bind=:8080',
        '--workers=4',
        '--timeout=60',
        '--log-file=/home/box/web/logs/unicorn.log',
        'apps.hello:app',
    ),
}
