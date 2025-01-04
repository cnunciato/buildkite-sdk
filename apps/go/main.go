package main

import (
	"log"
	"os"

	"github.com/cnunciato/buildkite-sdk/sdk/go/sdk/buildkite"
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

	err := os.MkdirAll("../../out/apps/go", 0755) // 0755 sets permissions (read, write, execute for owner; read and execute for others)
	if err != nil {
		log.Fatalf("Failed to create directory: %v", err)
	}

	file, err := os.Create("../../out/apps/go/pipeline.json")
	if err != nil {
		log.Fatalf("Failed to create file: %v", err)
	}
	defer file.Close()

	json, err := pipeline.ToJSON()
	if err != nil {
		log.Fatalf("Failed to serialize JSON: %v", err)
	}

	_, err = file.WriteString(json)
	if err != nil {
		log.Fatalf("Failed to write to file: %v", err)
	}
}
