package buildkite

import (
	"testing"
)

func TestBuildkite(t *testing.T) {
	pipeline := Pipeline{}

	pipeline.AddStep(Step{
		Type: "something",
	})

	if pipeline.Steps[0].Type != "something" {
		t.Error("Expected step type value to be 'something'")
	}
}
