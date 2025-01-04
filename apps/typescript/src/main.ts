import { Pipeline, Environment, environmentVariables } from "@cnunciato/buildkite-sdk";

const pipeline = new Pipeline();

pipeline.addStep({
    label: "some-label",
    command: "echo 'Hello, world!'",
});

console.log(Environment.get(environmentVariables.Environment.BUILDKITE_AGENT_EXPERIMENT))

console.log(pipeline.toJSON());
