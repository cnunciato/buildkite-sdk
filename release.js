const [from, to] = [process.argv[2], process.argv[3]];

if (!from || !to) {
    console.error(`Invalid 'from' or 'to' version: '${from}', '${to}'`);
    process.exit(1);
}

(async () => {
    const { replaceInFileSync } = await import("replace-in-file");
    const { simpleGit } = await import("simple-git");
    const { execSync } = await import("child_process");

    const paths = [
        "sdk/go/project.json",
        "sdk/python/pyproject.toml",
        "sdk/typescript/package.json",
        "sdk/ruby/lib/buildkite/version.rb",
    ];

    // Bump versions.
    replaceInFileSync({
        files: paths,
        from,
        to,
    });

    // Build.
    execSync("npm run build", { stdio: "inherit" });

    // Commit and tag.
    simpleGit().add("sdk"); // Include everything here, as lockfiles will also have changed.
    simpleGit().commit(`Release v${to}`);
    simpleGit().addTag(`v${to}`);
    simpleGit().addTag(`sdk/go/v${to}`);
})();
