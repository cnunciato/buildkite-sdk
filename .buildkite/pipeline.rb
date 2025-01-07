require_relative("../sdk/ruby/lib/buildkite")
require_relative("../sdk/ruby/lib/environment")

pipeline = Buildkite::Pipeline.new

%w[test build apps].each do |task|
  pipeline.add_step(
    id: task,
    label: ":hammer_and_wrench: #{task}",
    command: "npm run #{task}"
  )
end

tag = ENV[Environment::BUILDKITE_TAG]
if !tag.nil? and tag.start_with?("v")
  pipeline.add_step(
    label: ":rocket: Publish",
    command: "npm run publish",
    depends_on: "build"
  )
end

puts pipeline.to_json
