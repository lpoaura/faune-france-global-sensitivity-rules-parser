"""Default script file"""
import click

from .helpers import create_table, insert_data


@click.group()
@click.option("--debug/--no-debug", default=False)
def cli(debug):
    """Main CLI fct"""
    click.echo(f"Debug mode is {'on' if debug else 'off'}")


@cli.command("create-table")
@click.option("--conn-string", help="PostgreSQL connections string")
@click.option("--delete-table-if-exists", default=False, help="Delete table if exists")
def cli_create_table(conn_string: str, delete_table_if_exists):
    """Create PostgreSQL table src_lpodatas.t_c_..."""
    click.echo("Start table creation")
    if delete_table_if_exists:
        click.echo("will delete table")
    create_table(conn_string, delete_table_if_exists)


@cli.command("insert-data")
@click.option("--conn-string", help="PostgreSQL connections string")
@click.option("--flush-table", default=False, help="Flush all data in table")
def cli_insert_data(conn_string: str, flush_table: bool = False):
    """Populate rules in db"""
    click.echo("Insert data")

    insert_data(conn_string, flush_table=flush_table)
