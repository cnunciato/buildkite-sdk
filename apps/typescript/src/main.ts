import { Pipeline } from "@buildkite/buildkite-sdk";

const pipeline = new Pipeline();

pipeline.addSteps([
    {
        command: "echo 'Hello, world!'",
    },
    {
        command: "echo 'Bonjour!'",
    },
]);

console.log(pipeline.toJSON());
console.log(pipeline.toYAML());
