from buildkite_sdk.sdk import Pipeline

def test_sdk():
    pipeline = Pipeline()
    pipeline.add_command_step({ "label": "some-label" })

    assert pipeline.to_json() == """{"steps": [{"label": "some-label"}]}"""
    assert pipeline.to_yaml() == """steps:
- label: some-label
"""
