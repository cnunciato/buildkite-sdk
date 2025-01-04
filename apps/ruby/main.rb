require "buildkite"

pipeline = Buildkite::Pipeline.new
pipeline.add_command_step({ label: "some-label", command: "echo 'Hello, World!'" })

FileUtils.makedirs("../../out/apps/ruby")
File.write("../../out/apps/ruby/pipeline.json", pipeline.to_json)
