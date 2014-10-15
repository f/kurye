import os
import shutil
import argparse
import subprocess

parser = argparse.ArgumentParser(
        description='simple github cloner for boilerplate projects')
parser.add_argument('user/repo',
        help='user/repo of the repo url https://github.com/user/repo')
parser.add_argument('-b', '--base',
        help='base path to clone the project',
        default=os.getcwd())
parser.add_argument('-o', '--origin',
        help='origin of repo, "upstream" by default. requires -g',
        default='upstream')
parser.add_argument('--nogit',
        help='remove .git folder')
parser.add_argument('--noboot',
        help='do not boot the project')

args = vars(parser.parse_args())

class bcolors:
    HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    ENDC = '\033[0m'

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def kprint(message):
    print(bcolors.HEADER + '[kurye]: ' + bcolors.ENDC + message)

def main():
    try:
        (user, repo) = args['user/repo'].split('/', 1)
    except ValueError:
        kprint('user/repo format is possibly wrong')
        parser.print_help()
        return

    base = os.path.join(args['base'], repo)
    at_base = lambda (folder): os.path.join(base, folder)

    if os.path.exists(base):
      kprint('the project %s already exists. please specify another project folder' % repo)
      return

    origin = args['origin']

    kprint('cloning %s boilerplate as %s' % (repo, origin))
    git('clone', ('https://github.com/%s/%s' % (user, repo)), (base), '-o', origin)

    if 'nogit' in args:
      kprint('removing git folder')
      shutil.rmtree(at_base('.git'))

    if 'noboot' in args:
      boot = at_base('.kurye')
      kprint('trying to run .kurye boot file')
      if os.path.exists(boot):
        subprocess.Popen([boot])
      else:
        kprint('boot file not found, passing.')
