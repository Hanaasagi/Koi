import click


@click.command('migrate', short_help='exec migrate')
@click.option('--database', '-d',
              help='the database connection to use.')
@click.option('--path', '-p',
              help='the path of migration files')
def migrate(database, path):
    if not click.confirm(
            'Are you sure you want to proceed with the migration?'):
        return
    pass

