import * as buildkite from "../src";

test("pipeline", () => {
    const pipeline = new buildkite.StepBuilder();

    pipeline.addStep({
        type: "command",
        command: "echo 'Hello, world!'",
    });

    pipeline.addStep({
        type: "block",
        prompt: "Continue?",
    });

    expect(pipeline.toJSON()).toBeTruthy;
});
