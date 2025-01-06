require_relative("../sdk/ruby/lib/buildkite.rb")

pipeline = Buildkite::Pipeline.new
pipeline.add_command_step(
  label: ":hammer_and_wrench: Install, test, and build",
  commands: [
    "npm test",
    "npm run build"
  ]
)

if Environment::BUILDKITE_TAG != ""
  puts "Triggered by tag: #{Environment::BUILDKITE_TAG.sub("v", "")}"
end

puts pipeline.to_json
