from src.main import generate_pipeline

def test_main():
    assert generate_pipeline() == """{"steps": [{"command": "echo 'Hello, world!'"}]}"""
