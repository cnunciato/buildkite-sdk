# frozen_string_literal: true

RSpec.describe Buildkite do
  it "has a version number" do
    expect(Buildkite::VERSION).not_to be nil
  end

  it "does something useful" do
    pipeline = Buildkite::Pipeline.new
    pipeline.add_command_step({ label: "some-label", command: "echo 'Hello, World!'" })
    expect(pipeline.to_json).to eq("{\"steps\":[{\"label\":\"some-label\",\"command\":\"echo 'Hello, World!'\"}]}")
  end
end
