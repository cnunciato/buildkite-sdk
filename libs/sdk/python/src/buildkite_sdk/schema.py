from typing import Any, Literal, TypedDict, Union
from typing_extensions import Required


class JsonSchemaForBuildkitePipelineConfigurationFiles(TypedDict, total=False):
    """
    JSON schema for Buildkite pipeline configuration files.

    fileMatch:
      - buildkite.yml
      - buildkite.yaml
      - buildkite.json
      - buildkite.*.yml
      - buildkite.*.yaml
      - buildkite.*.json
      - .buildkite/pipeline.yml
      - .buildkite/pipeline.yaml
      - .buildkite/pipeline.json
      - .buildkite/pipeline.*.yml
      - .buildkite/pipeline.*.yaml
      - .buildkite/pipeline.*.json
    """

    env: "_Env"
    """
    Environment variables for this step

    examples:
      - NODE_ENV: test
    """

    agents: "_Agents"
    """ Aggregation type: oneOf """

    notify: "_BuildNotify"
    """ Array of notification options for this step """

    steps: Required[list["_JsonSchemaForBuildkitePipelineConfigurationFilesStepsItem"]]
    """
    A list of steps

    Required property
    """



_ALLOW_DEPENDENCY_FAILURE_DEFAULT = False
""" Default value of the field path 'allow dependency failure' """



_Agents = Union["_AgentsObject", "_AgentsList"]
""" Aggregation type: oneOf """



_AgentsList = list[str]
"""
Query rules to target specific agents in k=v format

examples:
  - queue=default
  - xcode=true
"""



_AgentsObject = dict[str, Any]
"""
Query rules to target specific agents

examples:
  - queue: deploy
  - ruby: 2*
"""



_AllowDependencyFailure = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether to proceed with this step and further steps if a step named in the depends_on attribute fails

default: False
"""
_ALLOWDEPENDENCYFAILURE_TRUE: Literal[True] = True
"""The values for the 'Whether to proceed with this step and further steps if a step named in the depends_on attribute fails' enum"""
_ALLOWDEPENDENCYFAILURE_FALSE: Literal[False] = False
"""The values for the 'Whether to proceed with this step and further steps if a step named in the depends_on attribute fails' enum"""
_ALLOWDEPENDENCYFAILURE_TRUE3335: Literal['true'] = "true"
"""The values for the 'Whether to proceed with this step and further steps if a step named in the depends_on attribute fails' enum"""
_ALLOWDEPENDENCYFAILURE_FALSE1074: Literal['false'] = "false"
"""The values for the 'Whether to proceed with this step and further steps if a step named in the depends_on attribute fails' enum"""



class _AutomaticRetry(TypedDict, total=False):
    exit_status: "_AutomaticRetryExitStatus"
    """
    The exit status number that will cause this job to retry

    Aggregation type: anyOf
    """

    limit: int
    """
    The number of times this job can be retried

    minimum: 1
    maximum: 10
    """

    signal: str
    """
    The exit signal, if any, that may be retried

    examples:
      - '*'
      - none
      - SIGKILL
      - term
    """

    signal_reason: "_AutomaticRetrySignalReason"
    """ The exit signal reason, if any, that may be retried """



_AutomaticRetryExitStatus = Union["_AutomaticRetryExitStatusAnyof0", int, list[int]]
"""
The exit status number that will cause this job to retry

Aggregation type: anyOf
"""



_AutomaticRetryExitStatusAnyof0 = Union[Literal['*']]
_AUTOMATICRETRYEXITSTATUSANYOF0__ASTERISK_: Literal['*'] = "*"
"""The values for the '_AutomaticRetryExitStatusAnyof0' enum"""



_AutomaticRetrySignalReason = Union[Literal['*'], Literal['none'], Literal['agent_refused'], Literal['agent_stop'], Literal['cancel'], Literal['process_run_error'], Literal['signature_rejected']]
""" The exit signal reason, if any, that may be retried """
_AUTOMATICRETRYSIGNALREASON__ASTERISK_: Literal['*'] = "*"
"""The values for the 'The exit signal reason, if any, that may be retried' enum"""
_AUTOMATICRETRYSIGNALREASON_NONE: Literal['none'] = "none"
"""The values for the 'The exit signal reason, if any, that may be retried' enum"""
_AUTOMATICRETRYSIGNALREASON_AGENT_REFUSED: Literal['agent_refused'] = "agent_refused"
"""The values for the 'The exit signal reason, if any, that may be retried' enum"""
_AUTOMATICRETRYSIGNALREASON_AGENT_STOP: Literal['agent_stop'] = "agent_stop"
"""The values for the 'The exit signal reason, if any, that may be retried' enum"""
_AUTOMATICRETRYSIGNALREASON_CANCEL: Literal['cancel'] = "cancel"
"""The values for the 'The exit signal reason, if any, that may be retried' enum"""
_AUTOMATICRETRYSIGNALREASON_PROCESS_RUN_ERROR: Literal['process_run_error'] = "process_run_error"
"""The values for the 'The exit signal reason, if any, that may be retried' enum"""
_AUTOMATICRETRYSIGNALREASON_SIGNATURE_REJECTED: Literal['signature_rejected'] = "signature_rejected"
"""The values for the 'The exit signal reason, if any, that may be retried' enum"""



_BLOCK_STEP_BLOCKED_STATE_DEFAULT = 'passed'
""" Default value of the field path 'block step blocked_state' """



_BlockStep = TypedDict('_BlockStep', {
    # | Whether to proceed with this step and further steps if a step named in the depends_on attribute fails
    # |
    # | default: False
    'allow_dependency_failure': "_AllowDependencyFailure",
    # | The label of the block step
    'block': str,
    # | The state that the build is set to when the build is blocked by this block step
    # |
    # | default: passed
    'blocked_state': "_BlockStepBlockedState",
    # | Which branches will include this step in their builds
    # |
    # | examples:
    # |   - master
    # |   - - feature/*
    # |     - chore/*
    # |
    # | Aggregation type: anyOf
    'branches': "_Branches",
    # | The step keys for a step to depend on
    # |
    # | Aggregation type: anyOf
    'depends_on': "_DependsOn",
    # | A list of input fields required to be filled out before unblocking the step
    'fields': "_Fields",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'key': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'identifier': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'id': "_Key",
    # | The label of the block step
    'label': "_BlockstepPropertiesBlock",
    # | The label of the block step
    'name': "_BlockstepPropertiesBlock",
    # | The instructional message displayed in the dialog box when the unblock step is activated
    # |
    # | examples:
    # |   - Release to production?
    'prompt': "_Prompt",
    'type': "_BlockStepType",
}, total=False)


_BlockStepBlockedState = Union[Literal['passed'], Literal['failed'], Literal['running']]
"""
The state that the build is set to when the build is blocked by this block step

default: passed
"""
_BLOCKSTEPBLOCKEDSTATE_PASSED: Literal['passed'] = "passed"
"""The values for the 'The state that the build is set to when the build is blocked by this block step' enum"""
_BLOCKSTEPBLOCKEDSTATE_FAILED: Literal['failed'] = "failed"
"""The values for the 'The state that the build is set to when the build is blocked by this block step' enum"""
_BLOCKSTEPBLOCKEDSTATE_RUNNING: Literal['running'] = "running"
"""The values for the 'The state that the build is set to when the build is blocked by this block step' enum"""



_BlockStepType = Union[Literal['block']]
_BLOCKSTEPTYPE_BLOCK: Literal['block'] = "block"
"""The values for the '_BlockStepType' enum"""



_BlockstepPropertiesBlock = str
""" The label of the block step """



_Branches = Union["_BranchesAnyof0", "_BranchesAnyof1"]
"""
Which branches will include this step in their builds

examples:
  - master
  - - feature/*
    - chore/*

Aggregation type: anyOf
"""



_BranchesAnyof0 = str
"""
examples:
  - master
  - - feature/*
    - chore/*
"""



_BranchesAnyof1 = list[str]
"""
examples:
  - master
  - - feature/*
    - chore/*
"""



_BuildNotify = list["_BuildNotifyItem"]
""" Array of notification options for this step """



_BuildNotifyItem = Union["_BuildNotifyItemOneof0", "_BuildNotifyItemOneof1", "_BuildNotifyItemOneof2", "_BuildNotifyItemOneof3", "_BuildNotifyItemOneof4", "_BuildNotifyItemOneof5", "_BuildNotifyItemOneof6", "_BuildNotifyItemOneof7"]
""" Aggregation type: oneOf """



_BuildNotifyItemOneof0 = Union[Literal['github_check'], Literal['github_commit_status']]
_BUILDNOTIFYITEMONEOF0_GITHUB_CHECK: Literal['github_check'] = "github_check"
"""The values for the '_BuildNotifyItemOneof0' enum"""
_BUILDNOTIFYITEMONEOF0_GITHUB_COMMIT_STATUS: Literal['github_commit_status'] = "github_commit_status"
"""The values for the '_BuildNotifyItemOneof0' enum"""



_BuildNotifyItemOneof1 = TypedDict('_BuildNotifyItemOneof1', {
    'email': str,
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


_BuildNotifyItemOneof2 = TypedDict('_BuildNotifyItemOneof2', {
    'basecamp_campfire': str,
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


_BuildNotifyItemOneof3 = TypedDict('_BuildNotifyItemOneof3', {
    # | Aggregation type: oneOf
    'slack': Union[str, "_BuildNotifyItemOneof3SlackOneof1"],
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


class _BuildNotifyItemOneof3SlackOneof1(TypedDict, total=False):
    channels: list[str]
    message: str


_BuildNotifyItemOneof4 = TypedDict('_BuildNotifyItemOneof4', {
    'webhook': str,
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


_BuildNotifyItemOneof5 = TypedDict('_BuildNotifyItemOneof5', {
    'pagerduty_change_event': str,
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


_BuildNotifyItemOneof6 = TypedDict('_BuildNotifyItemOneof6', {
    'github_commit_status': "_BuildNotifyItemOneof6GithubCommitStatus",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


class _BuildNotifyItemOneof6GithubCommitStatus(TypedDict, total=False):
    context: str
    """ GitHub commit status name """



_BuildNotifyItemOneof7 = TypedDict('_BuildNotifyItemOneof7', {
    'github_check': "_BuildNotifyItemOneof7GithubCheck",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


class _BuildNotifyItemOneof7GithubCheck(TypedDict, total=False):
    context: str
    """ GitHub commit status name """



_CANCEL_ON_BUILD_FAILING_DEFAULT = False
""" Default value of the field path 'cancel on build failing' """



_COMMAND_STEP_RETRY_AUTOMATIC_ANYOF0_DEFAULT = [{'exit_status': '*', 'limit': 2}]
""" Default value of the field path 'command step retry automatic anyof0' """



_COMMAND_STEP_RETRY_AUTOMATIC_ANYOF1_DEFAULT = [{'exit_status': '*', 'limit': 2}]
""" Default value of the field path 'command step retry automatic anyof1' """



_COMMAND_STEP_RETRY_AUTOMATIC_ANYOF2_DEFAULT = [{'exit_status': '*', 'limit': 2}]
""" Default value of the field path 'command step retry automatic anyof2' """



_COMMAND_STEP_RETRY_AUTOMATIC_DEFAULT = [{'exit_status': '*', 'limit': 2}]
""" Default value of the field path 'command step retry automatic' """



_COMMAND_STEP_RETRY_MANUAL_ANYOF0_DEFAULT = True
""" Default value of the field path 'command step retry manual anyof0' """



_COMMAND_STEP_RETRY_MANUAL_ANYOF1_ALLOWED_DEFAULT = True
""" Default value of the field path 'command step retry manual anyof1 allowed' """



_COMMAND_STEP_RETRY_MANUAL_ANYOF1_DEFAULT = True
""" Default value of the field path 'command step retry manual anyof1' """



_COMMAND_STEP_RETRY_MANUAL_ANYOF1_PERMIT_ON_PASSED_DEFAULT = True
""" Default value of the field path 'command step retry manual anyof1 permit_on_passed' """



_COMMAND_STEP_RETRY_MANUAL_DEFAULT = True
""" Default value of the field path 'command step retry manual' """



_Cache = Union["_CacheAnyof0", "_CacheAnyof1", "_CacheAnyof2"]
"""
The paths for the caches to be used in the step

examples:
  - dist/
  - - .build/*
    - assets/*
  - name: cool-cache
    paths:
    - /path/one
    - /path/two
    size: 20g

Aggregation type: anyOf
"""



_CacheAnyof0 = str
"""
examples:
  - dist/
  - - .build/*
    - assets/*
  - name: cool-cache
    paths:
    - /path/one
    - /path/two
    size: 20g
"""



_CacheAnyof1 = list[str]
"""
examples:
  - dist/
  - - .build/*
    - assets/*
  - name: cool-cache
    paths:
    - /path/one
    - /path/two
    size: 20g
"""



class _CacheAnyof2(TypedDict, total=False):
    """
    examples:
      - dist/
      - - .build/*
        - assets/*
      - name: cool-cache
        paths:
        - /path/one
        - /path/two
        size: 20g
    """

    paths: Required[list[str]]
    """ Required property """

    size: str
    """ pattern: ^\d+g$ """

    name: str


_CancelOnBuildFailing = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether to cancel the job as soon as the build is marked as failing

default: False
"""
_CANCELONBUILDFAILING_TRUE: Literal[True] = True
"""The values for the 'Whether to cancel the job as soon as the build is marked as failing' enum"""
_CANCELONBUILDFAILING_FALSE: Literal[False] = False
"""The values for the 'Whether to cancel the job as soon as the build is marked as failing' enum"""
_CANCELONBUILDFAILING_TRUE4743: Literal['true'] = "true"
"""The values for the 'Whether to cancel the job as soon as the build is marked as failing' enum"""
_CANCELONBUILDFAILING_FALSE6874: Literal['false'] = "false"
"""The values for the 'Whether to cancel the job as soon as the build is marked as failing' enum"""



_CommandStep = TypedDict('_CommandStep', {
    # | Aggregation type: oneOf
    'agents': "_Agents",
    # | Whether to proceed with this step and further steps if a step named in the depends_on attribute fails
    # |
    # | default: False
    'allow_dependency_failure': "_AllowDependencyFailure",
    # | The glob path/s of artifacts to upload once this step has finished running
    # |
    # | examples:
    # |   - - screenshots/*
    # |   - - dist/myapp.zip
    # |     - dist/myapp.tgz
    # |
    # | Aggregation type: anyOf
    'artifact_paths': "_CommandStepArtifactPaths",
    # | Which branches will include this step in their builds
    # |
    # | examples:
    # |   - master
    # |   - - feature/*
    # |     - chore/*
    # |
    # | Aggregation type: anyOf
    'branches': "_Branches",
    # | The paths for the caches to be used in the step
    # |
    # | examples:
    # |   - dist/
    # |   - - .build/*
    # |     - assets/*
    # |   - name: cool-cache
    # |     paths:
    # |     - /path/one
    # |     - /path/two
    # |     size: 20g
    # |
    # | Aggregation type: anyOf
    'cache': "_Cache",
    # | Whether to cancel the job as soon as the build is marked as failing
    # |
    # | default: False
    'cancel_on_build_failing': "_CancelOnBuildFailing",
    # | The commands to run on the agent
    # |
    # | Aggregation type: anyOf
    'command': "_CommandStepCommand",
    # | The commands to run on the agent
    # |
    # | Aggregation type: anyOf
    'commands': "_CommandstepPropertiesCommand",
    # | The maximum number of jobs created from this step that are allowed to run at the same time. If you use this attribute, you must also define concurrency_group.
    # |
    # | examples:
    # |   - 1
    'concurrency': int,
    # | A unique name for the concurrency group that you are creating with the concurrency attribute
    # |
    # | examples:
    # |   - my-pipeline/deploy
    'concurrency_group': str,
    # | Control command order, allowed values are 'ordered' (default) and 'eager'.  If you use this attribute, you must also define concurrency_group and concurrency.
    # |
    # | examples:
    # |   - ordered
    'concurrency_method': "_CommandStepConcurrencyMethod",
    # | The step keys for a step to depend on
    # |
    # | Aggregation type: anyOf
    'depends_on': "_DependsOn",
    # | Environment variables for this step
    # |
    # | examples:
    # |   - NODE_ENV: test
    'env': "_Env",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'key': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'identifier': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'id': "_Key",
    # | The label that will be displayed in the pipeline visualisation in Buildkite. Supports emoji.
    # |
    # | examples:
    # |   - ':docker: Build'
    'label': "_Label",
    # | The signature of the command step, generally injected by agents at pipeline upload
    'signature': "_CommandStepSignature",
    # | Aggregation type: oneOf
    'matrix': Union["_CommandStepMatrixOneof0", "_CommandStepMatrixOneof1"],
    # | The label that will be displayed in the pipeline visualisation in Buildkite. Supports emoji.
    # |
    # | examples:
    # |   - ':docker: Build'
    'name': "_Label",
    # | Array of notification options for this step
    'notify': list["_CommandStepNotifyItem"],
    # | The number of parallel jobs that will be created based on this step
    # |
    # | examples:
    # |   - 42
    'parallelism': int,
    # | Aggregation type: anyOf
    'plugins': "_CommandStepPlugins",
    # | The conditions for marking the step as a soft-fail.
    # |
    # | Aggregation type: anyOf
    'soft_fail': "_SoftFail",
    # | The conditions for retrying this step.
    'retry': "_CommandStepRetry",
    # | Whether this step should be skipped. Passing a string provides a reason for skipping this command
    # |
    # | examples:
    # |   - true
    # |   - false
    # |   - My reason
    # |
    # | Aggregation type: anyOf
    'skip': "_Skip",
    # | The number of minutes to time out a job
    # |
    # | minimum: 1
    # | examples:
    # |   - 60
    'timeout_in_minutes': int,
    'type': "_CommandStepType",
    # | Priority of the job, higher priorities are assigned to agents
    # |
    # | examples:
    # |   - -1
    # |   - 1
    'priority': int,
}, total=False)


_CommandStepArtifactPaths = Union["_CommandStepArtifactPathsAnyof0", "_CommandStepArtifactPathsAnyof1"]
"""
The glob path/s of artifacts to upload once this step has finished running

examples:
  - - screenshots/*
  - - dist/myapp.zip
    - dist/myapp.tgz

Aggregation type: anyOf
"""



_CommandStepArtifactPathsAnyof0 = str
"""
examples:
  - - screenshots/*
  - - dist/myapp.zip
    - dist/myapp.tgz
"""



_CommandStepArtifactPathsAnyof1 = list[str]
"""
examples:
  - - screenshots/*
  - - dist/myapp.zip
    - dist/myapp.tgz
"""



_CommandStepCommand = Union[list[str], str]
"""
The commands to run on the agent

Aggregation type: anyOf
"""



_CommandStepConcurrencyMethod = Union[Literal['ordered'], Literal['eager']]
"""
Control command order, allowed values are 'ordered' (default) and 'eager'.  If you use this attribute, you must also define concurrency_group and concurrency.

examples:
  - ordered
"""
_COMMANDSTEPCONCURRENCYMETHOD_ORDERED: Literal['ordered'] = "ordered"
"""The values for the 'Control command order, allowed values are 'ordered' (default) and 'eager'.  If you use this attribute, you must also define concurrency_group and concurrency' enum"""
_COMMANDSTEPCONCURRENCYMETHOD_EAGER: Literal['eager'] = "eager"
"""The values for the 'Control command order, allowed values are 'ordered' (default) and 'eager'.  If you use this attribute, you must also define concurrency_group and concurrency' enum"""



_CommandStepMatrixOneof0 = list["_MatrixElement"]
"""
List of elements for simple single-dimension Build Matrix

examples:
  - - linux
    - freebsd
"""



class _CommandStepMatrixOneof1(TypedDict, total=False):
    """ Configuration for multi-dimension Build Matrix """

    setup: Required[Union["_CommandStepMatrixOneof1SetupOneof0", "_CommandStepMatrixOneof1SetupOneof1"]]
    """
    Aggregation type: oneOf

    Required property
    """

    adjustments: list["_CommandStepMatrixOneof1AdjustmentsItem"]
    """ List of Build Matrix adjustments """



# | An adjustment to a Build Matrix
_CommandStepMatrixOneof1AdjustmentsItem = TypedDict('_CommandStepMatrixOneof1AdjustmentsItem', {
    # | Aggregation type: oneOf
    # |
    # | Required property
    'with': Required[Union["_CommandStepMatrixOneof1AdjustmentsItemWithOneof0", "_CommandStepMatrixOneof1AdjustmentsItemWithOneof1"]],
    # | Whether this step should be skipped. Passing a string provides a reason for skipping this command
    # |
    # | examples:
    # |   - true
    # |   - false
    # |   - My reason
    # |
    # | Aggregation type: anyOf
    'skip': "_Skip",
    # | The conditions for marking the step as a soft-fail.
    # |
    # | Aggregation type: anyOf
    'soft_fail': "_SoftFail",
}, total=False)


_CommandStepMatrixOneof1AdjustmentsItemWithOneof0 = list["_MatrixElement"]
""" List of existing or new elements for single-dimension Build Matrix """



_CommandStepMatrixOneof1AdjustmentsItemWithOneof1 = dict[str, "_CommandStepMatrixOneof1AdjustmentsItemWithOneof1Additionalproperties"]
"""
Specification of a new or existing Build Matrix combination

propertyNames:
  __type__: string
  description: Build Matrix dimension name
examples:
  - arch: arm64
    os: linux
"""



_CommandStepMatrixOneof1AdjustmentsItemWithOneof1Additionalproperties = str
""" Build Matrix dimension element """



_CommandStepMatrixOneof1SetupOneof0 = list["_MatrixElement"]
"""
List of elements for single-dimension Build Matrix

examples:
  - - linux
    - freebsd
"""



_CommandStepMatrixOneof1SetupOneof1 = dict[str, "_CommandStepMatrixOneof1SetupOneof1Additionalproperties"]
"""
Mapping of Build Matrix dimension names to their lists of elements

propertyNames:
  __type__: string
  description: Build Matrix dimension name
  pattern: ^[a-zA-Z0-9_]+$
examples:
  - arch:
    - arm64
    - riscv
    os:
    - linux
    - freebsd
"""



_CommandStepMatrixOneof1SetupOneof1Additionalproperties = list["_MatrixElement"]
""" List of elements for this Build Matrix dimension """



_CommandStepNotifyItem = Union["_CommandStepNotifyItemOneof0", "_CommandStepNotifyItemOneof1", "_CommandStepNotifyItemOneof2", "_CommandStepNotifyItemOneof3", "_CommandStepNotifyItemOneof4"]
""" Aggregation type: oneOf """



_CommandStepNotifyItemOneof0 = Union[Literal['github_check'], Literal['github_commit_status']]
_COMMANDSTEPNOTIFYITEMONEOF0_GITHUB_CHECK: Literal['github_check'] = "github_check"
"""The values for the '_CommandStepNotifyItemOneof0' enum"""
_COMMANDSTEPNOTIFYITEMONEOF0_GITHUB_COMMIT_STATUS: Literal['github_commit_status'] = "github_commit_status"
"""The values for the '_CommandStepNotifyItemOneof0' enum"""



_CommandStepNotifyItemOneof1 = TypedDict('_CommandStepNotifyItemOneof1', {
    'basecamp_campfire': str,
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


_CommandStepNotifyItemOneof2 = TypedDict('_CommandStepNotifyItemOneof2', {
    # | Aggregation type: oneOf
    'slack': Union[str, "_CommandStepNotifyItemOneof2SlackOneof1"],
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


class _CommandStepNotifyItemOneof2SlackOneof1(TypedDict, total=False):
    channels: list[str]
    message: str


_CommandStepNotifyItemOneof3 = TypedDict('_CommandStepNotifyItemOneof3', {
    'github_commit_status': "_CommandStepNotifyItemOneof3GithubCommitStatus",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


class _CommandStepNotifyItemOneof3GithubCommitStatus(TypedDict, total=False):
    context: str
    """ GitHub commit status name """



_CommandStepNotifyItemOneof4 = TypedDict('_CommandStepNotifyItemOneof4', {
    'github_check': "_CommandStepNotifyItemOneof4GithubCheck",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
}, total=False)


class _CommandStepNotifyItemOneof4GithubCheck(TypedDict, total=False):
    context: str
    """ GitHub commit status name """



_CommandStepPlugins = Union["_CommandStepPluginsAnyof0", "_CommandStepPluginsAnyof1"]
""" Aggregation type: anyOf """



_CommandStepPluginsAnyof0 = list["_CommandStepPluginsAnyof0Item"]
""" Array of plugins for this step """



_CommandStepPluginsAnyof0Item = Union[str, "_CommandStepPluginsAnyof0ItemOneof1"]
""" Aggregation type: oneOf """



_CommandStepPluginsAnyof0ItemOneof1 = dict[str, Any]
"""
maxProperties: 1
examples:
  - docker-compose#v1.0.0:
      run: app
"""



_CommandStepPluginsAnyof1 = dict[str, Any]
""" A map of plugins for this step. Deprecated: please use the array syntax. """



class _CommandStepRetry(TypedDict, total=False):
    """ The conditions for retrying this step. """

    automatic: "_CommandStepRetryAutomatic"
    """
    Whether to allow a job to retry automatically. If set to true, the retry conditions are set to the default value.

    default:
      - exit_status: '*'
        limit: 2

    Aggregation type: anyOf
    """

    manual: "_CommandStepRetryManual"
    """
    Whether to allow a job to be retried manually

    default: True

    Aggregation type: anyOf
    """



_CommandStepRetryAutomatic = Union["_CommandStepRetryAutomaticAnyof0", "_AutomaticRetry", "_CommandStepRetryAutomaticAnyof2"]
"""
Whether to allow a job to retry automatically. If set to true, the retry conditions are set to the default value.

default:
  - exit_status: '*'
    limit: 2

Aggregation type: anyOf
"""



_CommandStepRetryAutomaticAnyof0 = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
default:
  - exit_status: '*'
    limit: 2
"""
_COMMANDSTEPRETRYAUTOMATICANYOF0_TRUE: Literal[True] = True
"""The values for the 'default:' enum"""
_COMMANDSTEPRETRYAUTOMATICANYOF0_FALSE: Literal[False] = False
"""The values for the 'default:' enum"""
_COMMANDSTEPRETRYAUTOMATICANYOF0_TRUE9066: Literal['true'] = "true"
"""The values for the 'default:' enum"""
_COMMANDSTEPRETRYAUTOMATICANYOF0_FALSE3196: Literal['false'] = "false"
"""The values for the 'default:' enum"""



_CommandStepRetryAutomaticAnyof2 = list["_AutomaticRetry"]
"""
default:
  - exit_status: '*'
    limit: 2
"""



_CommandStepRetryManual = Union["_CommandStepRetryManualAnyof0", "_CommandStepRetryManualAnyof1"]
"""
Whether to allow a job to be retried manually

default: True

Aggregation type: anyOf
"""



_CommandStepRetryManualAnyof0 = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
""" default: True """
_COMMANDSTEPRETRYMANUALANYOF0_TRUE: Literal[True] = True
"""The values for the 'default: True' enum"""
_COMMANDSTEPRETRYMANUALANYOF0_FALSE: Literal[False] = False
"""The values for the 'default: True' enum"""
_COMMANDSTEPRETRYMANUALANYOF0_TRUE9618: Literal['true'] = "true"
"""The values for the 'default: True' enum"""
_COMMANDSTEPRETRYMANUALANYOF0_FALSE902: Literal['false'] = "false"
"""The values for the 'default: True' enum"""



class _CommandStepRetryManualAnyof1(TypedDict, total=False):
    """ default: True """

    allowed: "_CommandStepRetryManualAnyof1Allowed"
    """
    Whether or not this job can be retried manually

    default: True
    """

    permit_on_passed: "_CommandStepRetryManualAnyof1PermitOnPassed"
    """
    Whether or not this job can be retried after it has passed

    default: True
    """

    reason: str
    """
    A string that will be displayed in a tooltip on the Retry button in Buildkite. This will only be displayed if the allowed attribute is set to false.

    examples:
      - No retries allowed on deploy steps
    """



_CommandStepRetryManualAnyof1Allowed = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether or not this job can be retried manually

default: True
"""
_COMMANDSTEPRETRYMANUALANYOF1ALLOWED_TRUE: Literal[True] = True
"""The values for the 'Whether or not this job can be retried manually' enum"""
_COMMANDSTEPRETRYMANUALANYOF1ALLOWED_FALSE: Literal[False] = False
"""The values for the 'Whether or not this job can be retried manually' enum"""
_COMMANDSTEPRETRYMANUALANYOF1ALLOWED_TRUE8757: Literal['true'] = "true"
"""The values for the 'Whether or not this job can be retried manually' enum"""
_COMMANDSTEPRETRYMANUALANYOF1ALLOWED_FALSE1226: Literal['false'] = "false"
"""The values for the 'Whether or not this job can be retried manually' enum"""



_CommandStepRetryManualAnyof1PermitOnPassed = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether or not this job can be retried after it has passed

default: True
"""
_COMMANDSTEPRETRYMANUALANYOF1PERMITONPASSED_TRUE: Literal[True] = True
"""The values for the 'Whether or not this job can be retried after it has passed' enum"""
_COMMANDSTEPRETRYMANUALANYOF1PERMITONPASSED_FALSE: Literal[False] = False
"""The values for the 'Whether or not this job can be retried after it has passed' enum"""
_COMMANDSTEPRETRYMANUALANYOF1PERMITONPASSED_TRUE722: Literal['true'] = "true"
"""The values for the 'Whether or not this job can be retried after it has passed' enum"""
_COMMANDSTEPRETRYMANUALANYOF1PERMITONPASSED_FALSE169: Literal['false'] = "false"
"""The values for the 'Whether or not this job can be retried after it has passed' enum"""



class _CommandStepSignature(TypedDict, total=False):
    """ The signature of the command step, generally injected by agents at pipeline upload """

    algorithm: str
    """
    The algorithm used to generate the signature

    examples:
      - HS512
      - EdDSA
      - PS256
    """

    value: str
    """ The signature value, a JWS compact signature with a detached body """

    signed_fields: list[str]
    """
    The fields that were signed to form the signature value

    examples:
      - - command
        - matrix
        - plugins
        - env::SOME_ENV_VAR
    """



_CommandStepType = Union[Literal['script'], Literal['command'], Literal['commands']]
_COMMANDSTEPTYPE_SCRIPT: Literal['script'] = "script"
"""The values for the '_CommandStepType' enum"""
_COMMANDSTEPTYPE_COMMAND: Literal['command'] = "command"
"""The values for the '_CommandStepType' enum"""
_COMMANDSTEPTYPE_COMMANDS: Literal['commands'] = "commands"
"""The values for the '_CommandStepType' enum"""



_CommandstepPropertiesCommand = Union[list[str], str]
"""
The commands to run on the agent

Aggregation type: anyOf
"""



_DEPENDS_ON_ANYOF2_ITEM_ANYOF1_ALLOW_FAILURE_DEFAULT = False
""" Default value of the field path 'depends on anyof2 item anyof1 allow_failure' """



_DependsOn = Union[None, str, list["_DependsOnAnyof2Item"]]
"""
The step keys for a step to depend on

Aggregation type: anyOf
"""



_DependsOnAnyof2Item = Union[str, "_DependsOnAnyof2ItemAnyof1"]
""" Aggregation type: anyOf """



class _DependsOnAnyof2ItemAnyof1(TypedDict, total=False):
    step: str
    allow_failure: "_DependsOnAnyof2ItemAnyof1AllowFailure"
    """ default: False """



_DependsOnAnyof2ItemAnyof1AllowFailure = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
""" default: False """
_DEPENDSONANYOF2ITEMANYOF1ALLOWFAILURE_TRUE: Literal[True] = True
"""The values for the 'default: False' enum"""
_DEPENDSONANYOF2ITEMANYOF1ALLOWFAILURE_FALSE: Literal[False] = False
"""The values for the 'default: False' enum"""
_DEPENDSONANYOF2ITEMANYOF1ALLOWFAILURE_TRUE3388: Literal['true'] = "true"
"""The values for the 'default: False' enum"""
_DEPENDSONANYOF2ITEMANYOF1ALLOWFAILURE_FALSE1164: Literal['false'] = "false"
"""The values for the 'default: False' enum"""



_Env = dict[str, Any]
"""
Environment variables for this step

examples:
  - NODE_ENV: test
"""



_FIELDS_ITEM_ONEOF0_REQUIRED_DEFAULT = True
""" Default value of the field path 'fields item oneof0 required' """



_FIELDS_ITEM_ONEOF1_MULTIPLE_DEFAULT = False
""" Default value of the field path 'fields item oneof1 multiple' """



_FIELDS_ITEM_ONEOF1_OPTIONS_ITEM_REQUIRED_DEFAULT = True
""" Default value of the field path 'fields item oneof1 options item required' """



_FIELDS_ITEM_ONEOF1_REQUIRED_DEFAULT = True
""" Default value of the field path 'fields item oneof1 required' """



_Fields = list["_FieldsItem"]
""" A list of input fields required to be filled out before unblocking the step """



_FieldsItem = Union["_FieldsItemOneof0", "_FieldsItemOneof1"]
""" Aggregation type: oneOf """



class _FieldsItemOneof0(TypedDict, total=False):
    text: str
    """
    The text input name

    examples:
      - Release Name
    """

    key: Required[str]
    """
    The meta-data key that stores the field's input

    pattern: ^[a-zA-Z0-9-_]+$
    examples:
      - release-name

    Required property
    """

    hint: str
    """
    The explanatory text that is shown after the label

    examples:
      - "What\u2019s the code name for this release? :name_badge:"
    """

    format: str
    """
    The format must be a regular expression implicitly anchored to the beginning and end of the input and is functionally equivalent to the HTML5 pattern attribute.

    format: regex
    examples:
      - '[0-9a-f]+'
    """

    required: "_FieldsItemOneof0Required"
    """
    Whether the field is required for form submission

    default: True
    """

    default: str
    """
    The value that is pre-filled in the text field

    examples:
      - Flying Dolphin
    """



_FieldsItemOneof0Required = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether the field is required for form submission

default: True
"""
_FIELDSITEMONEOF0REQUIRED_TRUE: Literal[True] = True
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF0REQUIRED_FALSE: Literal[False] = False
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF0REQUIRED_TRUE8381: Literal['true'] = "true"
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF0REQUIRED_FALSE2341: Literal['false'] = "false"
"""The values for the 'Whether the field is required for form submission' enum"""



class _FieldsItemOneof1(TypedDict, total=False):
    select: str
    """
    The text input name

    examples:
      - Release Stream
    """

    key: Required[str]
    """
    The meta-data key that stores the field's input

    pattern: ^[a-zA-Z0-9-_]+$
    examples:
      - release-stream

    Required property
    """

    default: Union["_FieldsItemOneof1DefaultOneof0", "_FieldsItemOneof1DefaultOneof1"]
    """
    The value of the option(s) that will be pre-selected in the dropdown

    examples:
      - beta
      - - alpha
        - beta

    Aggregation type: oneOf
    """

    hint: str
    """
    The explanatory text that is shown after the label

    examples:
      - "What\u2019s the code name for this release? :name_badge:"
    """

    multiple: "_FieldsItemOneof1Multiple"
    """
    Whether more than one option may be selected

    default: False
    """

    options: Required[list["_FieldsItemOneof1OptionsItem"]]
    """
    minItems: 1

    Required property
    """

    required: "_FieldsItemOneof1Required"
    """
    Whether the field is required for form submission

    default: True
    """



_FieldsItemOneof1DefaultOneof0 = str
"""
examples:
  - beta
  - - alpha
    - beta
"""



_FieldsItemOneof1DefaultOneof1 = list[str]
"""
examples:
  - beta
  - - alpha
    - beta
"""



_FieldsItemOneof1Multiple = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether more than one option may be selected

default: False
"""
_FIELDSITEMONEOF1MULTIPLE_TRUE: Literal[True] = True
"""The values for the 'Whether more than one option may be selected' enum"""
_FIELDSITEMONEOF1MULTIPLE_FALSE: Literal[False] = False
"""The values for the 'Whether more than one option may be selected' enum"""
_FIELDSITEMONEOF1MULTIPLE_TRUE6910: Literal['true'] = "true"
"""The values for the 'Whether more than one option may be selected' enum"""
_FIELDSITEMONEOF1MULTIPLE_FALSE9963: Literal['false'] = "false"
"""The values for the 'Whether more than one option may be selected' enum"""



class _FieldsItemOneof1OptionsItem(TypedDict, total=False):
    label: Required[str]
    """
    The text displayed on the select list item

    examples:
      - Stable

    Required property
    """

    value: Required[str]
    """
    The value to be stored as meta-data

    examples:
      - stable

    Required property
    """

    hint: str
    """
    The text displayed directly under the select field’s label

    examples:
      - 'Which release stream does this belong in? :fork:'
    """

    required: "_FieldsItemOneof1OptionsItemRequired"
    """
    Whether the field is required for form submission

    default: True
    """



_FieldsItemOneof1OptionsItemRequired = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether the field is required for form submission

default: True
"""
_FIELDSITEMONEOF1OPTIONSITEMREQUIRED_TRUE: Literal[True] = True
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF1OPTIONSITEMREQUIRED_FALSE: Literal[False] = False
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF1OPTIONSITEMREQUIRED_TRUE967: Literal['true'] = "true"
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF1OPTIONSITEMREQUIRED_FALSE9986: Literal['false'] = "false"
"""The values for the 'Whether the field is required for form submission' enum"""



_FieldsItemOneof1Required = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether the field is required for form submission

default: True
"""
_FIELDSITEMONEOF1REQUIRED_TRUE: Literal[True] = True
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF1REQUIRED_FALSE: Literal[False] = False
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF1REQUIRED_TRUE2320: Literal['true'] = "true"
"""The values for the 'Whether the field is required for form submission' enum"""
_FIELDSITEMONEOF1REQUIRED_FALSE9575: Literal['false'] = "false"
"""The values for the 'Whether the field is required for form submission' enum"""



_GroupStep = TypedDict('_GroupStep', {
    # | The step keys for a step to depend on
    # |
    # | Aggregation type: anyOf
    'depends_on': "_DependsOn",
    # | The name to give to this group of steps
    # |
    # | examples:
    # |   - Tests
    # |
    # | Required property
    'group': Required[Union[str, None]],
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'key': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'identifier': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'id': "_Key",
    # | The name to give to this group of steps
    # |
    # | examples:
    # |   - Tests
    'label': "_GroupstepPropertiesGroup1180",
    # | The name to give to this group of steps
    # |
    # | examples:
    # |   - Tests
    'name': "_GroupstepPropertiesGroup1180",
    # | Whether to proceed with this step and further steps if a step named in the depends_on attribute fails
    # |
    # | default: False
    'allow_dependency_failure': "_AllowDependencyFailure",
    # | Array of notification options for this step
    'notify': "_BuildNotify",
    # | Whether this step should be skipped. Passing a string provides a reason for skipping this command
    # |
    # | examples:
    # |   - true
    # |   - false
    # |   - My reason
    # |
    # | Aggregation type: anyOf
    'skip': "_Skip",
    # | A list of steps
    # |
    # | minItems: 1
    # |
    # | Required property
    'steps': Required[list["_GroupStepStepsItem"]],
}, total=False)


_GroupStepStepsItem = Union["_BlockStep", "_NestedBlockStep", "_StringBlockStep", "_InputStep", "_NestedInputStep", "_StringInputStep", "_CommandStep", "_NestedCommandStep", "_WaitStep", "_NestedWaitStep", "_StringWaitStep", "_TriggerStep", "_NestedTriggerStep"]
""" Aggregation type: anyOf """



_GroupstepPropertiesGroup1180 = Union[str, None]
"""
The name to give to this group of steps

examples:
  - Tests
"""



_IfName = str
"""
A boolean expression that omits the step when false

examples:
  - build.message != 'skip me'
  - build.branch == 'master'
"""



_InputStep = TypedDict('_InputStep', {
    # | Whether to proceed with this step and further steps if a step named in the depends_on attribute fails
    # |
    # | default: False
    'allow_dependency_failure': "_AllowDependencyFailure",
    # | The label of the input step
    'input': str,
    # | Which branches will include this step in their builds
    # |
    # | examples:
    # |   - master
    # |   - - feature/*
    # |     - chore/*
    # |
    # | Aggregation type: anyOf
    'branches': "_Branches",
    # | The step keys for a step to depend on
    # |
    # | Aggregation type: anyOf
    'depends_on': "_DependsOn",
    # | A list of input fields required to be filled out before unblocking the step
    'fields': "_Fields",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'key': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'identifier': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'id': "_Key",
    # | The label of the input step
    'label': "_InputstepPropertiesInput",
    # | The label of the input step
    'name': "_InputstepPropertiesInput",
    # | The instructional message displayed in the dialog box when the unblock step is activated
    # |
    # | examples:
    # |   - Release to production?
    'prompt': "_Prompt",
    'type': "_InputStepType",
}, total=False)


_InputStepType = Union[Literal['input']]
_INPUTSTEPTYPE_INPUT: Literal['input'] = "input"
"""The values for the '_InputStepType' enum"""



_InputstepPropertiesInput = str
""" The label of the input step """



_JsonSchemaForBuildkitePipelineConfigurationFilesStepsItem = Union["_BlockStep", "_NestedBlockStep", "_StringBlockStep", "_InputStep", "_NestedInputStep", "_StringInputStep", "_CommandStep", "_NestedCommandStep", "_WaitStep", "_NestedWaitStep", "_StringWaitStep", "_TriggerStep", "_NestedTriggerStep", "_GroupStep"]
""" Aggregation type: anyOf """



_Key = str
"""
A unique identifier for a step, must not resemble a UUID

examples:
  - deploy-staging
  - test-integration
not:
  pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
"""



_Label = str
"""
The label that will be displayed in the pipeline visualisation in Buildkite. Supports emoji.

examples:
  - ':docker: Build'
"""



_MatrixElement = Union[str, int, bool]
""" Aggregation type: oneOf """



class _NestedBlockStep(TypedDict, total=False):
    block: "_BlockStep"


class _NestedCommandStep(TypedDict, total=False):
    command: "_CommandStep"
    commands: "_CommandStep"
    script: "_CommandStep"


class _NestedInputStep(TypedDict, total=False):
    input: "_InputStep"


class _NestedTriggerStep(TypedDict, total=False):
    trigger: "_TriggerStep"


class _NestedWaitStep(TypedDict, total=False):
    wait: "_WaitStep"
    waiter: "_WaitStep"


_Prompt = str
"""
The instructional message displayed in the dialog box when the unblock step is activated

examples:
  - Release to production?
"""



_Skip = Union["_SkipAnyof0", "_SkipAnyof1"]
"""
Whether this step should be skipped. Passing a string provides a reason for skipping this command

examples:
  - true
  - false
  - My reason

Aggregation type: anyOf
"""



_SkipAnyof0 = bool
"""
examples:
  - true
  - false
  - My reason
"""



_SkipAnyof1 = str
"""
examples:
  - true
  - false
  - My reason
"""



_SoftFail = Union["_SoftFailAnyof0", list["_SoftFailAnyof1Item"]]
"""
The conditions for marking the step as a soft-fail.

Aggregation type: anyOf
"""



_SoftFailAnyof0 = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
_SOFTFAILANYOF0_TRUE: Literal[True] = True
"""The values for the '_SoftFailAnyof0' enum"""
_SOFTFAILANYOF0_FALSE: Literal[False] = False
"""The values for the '_SoftFailAnyof0' enum"""
_SOFTFAILANYOF0_TRUE4688: Literal['true'] = "true"
"""The values for the '_SoftFailAnyof0' enum"""
_SOFTFAILANYOF0_FALSE8586: Literal['false'] = "false"
"""The values for the '_SoftFailAnyof0' enum"""



class _SoftFailAnyof1Item(TypedDict, total=False):
    exit_status: "_SoftFailAnyof1ItemExitStatus"
    """
    The exit status number that will cause this job to soft-fail

    Aggregation type: anyOf
    """



_SoftFailAnyof1ItemExitStatus = Union["_SoftFailAnyof1ItemExitStatusAnyof0", int]
"""
The exit status number that will cause this job to soft-fail

Aggregation type: anyOf
"""



_SoftFailAnyof1ItemExitStatusAnyof0 = Union[Literal['*']]
_SOFTFAILANYOF1ITEMEXITSTATUSANYOF0__ASTERISK_: Literal['*'] = "*"
"""The values for the '_SoftFailAnyof1ItemExitStatusAnyof0' enum"""



_StringBlockStep = Union[Literal['block']]
""" Pauses the execution of a build and waits on a user to unblock it """
_STRINGBLOCKSTEP_BLOCK: Literal['block'] = "block"
"""The values for the 'Pauses the execution of a build and waits on a user to unblock it' enum"""



_StringInputStep = Union[Literal['input']]
""" Pauses the execution of a build and waits on a user to unblock it """
_STRINGINPUTSTEP_INPUT: Literal['input'] = "input"
"""The values for the 'Pauses the execution of a build and waits on a user to unblock it' enum"""



_StringWaitStep = Union[Literal['wait'], Literal['waiter']]
""" Waits for previous steps to pass before continuing """
_STRINGWAITSTEP_WAIT: Literal['wait'] = "wait"
"""The values for the 'Waits for previous steps to pass before continuing' enum"""
_STRINGWAITSTEP_WAITER: Literal['waiter'] = "waiter"
"""The values for the 'Waits for previous steps to pass before continuing' enum"""



_TRIGGER_STEP_ASYNC_DEFAULT = False
""" Default value of the field path 'trigger step async' """



_TRIGGER_STEP_BUILD_BRANCH_DEFAULT = 'master'
""" Default value of the field path 'trigger step build branch' """



_TRIGGER_STEP_BUILD_COMMIT_DEFAULT = 'HEAD'
""" Default value of the field path 'trigger step build commit' """



_TRIGGER_STEP_BUILD_MESSAGE_DEFAULT = 'The label of the trigger step'
""" Default value of the field path 'trigger step build message' """



_TRIGGER_STEP_SOFT_FAIL_DEFAULT = False
""" Default value of the field path 'trigger step soft_fail' """



_TriggerStep = TypedDict('_TriggerStep', {
    # | Whether to proceed with this step and further steps if a step named in the depends_on attribute fails
    # |
    # | default: False
    'allow_dependency_failure': "_AllowDependencyFailure",
    # | Whether to continue the build without waiting for the triggered step to complete
    # |
    # | default: False
    'async': "_TriggerStepAsync",
    # | Which branches will include this step in their builds
    # |
    # | examples:
    # |   - master
    # |   - - feature/*
    # |     - chore/*
    # |
    # | Aggregation type: anyOf
    'branches': "_Branches",
    # | Properties of the build that will be created when the step is triggered
    'build': "_TriggerStepBuild",
    # | The step keys for a step to depend on
    # |
    # | Aggregation type: anyOf
    'depends_on': "_DependsOn",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'key': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'identifier': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'id': "_Key",
    # | The label that will be displayed in the pipeline visualisation in Buildkite. Supports emoji.
    # |
    # | examples:
    # |   - ':docker: Build'
    'label': "_Label",
    # | The label that will be displayed in the pipeline visualisation in Buildkite. Supports emoji.
    # |
    # | examples:
    # |   - ':docker: Build'
    'name': "_Label",
    'type': "_TriggerStepType",
    # | The slug of the pipeline to create a build
    # |
    # | Required property
    'trigger': Required[str],
    # | Whether this step should be skipped. Passing a string provides a reason for skipping this command
    # |
    # | examples:
    # |   - true
    # |   - false
    # |   - My reason
    # |
    # | Aggregation type: anyOf
    'skip': "_Skip",
    # | The conditions for marking the step as a soft-fail.
    # |
    # | default: False
    'soft_fail': "_TriggerStepSoftFail",
}, total=False)


_TriggerStepAsync = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Whether to continue the build without waiting for the triggered step to complete

default: False
"""
_TRIGGERSTEPASYNC_TRUE: Literal[True] = True
"""The values for the 'Whether to continue the build without waiting for the triggered step to complete' enum"""
_TRIGGERSTEPASYNC_FALSE: Literal[False] = False
"""The values for the 'Whether to continue the build without waiting for the triggered step to complete' enum"""
_TRIGGERSTEPASYNC_TRUE3069: Literal['true'] = "true"
"""The values for the 'Whether to continue the build without waiting for the triggered step to complete' enum"""
_TRIGGERSTEPASYNC_FALSE8372: Literal['false'] = "false"
"""The values for the 'Whether to continue the build without waiting for the triggered step to complete' enum"""



class _TriggerStepBuild(TypedDict, total=False):
    """ Properties of the build that will be created when the step is triggered """

    branch: str
    """
    The branch for the build

    default: master
    examples:
      - master
      - feature/xyz
    """

    commit: str
    """
    The commit hash for the build

    default: HEAD
    examples:
      - HEAD
      - b5fb108
    """

    env: "_Env"
    """
    Environment variables for this step

    examples:
      - NODE_ENV: test
    """

    message: str
    """
    The message for the build (supports emoji)

    default: The label of the trigger step
    examples:
      - 'Deployment 123 :rocket:'
    """

    meta_data: dict[str, Any]
    """
    Meta-data for the build

    examples:
      - server: i-b244e37160c
    """



_TriggerStepSoftFail = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
The conditions for marking the step as a soft-fail.

default: False
"""
_TRIGGERSTEPSOFTFAIL_TRUE: Literal[True] = True
"""The values for the 'The conditions for marking the step as a soft-fail' enum"""
_TRIGGERSTEPSOFTFAIL_FALSE: Literal[False] = False
"""The values for the 'The conditions for marking the step as a soft-fail' enum"""
_TRIGGERSTEPSOFTFAIL_TRUE7947: Literal['true'] = "true"
"""The values for the 'The conditions for marking the step as a soft-fail' enum"""
_TRIGGERSTEPSOFTFAIL_FALSE6864: Literal['false'] = "false"
"""The values for the 'The conditions for marking the step as a soft-fail' enum"""



_TriggerStepType = Union[Literal['trigger']]
_TRIGGERSTEPTYPE_TRIGGER: Literal['trigger'] = "trigger"
"""The values for the '_TriggerStepType' enum"""



_WAIT_STEP_CONTINUE_ON_FAILURE_DEFAULT = False
""" Default value of the field path 'wait step continue_on_failure' """



_WaitStep = TypedDict('_WaitStep', {
    # | Whether to proceed with this step and further steps if a step named in the depends_on attribute fails
    # |
    # | default: False
    'allow_dependency_failure': "_AllowDependencyFailure",
    # | Which branches will include this step in their builds
    # |
    # | examples:
    # |   - master
    # |   - - feature/*
    # |     - chore/*
    # |
    # | Aggregation type: anyOf
    'branches': "_Branches",
    # | Continue to the next steps, even if the previous group of steps fail
    # |
    # | default: False
    'continue_on_failure': "_WaitStepContinueOnFailure",
    # | The step keys for a step to depend on
    # |
    # | Aggregation type: anyOf
    'depends_on': "_DependsOn",
    # | A boolean expression that omits the step when false
    # |
    # | examples:
    # |   - build.message != 'skip me'
    # |   - build.branch == 'master'
    'if': "_IfName",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'key': "_Key",
    # | Waits for previous steps to pass before continuing
    'label': "_WaitstepPropertiesWait9502",
    # | Waits for previous steps to pass before continuing
    'name': "_WaitstepPropertiesWait9502",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'identifier': "_Key",
    # | A unique identifier for a step, must not resemble a UUID
    # |
    # | examples:
    # |   - deploy-staging
    # |   - test-integration
    # | not:
    # |   pattern: ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
    'id': "_Key",
    'type': "_WaitStepType",
    # | Waits for previous steps to pass before continuing
    'wait': Union[str, None],
    'waiter': Union[str, None],
}, total=False)


_WaitStepContinueOnFailure = Union[Literal[True], Literal[False], Literal['true'], Literal['false']]
"""
Continue to the next steps, even if the previous group of steps fail

default: False
"""
_WAITSTEPCONTINUEONFAILURE_TRUE: Literal[True] = True
"""The values for the 'Continue to the next steps, even if the previous group of steps fail' enum"""
_WAITSTEPCONTINUEONFAILURE_FALSE: Literal[False] = False
"""The values for the 'Continue to the next steps, even if the previous group of steps fail' enum"""
_WAITSTEPCONTINUEONFAILURE_TRUE9799: Literal['true'] = "true"
"""The values for the 'Continue to the next steps, even if the previous group of steps fail' enum"""
_WAITSTEPCONTINUEONFAILURE_FALSE7914: Literal['false'] = "false"
"""The values for the 'Continue to the next steps, even if the previous group of steps fail' enum"""



_WaitStepType = Union[Literal['wait'], Literal['waiter']]
_WAITSTEPTYPE_WAIT: Literal['wait'] = "wait"
"""The values for the '_WaitStepType' enum"""
_WAITSTEPTYPE_WAITER: Literal['waiter'] = "waiter"
"""The values for the '_WaitStepType' enum"""



_WaitstepPropertiesWait9502 = Union[str, None]
""" Waits for previous steps to pass before continuing """
