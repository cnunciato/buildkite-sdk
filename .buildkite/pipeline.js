const buildkite = require("@cnunciato/buildkite-sdk");

const pipeline = new buildkite.Pipeline();

pipeline.addStep({
    commands: [
        "npm install",
        "npx nx test:all",
        "npx nx build:all",
        "npx nx publish:all",
    ],
});

console.log(pipeline.toJSON());
