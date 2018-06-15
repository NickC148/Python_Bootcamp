#!/usr/bin/env python
import sys
import os
import os.path
import stat
import glob
import argparse

exists = os.path.exists

BLACK = '\033[30m\033[%dm'
RED = '\033[31m\033[%dm'
GREEN = '\033[32m\033[%dm'
ORANGE = '\033[33m\033[%dm'
BLUE = '\033[34m\033[%dm'
PURPLE = '\033[35m\033[%dm'
CYAN = '\033[36m\033[%dm'
WHITE = '\033[37m\033[%dm'


def printer(colour):
    def model(*args):
        text = '%s ' * len(args) % args
        if sys.platform == 'win32':
            print text
            return
        print '%s%s%s' % (colour % (1), text, colour % (0))
    return model


red = printer(RED)
green = printer(GREEN)
orange = printer(ORANGE)
blue = printer(BLUE)
purple = printer(PURPLE)
cyan = printer(CYAN)

parser = argparse.ArgumentParser()
if sys.platform == 'win32':
    parser.add_argument('-d', '--deploydir', type=str,
                        default='/nedbank/deployments')
    parser.add_argument('-w', '--workdir',   type=str,
                        default='/nedbank/deployments/work')
    parser.add_argument('-s', '--start',     type=str, default='/nedbank')
else:
    parser.add_argument('-d', '--deploydir', type=str,
                        default='/main/nedcor/bbd/common/deployments')
    parser.add_argument('-w', '--workdir',   type=str,
                        default='/main/nedcor/bbd/common/deployments/work')
    parser.add_argument('-s', '--start',     type=str,
                        default='/main/nedcor/bbd/common')
parser.add_argument('-u', '--usetar',    default=False,
                    action="store_true", help="use tar")
parser.add_argument('-t', '--testing',   default=False,
                    action="store_true", help="verbose")
parser.add_argument('-v', '--verbose',   default=False,
                    action="store_true", help="verbose")
parser.add_argument('manifest_file',     type=str,  help='manifest_file')
options = parser.parse_args()

vars = {}


def mkdir(dir):
    if not exists(dir):
        orange('making dir %s' % (dir))
        os.makedirs(dir, 0775)


mkdir(options.deploydir)
mkdir(options.workdir)


def fixname(name):
    result = name
    if len(result) > 2 and result[1] == ':':
        result = result[2:]
    result = result.replace('\\', '/')
    return result


check_rc = '''\
    if [[ $rc -ne 0 ]]
    then
        echo backup failed
        exit $rc
    fi
'''.splitlines()


class Project:
    global options

    def __init__(self, name):
        self.name = fixname(name)
        self.programs = []
        self.binfiles = []
        self.gnts = []
        self.cntls = []
        self.artifacts = []

    def write_sh(self, command):
        self.shfile.write('%s\n' % (command))
        if options.verbose:
            green(command)

    def open_shell(self, type='build'):
        shfilename = '%s/%s_%s.sh' % (options.workdir,
                                      self.name.replace('/', '_'), type)
        if options.verbose:
            orange(shfilename)
        self.shfile = open(shfilename, 'wt')
        os.chmod(shfilename, stat.S_IRWXU | stat.S_IRWXG)
        self.write_sh('#! /bin/ksh')

    def close_shell(self):
        self.shfile.close()

    def make_source_tar(self):
        project_name = self.name.replace('/', '_')
        self.programs_list_name = '%s/%s_program.list' % (
            options.workdir, project_name)
        self.source_list_name = '%s/%s_source.list' % (
            options.workdir, project_name)
        ofile = open(self.programs_list_name, 'wt')
        for program in self.programs:
            ofile.write('%s\n' % (program))
        ofile.close()
        command = 'dbxsrc -s %s -o %s -f %s' % (
            options.start, self.source_list_name, self.programs_list_name)
        self.write_sh(command)
        if options.usetar:
            self.write_sh('tar vcfL %s_source.tar %s' %
                          (project_name, self.source_list_name))
            self.write_sh('gzip %s_source.tar' % (project_name))
        else:
            command = 'zip %s_source.zip -@ < %s' % (
                project_name, self.source_list_name)
            self.write_sh(command)

    def make_deploy_zip(self):
        project_name = self.name.replace('/', '_')
        self.open_shell('build')
        if len(self.programs) > 0:
            self.make_source_tar()
        self.package_list_name = '%s/%s_package.list' % (
            options.workdir, project_name)
        ofile = open(self.package_list_name, 'wt')
        for program in self.programs:
            ofile.write('%s\n' % (program))
        for binfile in self.binfiles:
            ofile.write('%s\n' % (binfile))
        for gnt in self.gnts:
            ofile.write('%s\n' % (gnt))
        for cntl in self.cntls:
            ofile.write('%s\n' % (cntl))
        for artifact, _ in self.artifacts:
            ofile.write('%s\n' % (artifact))
        ofile.close()
        command = 'zip -j %s_package.zip -@ < %s' % (
            project_name, self.package_list_name)
        self.write_sh(command)
        command = 'zip -0 -j %s_deploy.zip %s_package.zip' % (
            project_name, project_name)
        self.write_sh(command)
        if len(self.programs) > 0:
            if options.usetar:
                command = 'zip -0 -j %s_deploy.zip %s_source.tar.gz' % (
                    project_name, project_name)
            else:
                command = 'zip -0 -j %s_deploy.zip %s_source.zip' % (
                    project_name, project_name)
            self.write_sh(command)
        command = 'zip -j %s_deploy.zip %s_backup.list' % (
            project_name, project_name)
        self.write_sh(command)
        command = 'zip -j %s_deploy.zip %s_backup.sh' % (
            project_name, project_name)
        self.write_sh(command)
        command = 'zip -j %s_deploy.zip %s_extract.sh' % (
            project_name, project_name)
        self.write_sh(command)
        command = 'zip -j %s_deploy.zip %s_restore.sh' % (
            project_name, project_name)
        self.write_sh(command)
        self.deploy_file = '%s/%s_deploy' % (options.deploydir, project_name)
        command = 'cat /usr/bin/unzipsfx %s_deploy.zip > %s' % (
            project_name, self.deploy_file)
        self.write_sh(command)
        command = 'chmod 755 %s' % (self.deploy_file)
        self.write_sh(command)
        command = 'zip -A %s' % (self.deploy_file)
        self.write_sh(command)
        self.close_shell()

    def make_backup_shell(self):
        project_name = self.name.replace('/', '_')
        self.backup_list_name = '%s/%s_backup.list' % (
            options.workdir, project_name)
        ofile = open(self.backup_list_name, 'wt')
        self.open_shell('backup')
        for program in self.programs:
            _, name = os.path.split(program)
            ofile.write('%s/%s\n' % (self.program_dir, name))
        for binfile in self.binfiles:
            _, name = os.path.split(binfile)
            ofile.write('%s/%s\n' % (self.binfile_dir, name))
        for gnt in self.gnts:
            _, name = os.path.split(gnt)
            ofile.write('%s/%s\n' % (self.gnt_dir, name))
        for cntl in self.cntls:
            _, name = os.path.split(cntl)
            ofile.write('%s/%s\n' % (self.cntl_dir, name))
        for artifact, arti_dir in self.artifacts:
            _, name = os.path.split(artifact)
            ofile.write('%s/%s\n' % (arti_dir, name))
        ofile.close()
        date_format = '$(date +%Y%m%d-%H%M%S)'
        if options.usetar:
            self.write_sh('if [[ ! -e "%s_backup.tar" ]]' % (project_name))
            self.write_sh('then')
            self.write_sh('    tar vcfL %s_backup.tar %s_backup.list' %
                          (project_name, project_name))
            self.write_sh('    rc=$?')
            self.write_sh('    chmod 440 %s_backup.tar' % (project_name))
            for line in check_rc:
                self.write_sh(line)
            self.write_sh('    cp %s_backup.tar %s_backup_%s.tar' %
                          (project_name, date_format, project_name))
            self.write_sh('fi')
        else:
            self.write_sh('if [[ ! -e "%s_backup.zip" ]]' % (project_name))
            self.write_sh('then')
            self.write_sh('    zip %s_backup.zip -@ < %s_backup.list' %
                          (project_name, project_name))
            self.write_sh('    rc=$?')
            self.write_sh('    chmod 440 %s_backup.zip' % (project_name))
            for line in check_rc:
                self.write_sh(line)
            self.write_sh('    cp %s_backup.zip %s_backup_%s.zip' %
                          (project_name, date_format, project_name))
            self.write_sh('fi')
        self.close_shell()

    def make_extract_shell(self):
        project_name = self.name.replace('/', '_')
        self.open_shell('extract')
        if options.usetar:
            self.write_sh('if [[ ! -e "%s_backup.tar" ]]' % (project_name))
            self.write_sh('then')
            self.write_sh('    ./%s_backup.sh' % (project_name))
            self.write_sh('    rc=$?')
            for line in check_rc:
                self.write_sh(line)
            self.write_sh('fi')
        else:
            self.write_sh('if [[ ! -e "%s_backup.zip" ]]' % (project_name))
            self.write_sh('then')
            self.write_sh('    ./%s_backup.sh' % (project_name))
            self.write_sh('    rc=$?')
            for line in check_rc:
                self.write_sh(line)
            self.write_sh('fi')
        for i, program in enumerate(self.programs):
            if i == 0:
                command = 'mkdir -p %s' % (self.program_dir)
                self.write_sh(command)
            _, name = os.path.split(program)
            command = 'unzip -o %s_package.zip -d %s %s' % (
                project_name, self.program_dir, name)
            self.write_sh(command)
        for i, binfile in enumerate(self.binfiles):
            if i == 0:
                command = 'mkdir -p %s' % (self.binfile_dir)
                self.write_sh(command)
            _, name = os.path.split(binfile)
            command = 'unzip -o %s_package.zip -d %s %s' % (
                project_name, self.binfile_dir, name)
            self.write_sh(command)
        for i, gnt in enumerate(self.gnts):
            if i == 0:
                command = 'mkdir -p %s' % (self.gnt_dir)
                self.write_sh(command)
            _, name = os.path.split(gnt)
            command = 'unzip -o %s_package.zip -d %s %s' % (
                project_name, self.gnt_dir, name)
            self.write_sh(command)
        for i, cntl in enumerate(self.cntls):
            if i == 0:
                command = 'mkdir -p %s' % (self.cntl_dir)
                self.write_sh(command)
            _, name = os.path.split(cntl)
            command = 'unzip -o %s_package.zip -d %s %s' % (
                project_name, self.cntl_dir, name)
            self.write_sh(command)
        prev_arti_dir = ''
        for artifact, arti_dir in self.artifacts:
            if arti_dir != prev_arti_dir:
                prev_arti_dir = arti_dir
                command = 'mkdir -p %s' % (arti_dir)
                self.write_sh(command)
            _, name = os.path.split(artifact)
            command = 'unzip -o %s_package.zip -d %s %s' % (
                project_name, arti_dir, name)
            self.write_sh(command)
        self.close_shell()

    def make_restore_shell(self):
        project_name = self.name.replace('/', '_')
        self.open_shell('restore')
        if options.usetar:
            command = 'tar vxf %s_backup.tar' % (project_name)
        else:
            command = 'unzip -d / %s_backup.zip' % (project_name)
        self.write_sh(command)
        self.close_shell()

    def run_build(self):
        project_name = self.name.replace('/', '_')
        cur_dir = os.curdir
        os.chdir(options.workdir)
        os.system('./%s_build.sh' % (project_name))
        os.chdir(cur_dir)


START, PROGRAM, BINFILE, GNT, CNTL, ARTIFACT = 0, 1, 2, 3, 4, 5
state = START


def remove_comment(line):
    p = line.find('#')
    if p >= 0:
        line = line[:p]
    return line


def expand(line):
    result = ''
    while True:
        s = line.find('${')
        if s < 0:
            result += line
            break
        result += line[:s]
        line = line[s+2:]
        e = line.find('}')
        if e < 0:
            result += line
            break
        var = line[:e]
        line = line[e+1:]
        if var in vars:
            result += vars[var]
    return result


def make_list(file):
    if '*' in file or '?' in file:
        return glob.glob(file)
    return [file]


def parse_manifest(sourceFile):
    ifile = open(sourceFile, 'rt')
    lines = ifile.readlines()
    ifile.close()
    project = None
    lineNo = 0
    for line in lines:
        lineNo += 1
        line = expand(remove_comment(line.strip()))
        if len(line) == 0:
            continue
        fields = line.split('=')
        if len(fields) == 2:
            vars[fields[0]] = fields[1]
            continue
        fields = line.split()
        if fields[0] == 'include':
            if len(fields) == 2:
                ifile = open(fields[1], 'rt')
                includeLines = ifile.readlines()
                ifile.close()
                lines[lineNo:lineNo] = includeLines
            continue
        if fields[0] == 'project' and len(fields) > 1:
            project = Project(fields[1])
            if options.verbose:
                green('project %s' % (project.name))
            continue
        if project == None:
            print('expecting project name')
            return None
        if len(fields) > 1 and fields[0] == 'program':
            project.program_dir = fields[1]
            state = PROGRAM
            continue
        if len(fields) > 1 and fields[0] == 'binfile':
            project.binfile_dir = fields[1]
            state = BINFILE
            continue
        if len(fields) > 1 and fields[0] == 'gnt':
            project.gnt_dir = fields[1]
            state = GNT
            continue
        if len(fields) > 1 and fields[0] == 'cntl':
            project.cntl_dir = fields[1]
            state = CNTL
            continue
        if len(fields) > 1 and fields[0] == 'artifact':
            project.artifact_dir = fields[1]
            state = ARTIFACT
            continue
        if state == PROGRAM:
            for file in make_list(fields[0]):
                project.programs.append(file)
            continue
        if state == BINFILE:
            for file in make_list(fields[0]):
                project.binfiles.append(file)
            continue
        if state == GNT:
            for file in make_list(fields[0]):
                project.gnts.append(file)
            continue
        if state == CNTL:
            for file in make_list(fields[0]):
                project.cntls.append(file)
            continue
        if state == ARTIFACT:
            for file in make_list(fields[0]):
                project.artifacts.append((file, project.artifact_dir))
            continue
        red('%s not used' % line)
    return project


def main():
    sourceFile = options.manifest_file
    project = parse_manifest(sourceFile)
    if project == None:
        red("Project not Created")
        return 1
    source_missing = False
    blue('programs:', project.program_dir if len(
        project.programs) > 0 else 'None')
    for program in project.programs:
        if exists(program) == False:
            source_missing = True
            red("program source %s is missing" % (program))
    blue('binfiles:', project.binfile_dir if len(
        project.binfiles) > 0 else 'None')
    for binfile in project.binfiles:
        if exists(binfile) == False:
            source_missing = True
            red("binfile source %s is missing" % (binfile))
    blue('gnts:', project.gnt_dir if len(project.gnts) > 0 else 'None')
    for gnt in project.gnts:
        if exists(gnt) == False:
            source_missing = True
            red("gnt source %s is missing" % (gnt))
    blue('cntls:', project.cntl_dir if len(project.cntls) > 0 else 'None')
    for cntl in project.cntls:
        if exists(cntl) == False:
            source_missing = True
            red("cntl source %s is missing" % (cntl))
    for artifact, _ in project.artifacts:
        if exists(artifact) == False:
            source_missing = True
            red("artifact source %s is missing" % (artifact))
    if source_missing == True:
        return 1
    project.make_backup_shell()
    project.make_extract_shell()
    project.make_restore_shell()
    project.make_deploy_zip()
    if sys.platform != 'win32':
        project.run_build()
    return 0


if __name__ == '__main__':
    rc = main()
    exit(rc)
