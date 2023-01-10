from core.converter import convert_file
from time import time
import click
# For more information about CLICK visit: https://pywombat.com/articles/CLI-python
# Author: Gabriel Ichcanziho


@click.command()
@click.argument('input_file')
@click.argument('output_type')
@click.option('--name', '-n', default=None)
def run(input_file, output_type, name):

    try:
        start = time()
        convert_file(file_dir=input_file, output_type=output_type, name=name)
        print(f"Process finished in: {time()-start} seconds.")
    except Exception as e:
        print(f"Error: {e}, {type(e).__name__}")


if __name__ == '__main__':
    run()
