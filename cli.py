import click
from chmod import Chmod


@click.command()
@click.argument('param')
def cli_chmod(param):
    c = Chmod(param)
    click.echo(click.style('numeric_mode: ', fg='green') + c.getNumeric())
    click.echo(click.style('text_mode: ', fg='green') + c.getText())


if __name__ == '__main__':
    cli_chmod()
