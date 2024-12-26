// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    schema, err := UnmarshalSchema(bytes)
//    bytes, err = schema.Marshal()

package buildkite

import "bytes"
import "errors"

import "encoding/json"

func UnmarshalSchema(data []byte) (Schema, error) {
	var r Schema
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Schema) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type Schema struct {
	Title       string           `json:"title"`
	Schema      string           `json:"$schema"`
	FileMatch   []string         `json:"fileMatch"`
	Type        string           `json:"type"`
	Required    []string         `json:"required"`
	Definitions Definitions      `json:"definitions"`
	Properties  SchemaProperties `json:"properties"`
}

type Definitions struct {
	AllowDependencyFailure AllowDependencyFailure `json:"allowDependencyFailure"`
	Agents                 DefinitionsAgents      `json:"agents"`
	AgentsObject           AgentsObject           `json:"agentsObject"`
	AgentsList             AgentsList             `json:"agentsList"`
	AutomaticRetry         AutomaticRetry         `json:"automaticRetry"`
	Branches               Branches               `json:"branches"`
	Cache                  Cache                  `json:"cache"`
	CancelOnBuildFailing   AllowDependencyFailure `json:"cancelOnBuildFailing"`
	DependsOn              DependsOn              `json:"dependsOn"`
	Env                    Env                    `json:"env"`
	If                     AgentsList             `json:"if"`
	Key                    AgentsList             `json:"key"`
	Label                  AgentsList             `json:"label"`
	BuildNotify            BuildNotify            `json:"buildNotify"`
	Fields                 Fields                 `json:"fields"`
	MatrixElement          MatrixElement          `json:"matrixElement"`
	Prompt                 AgentsList             `json:"prompt"`
	Skip                   Skip                   `json:"skip"`
	SoftFail               SoftFail               `json:"softFail"`
	BlockStep              Step                   `json:"blockStep"`
	NestedBlockStep        NestedBlockStep        `json:"nestedBlockStep"`
	StringBlockStep        StringBlockStep        `json:"stringBlockStep"`
	InputStep              Step                   `json:"inputStep"`
	NestedInputStep        NestedInputStep        `json:"nestedInputStep"`
	StringInputStep        StringBlockStep        `json:"stringInputStep"`
	CommandStep            CommandStep            `json:"commandStep"`
	NestedCommandStep      NestedCommandStep      `json:"nestedCommandStep"`
	StringWaitStep         StringBlockStep        `json:"stringWaitStep"`
	WaitStep               Step                   `json:"waitStep"`
	NestedWaitStep         NestedWaitStep         `json:"nestedWaitStep"`
	TriggerStep            TriggerStep            `json:"triggerStep"`
	NestedTriggerStep      NestedTriggerStep      `json:"nestedTriggerStep"`
	GroupStep              GroupStep              `json:"groupStep"`
}

type DefinitionsAgents struct {
	OneOf []AgentsElement `json:"oneOf"`
}

type AgentsElement struct {
	Ref string `json:"$ref"`
}

type AgentsList struct {
	Type        AgentsListType `json:"type"`
	Description string         `json:"description"`
	Examples    []string       `json:"examples"`
	Items       *ItemsElement  `json:"items,omitempty"`
	Enum        []string       `json:"enum,omitempty"`
	Format      *string        `json:"format,omitempty"`
	Pattern     *string        `json:"pattern,omitempty"`
	Not         *Not           `json:"not,omitempty"`
	Default     *string        `json:"default,omitempty"`
}

type ItemsElement struct {
	Type ItemsType `json:"type"`
}

type Not struct {
	Pattern string `json:"pattern"`
}

type AgentsObject struct {
	Type        string                `json:"type"`
	Description string                `json:"description"`
	Examples    []AgentsObjectExample `json:"examples"`
}

type AgentsObjectExample struct {
	Queue *string `json:"queue,omitempty"`
	Ruby  *string `json:"ruby,omitempty"`
}

type AllowDependencyFailure struct {
	Enum        []Enum `json:"enum"`
	Description string `json:"description"`
	Default     bool   `json:"default"`
}

type AutomaticRetry struct {
	Type                 string                   `json:"type"`
	Properties           AutomaticRetryProperties `json:"properties"`
	AdditionalProperties bool                     `json:"additionalProperties"`
}

type AutomaticRetryProperties struct {
	ExitStatus   PurpleExitStatus `json:"exit_status"`
	Limit        Limit            `json:"limit"`
	Signal       AgentsList       `json:"signal"`
	SignalReason StringBlockStep  `json:"signal_reason"`
}

type PurpleExitStatus struct {
	Description string            `json:"description"`
	AnyOf       []ExitStatusAnyOf `json:"anyOf"`
}

type ExitStatusAnyOf struct {
	Type  string        `json:"type"`
	Enum  []string      `json:"enum,omitempty"`
	Items *ItemsElement `json:"items,omitempty"`
}

type Limit struct {
	Type        ItemsType `json:"type"`
	Description string    `json:"description"`
	Minimum     int64     `json:"minimum"`
	Maximum     *int64    `json:"maximum,omitempty"`
	Examples    []int64   `json:"examples,omitempty"`
}

type StringBlockStep struct {
	Description string    `json:"description"`
	Type        ItemsType `json:"type"`
	Enum        []string  `json:"enum,omitempty"`
	Default     *string   `json:"default,omitempty"`
	Examples    []string  `json:"examples,omitempty"`
}

type Step struct {
	Type                 string              `json:"type"`
	Properties           BlockStepProperties `json:"properties"`
	AdditionalProperties bool                `json:"additionalProperties"`
}

type BlockStepProperties struct {
	AllowDependencyFailure AgentsElement           `json:"allow_dependency_failure"`
	Block                  *Block                  `json:"block,omitempty"`
	BlockedState           *StringBlockStep        `json:"blocked_state,omitempty"`
	Branches               AgentsElement           `json:"branches"`
	DependsOn              AgentsElement           `json:"depends_on"`
	Fields                 *AgentsElement          `json:"fields,omitempty"`
	If                     AgentsElement           `json:"if"`
	Key                    AgentsElement           `json:"key"`
	Identifier             AgentsElement           `json:"identifier"`
	ID                     ID                      `json:"id"`
	Label                  AgentsElement           `json:"label"`
	Name                   AgentsElement           `json:"name"`
	Prompt                 *AgentsElement          `json:"prompt,omitempty"`
	Type                   TypeElement             `json:"type"`
	Input                  *Block                  `json:"input,omitempty"`
	ContinueOnFailure      *AllowDependencyFailure `json:"continue_on_failure,omitempty"`
	Wait                   *Wait                   `json:"wait,omitempty"`
	Waiter                 *Waiter                 `json:"waiter,omitempty"`
}

type Block struct {
	Type        ItemsType `json:"type"`
	Description string    `json:"description"`
}

type ID struct {
	Ref        string `json:"$ref"`
	Deprecated bool   `json:"deprecated"`
}

type TypeElement struct {
	Type ItemsType `json:"type"`
	Enum []string  `json:"enum,omitempty"`
}

type Wait struct {
	Description string   `json:"description"`
	Type        []string `json:"type"`
}

type Waiter struct {
	Type []string `json:"type"`
}

type Branches struct {
	Description string            `json:"description"`
	AnyOf       []AnyOf           `json:"anyOf"`
	Examples    []BranchesExample `json:"examples"`
}

type AnyOf struct {
	Type  AgentsListType `json:"type"`
	Items *ItemsElement  `json:"items,omitempty"`
}

type BuildNotify struct {
	Type        AgentsListType   `json:"type"`
	Description string           `json:"description"`
	Items       BuildNotifyItems `json:"items"`
}

type BuildNotifyItems struct {
	OneOf []PurpleOneOf `json:"oneOf"`
}

type PurpleOneOf struct {
	Type                 string            `json:"type"`
	Enum                 []string          `json:"enum,omitempty"`
	Properties           *PurpleProperties `json:"properties,omitempty"`
	AdditionalProperties *bool             `json:"additionalProperties,omitempty"`
}

type PurpleProperties struct {
	Email                *ItemsElement       `json:"email,omitempty"`
	If                   AgentsElement       `json:"if"`
	BasecampCampfire     *ItemsElement       `json:"basecamp_campfire,omitempty"`
	Slack                *PurpleSlack        `json:"slack,omitempty"`
	Webhook              *ItemsElement       `json:"webhook,omitempty"`
	PagerdutyChangeEvent *ItemsElement       `json:"pagerduty_change_event,omitempty"`
	GithubCommitStatus   *GithubCommitStatus `json:"github_commit_status,omitempty"`
	GithubCheck          *GithubCheck        `json:"github_check,omitempty"`
}

type GithubCheck struct {
	Type       string                `json:"type"`
	Properties GithubCheckProperties `json:"properties"`
}

type GithubCheckProperties struct {
	Context Block `json:"context"`
}

type GithubCommitStatus struct {
	Type                 string                `json:"type"`
	Properties           GithubCheckProperties `json:"properties"`
	AdditionalProperties bool                  `json:"additionalProperties"`
}

type PurpleSlack struct {
	OneOf []FluffyOneOf `json:"oneOf"`
}

type FluffyOneOf struct {
	Type       string            `json:"type"`
	Properties *FluffyProperties `json:"properties,omitempty"`
}

type FluffyProperties struct {
	Channels AnyOf        `json:"channels"`
	Message  ItemsElement `json:"message"`
}

type Cache struct {
	Description string         `json:"description"`
	AnyOf       []CacheAnyOf   `json:"anyOf"`
	Examples    []CacheExample `json:"examples"`
}

type CacheAnyOf struct {
	Type       string               `json:"type"`
	Items      *ItemsElement        `json:"items,omitempty"`
	Properties *TentacledProperties `json:"properties,omitempty"`
	Required   []string             `json:"required,omitempty"`
}

type TentacledProperties struct {
	Paths AnyOf        `json:"paths"`
	Size  Size         `json:"size"`
	Name  ItemsElement `json:"name"`
}

type Size struct {
	Type    ItemsType `json:"type"`
	Pattern string    `json:"pattern"`
}

type PurpleExample struct {
	Name  string   `json:"name"`
	Size  string   `json:"size"`
	Paths []string `json:"paths"`
}

type CommandStep struct {
	Type                 string                `json:"type"`
	Properties           CommandStepProperties `json:"properties"`
	AdditionalProperties bool                  `json:"additionalProperties"`
}

type CommandStepProperties struct {
	Agents                 AgentsElement `json:"agents"`
	AllowDependencyFailure AgentsElement `json:"allow_dependency_failure"`
	ArtifactPaths          ArtifactPaths `json:"artifact_paths"`
	Branches               AgentsElement `json:"branches"`
	Cache                  AgentsElement `json:"cache"`
	CancelOnBuildFailing   AgentsElement `json:"cancel_on_build_failing"`
	Command                Command       `json:"command"`
	Commands               Commands      `json:"commands"`
	Concurrency            Concurrency   `json:"concurrency"`
	ConcurrencyGroup       AgentsList    `json:"concurrency_group"`
	ConcurrencyMethod      AgentsList    `json:"concurrency_method"`
	DependsOn              AgentsElement `json:"depends_on"`
	Env                    AgentsElement `json:"env"`
	If                     AgentsElement `json:"if"`
	Key                    AgentsElement `json:"key"`
	Identifier             AgentsElement `json:"identifier"`
	ID                     ID            `json:"id"`
	Label                  AgentsElement `json:"label"`
	Signature              Signature     `json:"signature"`
	Matrix                 Matrix        `json:"matrix"`
	Name                   AgentsElement `json:"name"`
	Notify                 Notify        `json:"notify"`
	Parallelism            Concurrency   `json:"parallelism"`
	Plugins                Plugins       `json:"plugins"`
	SoftFail               AgentsElement `json:"soft_fail"`
	Retry                  Retry         `json:"retry"`
	Skip                   AgentsElement `json:"skip"`
	TimeoutInMinutes       Limit         `json:"timeout_in_minutes"`
	Type                   TypeElement   `json:"type"`
	Priority               Concurrency   `json:"priority"`
}

type ArtifactPaths struct {
	AnyOf       []AnyOf    `json:"anyOf"`
	Description string     `json:"description"`
	Examples    [][]string `json:"examples"`
}

type Command struct {
	Description string  `json:"description"`
	AnyOf       []AnyOf `json:"anyOf"`
}

type Commands struct {
	Description string `json:"description"`
	Ref         string `json:"$ref"`
}

type Concurrency struct {
	Type        ItemsType `json:"type"`
	Description string    `json:"description"`
	Examples    []int64   `json:"examples"`
}

type Matrix struct {
	OneOf []MatrixOneOf `json:"oneOf"`
}

type MatrixOneOf struct {
	Type        string            `json:"type"`
	Description string            `json:"description"`
	Items       *AgentsElement    `json:"items,omitempty"`
	Examples    [][]string        `json:"examples,omitempty"`
	Properties  *StickyProperties `json:"properties,omitempty"`
	Required    []string          `json:"required,omitempty"`
}

type StickyProperties struct {
	Setup       Setup       `json:"setup"`
	Adjustments Adjustments `json:"adjustments"`
}

type Adjustments struct {
	Type        AgentsListType   `json:"type"`
	Description string           `json:"description"`
	Items       AdjustmentsItems `json:"items"`
}

type AdjustmentsItems struct {
	Type        string           `json:"type"`
	Description string           `json:"description"`
	Properties  IndigoProperties `json:"properties"`
	Required    []string         `json:"required"`
}

type IndigoProperties struct {
	With     With          `json:"with"`
	Skip     AgentsElement `json:"skip"`
	SoftFail AgentsElement `json:"soft_fail"`
}

type With struct {
	OneOf []WithOneOf `json:"oneOf"`
}

type WithOneOf struct {
	Type                 string          `json:"type"`
	Description          string          `json:"description"`
	Items                *AgentsElement  `json:"items,omitempty"`
	PropertyNames        *Block          `json:"propertyNames,omitempty"`
	AdditionalProperties *Block          `json:"additionalProperties,omitempty"`
	Examples             []FluffyExample `json:"examples,omitempty"`
}

type FluffyExample struct {
	OS   string `json:"os"`
	Arch string `json:"arch"`
}

type Setup struct {
	OneOf []SetupOneOf `json:"oneOf"`
}

type SetupOneOf struct {
	Type                 string                `json:"type"`
	Description          string                `json:"description"`
	Items                *AgentsElement        `json:"items,omitempty"`
	Examples             []OneOfExampleUnion   `json:"examples"`
	PropertyNames        *PropertyNames        `json:"propertyNames,omitempty"`
	AdditionalProperties *AdditionalProperties `json:"additionalProperties,omitempty"`
}

type AdditionalProperties struct {
	Type        AgentsListType `json:"type"`
	Description string         `json:"description"`
	Items       AgentsElement  `json:"items"`
}

type TentacledExample struct {
	OS   []string `json:"os"`
	Arch []string `json:"arch"`
}

type PropertyNames struct {
	Type        ItemsType `json:"type"`
	Description string    `json:"description"`
	Pattern     string    `json:"pattern"`
}

type Notify struct {
	Type        AgentsListType `json:"type"`
	Description string         `json:"description"`
	Items       NotifyItems    `json:"items"`
}

type NotifyItems struct {
	OneOf []TentacledOneOf `json:"oneOf"`
}

type TentacledOneOf struct {
	Type                 string              `json:"type"`
	Enum                 []string            `json:"enum,omitempty"`
	Properties           *IndecentProperties `json:"properties,omitempty"`
	AdditionalProperties *bool               `json:"additionalProperties,omitempty"`
}

type IndecentProperties struct {
	BasecampCampfire   *ItemsElement       `json:"basecamp_campfire,omitempty"`
	If                 AgentsElement       `json:"if"`
	Slack              *FluffySlack        `json:"slack,omitempty"`
	GithubCommitStatus *GithubCommitStatus `json:"github_commit_status,omitempty"`
	GithubCheck        *GithubCheck        `json:"github_check,omitempty"`
}

type FluffySlack struct {
	OneOf []StickyOneOf `json:"oneOf"`
}

type StickyOneOf struct {
	Type                 string            `json:"type"`
	Properties           *FluffyProperties `json:"properties,omitempty"`
	AdditionalProperties *bool             `json:"additionalProperties,omitempty"`
}

type Plugins struct {
	AnyOf []PluginsAnyOf `json:"anyOf"`
}

type PluginsAnyOf struct {
	Type        string       `json:"type"`
	Description string       `json:"description"`
	Items       *PurpleItems `json:"items,omitempty"`
}

type PurpleItems struct {
	OneOf []IndigoOneOf `json:"oneOf"`
}

type IndigoOneOf struct {
	Type          string          `json:"type"`
	MaxProperties *int64          `json:"maxProperties,omitempty"`
	Examples      []StickyExample `json:"examples,omitempty"`
}

type StickyExample struct {
	DockerComposeV100 DockerComposeV100 `json:"docker-compose#v1.0.0"`
}

type DockerComposeV100 struct {
	Run string `json:"run"`
}

type Retry struct {
	Type                 string          `json:"type"`
	Description          string          `json:"description"`
	Properties           RetryProperties `json:"properties"`
	AdditionalProperties bool            `json:"additionalProperties"`
}

type RetryProperties struct {
	Automatic Automatic `json:"automatic"`
	Manual    Manual    `json:"manual"`
}

type Automatic struct {
	AnyOf       []AutomaticAnyOf `json:"anyOf"`
	Description string           `json:"description"`
	Default     []DefaultElement `json:"default"`
}

type AutomaticAnyOf struct {
	Enum  []Enum          `json:"enum,omitempty"`
	Ref   *string         `json:"$ref,omitempty"`
	Type  *AgentsListType `json:"type,omitempty"`
	Items *AgentsElement  `json:"items,omitempty"`
}

type DefaultElement struct {
	ExitStatus string `json:"exit_status"`
	Limit      int64  `json:"limit"`
}

type Manual struct {
	Description string        `json:"description"`
	AnyOf       []ManualAnyOf `json:"anyOf"`
	Default     bool          `json:"default"`
}

type ManualAnyOf struct {
	Enum                 []Enum               `json:"enum,omitempty"`
	Type                 *string              `json:"type,omitempty"`
	Properties           *HilariousProperties `json:"properties,omitempty"`
	AdditionalProperties *bool                `json:"additionalProperties,omitempty"`
}

type HilariousProperties struct {
	Allowed        AllowDependencyFailure `json:"allowed"`
	PermitOnPassed AllowDependencyFailure `json:"permit_on_passed"`
	Reason         AgentsList             `json:"reason"`
}

type Signature struct {
	Type        string              `json:"type"`
	Description string              `json:"description"`
	Properties  SignatureProperties `json:"properties"`
}

type SignatureProperties struct {
	Algorithm    AgentsList   `json:"algorithm"`
	Value        Block        `json:"value"`
	SignedFields SignedFields `json:"signed_fields"`
}

type SignedFields struct {
	Type        AgentsListType `json:"type"`
	Description string         `json:"description"`
	Items       ItemsElement   `json:"items"`
	Examples    [][]string     `json:"examples"`
}

type DependsOn struct {
	Description string           `json:"description"`
	AnyOf       []DependsOnAnyOf `json:"anyOf"`
}

type DependsOnAnyOf struct {
	Type  string       `json:"type"`
	Items *FluffyItems `json:"items,omitempty"`
}

type FluffyItems struct {
	AnyOf []ItemsAnyOf `json:"anyOf"`
}

type ItemsAnyOf struct {
	Type                 string               `json:"type"`
	Properties           *AmbitiousProperties `json:"properties,omitempty"`
	AdditionalProperties *bool                `json:"additionalProperties,omitempty"`
}

type AmbitiousProperties struct {
	Step         ItemsElement `json:"step"`
	AllowFailure AllowFailure `json:"allow_failure"`
}

type AllowFailure struct {
	Enum    []Enum `json:"enum"`
	Default bool   `json:"default"`
}

type Env struct {
	Type        string       `json:"type"`
	Description string       `json:"description"`
	Examples    []EnvExample `json:"examples"`
}

type EnvExample struct {
	NodeEnv string `json:"NODE_ENV"`
}

type Fields struct {
	Type        AgentsListType `json:"type"`
	Description string         `json:"description"`
	Items       FieldsItems    `json:"items"`
}

type FieldsItems struct {
	OneOf []IndecentOneOf `json:"oneOf"`
}

type IndecentOneOf struct {
	Type                 string            `json:"type"`
	Properties           CunningProperties `json:"properties"`
	AdditionalProperties bool              `json:"additionalProperties"`
	Required             []string          `json:"required"`
}

type CunningProperties struct {
	Text     *AgentsList             `json:"text,omitempty"`
	Key      AgentsList              `json:"key"`
	Hint     AgentsList              `json:"hint"`
	Format   *AgentsList             `json:"format,omitempty"`
	Required AllowDependencyFailure  `json:"required"`
	Default  PropertiesDefault       `json:"default"`
	Select   *AgentsList             `json:"select,omitempty"`
	Multiple *AllowDependencyFailure `json:"multiple,omitempty"`
	Options  *Options                `json:"options,omitempty"`
}

type PropertiesDefault struct {
	Type        *ItemsType        `json:"type,omitempty"`
	Description string            `json:"description"`
	Examples    []BranchesExample `json:"examples"`
	OneOf       []AnyOf           `json:"oneOf,omitempty"`
}

type Options struct {
	Type     AgentsListType `json:"type"`
	MinItems int64          `json:"minItems"`
	Items    OptionsItems   `json:"items"`
}

type OptionsItems struct {
	Type                 string            `json:"type"`
	Properties           MagentaProperties `json:"properties"`
	AdditionalProperties bool              `json:"additionalProperties"`
	Required             []string          `json:"required"`
}

type MagentaProperties struct {
	Label    AgentsList             `json:"label"`
	Value    AgentsList             `json:"value"`
	Hint     AgentsList             `json:"hint"`
	Required AllowDependencyFailure `json:"required"`
}

type GroupStep struct {
	Type                 string              `json:"type"`
	Properties           GroupStepProperties `json:"properties"`
	Required             []string            `json:"required"`
	AdditionalProperties bool                `json:"additionalProperties"`
}

type GroupStepProperties struct {
	DependsOn              AgentsElement `json:"depends_on"`
	Group                  Group         `json:"group"`
	If                     AgentsElement `json:"if"`
	Key                    AgentsElement `json:"key"`
	Identifier             AgentsElement `json:"identifier"`
	ID                     ID            `json:"id"`
	Label                  AgentsElement `json:"label"`
	Name                   AgentsElement `json:"name"`
	AllowDependencyFailure AgentsElement `json:"allow_dependency_failure"`
	Notify                 AgentsElement `json:"notify"`
	Skip                   AgentsElement `json:"skip"`
	Steps                  Steps         `json:"steps"`
}

type Group struct {
	Type        []string `json:"type"`
	Description string   `json:"description"`
	Examples    []string `json:"examples"`
}

type Steps struct {
	Type        AgentsListType `json:"type"`
	Description string         `json:"description"`
	Items       StepsItems     `json:"items"`
	MinItems    *int64         `json:"minItems,omitempty"`
}

type StepsItems struct {
	AnyOf []AgentsElement `json:"anyOf"`
}

type MatrixElement struct {
	OneOf []ItemsElement `json:"oneOf"`
}

type NestedBlockStep struct {
	Type                 string                    `json:"type"`
	Properties           NestedBlockStepProperties `json:"properties"`
	AdditionalProperties bool                      `json:"additionalProperties"`
}

type NestedBlockStepProperties struct {
	Block AgentsElement `json:"block"`
}

type NestedCommandStep struct {
	Type                 string                      `json:"type"`
	Properties           NestedCommandStepProperties `json:"properties"`
	AdditionalProperties bool                        `json:"additionalProperties"`
}

type NestedCommandStepProperties struct {
	Command  AgentsElement `json:"command"`
	Commands AgentsElement `json:"commands"`
	Script   AgentsElement `json:"script"`
}

type NestedInputStep struct {
	Type                 string                    `json:"type"`
	Properties           NestedInputStepProperties `json:"properties"`
	AdditionalProperties bool                      `json:"additionalProperties"`
}

type NestedInputStepProperties struct {
	Input AgentsElement `json:"input"`
}

type NestedTriggerStep struct {
	Type                 string                      `json:"type"`
	Properties           NestedTriggerStepProperties `json:"properties"`
	AdditionalProperties bool                        `json:"additionalProperties"`
}

type NestedTriggerStepProperties struct {
	Trigger AgentsElement `json:"trigger"`
}

type NestedWaitStep struct {
	Type                 string                   `json:"type"`
	Properties           NestedWaitStepProperties `json:"properties"`
	AdditionalProperties bool                     `json:"additionalProperties"`
}

type NestedWaitStepProperties struct {
	Wait   Commands      `json:"wait"`
	Waiter AgentsElement `json:"waiter"`
}

type Skip struct {
	AnyOf       []ItemsElement `json:"anyOf"`
	Description string         `json:"description"`
	Examples    []Enum         `json:"examples"`
}

type SoftFail struct {
	Description string          `json:"description"`
	AnyOf       []SoftFailAnyOf `json:"anyOf"`
}

type SoftFailAnyOf struct {
	Enum  []Enum          `json:"enum,omitempty"`
	Type  *AgentsListType `json:"type,omitempty"`
	Items *TentacledItems `json:"items,omitempty"`
}

type TentacledItems struct {
	Type       string           `json:"type"`
	Properties FriskyProperties `json:"properties"`
}

type FriskyProperties struct {
	ExitStatus FluffyExitStatus `json:"exit_status"`
}

type FluffyExitStatus struct {
	Description string        `json:"description"`
	AnyOf       []TypeElement `json:"anyOf"`
}

type TriggerStep struct {
	Type                 string                `json:"type"`
	Properties           TriggerStepProperties `json:"properties"`
	AdditionalProperties bool                  `json:"additionalProperties"`
	Required             []string              `json:"required"`
}

type TriggerStepProperties struct {
	AllowDependencyFailure AgentsElement          `json:"allow_dependency_failure"`
	Async                  AllowDependencyFailure `json:"async"`
	Branches               AgentsElement          `json:"branches"`
	Build                  Build                  `json:"build"`
	DependsOn              AgentsElement          `json:"depends_on"`
	If                     AgentsElement          `json:"if"`
	Key                    AgentsElement          `json:"key"`
	Identifier             AgentsElement          `json:"identifier"`
	ID                     ID                     `json:"id"`
	Label                  AgentsElement          `json:"label"`
	Name                   AgentsElement          `json:"name"`
	Type                   TypeElement            `json:"type"`
	Trigger                Block                  `json:"trigger"`
	Skip                   AgentsElement          `json:"skip"`
	SoftFail               AllowDependencyFailure `json:"soft_fail"`
}

type Build struct {
	Type                 string          `json:"type"`
	Description          string          `json:"description"`
	Properties           BuildProperties `json:"properties"`
	AdditionalProperties bool            `json:"additionalProperties"`
}

type BuildProperties struct {
	Branch   AgentsList      `json:"branch"`
	Commit   AgentsList      `json:"commit"`
	Env      AgentsElement   `json:"env"`
	Message  StringBlockStep `json:"message"`
	MetaData MetaData        `json:"meta_data"`
}

type MetaData struct {
	Type        string            `json:"type"`
	Description string            `json:"description"`
	Examples    []MetaDataExample `json:"examples"`
}

type MetaDataExample struct {
	Server string `json:"server"`
}

type SchemaProperties struct {
	Env    AgentsElement `json:"env"`
	Agents AgentsElement `json:"agents"`
	Notify AgentsElement `json:"notify"`
	Steps  Steps         `json:"steps"`
}

type ItemsType string

const (
	Boolean      ItemsType = "boolean"
	Integer      ItemsType = "integer"
	PurpleString ItemsType = "string"
)

type AgentsListType string

const (
	Array        AgentsListType = "array"
	FluffyString AgentsListType = "string"
)

type Enum struct {
	Bool   *bool
	String *string
}

func (x *Enum) UnmarshalJSON(data []byte) error {
	object, err := unmarshalUnion(data, nil, nil, &x.Bool, &x.String, false, nil, false, nil, false, nil, false, nil, false)
	if err != nil {
		return err
	}
	if object {
	}
	return nil
}

func (x *Enum) MarshalJSON() ([]byte, error) {
	return marshalUnion(nil, nil, x.Bool, x.String, false, nil, false, nil, false, nil, false, nil, false)
}

type BranchesExample struct {
	String      *string
	StringArray []string
}

func (x *BranchesExample) UnmarshalJSON(data []byte) error {
	x.StringArray = nil
	object, err := unmarshalUnion(data, nil, nil, nil, &x.String, true, &x.StringArray, false, nil, false, nil, false, nil, false)
	if err != nil {
		return err
	}
	if object {
	}
	return nil
}

func (x *BranchesExample) MarshalJSON() ([]byte, error) {
	return marshalUnion(nil, nil, nil, x.String, x.StringArray != nil, x.StringArray, false, nil, false, nil, false, nil, false)
}

type CacheExample struct {
	PurpleExample *PurpleExample
	String        *string
	StringArray   []string
}

func (x *CacheExample) UnmarshalJSON(data []byte) error {
	x.StringArray = nil
	x.PurpleExample = nil
	var c PurpleExample
	object, err := unmarshalUnion(data, nil, nil, nil, &x.String, true, &x.StringArray, true, &c, false, nil, false, nil, false)
	if err != nil {
		return err
	}
	if object {
		x.PurpleExample = &c
	}
	return nil
}

func (x *CacheExample) MarshalJSON() ([]byte, error) {
	return marshalUnion(nil, nil, nil, x.String, x.StringArray != nil, x.StringArray, x.PurpleExample != nil, x.PurpleExample, false, nil, false, nil, false)
}

type OneOfExampleUnion struct {
	StringArray      []string
	TentacledExample *TentacledExample
}

func (x *OneOfExampleUnion) UnmarshalJSON(data []byte) error {
	x.StringArray = nil
	x.TentacledExample = nil
	var c TentacledExample
	object, err := unmarshalUnion(data, nil, nil, nil, nil, true, &x.StringArray, true, &c, false, nil, false, nil, false)
	if err != nil {
		return err
	}
	if object {
		x.TentacledExample = &c
	}
	return nil
}

func (x *OneOfExampleUnion) MarshalJSON() ([]byte, error) {
	return marshalUnion(nil, nil, nil, nil, x.StringArray != nil, x.StringArray, x.TentacledExample != nil, x.TentacledExample, false, nil, false, nil, false)
}

func unmarshalUnion(data []byte, pi **int64, pf **float64, pb **bool, ps **string, haveArray bool, pa interface{}, haveObject bool, pc interface{}, haveMap bool, pm interface{}, haveEnum bool, pe interface{}, nullable bool) (bool, error) {
	if pi != nil {
			*pi = nil
	}
	if pf != nil {
			*pf = nil
	}
	if pb != nil {
			*pb = nil
	}
	if ps != nil {
			*ps = nil
	}

	dec := json.NewDecoder(bytes.NewReader(data))
	dec.UseNumber()
	tok, err := dec.Token()
	if err != nil {
			return false, err
	}

	switch v := tok.(type) {
	case json.Number:
			if pi != nil {
					i, err := v.Int64()
					if err == nil {
							*pi = &i
							return false, nil
					}
			}
			if pf != nil {
					f, err := v.Float64()
					if err == nil {
							*pf = &f
							return false, nil
					}
					return false, errors.New("Unparsable number")
			}
			return false, errors.New("Union does not contain number")
	case float64:
			return false, errors.New("Decoder should not return float64")
	case bool:
			if pb != nil {
					*pb = &v
					return false, nil
			}
			return false, errors.New("Union does not contain bool")
	case string:
			if haveEnum {
					return false, json.Unmarshal(data, pe)
			}
			if ps != nil {
					*ps = &v
					return false, nil
			}
			return false, errors.New("Union does not contain string")
	case nil:
			if nullable {
					return false, nil
			}
			return false, errors.New("Union does not contain null")
	case json.Delim:
			if v == '{' {
					if haveObject {
							return true, json.Unmarshal(data, pc)
					}
					if haveMap {
							return false, json.Unmarshal(data, pm)
					}
					return false, errors.New("Union does not contain object")
			}
			if v == '[' {
					if haveArray {
							return false, json.Unmarshal(data, pa)
					}
					return false, errors.New("Union does not contain array")
			}
			return false, errors.New("Cannot handle delimiter")
	}
	return false, errors.New("Cannot unmarshal union")

}

func marshalUnion(pi *int64, pf *float64, pb *bool, ps *string, haveArray bool, pa interface{}, haveObject bool, pc interface{}, haveMap bool, pm interface{}, haveEnum bool, pe interface{}, nullable bool) ([]byte, error) {
	if pi != nil {
			return json.Marshal(*pi)
	}
	if pf != nil {
			return json.Marshal(*pf)
	}
	if pb != nil {
			return json.Marshal(*pb)
	}
	if ps != nil {
			return json.Marshal(*ps)
	}
	if haveArray {
			return json.Marshal(pa)
	}
	if haveObject {
			return json.Marshal(pc)
	}
	if haveMap {
			return json.Marshal(pm)
	}
	if haveEnum {
			return json.Marshal(pe)
	}
	if nullable {
			return json.Marshal(nil)
	}
	return nil, errors.New("Union must not be null")
}
