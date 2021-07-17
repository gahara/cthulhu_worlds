import subprocess

from app.settings import APP_ROOT


def run_docker_script():
    full_path = f'{APP_ROOT}/docker/run_docker.sh'
    res = subprocess.check_output([full_path])

    return res.decode("utf-8").strip()
