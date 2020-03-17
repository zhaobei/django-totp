from django.core.management.base import BaseCommand
from django.conf import settings
import MySQLdb


class Command(BaseCommand):
    '''
    # Reference

    * https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
    * https://stackoverflow.com/a/28338524/6522746
    '''

    def handle(self, *args, **options):
        # Open database connection ( If database is not created don't give dbname)
        db = MySQLdb.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            port=settings.DB_PORT,
        )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # For creating create db
        # Below line  is hide your warning
        cursor.execute("SET sql_notes = 0; ")
        # create db here....
        cursor.execute(
            f'create database {settings.DB_NAME} ' +
            # f'create database IF NOT EXISTS {settings.DB_NAME} ' +
            'default character set utf8mb4 collate utf8mb4_unicode_ci;'
        )

        # Commit your changes in the database
        db.commit()

        # disconnect from server
        db.close()
