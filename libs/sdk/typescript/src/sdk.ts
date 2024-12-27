import * as yaml from "yaml";
import * as schema from "./schema";

type Step =
    | schema.CommandStep
    | schema.WaitStep
    | schema.InputStep
    | schema.TriggerStep
    | schema.GroupStepClass;

export class Pipeline {
    private steps: Step[] = [];

    constructor() {
        this.steps = [];
    }

    addStep(step: Step) {
        this.steps.push(step);
        return this;
    }

    addSteps(steps: Step[]) {
        this.steps.push(...steps);
        return this;
    }

    toJSON() {
        return JSON.stringify(this.steps, null, 4);
    }

    toYAML() {
        return yaml.stringify(this.steps);
    }
}
