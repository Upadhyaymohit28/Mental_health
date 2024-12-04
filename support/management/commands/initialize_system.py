import os
import shutil
import sys
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):
    help = 'Initialize system by checking if it is the first run, and cleaning up unnecessary files and folders.'

    def handle(self, *args, **kwargs):
        # Get the root directory of the Django project (where manage.py is located)
        project_root_dir = settings.BASE_DIR
        initialized_file = os.path.join(project_root_dir, 'initialized.txt')

        # Check if the initialized.txt file exists
        if os.path.exists(initialized_file):
            print("Not the first run, skipping initialization.")
        else:
            print("First run, proceeding with initialization...")

            # Delete the db.sqlite3 file
            print("Deleting db.sqlite3...")
            self.delete_file_or_directory(os.path.join(project_root_dir, 'db.sqlite3'))

            # Get the top-level subdirectories in the project root directory
            print("Getting subdirectories...")
            subdirs = [d for d in os.listdir(project_root_dir) if os.path.isdir(os.path.join(project_root_dir, d))]

            # Iterate through subdirectories to clean up cache files and migrations folders
            for subdir in subdirs:
                if subdir == '.git':
                    continue

                subdir_path = os.path.join(project_root_dir, subdir)

                # Delete __pycache__ folders and .pyc files
                print(f"Cleaning {subdir_path}...")
                self.delete_pycache_and_pyc_files(subdir_path)

                # Delete the migrations folder
                print(f"Deleting migrations folder in {subdir_path}...")
                self.delete_file_or_directory(os.path.join(subdir_path, 'migrations'))

                # Create migrations folder and an empty __init__.py file
                print(f"Creating migrations folder and __init__.py in {subdir_path}...")
                self.create_migrations_and_init(subdir_path)

            # Run database migrations
            print("Running makemigrations...")
            self.run_management_command('makemigrations')

            print("Running migrate...")
            self.run_management_command('migrate')

            # Run population commands
            print("Running populate_content...")
            self.run_management_command('populate_content')

            print("Running populate_challenges...")
            self.run_management_command('populate_challenges')

            print("Running populate_support...")
            self.run_management_command('populate_support')

            # After initialization, create the initialized.txt file
            print("Initialization completed. Creating 'initialized.txt' file...")
            self.create_initialized_file(initialized_file)

    def delete_file_or_directory(self, path):
        """Delete a file or directory"""
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    def delete_pycache_and_pyc_files(self, subdir_path):
        """Delete __pycache__ folders and .pyc files"""
        for root, dirs, files in os.walk(subdir_path):
            if '__pycache__' in dirs:
                shutil.rmtree(os.path.join(root, '__pycache__'))
            for file in files:
                if file.endswith('.pyc'):
                    os.remove(os.path.join(root, file))

    def create_migrations_and_init(self, subdir_path):
        """Create a migrations folder and an empty __init__.py file in each subdirectory"""
        migrations_path = os.path.join(subdir_path, 'migrations')
        if not os.path.exists(migrations_path):
            os.makedirs(migrations_path)
            open(os.path.join(migrations_path, '__init__.py'), 'w').close()

    def create_initialized_file(self, path):
        """Create the initialized.txt file"""
        with open(path, 'w') as f:
            f.write('Initialization completed.\n')

    def run_management_command(self, command_name):
        """Run a Django management command"""
        call_command(command_name)
