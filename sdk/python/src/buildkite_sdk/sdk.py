from buildkite_sdk.schema import CommandStep
from buildkite_sdk.environment import Environment
import json
import yaml

class Pipeline:
    def __init__(self):
        self.steps = []

    def add_command_step(self, props: CommandStep):
        self.steps.append(props)

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_yaml(self):
        return yaml.dump(self.__dict__)
