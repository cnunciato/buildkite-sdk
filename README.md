# buildkite-sdk

A multi-language SDK for [Buildkite](https://buildkite.com) managed with [Nx](https://nx.dev/). 🪁

Generates packages in JS/TS, Python, Go.

```bash
# Install dependencies.
npm install

# Test.
npx nx test:all

# Build.
npx nx build:all

# Publish to npm, PyPi and pkg.go.dev.
npx nx publish:all
```

## Try it out

```bash
npm install @cnunciato/buildkite-sdk
```

```typescript
import { Pipeline } from "@cnunciato/buildkite-sdk";

const pipeline = new Pipeline();

pipeline.addStep({
    command: "echo 'Hello, world!'",
});

console.log(pipeline.toJSON());
```

```python
from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_command_step({"command": "echo 'Hello, world!'"})
return

print(pipeline.to_json())
print(pipeline.to_yaml())
```

```go
package main

import (
	"fmt"
	"github.com/cnunciato/buildkite-sdk/libs/sdk/go/sdk/buildkite"
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
}
```
