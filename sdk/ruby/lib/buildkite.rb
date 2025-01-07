require_relative "buildkite/version"
# require_relative "schema"
require_relative "environment"
require "json"
require "yaml"

module Buildkite
  class Error < StandardError; end

  # Here is a comment.
  class Pipeline
    def initialize
      @steps = []
    end

    # Reverses the contents of a String or IO object.
    #
    # @param contents [String, #read] the contents to reverse
    # @return [String] the contents reversed lexically
    def add_command_step(step)
      @steps << step
      self
    end

    def to_json(*_args)
      JSON.pretty_generate({ steps: @steps }, indent: "    ")
    end

    def to_yaml
      { steps: @steps }.to_yaml
    end
  end
end
