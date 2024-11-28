import os
import sys
from django.core.management import call_command

# 禁用输出缓冲
sys.stdout = sys.stderr = open(sys.stdout.fileno(), mode='w', buffering=1)

from django.core.management import execute_from_command_line
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health_project.settings')

    try:
        import django
        django.setup()

        # 检查是否已经执行过初始化命令
        initialized_file = os.path.join(os.getcwd(), 'initialized.txt')  # 获取当前目录

        if not os.path.exists(initialized_file):
            print("First run, initializing system...")
            call_command('initialize_system')  # 执行初始化命令
            # 创建初始化标记文件
            with open(initialized_file, 'w') as f:
                f.write("Initialization completed.\n")
        else:
            print("Not the first run, skipping initialization.")

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
