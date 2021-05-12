import click
import creache


@click.group()
def main():
    pass


@main.command()
@click.option(
    "--file", "-f", help="The Swift file you'd like to convert", type=click.Path()
)
def convert(file: str):
    """
    This is used to convert a swift file containing a struct into a struct that can be used with Realm Swift.
    """
    file = click.prompt(
        "Please enter the path to the file you'd like to convert", default=file
    )

    try:
        print("Opening...")
        file_contents = open(file)

        if click.confirm("This file exists. Continue?"):
            creache.run(file=file)
    except:
        print("this is not a file")
        print("Terminating program...")
    finally:
        file_contents.close()


if __name__ == "__main__":
    main()
