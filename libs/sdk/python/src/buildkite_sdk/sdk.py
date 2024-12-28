from buildkite_sdk.schema import _CommandStep
import json
import yaml

class Pipeline:
    def __init__(self):
        self.steps = []

    def add_command_step(self, props: _CommandStep):
        self.steps.append(props)

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_yaml(self):
        return yaml.dump(self.__dict__)
