import bz2
import math
import os
import pickle
import traceback

import pandas as pd

from Image import Image
from utils import extract_plate_name


def convert_index_to_plate(coords):
    index = (coords.split('-')[0]).strip()
    base = math.ceil(int(index) / 4) * 4
    return f'{base - 3}-{base}'


class Experiment:

    def __init__(self, bait, images, datasheet, base_path, initialize=True):
        self.bait = bait
        self.base_path = base_path
        self.output_path = os.path.join(base_path, 'output')
        if initialize:
            self.datasheet = pd.read_excel(datasheet, engine='openpyxl')
            self.datasheet['plate'] = self.datasheet['Coordinate'].apply(lambda x: convert_index_to_plate(x))
            self.images = [
                Image(image, self.output_path, self.datasheet[self.datasheet['plate'] == extract_plate_name(image)]) for
                image in images]
        else:
            self.datasheet = datasheet
            self.images = images
        self.plate_map = {}
        for image in self.images:
            if image.plate_base_number in self.plate_map:
                self.plate_map[image.plate_base_number].append(image)
            else:
                self.plate_map[image.plate_base_number] = [image]
        # self.headers = '<thead><tr>' + f'<th colspan="3">Bait Number {self.bait}</th>' + '<th colspan="2">TF</th>' + ''.join(
        #     [f'<th colspan="3">Day {day}</th>' for day in self.days]) \
        #                + '</tr>' + '<tr><th>Index</th><th>Activated</th><th>Coordinate</th><th>TF1</th><th>TF2</th>' \
        #                + (Bait.STATIC_HEADER * len(self.days)) + '</tr></thead>'

    def apply_funct(self, funct, params=None):
        for image in self.images:
            if image.exception_occured:
                continue
            try:
                if params is None:
                    yield image, funct(image)
                else:
                    yield image, funct(image, params)
            except Exception as e:
                image.exception_occured = True
                image.exception_reason = str(e)
                print(f"Error while processing :{image}")
                traceback.print_exc()


def export_experiment(experiment, single_file=True):
    if single_file:
        pickle.dump(experiment,
                    bz2.BZ2File(os.path.join(experiment.base_path, f'bait_{experiment.bait}_results.dhy1h'), 'wb'))
    else:
        for plate in experiment.plate_map.keys():
            imgs = experiment.plate_map[plate]
            sub_experiment = Experiment(experiment.bait, imgs, experiment.datasheet, experiment.base_path, False)
            pickle.dump(sub_experiment,
                        bz2.BZ2File(
                            os.path.join(sub_experiment.base_path, f'bait_{sub_experiment.bait}_{plate}_results.dhy1h'),
                            'wb'))
            del sub_experiment
