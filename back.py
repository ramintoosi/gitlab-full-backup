import gitlab
import os

gl = gitlab.Gitlab.from_config('gitlab', ['./config.cfg'])
gl.auth()

if not os.path.isdir('backup'):
    os.mkdir('backup')

projects = gl.projects.list(visibility='private', all=True)
n_projects = len(projects)
for i, project in enumerate(projects):
    print('Cloning Project {} - {} ...'.format(i, n_projects))
    os.system('git clone --recursive {} "{}"'.format(project.ssh_url_to_repo, os.path.join('backup',project.name)))




