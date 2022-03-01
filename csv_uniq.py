import numpy as np
from typing import IO
from numpy import genfromtxt
import click
from pathlib import Path

@click.command()
@click.option('-f', '--file', required=True, help='Csv file to process', type=click.File('r'))
@click.option('-c', '--colnum', required=True, help='Nmber of column to parse', type=click.INT)
@click.option('-d', '--delimiter', default=',', help='Delimiter', type=click.STRING)
@click.option('-o', '--output_dir', default='out', help='Output directory', type=click.STRING)
def main(file: IO,  colnum: int, delimiter: str, output_dir: str) -> None:
    output_path = Path(f'./{output_dir}')
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)


    data = genfromtxt(file, delimiter=delimiter, dtype=str, replace_space='_')
    uniq_items = np.unique(data[:, colnum])

    for item in uniq_items:
        fname = item.replace(' ', '_')
        with open(output_path / f'{fname}.csv', 'w+') as outfile:
            np.savetxt(outfile, data[data[:, colnum] == item], delimiter=delimiter, fmt='%s')


if __name__ == '__main__':
    main()