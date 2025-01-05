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

	json, err := pipeline.ToJSON()
	if err != nil {
		log.Fatalf("Failed to serialize JSON: %v", err)
	}

	jsonFile, err := os.Create("../../out/apps/go/pipeline.json")
	if err != nil {
		log.Fatalf("Failed to create file: %v", err)
	}
	defer jsonFile.Close()

	_, err = jsonFile.WriteString(json)
	if err != nil {
		log.Fatalf("Failed to write to file: %v", err)
	}

	yaml, err := pipeline.ToYAML()
	if err != nil {
		log.Fatalf("Failed to serialize JSON: %v", err)
	}

	yamlFile, err := os.Create("../../out/apps/go/pipeline.yaml")
	if err != nil {
		log.Fatalf("Failed to create file: %v", err)
	}
	defer yamlFile.Close()

	_, err = yamlFile.WriteString(yaml)
	if err != nil {
		log.Fatalf("Failed to write to file: %v", err)
	}
}
