package buildkite

import (
	"encoding/json"

	"gopkg.in/yaml.v3"
)

type Pipeline struct {
	Steps []CommandStep
}

func (p *Pipeline) AddCommandStep(step CommandStep) {
	p.Steps = append(p.Steps, step)
}

func (p *Pipeline) ToJSON() (string, error) {
	data, err := json.Marshal(p.Steps)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func (p *Pipeline) ToYAML() (string, error) {
	data, err := yaml.Marshal(p.Steps)
	if err != nil {
		return "", err
	}
	return string(data), nil
}
