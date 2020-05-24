import io
import re

from sh import git


class Commit:
    RE_COMMIT_SHA = re.compile(r'^(.{7})\s(.+)$')

    def __init__(self, log_line: str):
        match = self.RE_COMMIT_SHA.match(log_line)
        if match:
            self.sha = match.group(1)
            self.message = match.group(2)
        else:
            raise ValueError('Invalid log line: %s', log_line)


if __name__ == '__main__':
    buf = io.StringIO()
    git.log('master..', '--oneline', '--no-decorate', _out=buf, _tty_out=False)
    print(buf.getvalue())

    branch_commits = buf.getvalue().splitlines()
    branch_commits.reverse()
    for idx, ll in enumerate(branch_commits):
        commit = Commit(ll)
        print(idx, commit.sha, commit.message)
