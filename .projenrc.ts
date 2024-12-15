import { cdk } from "projen";
import { TrailingComma } from "projen/lib/javascript";
import { ReleaseTrigger } from "projen/lib/release";

const project = new cdk.JsiiProject({
    majorVersion: 0,
    releaseTrigger: ReleaseTrigger.manual(),
    name: "@cnunciato/buildkite-sdk",
    author: "Christian Nunciato",
    authorAddress: "chris.nunciato@buildkite.com",
    repositoryUrl: "https://github.com/cnunciato/buildkite-sdk.git",
    defaultReleaseBranch: "main",
    jsiiVersion: "~5.5.0",
    projenrcTs: true,
    prettier: true,
    prettierOptions: {
        settings: {
            tabWidth: 4,
            singleQuote: false,
            trailingComma: TrailingComma.ALL,
        },
        ignoreFileOptions: {
            ignorePatterns: [
                ".projen/",
                ".github/",
                ".eslintrc.json",
                ".mergify.yml",
                ".prettierrc.json",
                "tsconfig.dev.json",
            ],
        },
    },
    vscode: true,
    publishToPypi: {
        distName: "buildkite-sdk",
        module: "buildkite_sdk",
    },
    publishToGo: {
        moduleName: "github.com/cnunciato/buildkite-sdk",
        packageName: "buildkitesdk",
    },
    publishToNuget: {
        dotNetNamespace: "Buildkite.SDK",
        packageId: "Buildkite.SDK",
    },
    deps: [],
    devDeps: ["publib", "json-schema-to-typescript"],
});

project.setScript(
    "generate",
    "curl -fs https://raw.githubusercontent.com/buildkite/pipeline-schema/refs/heads/main/schema.json -o ./schema.json && npx json2ts ./schema.json > ./src/types.d.ts",
);

project.vscode?.settings.addSettings({
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,

    "explorer.excludeGitIgnore": true,

    "files.trimTrailingWhitespace": true,
    "files.trimFinalNewlines": true,
    "files.insertFinalNewline": true,

    "prettier.configPath": "./.prettierrc.json",
    "prettier.documentSelectors": ["**/*.{ts,js,cjs,mjs,json,md,svg}"],
});

project.synth();
