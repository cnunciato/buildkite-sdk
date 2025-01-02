const fs = require("fs");

const {
    quicktype,
    InputData,
    JSONSchemaInput,
    TypeScriptTargetLanguage,
    PythonTargetLanguage,
    GoTargetLanguage,
    RubyTargetLanguage,
} = require("quicktype-core");

async function main() {
    const inputData = new InputData();

    const result = await fetch(
        "https://raw.githubusercontent.com/buildkite/pipeline-schema/refs/heads/main/schema.json"
    );

    const schema = await result.json();
    const source = {
        name: "schema",
        schema: JSON.stringify(schema),
    };

    await inputData.addSource(
        "schema",
        source,
        () => new JSONSchemaInput(undefined)
    );

    const typescript = new TypeScriptTargetLanguage(
        "TypeScript",
        ["typescript"],
        "ts"
    );
    const python = new PythonTargetLanguage("Python", ["python"], "py");
    const go = new GoTargetLanguage("Go", ["go"], "go");
    const ruby = new RubyTargetLanguage("Ruby", ["ruby"], "rb");

    const opts = {
        typescript: {
            path: "./sdk/typescript/src/schema.d.ts",
            options: undefined,
        },
        python: {
            path: "./sdk/python/src/buildkite_sdk/schema.py",
            options: undefined,
        },
        go: {
            path: "./sdk/go/sdk/buildkite/schema.go",
            options: { package: "buildkite" },
        },
        ruby: {
            path: "./sdk/ruby/lib/schema.rb",
            options: undefined,
        },
    };

    for await (lang of [typescript, python, go, ruby]) {
        const langOpts = opts[lang.name];
        let { lines } = await quicktype({
            lang,
            inputData,
            rendererOptions: langOpts.options,
        });

        // Go formatter seems a bit buggy.
        if (lang.name === "go") {
            lines = lines.map((line) => {
                if (line.match(/Command[s]?\W+\*Branches/)) {
                    return line.replace("*Branches    ", "*CommandUnion");
                }

                if (line.match(/ArtifactPaths\W+\*Branches/)) {
                    return line.replace("*Branches", "[]string ");
                }

                return line;
            });
        }

        fs.writeFileSync(langOpts.path, lines.join("\n"), "utf-8");
    }
}

main();
