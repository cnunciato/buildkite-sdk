from buildkite_sdk.sdk import Pipeline

def generate_pipeline():
    pipeline = Pipeline()
    pipeline.add_command_step({"label": "some-label", "command": "echo 'Hello, world!'"})
    return pipeline.to_json()

print(generate_pipeline())