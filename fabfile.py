import os
import glob
from fabric import task


def get_rel_path():
    res = glob.glob('**/manage.py', recursive=True)
    if not len(res) == 1:
        raise FileExistsError('Go to folder with manage.py')
    ret = '.'
    if os.path.dirname(res[0]):
        ret = os.path.dirname(res[0])
    return ret

@task
def test(c):
    cmd = list()
    cmd.append('cd {}'.format(get_rel_path()))
    if 'TRAVIS' in os.environ:
        cmd.append('. ../venv/bin/activate')
    cmd.append('coverage run --source=priceapi ./manage.py test')
    cmd.append('coverage report -m')
    cmd.append('cd -')
    cmd = ' && '.join(cmd)
    c.run(cmd)
