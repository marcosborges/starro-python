import subprocess

def test():
    subprocess.run(['python' , '-m', 'pytest', 'starro']) # nosec


def coverage():
    subprocess.run(['python' , '-m', 'coverage', 'erase']) # nosec
    subprocess.run(['python' , '-m', 'coverage', 'run', '--source=starro', '-m', 'pytest', '--junitxml=results.xml' , 'tests']) # nosec
    subprocess.run(['python' , '-m', 'coverage', 'xml', '-i']) # nosec
    subprocess.run(['python' , '-m', 'coverage', 'report', '-m']) # nosec


def lint():    
    print("PYLINT")
    subprocess.run(['python' , '-m', 'pylint', '--ignore-patterns=test_', 'starro/']) # nosec
    print("FLAK8")
    subprocess.run(['python' , '-m', 'flake8','starro/starro.py']) # nosec


def security():    
    print("BANDIT")
    subprocess.run(['python' , '-m', 'bandit','-r', './', '-n', '3', '-lll']) # nosec
    print("DEPENDENCY-CHECK")
    subprocess.run(['python' , '-m', 'dependency-check', '--disableAssembly', '-s', '.', '-o', 'build', '--exclude', 'tests/', '-f', 'ALL']) # nosec


def packing():
    print("packing")


def publish():
    print("Publishing")
