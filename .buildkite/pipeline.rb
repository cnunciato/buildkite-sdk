require_relative("../sdk/ruby/lib/buildkite.rb")
require_relative("../sdk/ruby/lib/environment.rb")

pipeline = Buildkite::Pipeline.new
tag = ENV[Environment::BUILDKITE_TAG]

commands = [
  "npm test",
  "npm run build",
  "echo '#{Environment::BUILDKITE_TAG}'",
  "echo '#{tag}'"
]

if not tag.nil? and not tag == ""
  commands.push("npm run publish")
end

pipeline.add_command_step(
  label: ":hammer_and_wrench: Install, test, and build",
  commands: commands
)

puts pipeline.to_json
