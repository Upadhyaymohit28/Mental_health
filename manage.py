#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health_project.settings')

    try:
        # 确保 Django 环境初始化
        import django
        from django.core.management import call_command
        django.setup()

        # 自动执行 populate_content 命令
        try:
            call_command('populate_content')
            print("Successfully executed populate_content.")
        except Exception as e:
            print(f"Error executing populate_content: {e}")

        # 执行管理命令
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

if __name__ == '__main__':
    main()
