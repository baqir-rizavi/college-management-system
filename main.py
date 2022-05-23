import InitDB
from Portal import Portal


def main():
    InitDB.__init_db__()
    portal = Portal()
    portal.run()


if __name__ == '__main__':
    main()
