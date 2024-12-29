import { Pipeline } from "@buildkite/buildkite-sdk";

const pipeline = new Pipeline();

pipeline.addStep({
    label: "some-label",
    command: "echo 'Hello, world!'",
});

console.log(pipeline.toJSON());
