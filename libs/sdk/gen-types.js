const fs = require("fs");

const {
    quicktype,
    InputData,
    JSONSchemaInput,
    TypeScriptTargetLanguage,
    PythonTargetLanguage,
    GoTargetLanguage,
} = require("quicktype-core");

async function main() {
    const inputData = new InputData();
    // const source = {
    //     name: "schema",
    //     schema: fs.readFileSync("./libs/sdk/schema.json", "utf8"),
    // };

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

    const opts = {
        typescript: {
            path: "./libs/sdk/typescript/src/schema.d.ts",
            options: undefined,
        },
        python: {
            path: "./libs/sdk/python/src/buildkite_sdk/schema.py",
            options: undefined,
        },
        go: {
            path: "./libs/sdk/go/pkg/buildkite/schema.go",
            options: { package: "buildkite" },
        },
    };

    for await (lang of [typescript, python, go]) {
        const langOpts = opts[lang.name];
        const { lines } = await quicktype({
            lang,
            inputData,
            rendererOptions: langOpts.options,
        });
        fs.writeFileSync(langOpts.path, lines.join("\n"), "utf-8");
    }
}

main();
