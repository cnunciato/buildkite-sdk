package main

import (
	"fmt"

	"github.com/cnunciato/buildkite-sdk/sdkgo/sdk/buildkite"
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
