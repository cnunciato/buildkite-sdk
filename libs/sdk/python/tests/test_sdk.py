from buildkite_sdk.sdk import Pipeline, CommandStep

def test_sdk():
    pipeline = Pipeline()
    pipeline.add_command_step(CommandStep(type="something"))
    assert pipeline.to_json() == "nope"
