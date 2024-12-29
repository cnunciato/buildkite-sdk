from buildkite_sdk.sdk import Pipeline

def generate_json():
    pipeline = Pipeline()
    pipeline.add_command_step({"label": "some-label", "command": "echo 'Hello, world!'"})
    return pipeline.to_json()

def generate_yaml():
    pipeline = Pipeline()
    pipeline.add_command_step({"label": "some-label", "command": "echo 'Hello, world!'"})
    return pipeline.to_yaml()
