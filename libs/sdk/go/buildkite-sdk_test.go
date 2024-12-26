package buildkite

import (
	"testing"
)

func TestBuildkite(t *testing.T) {
	result := Buildkite("works")
	if result != "Buildkite works" {
		t.Error("Expected Buildkite to append 'works'")
	}
}
