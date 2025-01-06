const [from, to] = [process.argv[2], process.argv[3]];

if (!from || !to) {
    console.error(`Invalid 'from' or 'to' version: '${from}', '${to}'`);
    process.exit(1);
}

(async () => {
    const { replaceInFileSync } = await import("replace-in-file");
    const { simpleGit } = await import("simple-git");
    const { execSync } = await import("child_process");
    const { Octokit } = await import("@octokit/rest");

    const paths = [
        "sdk/go/project.json",
        "sdk/python/pyproject.toml",
        "sdk/typescript/package.json",
        "sdk/ruby/lib/buildkite/version.rb",
        "sdk/ruby/project.json",
    ];

    // Bump versions.
    replaceInFileSync({
        files: paths,
        from,
        to,
    });

    // Build all SDKs.
    execSync("npm run build", { stdio: "inherit" });

    // Commit and tag.
    const git = simpleGit();
    await git.add("sdk"); // Include everything here, as lockfiles will also have changed.
    await git.add("project.json"); // As this contains the new version.
    await git.commit(`Release v${to}`);
    await git.addTag(`v${to}`);
    await git.addTag(`sdk/go/v${to}`);

    // Push the commit and tags. This is what triggers publishing.
    await git.push("origin", "main", { "--tags": true });

    // Auth with GitHub.
    const octokit = new Octokit({
        auth: process.env.GITHUB_TOKEN,
    });

    // Create a GitHub release.
    const response = await octokit.rest.repos.createRelease({
        owner: "cnunciato",
        repo: "buildkite-sdk",
        tag_name: `v${to}`,
        name: `Release v${to}`,
        body: [
            `* https://www.npmjs.com/package/@cnunciato/buildkite-sdk/v/${to}`,
            `* https://pypi.org/project/cnunciato-buildkite-sdk/${to}/`,
            `* https://pkg.go.dev/github.com/cnunciato/buildkite-sdk/sdk/go@v${to}`,
            `* https://rubygems.org/gems/cnunciato-buildkite/versions/${to}`,
        ].join("\n"),
        draft: false,
        prerelease: false,
    });

    console.log("Release created successfully:", response.data.html_url);
})();
