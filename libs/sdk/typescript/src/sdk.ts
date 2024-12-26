import * as schema from './schema';

export class StepBuilder {
    private steps: schema.Step[] = [];

    constructor() {
        this.steps = [];
    }

    add(step: schema.Step) {
        this.steps.push(step);
    }

    toJSON() {
        return JSON.stringify(this.steps, null, 4);
    }
}
