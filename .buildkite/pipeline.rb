require_relative("../sdk/ruby/lib/buildkite.rb")
require_relative("../sdk/ruby/lib/environment.rb")

pipeline = Buildkite::Pipeline.new
tag = ENV[Environment::BUILDKITE_TAG]

commands = [
  "npm test",
  "npm run build",
]

# We create two tags, which results in two webhooks from GitHub.
# Since we need the Go SDK's tag to be in place when we make the
# call to pkg.go.dev, we run the build task on that one.
if not tag.nil? and tag.start_with?("sdk/go/v")
  commands.push("npm run publish")
end

pipeline.add_command_step(
  label: ":hammer_and_wrench: Install, test, and build",
  commands: commands
)

puts pipeline.to_json
