#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'getit.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# Creating app... done, ⬢ pure-dawn-86326
# https://pure-dawn-86326.herokuapp.com/ | https://git.heroku.com/pure-dawn-86326.git


# heroku	https://git.heroku.com/pure-dawn-86326.git (fetch)
# heroku	https://git.heroku.com/pure-dawn-86326.git (push)
# origin	https://github.com/Antonioarf/Projeto1-B.git (fetch)
# origin	https://github.com/Antonioarf/Projeto1-B.git (push)

