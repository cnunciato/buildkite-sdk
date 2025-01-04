# frozen_string_literal: true

require_relative "buildkite/version"
require_relative "schema"
require_relative "environment"
require "json"
require "yaml"

module Buildkite
  class Error < StandardError; end

  class Pipeline

    def initialize
      @steps = []
    end

    def add_command_step(step)
      @steps << step
      self
    end

    def to_json
      JSON.generate({ steps: @steps })
    end

    def to_yaml
      { steps: @steps }.to_yaml
    end
  end
end
