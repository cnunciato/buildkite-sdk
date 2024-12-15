import { BlockStep, CommandStep } from "./types";

export class StepBuilder {
    public steps: (BlockStep | CommandStep)[] = [];

    public addStep(step: BlockStep | CommandStep) {
        this.steps.push(step);
    }

    public toJSON() {
        return JSON.stringify({ steps: this.steps }, null, 4);
    }
}

export default StepBuilder;
