import { cdk } from "projen";
import { TrailingComma } from "projen/lib/javascript";

const project = new cdk.JsiiProject({
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
        packageName: "buildkite-sdk",
    },
    deps: [],
    devDeps: ["publib"],
});

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
