package buildkite

import (
	"testing"
)

func TestAddCommandStep(t *testing.T) {
	pipeline := Pipeline{}

	command := "echo 'Hello, world!'"
	pipeline.AddCommandStep(CommandStep{
		Command: &CommandUnion{
			String: &command,
		},
	})

	actual, _ := pipeline.ToJSON()
	expected := `[{"agents":null,"allow_dependency_failure":null,"artifact_paths":null,"branches":null,"cache":null,"cancel_on_build_failing":null,"command":"echo 'Hello, world!'","commands":null,"depends_on":null,"matrix":null,"plugins":null,"skip":null,"soft_fail":null}]`
	if actual != expected {
		t.Errorf("Expected '%s' to be '%s'", actual, expected)
	}

	// actual, _ = pipeline.ToYAML()
	// expected = `nope`
	// if actual != expected {
	// 	t.Errorf("Expected '%s' to be '%s'", actual, expected)
	// }
}