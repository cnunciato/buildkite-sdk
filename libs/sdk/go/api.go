package buildkite

import (
	"encoding/json"
)

type Pipeline struct {
	steps []Step
}

func (p *Pipeline) AddStep(step Step) {
	p.steps = append(p.steps, step)
}

func (p *Pipeline) ToJSON() (string, error) {
	data, err := json.Marshal(p.steps)
	if err != nil {
		return "", err
	}
	return string(data), nil
}
