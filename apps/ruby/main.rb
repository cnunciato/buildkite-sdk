require "buildkite"

pipeline = Buildkite::Pipeline.new
pipeline.add_command_step({ label: "some-label", command: "echo 'Hello, World!'" })

puts pipeline.to_json
puts pipeline.to_yaml
