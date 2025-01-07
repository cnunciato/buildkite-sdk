require_relative("../sdk/ruby/lib/buildkite")
require_relative("../sdk/ruby/lib/environment")

pipeline = Buildkite::Pipeline.new
tag = ENV[Environment::BUILDKITE_TAG]

commands = [
  "npm test",
  "npm run build",
  "npm run docs",
  "npm run apps"
]

commands.push("npm run publish") if !tag.nil? and tag.start_with?("v")

pipeline.add_step(
  label: ":hammer_and_wrench: Install, test, build, publish",
  commands: commands
)

puts pipeline.to_json
