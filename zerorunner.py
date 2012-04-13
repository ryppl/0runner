from zeroinstall.injector import cli
from multiprocessing import Process
import sys

def run(argv):
    # Break up the argument list on ';' boundaries and un-quote
    # escaped semicolons
    commands = [[]]
    for a in argv:
        if a == ';':
            commands.append([])
        else:
            if a == r'\;':
                a = ';'
            commands[-1].append(a)

    # Because 0launch doesn't return, we need to invoke all but the
    # last one from a subprocess
    for c in commands[:-1]:
        p = Process(target = cli.main, args=(c,))
        p.start()
        p.join()
        if p.exitcode:
            exit(p.exitcode)

    # The last one can be launched directly; we don't need control later.
    cli.main(commands[-1])

if __name__ == '__main__':
    run(sys.argv[1:])
