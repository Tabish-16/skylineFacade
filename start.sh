pkill gunicorn
gunicorn --bind 127.0.0.1:8000 --workers=4 --timeout 7200 skylineFacade.wsgi:application  --daemon --reload --error-logfile error.log --access-logfile access.log --capture-output --log-level debug
#gunicorn --bind 127.0.0.1:8000  --workers=4 --timeout 7200 skylineFacade.wsgi:application  --reload

