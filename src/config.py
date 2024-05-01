from dataclasses import dataclass
from importlib import import_module

import yaml

from src.pattern_creator import PatternCreator
from src.pattern_guesser import PatternGuesser


@dataclass
class Config:

    dims: list[int]
    creator: PatternCreator
    guesser: PatternGuesser
    max_n_turns: int
    min_n_correct: int

    @staticmethod
    def get_class(classpath: str):
        module, class_name = classpath.rsplit(".", 1)
        return getattr(import_module(module), class_name)

    @staticmethod
    def from_yaml_file(file_path: str):
        with open(file_path) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        dims: list[int] = config["dims"]
        sub_dims = dims[1:] or [1]
        config["creator"] = Config.get_class(config["creator"])(dims)
        config["guesser"] = Config.get_class(config["guesser"])(sub_dims)
        return Config(**config)
