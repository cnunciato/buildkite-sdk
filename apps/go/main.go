package main

import (
	"fmt"

	"github.com/buildkite/buildkite-sdk/pkg/buildkite"
)

func main() {
	pipeline := buildkite.Pipeline{}
	label := "some-label"
	pipeline.AddCommandStep(buildkite.CommandStep{
		Label: &label,
	})

	fmt.Println(pipeline.ToJSON())
}
