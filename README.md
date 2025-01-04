# buildkite-sdk

[![Build status](https://badge.buildkite.com/a21842ec1f3c8f405b167966b2468ef995317dfe568836aa63.svg)](https://buildkite.com/nunciato/buildkite-sdk)

A multi-language SDK for [Buildkite](https://buildkite.com) managed with [Nx](https://nx.dev/). 🪁

Consumes the [Buildkite pipeline schema](https://github.com/buildkite/pipeline-schema) and generates packages for TypeScript, Python, Go, and Ruby!

## Prerequisites

-   Node.js, Python, Ruby, Go
-   For Python: [uv](https://docs.astral.sh/uv/), [Black](https://black.readthedocs.io/en/stable/)
-   For Ruby: [Bundler](https://bundler.io/)

See `.tool-versions` for the versions currently in use. If you're on a Mac and use [Homebrew](https://brew.sh/), you can run:

```bash
brew bundle
asdf install
```

.. to get all you need. (If you don't, please file an issue!)

```bash
# Install dependencies.
npm install

# Test all SDKs and apps.
npm test

# Build  (to dist/sdk).
npm run build

# Build the docs (to dist/docs).
npm run docs

# Serve the docs locally (which builds them implicitly, but doesn't yet watch).
npm run docs:serve

# Run all apps (e.g., to use the SDKs to generate pipelines).
npm start

# Publish to npm, PyPi pkg.go.dev, and RubyGems.
npm run publish
```

## Usage

### Node.js

```bash
npm install @cnunciato/buildkite-sdk
```

```javascript
const { Pipeline } = require("@cnunciato/buildkite-sdk");

const pipeline = new Pipeline();

pipeline.addStep({
    command: "echo 'Hello, world!'",
});

console.log(pipeline.toJSON());
console.log(pipeline.toYAML());
```

### Python

Currently publishing to TestPyPI (to leave `buildkite-sdk` unclaimed).

```bash
uv add buildkite-sdk --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple
```

```python
from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_command_step({"command": "echo 'Hello, world!'"})

print(pipeline.to_json())
print(pipeline.to_yaml())
```

### Go

```bash
go get github.com/cnunciato/buildkite-sdk/sdk/go
```

```go
package main

import (
	"fmt"
	"github.com/cnunciato/buildkite-sdk/sdk/go/sdk/buildkite"
)

func main() {
	pipeline := buildkite.Pipeline{}
	command := "echo 'Hello, world!"

	pipeline.AddCommandStep(buildkite.CommandStep{
		Command: &buildkite.CommandUnion{
			String: &command,
		},
	})

	fmt.Println(pipeline.ToJSON())
	fmt.Println(pipeline.ToYAML())
}
```

### Ruby

Still working on this one, so it's not yet publishing to RubyGems.

```ruby
require "buildkite"

pipeline = Buildkite::Pipeline.new
pipeline.add_command_step(
  label: "some-label",
  command: "echo 'Hello, World!'"
)

puts pipeline.to_json
puts pipeline.to_yaml
```

## Publishing new versions

All SDKs version on the same cadence, and the versioning and publishing are still done manually. To upgrade all SDKs from `0.0.1` to `0.0.2`, for example, follow these steps:

-   Bump the version numbers in these files to `0.0.2`:
    -   `sdk/go/project.json`
    -   `sdk/python/pyproject.toml`
    -   `sdk/typescript/package.json`
    -   `sdk/ruby/lib/buildkite/version.rb`
-   Commit those changes with a message like `Release v0.0.2`
-   Tag thusly: `git tag v0.0.2 && git tag sdk/go/v0.0.2`
-   Push the commit and the tags to `main`: `git push origin main --tags`
-   Run `npm run publish`
