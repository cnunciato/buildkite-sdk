# buildkite-sdk

Testing out using [projen](https://projen.io/) and [jsii](https://aws.github.io/jsii/) to generate a multi-language SDK for [Buildkite](https://buildkite.com). 🪁

Source in `./src`. Generates packages in JS/TS, Python, Go.

```bash
# Install dependencies.
npm install

# Build.
npm run build

# Test.
npm test

# Generate all packages. Writes to ./dist.
npm run package-all

# Bump the version.
git tag v0.0.x
npm run bump

# Generate a release. (Requires a clean working directory.)
npm run release

# Publish to npm.
NPM_TOKEN="${your_token}" npx publib
```

## Try it out

```bash
npm install @cnunciato/buildkite-sdk
```

```typescript
// index.js
const buildkite = require("@cnunciato/buildkite-sdk");

const pipeline = new buildkite.StepBuilder();

pipeline.addCommandStep({
    commands: ["echo 'Hello, world!'"],
});

pipeline.write();
```
