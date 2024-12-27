package main

import (
	"testing"

	"github.com/buildkite/buildkite-sdk/pkg/buildkite"
)

func TestHello(t *testing.T) {
	pipeline := buildkite.Pipeline{}
	pipeline.AddStep(buildkite.Step{
		Type: "something",
	})

	if pipeline.Steps[0].Type != "something" {
		t.Error("Expected step type value to be 'something'")
	}
}
