import argparse
import os
import shutil
import signal
import subprocess

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

    parser = argparse.ArgumentParser(
            description='simple github cloner for boilerplate projects')
    parser.add_argument('github_path',
            help='github path of the repo url, looks like "user/path"')
    parser.add_argument('-b', '--base',
            help='base path to clone the project',
            default=os.getcwd())
    parser.add_argument('-o', '--origin',
            help='origin of repo, "upstream" by default. requires -g',
            default='upstream')
    parser.add_argument('-n', '--name',
            help='name of the project. repo name by default')
    parser.add_argument('--nogit',
            help='remove .git folder',
            action='store_true',
            default=False)
    parser.add_argument('--noboot',
            help='do not boot the project',
            action='store_true',
            default=False)

    args = parser.parse_args()

    try:
        user, repo = args.github_path.split('/', 1)
    except ValueError:
        kprint('github path format is possibly wrong. should be `user/repo`')
        parser.exit(1, parser.format_help())


    project = args.name if (args.name) else repo

    base = os.path.join(args.base, project)
    at_base = lambda folder: os.path.join(base, folder)

    if os.path.exists(base):
      kprint('the project %s already exists. please specify another project folder' % project)
      return

    origin = args.origin

    kprint('cloning %s to %s boilerplate as %s' % (repo, project, origin))
    git('clone', 'https://github.com/%s/%s' % (user, repo), base, '-o', origin)

    if args.nogit:
      kprint('removing git folder')
      shutil.rmtree(at_base('.git'))
    else:
      kprint('keeping `.git` folder at `%s` origin' % origin)

    if args.noboot:
      kprint('%s/.kurye file won\'t be run' % project)
    else:
      boot = at_base('.kurye')
      kprint('trying to run .kurye boot file')
      if os.path.exists(boot):
        subprocess.call(boot, cwd=base)
      else:
        kprint('boot file not found, passing.')
