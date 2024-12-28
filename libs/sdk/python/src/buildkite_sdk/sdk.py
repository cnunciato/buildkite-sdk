from buildkite_sdk.schema import CommandStep
import json

class Pipeline:
    def __init__(self):
        self.steps = []

    def add_command_step(self, step: CommandStep):
        self.steps.append(step)

    def to_json(self):
        return json.dumps(self.steps)
