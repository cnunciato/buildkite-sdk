from buildkite_sdk.schema import CommandStep
import json

class Pipeline:
    def __init__(self):
        self.steps = []

    def add_command_step(self, props: CommandStep):
        self.steps.append(props)

    def to_json(self):
        return json.dumps(self.__dict__)
