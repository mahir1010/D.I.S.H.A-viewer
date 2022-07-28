import logging
import os
import traceback
from pathlib import Path

from PIL import Image as PIL_Image
from PIL import ImageDraw

from utils import *


class Image:
    def __init__(self, file_path, output_path, dataframe):
        self.dataframe = dataframe.copy()
        self.plate_base_number = int(dataframe['plate'].iloc[0].split('-')[0])
        self.file_path = file_path
        self.name = Path(file_path).stem
        self.image = np.array(PIL_Image.open(file_path))
        if self.image is None:
            logging.error("Error while Processing {}:\n\n{}".format(file_path, traceback.format_exc()))
        self.output_colonies_path = os.path.join(output_path, self.name.split('.')[0])
        Path(self.output_colonies_path).mkdir(parents=True, exist_ok=True)
        self.display_dataframe = None
        self.intensity_map = None
        self.exception_occured = False
        self.exception_reason = None

    def getIndex(self, coords):
        index = coords.split("-")
        index[0] = int(index[0])
        yIndex = row2IndexMap[index[1][0]]
        xIndex = int(index[1][1:]) - 1
        colonies = []

        if index[0] % 4 == 1:
            xIndex = 4 * xIndex
            yIndex = 4 * yIndex
        elif index[0] % 4 == 2:
            xIndex = 4 * xIndex + 2
            yIndex = 4 * yIndex
        elif index[0] % 4 == 3:
            xIndex = 4 * xIndex
            yIndex = 4 * yIndex + 2
        elif index[0] % 4 == 0:
            xIndex = 4 * xIndex + 2
            yIndex = 4 * yIndex + 2

        for i in range(2):
            for j in range(2):
                colonies.append(
                    [[self.rows[xIndex + i] - self.rows[xIndex], self.rows[xIndex + 1 + i] - self.rows[xIndex]],
                     [self.cols[yIndex + j] - self.cols[yIndex], self.cols[yIndex + j + 1] - self.cols[yIndex]]])
        return [[self.rows[xIndex], self.rows[xIndex + 2]], [self.cols[yIndex], self.cols[yIndex + 2]]], colonies

    # Returns TF1 TF2 Intensity Area
    def getDetails(self, coords):
        return self.dataframe[self.dataframe['Coordinate'] == coords][['TF1', 'TF2', 'Intensity', 'Area']].values[0]

    def set_grid(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def export_grid_image(self):
        image = PIL_Image.fromarray(self.image.copy())
        draw = ImageDraw.Draw(image)
        for i, p in enumerate(self.rows):
            if i % 4 == 0:
                draw.line([(p, 0), (p, image.size[1] - 1)], (0, 0, 255), width=3)
            elif i % 2 == 0:
                draw.line([(p, 0), (p, image.size[1] - 1)], (0, 0, 153), width=3)
            else:
                draw.line([(p, 0), (p, image.size[1] - 1)], (0, 0, 0), width=3)
        for i, p in enumerate(self.cols):
            if i % 4 == 0:
                draw.line([(0, p), (image.size[0] - 1, p)], (0, 0, 255), width=3)
            elif i % 2 == 0:
                draw.line([(0, p), (image.size[0] - 1, p)], (0, 0, 153), width=3)
            else:
                draw.line([(0, p), (image.size[0] - 1, p)], (0, 0, 0), width=3)
        return np.array(image)

    def get_coordinate(self, x, y, transpose=False):
        rows, cols = [self.rows, self.cols] if not transpose else [self.cols, self.rows]
        row_index = col_index = 0
        if x < rows[0] or x > rows[-1] or y < cols[0] or y > cols[-1]:
            return ''
        for i in range(0, len(rows), 4):
            if x < rows[i + 4]:
                row_index = i
                break
        for i in range(0, len(cols), 4):
            if y < cols[i + 4]:
                col_index = i
                break
        coords = f"{Index2rowMap[math.floor(col_index / 4)]}{math.floor(row_index / 4) + 1:02d}"
        if x < rows[row_index + 2] and y < cols[col_index + 2]:
            quad_id = 0
        elif x < rows[row_index + 4] and y < cols[col_index + 2]:
            quad_id = 1
        elif x < rows[row_index + 2] and y < cols[col_index + 4]:
            quad_id = 2
        else:
            quad_id = 3
        return f"{self.plate_base_number + quad_id}-{coords}"

    def __str__(self):
        return self.name
