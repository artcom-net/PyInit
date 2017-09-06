"""PyInit - a simple script to ease the creation of projects for Python.

You should specify the paths to the directories templates and projects via
environment variables: PY_INIT_PROJECTS, PY_INIT_TEMPLATES.
Supported Python versions: 3.5+

"""
import os
import sys
import shutil
import subprocess


ENV_VARS = {'projects': 'PY_INIT_PROJECTS', 'templates': 'PY_INIT_TEMPLATES'}


def main():
    # Checking environment vars.
    projects_path = os.environ.get(ENV_VARS['projects'], None)
    templates_path = os.environ.get(ENV_VARS['templates'], None)

    if not all((projects_path, templates_path)):
        print('>> Set the environment variables: '
              '{projects}, {templates}'.format(**ENV_VARS))
        sys.exit(1)

    if not os.path.exists(templates_path):
        raise FileNotFoundError(templates_path)

    project_name = None

    # Getting a project name.
    while not project_name:
        project_name = input('>> Project name: ')

    project_full_path = os.path.join(projects_path, project_name)

    # Creating a project directory.
    if not os.path.exists(project_full_path):
        print('>> Create project dir: {}'.format(project_full_path))
        os.makedirs(project_full_path)

    # Getting the Python version.
    result = subprocess.check_output([sys.executable, '-V']).decode()
    py_version = ''.join(result.split()[1].split('.'))
    venv_path = os.path.join(project_full_path, 'venv')

    # Creating virtualenv.
    if not os.path.exists(venv_path):
        print('>> Create virtualenv: {}'.format(venv_path))
        if py_version[:2] == '36':
            subprocess.call([sys.executable, '-m', 'venv', venv_path],
                            stdout=subprocess.PIPE)
        else:
            subprocess.run(
                ['virtualenv', '-p', sys.executable, venv_path],
                stdout=subprocess.PIPE
            )

    os.chdir(templates_path)

    # Copying templates.
    for template in os.listdir('.'):
        if not os.path.exists(os.path.join(project_full_path, template)):
            print('>> Create file: {}'.format(template))
            shutil.copy(template, project_full_path)

    os.chdir(project_full_path)

    # Tests dir.
    if not os.path.exists('tests'):
        print('>> Create dir: tests')
        os.mkdir('tests')

    # Initializing the git repo.
    if not os.path.exists('.git'):
        print('>> Create git repository')
        subprocess.run(['git', 'init'], stdout=subprocess.PIPE)


if __name__ == '__main__':
    main()
