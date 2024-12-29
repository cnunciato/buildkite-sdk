package main

import (
	"fmt"

	"github.com/buildkite/buildkite-sdk/pkg/buildkite"
)

func main() {
	pipeline := buildkite.Pipeline{}

	label := "some-label"
	command := "echo 'Hello, world!'"

	pipeline.AddCommandStep(buildkite.CommandStep{
		Label: &label,
		Command: &buildkite.CommandUnion{
			String: &command,
		},
	})

	fmt.Println(pipeline.ToJSON())
}
