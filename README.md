# buildkite-sdk

[![Build status](https://badge.buildkite.com/a21842ec1f3c8f405b167966b2468ef995317dfe568836aa63.svg)](https://buildkite.com/nunciato/buildkite-sdk)

A multi-language SDK for [Buildkite](https://buildkite.com) managed with [Nx](https://nx.dev/). 🪁

Consumes the [Buildkite pipeline schema](https://github.com/buildkite/pipeline-schema) and generates packages for TypeScript, Python, Go, and Ruby!

## Prerequisites

For development, you'll need current versions of the following tools:

-   [Node.js](https://nodejs.org/en/download), [Python](https://www.python.org/downloads/), [Go](https://go.dev/doc/install), [Ruby](https://www.ruby-lang.org/en/documentation/installation/)
-   For Python: [uv](https://docs.astral.sh/uv/), [Black](https://black.readthedocs.io/en/stable/)
-   For Ruby: [Bundler](https://bundler.io/)

See `.tool-versions` for details. If you're on a Mac, and you use [Homebrew](https://brew.sh/), you can run `brew bundle` and `asdf install` to get all you need:

```bash
brew bundle
asdf install
```

If you hit any rough edges during development, please file an issue. Thanks!

### Useful commands

```bash
# Install dependencies.
npm install

# Test all SDKs and apps.
npm test

# Build all SDKs (and write them to ./dist/sdks).
npm run build

# Build all SDK docs (and write them to ./dist/docs).
npm run docs

# Serve the docs locally (which builds them implicitly).
npm run docs:serve

# Run all apps (which writes JSON and YAML pipelines to ./out).
npm run apps

# Watch all projects for changes (which rebuilds the docs and SDKs and re-runs all apps).
npm run watch

# Launch web servers for all docsets and watch all projects for changes. (Requires reload.)
npm run dev

# Format all SDK code.
npm run format

# Publish to npm, PyPi pkg.go.dev, and RubyGems.
npm run publish

# Clear away build and test artifacts.
npm run clean
```

## Installing and using the SDKs

The easiest way to use the SDK is to install the appropriate package for your language of choice, import the library into your program, assemble your pipeline steps programmatically, and serialize the pipeline to JSON or YAML, passing the output to `buildkite-agent pipeline upload`.

For example, if your language of choice were Ruby:

```bash
gem install cnunciato-buildkite
```

```ruby
# In ~/.buildkite/pipeline.rb:
require "buildkite"

pipeline = Buildkite::Pipeline.new

pipeline.add_command_step(
  label: "some-label",
  command: "echo 'Hello, World!'"
)

puts pipeline.to_json
```

```yaml
# In your pipeline's Settings > Steps:
steps:
    - label: ":pipeline: Generate pipeline"
      command: ruby .buildkite/pipeline.rb | buildkite-agent pipeline upload
```

This repository [uses this approach](./.buildkite/pipeline.rb) to ship the Buildkite SDK ... with the Buildkite SDK!

See below for more examples.

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

```bash
uv add cnunciato-buildkite-sdk
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

```bash
gem install cnunciato-buildkite
```

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

All SDKs version on the same cadence. To publish new versions of all SDKs, follow these steps:

1.  Commit all pending changes. We want the release commit to be "clean" (i.e., to consist only of changes related to the release itself.)

1.  Update the `FROM` and `TO` versions in the `release:all` task in [`./project.json`](./project.json).

1.  With that single change uncommitted, run the release script:

    ```bash
    npm run release
    ```

    This script:

    -   Updates the version numbers in all affected files
    -   Rebuilds all SDKs
    -   Commits all changes (e.g., to version files, lockfiles, and anything else under `./sdk`)
    -   Adds two new tags to mark the release (`v0.0.0` and `sdk/go/v0.0.0`)
    -   Pushes the commit and tags to GitHub, triggering the `publish` task
    -   Creates a new GitHub release

1.  Once the Buildkite job completes, verify the releases at their respective URLs:

    -   https://github.com/cnunciato/buildkite-sdk/releases
    -   https://www.npmjs.com/package/@cnunciato/buildkite-sdk
    -   https://pypi.org/project/cnunciato-buildkite-sdk/
    -   https://pkg.go.dev/github.com/cnunciato/buildkite-sdk/sdk/go (usually a slight delay)
    -   https://rubygems.org/gems/cnunciato-buildkite

### Required environment variables

The following environment variables are required for releasing and publishing:

-   `GITHUB_TOKEN` for creating GitHub releases
-   `NPM_TOKEN` for publishing to npm
-   `PYPI_TOKEN` fror publishing to PyPI
-   `RUBYGEMS_API_KEY` for publishing to RubyGems
