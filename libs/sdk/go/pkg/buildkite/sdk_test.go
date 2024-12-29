package buildkite

import (
	"testing"
)

func TestAddCommandStep(t *testing.T) {
	pipeline := Pipeline{}

	cmd := "some-label"
	pipeline.AddCommandStep(CommandStep{
		Label: &cmd,
	})

	actual, _ := pipeline.ToJSON()
	expected := `[{"agents":null,"allow_dependency_failure":null,"artifact_paths":null,"branches":null,"cache":null,"cancel_on_build_failing":null,"command":null,"commands":null,"depends_on":null,"label":"some-label","matrix":null,"plugins":null,"skip":null,"soft_fail":null}]`
	if actual != expected {
		t.Errorf("Expected '%s' to be '%s'", actual, expected)
	}
}
