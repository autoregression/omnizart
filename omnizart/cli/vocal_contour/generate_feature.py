import click

from omnizart.cli.common_options import add_common_options, COMMON_GEN_FEATURE_OPTIONS
from omnizart.vocal_contour import app
from omnizart.setting_loaders import VocalContourSettings


@click.command()
@add_common_options(COMMON_GEN_FEATURE_OPTIONS)
@click.option(
    "-h",
    "--hop-size",
    help="Hop size in seconds with respect to sampling rate.",
    type=float,
    default=0.02,
    show_default=True
)
@click.option(
    "-s",
    "--sampling-rate",
    help="Adjust input sampling rate to this value.",
    type=int,
    default=16000,
    show_default=True
)
def generate_feature(dataset_path, output_path, num_threads, hop_size, sampling_rate):
    """Extract the feature of the whole dataset for training.

    The command will try to infer the dataset type from the given dataset path.

    \b
    * MIR-1K
    * MedleyDB (not supported yet)
    """
    settings = VocalContourSettings()
    settings.feature.hop_size = hop_size
    settings.feature.sampling_rate = sampling_rate
    if output_path is not None:
        settings.dataset.feature_save_path = output_path

    app.generate_feature(dataset_path, settings, num_threads=num_threads)
