package main

import (
	"fmt"

	buildkite "github.com/buildkite/buildkite-sdk"
)

func Hello(name string) string {
	result := "Hello " + name
	return result
}

func main() {
	fmt.Println(Hello("app-go"))

	pipeline := buildkite.Pipeline{}
	pipeline.AddStep(buildkite.Step{
		Type: "thing",
	})

	fmt.Println(pipeline.ToJSON())
}
