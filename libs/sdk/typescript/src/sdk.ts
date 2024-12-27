import * as yaml from "yaml";
import * as schema from "./schema";

type PipelineStep =
    | schema.CommandStep
    | schema.WaitStep
    | schema.InputStep
    | schema.TriggerStep
    | schema.GroupStep;

export class Pipeline {
    private steps: PipelineStep[] = [];

    constructor() {
        this.steps = [];
    }

    addStep(step: PipelineStep) {
        this.steps.push(step);
        return this;
    }

    toJSON() {
        return JSON.stringify(
            {
                steps: this.steps,
            },
            null,
            4
        );
    }

    toYAML() {
        return yaml.stringify({
            steps: this.steps,
        });
    }
}
