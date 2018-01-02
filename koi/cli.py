import click
from migrate_command import migrate


@click.group()
def cli():
    """"""


cli.add_command(migrate)

if __name__ == '__main__':
    cli()
