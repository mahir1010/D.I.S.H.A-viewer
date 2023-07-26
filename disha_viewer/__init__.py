from importlib.resources import files, as_file

import disha_viewer.resources


def get_resource(name):
    with as_file(files(disha_viewer.resources).joinpath(name)) as file:
        return str(file)