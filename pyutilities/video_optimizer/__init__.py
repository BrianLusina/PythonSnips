#!/usr/bin/env python

import os
import re
import time
from multiprocessing import Pool

import click
import ffmpy
from ffprobe import FFProbe

"""
    Optimize for Chrome with low profile, low bandwith and low patience.
"""

FFMPEG_OPTIONS = '-codec:v libx264 -profile:v main -preset slow -movflags faststart -b:v 300k -maxrate 300k ' \
                 '-bufsize 300k -vf scale=640:480 -threads 0 -codec:a libfdk_aac -b:a 96k -y'

current_milli_time = lambda: int(round(time.time() * 1000))

source_dir = False


@click.command()
@click.option('--source', default='.', help='Directory where to find videos.')
@click.option('--force-yes', default=False, help='Do not prompt yes/no')
@click.option('--workers', default=1, help='Number of FFMpeg concurrent processes')
def optimize(source, force_yes, workers):
    """

    :param source: Directory where to find videos.
    :param force_yes: Override something, I am still deciding.
    :param workers: Number of processes to spawn.
    :return:
    """
    global source_dir
    source_dir = source

    matches = []
    for filename in iter_matching(source, re.compile(r'.*\.(mp4|wmv|ogv|avi|flv)$').match):
        matches.append(filename)

    click.echo(str(len(matches)) + " videos founded in " + source)
    pool = Pool(processes=workers)
    click.echo(pool.map(ffmpeg, matches))


def ffmpeg(file_input, root_output='output'):
    """
    Transcode files
    :param file_input: Name of the file to transcode.
    :return:
    """

    # output_dir = os.path.join(source_dir, '/', os.path.dirname(file_input))
    output_dir = os.path.join(root_output, os.path.normpath(os.path.relpath(os.path.dirname(file_input), source_dir)))
    click.echo("Folders: " + output_dir)

    if os.path.exists(output_dir):
        click.echo("Folder " + output_dir + " already exists.")
    else:
        os.makedirs(output_dir)

    duration = 0
    start_time = current_milli_time()
    metadata = FFProbe(file_input)
    for stream in metadata.streams:
        click.echo(str(stream.durationSeconds()) + " seconds for " + os.path.basename(file_input))
        duration = stream.durationSeconds()

    try:
        ff = ffmpy.FF(inputs={file_input: None},
                      outputs={os.path.abspath(os.path.join(output_dir, os.path.basename(file_input))): FFMPEG_OPTIONS})
        click.echo(ff.cmd_str)
        ff.run()
    except:
        return "Problem with " + file_input

    end_time = current_milli_time()
    return "Converted " + str(duration) + " in ~" + str(round((end_time - start_time) / 1000 / 60))


def iter_matching(dirpath, predicate):
    """
    Yield all the matches
    :param dirpath:
    :param predicate:
    :return:
    """

    for dir_, dirnames, filenames in os.walk(dirpath):
        for filename in filenames:
            abspath = os.path.join(dir_, filename)
            if predicate(abspath):
                yield abspath


if __name__ == '__main__':
    optimize()
