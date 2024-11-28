import os
import shutil
import sys
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):
    help = 'Initialize system by checking if it is the first run, and cleaning up unnecessary files and folders.'

    def handle(self, *args, **kwargs):
        # 获取 Django 项目的根目录 (manage.py 所在目录)
        project_root_dir = settings.BASE_DIR
        initialized_file = os.path.join(project_root_dir, 'initialized.txt')

        # 检查 initialized.txt 是否存在
        if os.path.exists(initialized_file):
            print("Not the first run, skipping initialization.")
        else:
            print("First run, proceeding with initialization...")

            # 删除 db.sqlite3 文件
            print("Deleting db.sqlite3...")
            self.delete_file_or_directory(os.path.join(project_root_dir, 'db.sqlite3'))

            # 获取项目根目录下的第一级子文件夹
            print("Getting subdirectories...")
            subdirs = [d for d in os.listdir(project_root_dir) if os.path.isdir(os.path.join(project_root_dir, d))]

            # 遍历子文件夹，删除不需要的缓存文件和 migrations 文件夹
            for subdir in subdirs:
                if subdir == '.git':
                    continue

                subdir_path = os.path.join(project_root_dir, subdir)

                # 删除 __pycache__ 文件夹及其中的 .pyc 文件
                print(f"Cleaning {subdir_path}...")
                self.delete_pycache_and_pyc_files(subdir_path)

                # 删除 migrations 文件夹
                print(f"Deleting migrations folder in {subdir_path}...")
                self.delete_file_or_directory(os.path.join(subdir_path, 'migrations'))

                # 创建 migrations 文件夹和空的 __init__.py 文件
                print(f"Creating migrations folder and __init__.py in {subdir_path}...")
                self.create_migrations_and_init(subdir_path)

            # 执行数据库迁移
            print("Running makemigrations...")
            self.run_management_command('makemigrations')

            print("Running migrate...")
            self.run_management_command('migrate')

            # 执行填充命令
            print("Running populate_content...")
            self.run_management_command('populate_content')

            print("Running populate_challenges...")
            self.run_management_command('populate_challenges')

            print("Running generate_challenges...")
            self.run_management_command('generate_challenges')

            print("Running populate_support...")
            self.run_management_command('populate_support')

            # 初始化完成后，创建 initialized.txt 文件
            print("Initialization completed. Creating 'initialized.txt' file...")
            self.create_initialized_file(initialized_file)

    def delete_file_or_directory(self, path):
        """删除文件或目录"""
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    def delete_pycache_and_pyc_files(self, subdir_path):
        """删除 __pycache__ 文件夹和 .pyc 文件"""
        for root, dirs, files in os.walk(subdir_path):
            if '__pycache__' in dirs:
                shutil.rmtree(os.path.join(root, '__pycache__'))
            for file in files:
                if file.endswith('.pyc'):
                    os.remove(os.path.join(root, file))

    def create_migrations_and_init(self, subdir_path):
        """在每个子文件夹中创建 migrations 文件夹和空的 __init__.py 文件"""
        migrations_path = os.path.join(subdir_path, 'migrations')
        if not os.path.exists(migrations_path):
            os.makedirs(migrations_path)
            open(os.path.join(migrations_path, '__init__.py'), 'w').close()

    def create_initialized_file(self, path):
        """创建 initialized.txt 文件"""
        with open(path, 'w') as f:
            f.write('Initialization completed.\n')

    def run_management_command(self, command_name):
        """运行 Django 管理命令"""
        call_command(command_name)

