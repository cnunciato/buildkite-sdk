from enum import Enum

class Environment(Enum):
    # Always &#x60;true&#x60;
    BUILDKITE = "BUILDKITE"
    # The agent session token for the job. The variable is read by the agent &#x60;artifact&#x60; and &#x60;meta-data&#x60; commands.
    BUILDKITE_AGENT_ACCESS_TOKEN = "BUILDKITE_AGENT_ACCESS_TOKEN"
    # The value of the &#x60;debug&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_AGENT_DEBUG = "BUILDKITE_AGENT_DEBUG"
    # The value of the &#x60;disconnect-after-job&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_AGENT_DISCONNECT_AFTER_JOB = "BUILDKITE_AGENT_DISCONNECT_AFTER_JOB"
    # The value of the &#x60;disconnect-after-idle-timeout&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_AGENT_DISCONNECT_AFTER_IDLE_TIMEOUT = "BUILDKITE_AGENT_DISCONNECT_AFTER_IDLE_TIMEOUT"
    # The value of the &#x60;endpoint&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration). This is set as an environment variable by the bootstrap and then read by most of the &#x60;buildkite-agent&#x60; commands.
    BUILDKITE_AGENT_ENDPOINT = "BUILDKITE_AGENT_ENDPOINT"
    # A list of the [experimental agent features](&#x2F;docs&#x2F;agent&#x2F;v3#experimental-features) that are currently enabled. The value can be set using the &#x60;--experiment&#x60; flag on the [&#x60;buildkite-agent start&#x60; command](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;cli-start#starting-an-agent) or in your [agent configuration file](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_AGENT_EXPERIMENT = "BUILDKITE_AGENT_EXPERIMENT"
    # The value of the &#x60;health-check-addr&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_AGENT_HEALTH_CHECK_ADDR = "BUILDKITE_AGENT_HEALTH_CHECK_ADDR"
    # The UUID of the agent.
    BUILDKITE_AGENT_ID = "BUILDKITE_AGENT_ID"
    # The value of each [agent tag](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;cli-start#setting-tags). The tag name is appended to the end of the variable name. They can be set using the &#x60;--tags&#x60; flag on the &#x60;buildkite-agent start&#x60; command, or in the [agent configuration file](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration). The [Queue tag](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;queues) is specifically used for isolating jobs and agents, and appears as the &#x60;BUILDKITE_AGENT_META_DATA_QUEUE&#x60; environment variable.
    BUILDKITE_AGENT_META_DATA_ = "BUILDKITE_AGENT_META_DATA_"
    # The name of the agent that ran the job.
    BUILDKITE_AGENT_NAME = "BUILDKITE_AGENT_NAME"
    # The process ID of the agent.
    BUILDKITE_AGENT_PID = "BUILDKITE_AGENT_PID"
    # The artifact paths to upload after the job, if any have been specified. The value can be modified by exporting the environment variable in the &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks.
    BUILDKITE_ARTIFACT_PATHS = "BUILDKITE_ARTIFACT_PATHS"
    # The path where artifacts will be uploaded. This variable is read by the &#x60;buildkite-agent artifact upload&#x60; command, and during the artifact upload phase of [command steps](&#x2F;docs&#x2F;pipelines&#x2F;command-step#command-step-attributes). It can only be set by exporting the environment variable in the &#x60;environment&#x60;, &#x60;pre-checkout&#x60; or &#x60;pre-command&#x60; hooks.
    BUILDKITE_ARTIFACT_UPLOAD_DESTINATION = "BUILDKITE_ARTIFACT_UPLOAD_DESTINATION"
    # The path to the directory containing the &#x60;buildkite-agent&#x60; binary.
    BUILDKITE_BIN_PATH = "BUILDKITE_BIN_PATH"
    # The branch being built. Note that for manually triggered builds, this branch is not guaranteed to contain the commit specified by &#x60;BUILDKITE_COMMIT&#x60;.
    BUILDKITE_BRANCH = "BUILDKITE_BRANCH"
    # The path where the agent has checked out your code for this build. This variable is read by the bootstrap when the agent is started, and can only be set by exporting the environment variable in the &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks.
    BUILDKITE_BUILD_CHECKOUT_PATH = "BUILDKITE_BUILD_CHECKOUT_PATH"
    # The name of the user who authored the commit being built. May be **[unverified](#unverified-commits)**. This value can be blank in some situations, including builds manually triggered using API or Buildkite web interface.
    BUILDKITE_BUILD_AUTHOR = "BUILDKITE_BUILD_AUTHOR"
    # The notification email of the user who authored the commit being built. May be **[unverified](#unverified-commits)**. This value can be blank in some situations, including builds manually triggered using API or Buildkite web interface.
    BUILDKITE_BUILD_AUTHOR_EMAIL = "BUILDKITE_BUILD_AUTHOR_EMAIL"
    # The name of the user who created the build. The value differs depending on how the build was created:
# 
# - **Buildkite dashboard:** Set based on who manually created the build.
# - **GitHub webhook:** Set from the  **[unverified](#unverified-commits)** HEAD commit.
# - **Webhook:** Set based on which user is attached to the API Key used.
    BUILDKITE_BUILD_CREATOR = "BUILDKITE_BUILD_CREATOR"
    # The notification email of the user who created the build. The value differs depending on how the build was created:
# 
# - **Buildkite dashboard:** Set based on who manually created the build.
# - **GitHub webhook:** Set from the  **[unverified](#unverified-commits)** HEAD commit.
# - **Webhook:** Set based on which user is attached to the API Key used.
    BUILDKITE_BUILD_CREATOR_EMAIL = "BUILDKITE_BUILD_CREATOR_EMAIL"
    # A colon separated list of non-private team slugs that the build creator belongs to. The value differs depending on how the build was created:
# 
# - **Buildkite dashboard:** Set based on who manually created the build.
# - **GitHub webhook:** Set from the  **[unverified](#unverified-commits)** HEAD commit.
# - **Webhook:** Set based on which user is attached to the API Key used.
    BUILDKITE_BUILD_CREATOR_TEAMS = "BUILDKITE_BUILD_CREATOR_TEAMS"
    # The UUID of the build.
    BUILDKITE_BUILD_ID = "BUILDKITE_BUILD_ID"
    # The build number. This number increases with every build, and is guaranteed to be unique within each pipeline.
    BUILDKITE_BUILD_NUMBER = "BUILDKITE_BUILD_NUMBER"
    # The value of the &#x60;build-path&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_BUILD_PATH = "BUILDKITE_BUILD_PATH"
    # The url for this build on Buildkite.
    BUILDKITE_BUILD_URL = "BUILDKITE_BUILD_URL"
    # The value of the &#x60;cancel-grace-period&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration) in seconds.
    BUILDKITE_CANCEL_GRACE_PERIOD = "BUILDKITE_CANCEL_GRACE_PERIOD"
    # The value of the &#x60;cancel-signal&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration). The value can be modified by exporting the environment variable in the &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks.
    BUILDKITE_CANCEL_SIGNAL = "BUILDKITE_CANCEL_SIGNAL"
    # Whether the build should perform a clean checkout. The variable is read during the default checkout phase of the bootstrap and can be overridden in &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks.
    BUILDKITE_CLEAN_CHECKOUT = "BUILDKITE_CLEAN_CHECKOUT"
    # The UUID value of the cluster, but only if the build has an associated &#x60;cluster_queue&#x60;. Otherwise, this environment variable is not set.
    BUILDKITE_CLUSTER_ID = "BUILDKITE_CLUSTER_ID"
    # The command that will be run for the job.
    BUILDKITE_COMMAND = "BUILDKITE_COMMAND"
    # The opposite of the value of the &#x60;no-command-eval&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_COMMAND_EVAL = "BUILDKITE_COMMAND_EVAL"
    # The exit code from the last command run in the command hook.
    BUILDKITE_COMMAND_EXIT_STATUS = "BUILDKITE_COMMAND_EXIT_STATUS"
    # The git commit object of the build. This is usually a 40-byte hexadecimal SHA-1 hash, but can also be a symbolic name like &#x60;HEAD&#x60;.
    BUILDKITE_COMMIT = "BUILDKITE_COMMIT"
    # The path to the agent config file.
    BUILDKITE_CONFIG_PATH = "BUILDKITE_CONFIG_PATH"
    # The path to the file containing the job&#39;s environment variables.
    BUILDKITE_ENV_FILE = "BUILDKITE_ENV_FILE"
    # The value of the &#x60;git-clean-flags&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration). The value can be modified by exporting the environment variable in the &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks.
    BUILDKITE_GIT_CLEAN_FLAGS = "BUILDKITE_GIT_CLEAN_FLAGS"
    # The value of the &#x60;git-clone-flags&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration). The value can be modified by exporting the environment variable in the &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks.
    BUILDKITE_GIT_CLONE_FLAGS = "BUILDKITE_GIT_CLONE_FLAGS"
    # The opposite of the value of the &#x60;no-git-submodules&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_GIT_SUBMODULES = "BUILDKITE_GIT_SUBMODULES"
    # The GitHub deployment ID. Only available on builds triggered by a [GitHub Deployment](https:&#x2F;&#x2F;developer.github.com&#x2F;v3&#x2F;repos&#x2F;deployments&#x2F;).
    BUILDKITE_GITHUB_DEPLOYMENT_ID = "BUILDKITE_GITHUB_DEPLOYMENT_ID"
    # The name of the GitHub deployment environment. Only available on builds triggered by a [GitHub Deployment](https:&#x2F;&#x2F;developer.github.com&#x2F;v3&#x2F;repos&#x2F;deployments&#x2F;).
    BUILDKITE_GITHUB_DEPLOYMENT_ENVIRONMENT = "BUILDKITE_GITHUB_DEPLOYMENT_ENVIRONMENT"
    # The name of the GitHub deployment task. Only available on builds triggered by a [GitHub Deployment](https:&#x2F;&#x2F;developer.github.com&#x2F;v3&#x2F;repos&#x2F;deployments&#x2F;).
    BUILDKITE_GITHUB_DEPLOYMENT_TASK = "BUILDKITE_GITHUB_DEPLOYMENT_TASK"
    # The GitHub deployment payload data as serialized JSON. Only available on builds triggered by a [GitHub Deployment](https:&#x2F;&#x2F;developer.github.com&#x2F;v3&#x2F;repos&#x2F;deployments&#x2F;).
    BUILDKITE_GITHUB_DEPLOYMENT_PAYLOAD = "BUILDKITE_GITHUB_DEPLOYMENT_PAYLOAD"
    # The UUID of the [group step](&#x2F;docs&#x2F;pipelines&#x2F;group-step) the job belongs to. This variable is only available if the job belongs to a group step.
    BUILDKITE_GROUP_ID = "BUILDKITE_GROUP_ID"
    # The value of the &#x60;key&#x60; attribute of the [group step](&#x2F;docs&#x2F;pipelines&#x2F;group-step) the job belongs to. This variable is only available if the job belongs to a group step.
    BUILDKITE_GROUP_KEY = "BUILDKITE_GROUP_KEY"
    # The label&#x2F;name of the [group step](&#x2F;docs&#x2F;pipelines&#x2F;group-step) the job belongs to. This variable is only available if the job belongs to a group step.
    BUILDKITE_GROUP_LABEL = "BUILDKITE_GROUP_LABEL"
    # The value of the &#x60;hooks-path&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_HOOKS_PATH = "BUILDKITE_HOOKS_PATH"
    # A list of environment variables that have been set in your pipeline that are protected and will be overridden, used internally to pass data from the bootstrap to the agent.
    BUILDKITE_IGNORED_ENV = "BUILDKITE_IGNORED_ENV"
    # The internal UUID Buildkite uses for this job.
    BUILDKITE_JOB_ID = "BUILDKITE_JOB_ID"
    # The path to a temporary file containing the logs for this job. Requires enabling the &#x60;enable-job-log-tmpfile&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_JOB_LOG_TMPFILE = "BUILDKITE_JOB_LOG_TMPFILE"
    # The label&#x2F;name of the current job.
    BUILDKITE_LABEL = "BUILDKITE_LABEL"
    # The exit code of the last hook that ran, used internally by the hooks.
    BUILDKITE_LAST_HOOK_EXIT_STATUS = "BUILDKITE_LAST_HOOK_EXIT_STATUS"
    # The opposite of the value of the &#x60;no-local-hooks&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_LOCAL_HOOKS_ENABLED = "BUILDKITE_LOCAL_HOOKS_ENABLED"
    # The message associated with the build, usually the commit message or the message provided when the build is triggered. The value is empty when a message is not set. For example, when a user triggers a build from the Buildkite dashboard without entering a message, the variable returns an empty value.
    BUILDKITE_MESSAGE = "BUILDKITE_MESSAGE"
    # The UUID of the organization.
    BUILDKITE_ORGANIZATION_ID = "BUILDKITE_ORGANIZATION_ID"
    # The organization name on Buildkite as used in URLs.
    BUILDKITE_ORGANIZATION_SLUG = "BUILDKITE_ORGANIZATION_SLUG"
    # The index of each parallel job created from a parallel build step, starting from 0. For a build step with &#x60;parallelism: 5&#x60;, the value would be 0, 1, 2, 3, and 4 respectively.
    BUILDKITE_PARALLEL_JOB = "BUILDKITE_PARALLEL_JOB"
    # The total number of parallel jobs created from a parallel build step. For a build step with &#x60;parallelism: 5&#x60;, the value is 5.
    BUILDKITE_PARALLEL_JOB_COUNT = "BUILDKITE_PARALLEL_JOB_COUNT"
    # The default branch for this pipeline.
    BUILDKITE_PIPELINE_DEFAULT_BRANCH = "BUILDKITE_PIPELINE_DEFAULT_BRANCH"
    # The UUID of the pipeline.
    BUILDKITE_PIPELINE_ID = "BUILDKITE_PIPELINE_ID"
    # The displayed pipeline name on Buildkite.
    BUILDKITE_PIPELINE_NAME = "BUILDKITE_PIPELINE_NAME"
    # The ID of the source code provider for the pipeline&#39;s repository.
    BUILDKITE_PIPELINE_PROVIDER = "BUILDKITE_PIPELINE_PROVIDER"
    # The pipeline slug on Buildkite as used in URLs.
    BUILDKITE_PIPELINE_SLUG = "BUILDKITE_PIPELINE_SLUG"
    # A colon separated list of the pipeline&#39;s non-private team slugs.
    BUILDKITE_PIPELINE_TEAMS = "BUILDKITE_PIPELINE_TEAMS"
    # A JSON string holding the current plugin&#39;s configuration (as opposed to all the plugin configurations in the &#x60;BUILDKITE_PLUGINS&#x60; environment variable).
    BUILDKITE_PLUGIN_CONFIGURATION = "BUILDKITE_PLUGIN_CONFIGURATION"
    # The current plugin&#39;s name, with all letters in uppercase and any spaces replaced with underscores.
    BUILDKITE_PLUGIN_NAME = "BUILDKITE_PLUGIN_NAME"
    # A JSON object containing a list plugins used in the step, and their configuration.
    BUILDKITE_PLUGINS = "BUILDKITE_PLUGINS"
    # The opposite of the value of the &#x60;no-plugins&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_PLUGINS_ENABLED = "BUILDKITE_PLUGINS_ENABLED"
    # The value of the &#x60;plugins-path&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_PLUGINS_PATH = "BUILDKITE_PLUGINS_PATH"
    # Whether to validate plugin configuration and requirements. The value can be modified by exporting the environment variable in the &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks, or in a &#x60;pipeline.yml&#x60; file. It can also be enabled using the &#x60;no-plugin-validation&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_PLUGIN_VALIDATION = "BUILDKITE_PLUGIN_VALIDATION"
    # The number of the pull request or &#x60;false&#x60; if not a pull request.
    BUILDKITE_PULL_REQUEST = "BUILDKITE_PULL_REQUEST"
    # The base branch that the pull request is targeting or &#x60;&quot;&quot;&#x60; if not a pull request.&#x60;
    BUILDKITE_PULL_REQUEST_BASE_BRANCH = "BUILDKITE_PULL_REQUEST_BASE_BRANCH"
    # Set to &#x60;true&#x60; when the pull request is a draft. This variable is only available if a build contains a draft pull request.
    BUILDKITE_PULL_REQUEST_DRAFT = "BUILDKITE_PULL_REQUEST_DRAFT"
    # The repository URL of the pull request or &#x60;&quot;&quot;&#x60; if not a pull request.
    BUILDKITE_PULL_REQUEST_REPO = "BUILDKITE_PULL_REQUEST_REPO"
    # The UUID of the original build this was rebuilt from or &#x60;&quot;&quot;&#x60; if not a rebuild.
    BUILDKITE_REBUILT_FROM_BUILD_ID = "BUILDKITE_REBUILT_FROM_BUILD_ID"
    # The number of the original build this was rebuilt from or &#x60;&quot;&quot;&#x60; if not a rebuild.
    BUILDKITE_REBUILT_FROM_BUILD_NUMBER = "BUILDKITE_REBUILT_FROM_BUILD_NUMBER"
    # A custom refspec for the buildkite-agent bootstrap script to use when checking out code. This variable can be modified by exporting the environment variable in the &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks.
    BUILDKITE_REFSPEC = "BUILDKITE_REFSPEC"
    # The repository of your pipeline. This variable can be set by exporting the environment variable in the &#x60;environment&#x60; or &#x60;pre-checkout&#x60; hooks.
    BUILDKITE_REPO = "BUILDKITE_REPO"
    # The path to the shared git mirror. Introduced in [v3.47.0](https:&#x2F;&#x2F;github.com&#x2F;buildkite&#x2F;agent&#x2F;releases&#x2F;tag&#x2F;v3.47.0).
    BUILDKITE_REPO_MIRROR = "BUILDKITE_REPO_MIRROR"
    # How many times this job has been retried.
    BUILDKITE_RETRY_COUNT = "BUILDKITE_RETRY_COUNT"
    # The access key ID for your S3 IAM user, for use with [private S3 buckets](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;cli-artifact#using-your-private-aws-s3-bucket). The variable is read by the &#x60;buildkite-agent artifact upload&#x60; command, and during the artifact upload phase of [command steps](&#x2F;docs&#x2F;pipelines&#x2F;command-step#command-step-attributes). The value can only be set by exporting the environment variable in the &#x60;environment&#x60;, &#x60;pre-checkout&#x60; or &#x60;pre-command&#x60; hooks.
    BUILDKITE_S3_ACCESS_KEY_ID = "BUILDKITE_S3_ACCESS_KEY_ID"
    # The access URL for your [private S3 bucket](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;cli-artifact#using-your-private-aws-s3-bucket), if you are using a proxy. The variable is read by the &#x60;buildkite-agent artifact upload&#x60; command, as well as during the artifact upload phase of [command steps](&#x2F;docs&#x2F;pipelines&#x2F;command-step#command-step-attributes). The value can only be set by exporting the environment variable in the &#x60;environment&#x60;, &#x60;pre-checkout&#x60; or &#x60;pre-command&#x60; hooks.
    BUILDKITE_S3_ACCESS_URL = "BUILDKITE_S3_ACCESS_URL"
    # The Access Control List to be set on artifacts being uploaded to your [private S3 bucket](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;cli-artifact#using-your-private-aws-s3-bucket). The variable is read by the &#x60;buildkite-agent artifact upload&#x60; command, as well as during the artifact upload phase of [command steps](&#x2F;docs&#x2F;pipelines&#x2F;command-step#command-step-attributes). The value can only be set by exporting the environment variable in the &#x60;environment&#x60;, &#x60;pre-checkout&#x60; or &#x60;pre-command&#x60; hooks.
# 
# Must be one of the following values which map to [S3 Canned ACL grants](https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;acl-overview.html#canned-acl).
    BUILDKITE_S3_ACL = "BUILDKITE_S3_ACL"
    # The region of your [private S3 bucket](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;cli-artifact#using-your-private-aws-s3-bucket). The variable is read by the &#x60;buildkite-agent artifact upload&#x60; command, as well as during the artifact upload phase of [command steps](&#x2F;docs&#x2F;pipelines&#x2F;command-step#command-step-attributes). The value can only be set by exporting the environment variable in the &#x60;environment&#x60;, &#x60;pre-checkout&#x60; or &#x60;pre-command&#x60; hooks.
    BUILDKITE_S3_DEFAULT_REGION = "BUILDKITE_S3_DEFAULT_REGION"
    # The secret access key for your S3 IAM user, for use with [private S3 buckets](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;cli-artifact#using-your-private-aws-s3-bucket). The variable is read by the &#x60;buildkite-agent artifact upload&#x60; command, as well as during the artifact upload phase of [command steps](&#x2F;docs&#x2F;pipelines&#x2F;command-step#command-step-attributes). The value can only be set by exporting the environment variable in the &#x60;environment&#x60;, &#x60;pre-checkout&#x60; or &#x60;pre-command&#x60; hooks. Do not print or export this variable anywhere except your agent hooks.
    BUILDKITE_S3_SECRET_ACCESS_KEY = "BUILDKITE_S3_SECRET_ACCESS_KEY"
    # Whether to enable encryption for the artifacts in your [private S3 bucket](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;cli-artifact#using-your-private-aws-s3-bucket). The variable is read by the &#x60;buildkite-agent artifact upload&#x60; command, as well as during the artifact upload phase of [command steps](&#x2F;docs&#x2F;pipelines&#x2F;command-step#command-step-attributes). The value can only be set by exporting the environment variable in the &#x60;environment&#x60;, &#x60;pre-checkout&#x60; or &#x60;pre-command&#x60; hooks.
    BUILDKITE_S3_SSE_ENABLED = "BUILDKITE_S3_SSE_ENABLED"
    # The value of the &#x60;shell&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_SHELL = "BUILDKITE_SHELL"
    # The source of the event that created the build.
    BUILDKITE_SOURCE = "BUILDKITE_SOURCE"
    # The opposite of the value of the &#x60;no-ssh-keyscan&#x60; [agent configuration option](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration).
    BUILDKITE_SSH_KEYSCAN = "BUILDKITE_SSH_KEYSCAN"
    # A unique string that identifies a step.
    BUILDKITE_STEP_ID = "BUILDKITE_STEP_ID"
    # The value of the &#x60;key&#x60; [command step attribute](&#x2F;docs&#x2F;pipelines&#x2F;command-step#command-step-attributes), a unique string set by you to identify a step.
    BUILDKITE_STEP_KEY = "BUILDKITE_STEP_KEY"
    # The name of the tag being built, if this build was triggered from a tag.
    BUILDKITE_TAG = "BUILDKITE_TAG"
    # The number of minutes until Buildkite automatically cancels this job, if a timeout has been specified, otherwise it &#x60;false&#x60; if no timeout is set. Jobs that time out with an exit status of 0 are marked as &quot;passed&quot;.
    BUILDKITE_TIMEOUT = "BUILDKITE_TIMEOUT"
    # Set to &#x60;&quot;datadog&quot;&#x60; to send metrics to the [Datadog APM](https:&#x2F;&#x2F;docs.datadoghq.com&#x2F;tracing&#x2F;) using &#x60;localhost:8126&#x60;, or &#x60;DD_AGENT_HOST:DD_AGENT_APM_PORT&#x60;.
# 
# Also available as a [buildkite agent configuration option.](&#x2F;docs&#x2F;agent&#x2F;v3&#x2F;configuration#configuration-settings)
    BUILDKITE_TRACING_BACKEND = "BUILDKITE_TRACING_BACKEND"
    # The UUID of the build that triggered this build. This will be empty if the build was not triggered from another build.
    BUILDKITE_TRIGGERED_FROM_BUILD_ID = "BUILDKITE_TRIGGERED_FROM_BUILD_ID"
    # The number of the build that triggered this build or &#x60;&quot;&quot;&#x60; if the build was not triggered from another build.
    BUILDKITE_TRIGGERED_FROM_BUILD_NUMBER = "BUILDKITE_TRIGGERED_FROM_BUILD_NUMBER"
    # The slug of the pipeline that was used to trigger this build or &#x60;&quot;&quot;&#x60; if the build was not triggered from another build.
    BUILDKITE_TRIGGERED_FROM_BUILD_PIPELINE_SLUG = "BUILDKITE_TRIGGERED_FROM_BUILD_PIPELINE_SLUG"
    # The name of the user who unblocked the build.
    BUILDKITE_UNBLOCKER = "BUILDKITE_UNBLOCKER"
    # The notification email of the user who unblocked the build.
    BUILDKITE_UNBLOCKER_EMAIL = "BUILDKITE_UNBLOCKER_EMAIL"
    # The UUID of the user who unblocked the build.
    BUILDKITE_UNBLOCKER_ID = "BUILDKITE_UNBLOCKER_ID"
    # A colon separated list of non-private team slugs that the user who unblocked the build belongs to.
    BUILDKITE_UNBLOCKER_TEAMS = "BUILDKITE_UNBLOCKER_TEAMS"
    # Always &#x60;true&#x60;.
    CI = "CI"
