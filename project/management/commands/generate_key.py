import random
import string

from django.core.management.base import BaseCommand


def gen_key():
    return ''.join([
        random.SystemRandom().choice(string.ascii_letters + string.digits + '!@#%^&*(-_=+)')
        for _ in range(50)
    ])


def print_key():
    print('Paste the key below into the settings.py in `project` app:\n')
    print(gen_key())


class Command(BaseCommand):
    '''
    # Reference

    * https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
    '''

    def handle(self, *args, **options):
        print_key()


if __name__ == "__main__":
    print_key()
