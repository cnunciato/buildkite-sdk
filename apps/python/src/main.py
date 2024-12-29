from buildkite_sdk.sdk import Pipeline

pipeline = Pipeline()
pipeline.add_command_step({"label": "some-label", "command": "echo 'Hello, world!'"})

print(pipeline.to_json())
print(pipeline.to_yaml())
