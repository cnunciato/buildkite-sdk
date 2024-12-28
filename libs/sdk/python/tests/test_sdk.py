from buildkite_sdk.sdk import Pipeline

def test_sdk():
    pipeline = Pipeline()
    pipeline.add_command_step(props={"command": "echo 'Hello, world!'"})
    assert pipeline.to_json() == """{"steps": [{"command": "echo 'Hello, world!'"}]}"""
