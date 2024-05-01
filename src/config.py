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
        for key in ["creator", "guesser"]:
            config[key] = Config.get_class(config[key])()
        return Config(**config)
    