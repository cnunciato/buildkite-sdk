// To parse this data:
//
//   import { Convert, Schema } from "./file";
//
//   const schema = Convert.toSchema(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface Schema {
    title:       string;
    $schema:     string;
    fileMatch:   string[];
    type:        string;
    required:    string[];
    definitions: Definitions;
    properties:  SchemaProperties;
}

export interface Definitions {
    allowDependencyFailure: AllowDependencyFailure;
    agents:                 DefinitionsAgents;
    agentsObject:           AgentsObject;
    agentsList:             AgentsList;
    automaticRetry:         AutomaticRetry;
    branches:               Branches;
    cache:                  Cache;
    cancelOnBuildFailing:   AllowDependencyFailure;
    dependsOn:              DependsOn;
    env:                    Env;
    if:                     AgentsList;
    key:                    AgentsList;
    label:                  AgentsList;
    buildNotify:            BuildNotify;
    fields:                 Fields;
    matrixElement:          MatrixElement;
    prompt:                 AgentsList;
    skip:                   Skip;
    softFail:               SoftFail;
    blockStep:              Step;
    nestedBlockStep:        NestedBlockStep;
    stringBlockStep:        StringBlockStep;
    inputStep:              Step;
    nestedInputStep:        NestedInputStep;
    stringInputStep:        StringBlockStep;
    commandStep:            CommandStep;
    nestedCommandStep:      NestedCommandStep;
    stringWaitStep:         StringBlockStep;
    waitStep:               Step;
    nestedWaitStep:         NestedWaitStep;
    triggerStep:            TriggerStep;
    nestedTriggerStep:      NestedTriggerStep;
    groupStep:              GroupStep;
}

export interface DefinitionsAgents {
    oneOf: AgentsElement[];
}

export interface AgentsElement {
    $ref: string;
}

export interface AgentsList {
    type:        AgentsListType;
    description: string;
    examples:    string[];
    items?:      ItemsElement;
    enum?:       string[];
    format?:     string;
    pattern?:    string;
    not?:        Not;
    default?:    string;
}

export interface ItemsElement {
    type: ItemsType;
}

export enum ItemsType {
    Boolean = "boolean",
    Integer = "integer",
    String = "string",
}

export interface Not {
    pattern: string;
}

export enum AgentsListType {
    Array = "array",
    String = "string",
}

export interface AgentsObject {
    type:        string;
    description: string;
    examples:    AgentsObjectExample[];
}

export interface AgentsObjectExample {
    queue?: string;
    ruby?:  string;
}

export interface AllowDependencyFailure {
    enum:        Array<boolean | string>;
    description: string;
    default:     boolean;
}

export interface AutomaticRetry {
    type:                 string;
    properties:           AutomaticRetryProperties;
    additionalProperties: boolean;
}

export interface AutomaticRetryProperties {
    exit_status:   PurpleExitStatus;
    limit:         Limit;
    signal:        AgentsList;
    signal_reason: StringBlockStep;
}

export interface PurpleExitStatus {
    description: string;
    anyOf:       ExitStatusAnyOf[];
}

export interface ExitStatusAnyOf {
    type:   string;
    enum?:  string[];
    items?: ItemsElement;
}

export interface Limit {
    type:        ItemsType;
    description: string;
    minimum:     number;
    maximum?:    number;
    examples?:   number[];
}

export interface StringBlockStep {
    description: string;
    type:        ItemsType;
    enum?:       string[];
    default?:    string;
    examples?:   string[];
}

export interface Step {
    type:                 string;
    properties:           BlockStepProperties;
    additionalProperties: boolean;
}

export interface BlockStepProperties {
    allow_dependency_failure: AgentsElement;
    block?:                   Block;
    blocked_state?:           StringBlockStep;
    branches:                 AgentsElement;
    depends_on:               AgentsElement;
    fields?:                  AgentsElement;
    if:                       AgentsElement;
    key:                      AgentsElement;
    identifier:               AgentsElement;
    id:                       ID;
    label:                    AgentsElement;
    name:                     AgentsElement;
    prompt?:                  AgentsElement;
    type:                     TypeElement;
    input?:                   Block;
    continue_on_failure?:     AllowDependencyFailure;
    wait?:                    Wait;
    waiter?:                  Waiter;
}

export interface Block {
    type:        ItemsType;
    description: string;
}

export interface ID {
    $ref:       string;
    deprecated: boolean;
}

export interface TypeElement {
    type:  ItemsType;
    enum?: string[];
}

export interface Wait {
    description: string;
    type:        string[];
}

export interface Waiter {
    type: string[];
}

export interface Branches {
    description: string;
    anyOf:       AnyOf[];
    examples:    Array<string[] | string>;
}

export interface AnyOf {
    type:   AgentsListType;
    items?: ItemsElement;
}

export interface BuildNotify {
    type:        AgentsListType;
    description: string;
    items:       BuildNotifyItems;
}

export interface BuildNotifyItems {
    oneOf: PurpleOneOf[];
}

export interface PurpleOneOf {
    type:                  string;
    enum?:                 string[];
    properties?:           PurpleProperties;
    additionalProperties?: boolean;
}

export interface PurpleProperties {
    email?:                  ItemsElement;
    if:                      AgentsElement;
    basecamp_campfire?:      ItemsElement;
    slack?:                  PurpleSlack;
    webhook?:                ItemsElement;
    pagerduty_change_event?: ItemsElement;
    github_commit_status?:   GithubCommitStatus;
    github_check?:           GithubCheck;
}

export interface GithubCheck {
    type:       string;
    properties: GithubCheckProperties;
}

export interface GithubCheckProperties {
    context: Block;
}

export interface GithubCommitStatus {
    type:                 string;
    properties:           GithubCheckProperties;
    additionalProperties: boolean;
}

export interface PurpleSlack {
    oneOf: FluffyOneOf[];
}

export interface FluffyOneOf {
    type:        string;
    properties?: FluffyProperties;
}

export interface FluffyProperties {
    channels: AnyOf;
    message:  ItemsElement;
}

export interface Cache {
    description: string;
    anyOf:       CacheAnyOf[];
    examples:    Array<string[] | PurpleExample | string>;
}

export interface CacheAnyOf {
    type:        string;
    items?:      ItemsElement;
    properties?: TentacledProperties;
    required?:   string[];
}

export interface TentacledProperties {
    paths: AnyOf;
    size:  Size;
    name:  ItemsElement;
}

export interface Size {
    type:    ItemsType;
    pattern: string;
}

export interface PurpleExample {
    name:  string;
    size:  string;
    paths: string[];
}

export interface CommandStep {
    type:                 string;
    properties:           CommandStepProperties;
    additionalProperties: boolean;
}

export interface CommandStepProperties {
    agents:                   AgentsElement;
    allow_dependency_failure: AgentsElement;
    artifact_paths:           ArtifactPaths;
    branches:                 AgentsElement;
    cache:                    AgentsElement;
    cancel_on_build_failing:  AgentsElement;
    command:                  Command;
    commands:                 Commands;
    concurrency:              Concurrency;
    concurrency_group:        AgentsList;
    concurrency_method:       AgentsList;
    depends_on:               AgentsElement;
    env:                      AgentsElement;
    if:                       AgentsElement;
    key:                      AgentsElement;
    identifier:               AgentsElement;
    id:                       ID;
    label:                    AgentsElement;
    signature:                Signature;
    matrix:                   Matrix;
    name:                     AgentsElement;
    notify:                   Notify;
    parallelism:              Concurrency;
    plugins:                  Plugins;
    soft_fail:                AgentsElement;
    retry:                    Retry;
    skip:                     AgentsElement;
    timeout_in_minutes:       Limit;
    type:                     TypeElement;
    priority:                 Concurrency;
}

export interface ArtifactPaths {
    anyOf:       AnyOf[];
    description: string;
    examples:    Array<string[]>;
}

export interface Command {
    description: string;
    anyOf:       AnyOf[];
}

export interface Commands {
    description: string;
    $ref:        string;
}

export interface Concurrency {
    type:        ItemsType;
    description: string;
    examples:    number[];
}

export interface Matrix {
    oneOf: MatrixOneOf[];
}

export interface MatrixOneOf {
    type:        string;
    description: string;
    items?:      AgentsElement;
    examples?:   Array<string[]>;
    properties?: StickyProperties;
    required?:   string[];
}

export interface StickyProperties {
    setup:       Setup;
    adjustments: Adjustments;
}

export interface Adjustments {
    type:        AgentsListType;
    description: string;
    items:       AdjustmentsItems;
}

export interface AdjustmentsItems {
    type:        string;
    description: string;
    properties:  IndigoProperties;
    required:    string[];
}

export interface IndigoProperties {
    with:      With;
    skip:      AgentsElement;
    soft_fail: AgentsElement;
}

export interface With {
    oneOf: WithOneOf[];
}

export interface WithOneOf {
    type:                  string;
    description:           string;
    items?:                AgentsElement;
    propertyNames?:        Block;
    additionalProperties?: Block;
    examples?:             FluffyExample[];
}

export interface FluffyExample {
    os:   string;
    arch: string;
}

export interface Setup {
    oneOf: SetupOneOf[];
}

export interface SetupOneOf {
    type:                  string;
    description:           string;
    items?:                AgentsElement;
    examples:              Array<string[] | TentacledExample>;
    propertyNames?:        PropertyNames;
    additionalProperties?: AdditionalProperties;
}

export interface AdditionalProperties {
    type:        AgentsListType;
    description: string;
    items:       AgentsElement;
}

export interface TentacledExample {
    os:   string[];
    arch: string[];
}

export interface PropertyNames {
    type:        ItemsType;
    description: string;
    pattern:     string;
}

export interface Notify {
    type:        AgentsListType;
    description: string;
    items:       NotifyItems;
}

export interface NotifyItems {
    oneOf: TentacledOneOf[];
}

export interface TentacledOneOf {
    type:                  string;
    enum?:                 string[];
    properties?:           IndecentProperties;
    additionalProperties?: boolean;
}

export interface IndecentProperties {
    basecamp_campfire?:    ItemsElement;
    if:                    AgentsElement;
    slack?:                FluffySlack;
    github_commit_status?: GithubCommitStatus;
    github_check?:         GithubCheck;
}

export interface FluffySlack {
    oneOf: StickyOneOf[];
}

export interface StickyOneOf {
    type:                  string;
    properties?:           FluffyProperties;
    additionalProperties?: boolean;
}

export interface Plugins {
    anyOf: PluginsAnyOf[];
}

export interface PluginsAnyOf {
    type:        string;
    description: string;
    items?:      PurpleItems;
}

export interface PurpleItems {
    oneOf: IndigoOneOf[];
}

export interface IndigoOneOf {
    type:           string;
    maxProperties?: number;
    examples?:      StickyExample[];
}

export interface StickyExample {
    "docker-compose#v1.0.0": DockerComposeV100;
}

export interface DockerComposeV100 {
    run: string;
}

export interface Retry {
    type:                 string;
    description:          string;
    properties:           RetryProperties;
    additionalProperties: boolean;
}

export interface RetryProperties {
    automatic: Automatic;
    manual:    Manual;
}

export interface Automatic {
    anyOf:       AutomaticAnyOf[];
    description: string;
    default:     DefaultElement[];
}

export interface AutomaticAnyOf {
    enum?:  Array<boolean | string>;
    $ref?:  string;
    type?:  AgentsListType;
    items?: AgentsElement;
}

export interface DefaultElement {
    exit_status: string;
    limit:       number;
}

export interface Manual {
    description: string;
    anyOf:       ManualAnyOf[];
    default:     boolean;
}

export interface ManualAnyOf {
    enum?:                 Array<boolean | string>;
    type?:                 string;
    properties?:           HilariousProperties;
    additionalProperties?: boolean;
}

export interface HilariousProperties {
    allowed:          AllowDependencyFailure;
    permit_on_passed: AllowDependencyFailure;
    reason:           AgentsList;
}

export interface Signature {
    type:        string;
    description: string;
    properties:  SignatureProperties;
}

export interface SignatureProperties {
    algorithm:     AgentsList;
    value:         Block;
    signed_fields: SignedFields;
}

export interface SignedFields {
    type:        AgentsListType;
    description: string;
    items:       ItemsElement;
    examples:    Array<string[]>;
}

export interface DependsOn {
    description: string;
    anyOf:       DependsOnAnyOf[];
}

export interface DependsOnAnyOf {
    type:   string;
    items?: FluffyItems;
}

export interface FluffyItems {
    anyOf: ItemsAnyOf[];
}

export interface ItemsAnyOf {
    type:                  string;
    properties?:           AmbitiousProperties;
    additionalProperties?: boolean;
}

export interface AmbitiousProperties {
    step:          ItemsElement;
    allow_failure: AllowFailure;
}

export interface AllowFailure {
    enum:    Array<boolean | string>;
    default: boolean;
}

export interface Env {
    type:        string;
    description: string;
    examples:    EnvExample[];
}

export interface EnvExample {
    NODE_ENV: string;
}

export interface Fields {
    type:        AgentsListType;
    description: string;
    items:       FieldsItems;
}

export interface FieldsItems {
    oneOf: IndecentOneOf[];
}

export interface IndecentOneOf {
    type:                 string;
    properties:           CunningProperties;
    additionalProperties: boolean;
    required:             string[];
}

export interface CunningProperties {
    text?:     AgentsList;
    key:       AgentsList;
    hint:      AgentsList;
    format?:   AgentsList;
    required:  AllowDependencyFailure;
    default:   PropertiesDefault;
    select?:   AgentsList;
    multiple?: AllowDependencyFailure;
    options?:  Options;
}

export interface PropertiesDefault {
    type?:       ItemsType;
    description: string;
    examples:    Array<string[] | string>;
    oneOf?:      AnyOf[];
}

export interface Options {
    type:     AgentsListType;
    minItems: number;
    items:    OptionsItems;
}

export interface OptionsItems {
    type:                 string;
    properties:           MagentaProperties;
    additionalProperties: boolean;
    required:             string[];
}

export interface MagentaProperties {
    label:    AgentsList;
    value:    AgentsList;
    hint:     AgentsList;
    required: AllowDependencyFailure;
}

export interface GroupStep {
    type:                 string;
    properties:           GroupStepProperties;
    required:             string[];
    additionalProperties: boolean;
}

export interface GroupStepProperties {
    depends_on:               AgentsElement;
    group:                    Group;
    if:                       AgentsElement;
    key:                      AgentsElement;
    identifier:               AgentsElement;
    id:                       ID;
    label:                    AgentsElement;
    name:                     AgentsElement;
    allow_dependency_failure: AgentsElement;
    notify:                   AgentsElement;
    skip:                     AgentsElement;
    steps:                    Steps;
}

export interface Group {
    type:        string[];
    description: string;
    examples:    string[];
}

export interface Steps {
    type:        AgentsListType;
    description: string;
    items:       StepsItems;
    minItems?:   number;
}

export interface StepsItems {
    anyOf: AgentsElement[];
}

export interface MatrixElement {
    oneOf: ItemsElement[];
}

export interface NestedBlockStep {
    type:                 string;
    properties:           NestedBlockStepProperties;
    additionalProperties: boolean;
}

export interface NestedBlockStepProperties {
    block: AgentsElement;
}

export interface NestedCommandStep {
    type:                 string;
    properties:           NestedCommandStepProperties;
    additionalProperties: boolean;
}

export interface NestedCommandStepProperties {
    command:  AgentsElement;
    commands: AgentsElement;
    script:   AgentsElement;
}

export interface NestedInputStep {
    type:                 string;
    properties:           NestedInputStepProperties;
    additionalProperties: boolean;
}

export interface NestedInputStepProperties {
    input: AgentsElement;
}

export interface NestedTriggerStep {
    type:                 string;
    properties:           NestedTriggerStepProperties;
    additionalProperties: boolean;
}

export interface NestedTriggerStepProperties {
    trigger: AgentsElement;
}

export interface NestedWaitStep {
    type:                 string;
    properties:           NestedWaitStepProperties;
    additionalProperties: boolean;
}

export interface NestedWaitStepProperties {
    wait:   Commands;
    waiter: AgentsElement;
}

export interface Skip {
    anyOf:       ItemsElement[];
    description: string;
    examples:    Array<boolean | string>;
}

export interface SoftFail {
    description: string;
    anyOf:       SoftFailAnyOf[];
}

export interface SoftFailAnyOf {
    enum?:  Array<boolean | string>;
    type?:  AgentsListType;
    items?: TentacledItems;
}

export interface TentacledItems {
    type:       string;
    properties: FriskyProperties;
}

export interface FriskyProperties {
    exit_status: FluffyExitStatus;
}

export interface FluffyExitStatus {
    description: string;
    anyOf:       TypeElement[];
}

export interface TriggerStep {
    type:                 string;
    properties:           TriggerStepProperties;
    additionalProperties: boolean;
    required:             string[];
}

export interface TriggerStepProperties {
    allow_dependency_failure: AgentsElement;
    async:                    AllowDependencyFailure;
    branches:                 AgentsElement;
    build:                    Build;
    depends_on:               AgentsElement;
    if:                       AgentsElement;
    key:                      AgentsElement;
    identifier:               AgentsElement;
    id:                       ID;
    label:                    AgentsElement;
    name:                     AgentsElement;
    type:                     TypeElement;
    trigger:                  Block;
    skip:                     AgentsElement;
    soft_fail:                AllowDependencyFailure;
}

export interface Build {
    type:                 string;
    description:          string;
    properties:           BuildProperties;
    additionalProperties: boolean;
}

export interface BuildProperties {
    branch:    AgentsList;
    commit:    AgentsList;
    env:       AgentsElement;
    message:   StringBlockStep;
    meta_data: MetaData;
}

export interface MetaData {
    type:        string;
    description: string;
    examples:    MetaDataExample[];
}

export interface MetaDataExample {
    server: string;
}

export interface SchemaProperties {
    env:    AgentsElement;
    agents: AgentsElement;
    notify: AgentsElement;
    steps:  Steps;
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toSchema(json: string): Schema {
        return cast(JSON.parse(json), r("Schema"));
    }

    public static schemaToJson(value: Schema): string {
        return JSON.stringify(uncast(value, r("Schema")), null, 2);
    }
}

function invalidValue(typ: any, val: any, key: any, parent: any = ''): never {
    const prettyTyp = prettyTypeName(typ);
    const parentText = parent ? ` on ${parent}` : '';
    const keyText = key ? ` for key "${key}"` : '';
    throw Error(`Invalid value${keyText}${parentText}. Expected ${prettyTyp} but got ${JSON.stringify(val)}`);
}

function prettyTypeName(typ: any): string {
    if (Array.isArray(typ)) {
        if (typ.length === 2 && typ[0] === undefined) {
            return `an optional ${prettyTypeName(typ[1])}`;
        } else {
            return `one of [${typ.map(a => { return prettyTypeName(a); }).join(", ")}]`;
        }
    } else if (typeof typ === "object" && typ.literal !== undefined) {
        return typ.literal;
    } else {
        return typeof typ;
    }
}

function jsonToJSProps(typ: any): any {
    if (typ.jsonToJS === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.json] = { key: p.js, typ: p.typ });
        typ.jsonToJS = map;
    }
    return typ.jsonToJS;
}

function jsToJSONProps(typ: any): any {
    if (typ.jsToJSON === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.js] = { key: p.json, typ: p.typ });
        typ.jsToJSON = map;
    }
    return typ.jsToJSON;
}

function transform(val: any, typ: any, getProps: any, key: any = '', parent: any = ''): any {
    function transformPrimitive(typ: string, val: any): any {
        if (typeof typ === typeof val) return val;
        return invalidValue(typ, val, key, parent);
    }

    function transformUnion(typs: any[], val: any): any {
        // val must validate against one typ in typs
        const l = typs.length;
        for (let i = 0; i < l; i++) {
            const typ = typs[i];
            try {
                return transform(val, typ, getProps);
            } catch (_) {}
        }
        return invalidValue(typs, val, key, parent);
    }

    function transformEnum(cases: string[], val: any): any {
        if (cases.indexOf(val) !== -1) return val;
        return invalidValue(cases.map(a => { return l(a); }), val, key, parent);
    }

    function transformArray(typ: any, val: any): any {
        // val must be an array with no invalid elements
        if (!Array.isArray(val)) return invalidValue(l("array"), val, key, parent);
        return val.map(el => transform(el, typ, getProps));
    }

    function transformDate(val: any): any {
        if (val === null) {
            return null;
        }
        const d = new Date(val);
        if (isNaN(d.valueOf())) {
            return invalidValue(l("Date"), val, key, parent);
        }
        return d;
    }

    function transformObject(props: { [k: string]: any }, additional: any, val: any): any {
        if (val === null || typeof val !== "object" || Array.isArray(val)) {
            return invalidValue(l(ref || "object"), val, key, parent);
        }
        const result: any = {};
        Object.getOwnPropertyNames(props).forEach(key => {
            const prop = props[key];
            const v = Object.prototype.hasOwnProperty.call(val, key) ? val[key] : undefined;
            result[prop.key] = transform(v, prop.typ, getProps, key, ref);
        });
        Object.getOwnPropertyNames(val).forEach(key => {
            if (!Object.prototype.hasOwnProperty.call(props, key)) {
                result[key] = transform(val[key], additional, getProps, key, ref);
            }
        });
        return result;
    }

    if (typ === "any") return val;
    if (typ === null) {
        if (val === null) return val;
        return invalidValue(typ, val, key, parent);
    }
    if (typ === false) return invalidValue(typ, val, key, parent);
    let ref: any = undefined;
    while (typeof typ === "object" && typ.ref !== undefined) {
        ref = typ.ref;
        typ = typeMap[typ.ref];
    }
    if (Array.isArray(typ)) return transformEnum(typ, val);
    if (typeof typ === "object") {
        return typ.hasOwnProperty("unionMembers") ? transformUnion(typ.unionMembers, val)
            : typ.hasOwnProperty("arrayItems")    ? transformArray(typ.arrayItems, val)
            : typ.hasOwnProperty("props")         ? transformObject(getProps(typ), typ.additional, val)
            : invalidValue(typ, val, key, parent);
    }
    // Numbers can be parsed by Date but shouldn't be.
    if (typ === Date && typeof val !== "number") return transformDate(val);
    return transformPrimitive(typ, val);
}

function cast<T>(val: any, typ: any): T {
    return transform(val, typ, jsonToJSProps);
}

function uncast<T>(val: T, typ: any): any {
    return transform(val, typ, jsToJSONProps);
}

function l(typ: any) {
    return { literal: typ };
}

function a(typ: any) {
    return { arrayItems: typ };
}

function u(...typs: any[]) {
    return { unionMembers: typs };
}

function o(props: any[], additional: any) {
    return { props, additional };
}

function m(additional: any) {
    return { props: [], additional };
}

function r(name: string) {
    return { ref: name };
}

const typeMap: any = {
    "Schema": o([
        { json: "title", js: "title", typ: "" },
        { json: "$schema", js: "$schema", typ: "" },
        { json: "fileMatch", js: "fileMatch", typ: a("") },
        { json: "type", js: "type", typ: "" },
        { json: "required", js: "required", typ: a("") },
        { json: "definitions", js: "definitions", typ: r("Definitions") },
        { json: "properties", js: "properties", typ: r("SchemaProperties") },
    ], false),
    "Definitions": o([
        { json: "allowDependencyFailure", js: "allowDependencyFailure", typ: r("AllowDependencyFailure") },
        { json: "agents", js: "agents", typ: r("DefinitionsAgents") },
        { json: "agentsObject", js: "agentsObject", typ: r("AgentsObject") },
        { json: "agentsList", js: "agentsList", typ: r("AgentsList") },
        { json: "automaticRetry", js: "automaticRetry", typ: r("AutomaticRetry") },
        { json: "branches", js: "branches", typ: r("Branches") },
        { json: "cache", js: "cache", typ: r("Cache") },
        { json: "cancelOnBuildFailing", js: "cancelOnBuildFailing", typ: r("AllowDependencyFailure") },
        { json: "dependsOn", js: "dependsOn", typ: r("DependsOn") },
        { json: "env", js: "env", typ: r("Env") },
        { json: "if", js: "if", typ: r("AgentsList") },
        { json: "key", js: "key", typ: r("AgentsList") },
        { json: "label", js: "label", typ: r("AgentsList") },
        { json: "buildNotify", js: "buildNotify", typ: r("BuildNotify") },
        { json: "fields", js: "fields", typ: r("Fields") },
        { json: "matrixElement", js: "matrixElement", typ: r("MatrixElement") },
        { json: "prompt", js: "prompt", typ: r("AgentsList") },
        { json: "skip", js: "skip", typ: r("Skip") },
        { json: "softFail", js: "softFail", typ: r("SoftFail") },
        { json: "blockStep", js: "blockStep", typ: r("Step") },
        { json: "nestedBlockStep", js: "nestedBlockStep", typ: r("NestedBlockStep") },
        { json: "stringBlockStep", js: "stringBlockStep", typ: r("StringBlockStep") },
        { json: "inputStep", js: "inputStep", typ: r("Step") },
        { json: "nestedInputStep", js: "nestedInputStep", typ: r("NestedInputStep") },
        { json: "stringInputStep", js: "stringInputStep", typ: r("StringBlockStep") },
        { json: "commandStep", js: "commandStep", typ: r("CommandStep") },
        { json: "nestedCommandStep", js: "nestedCommandStep", typ: r("NestedCommandStep") },
        { json: "stringWaitStep", js: "stringWaitStep", typ: r("StringBlockStep") },
        { json: "waitStep", js: "waitStep", typ: r("Step") },
        { json: "nestedWaitStep", js: "nestedWaitStep", typ: r("NestedWaitStep") },
        { json: "triggerStep", js: "triggerStep", typ: r("TriggerStep") },
        { json: "nestedTriggerStep", js: "nestedTriggerStep", typ: r("NestedTriggerStep") },
        { json: "groupStep", js: "groupStep", typ: r("GroupStep") },
    ], false),
    "DefinitionsAgents": o([
        { json: "oneOf", js: "oneOf", typ: a(r("AgentsElement")) },
    ], false),
    "AgentsElement": o([
        { json: "$ref", js: "$ref", typ: "" },
    ], false),
    "AgentsList": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a("") },
        { json: "items", js: "items", typ: u(undefined, r("ItemsElement")) },
        { json: "enum", js: "enum", typ: u(undefined, a("")) },
        { json: "format", js: "format", typ: u(undefined, "") },
        { json: "pattern", js: "pattern", typ: u(undefined, "") },
        { json: "not", js: "not", typ: u(undefined, r("Not")) },
        { json: "default", js: "default", typ: u(undefined, "") },
    ], false),
    "ItemsElement": o([
        { json: "type", js: "type", typ: r("ItemsType") },
    ], false),
    "Not": o([
        { json: "pattern", js: "pattern", typ: "" },
    ], false),
    "AgentsObject": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a(r("AgentsObjectExample")) },
    ], false),
    "AgentsObjectExample": o([
        { json: "queue", js: "queue", typ: u(undefined, "") },
        { json: "ruby", js: "ruby", typ: u(undefined, "") },
    ], false),
    "AllowDependencyFailure": o([
        { json: "enum", js: "enum", typ: a(u(true, "")) },
        { json: "description", js: "description", typ: "" },
        { json: "default", js: "default", typ: true },
    ], false),
    "AutomaticRetry": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("AutomaticRetryProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "AutomaticRetryProperties": o([
        { json: "exit_status", js: "exit_status", typ: r("PurpleExitStatus") },
        { json: "limit", js: "limit", typ: r("Limit") },
        { json: "signal", js: "signal", typ: r("AgentsList") },
        { json: "signal_reason", js: "signal_reason", typ: r("StringBlockStep") },
    ], false),
    "PurpleExitStatus": o([
        { json: "description", js: "description", typ: "" },
        { json: "anyOf", js: "anyOf", typ: a(r("ExitStatusAnyOf")) },
    ], false),
    "ExitStatusAnyOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "enum", js: "enum", typ: u(undefined, a("")) },
        { json: "items", js: "items", typ: u(undefined, r("ItemsElement")) },
    ], false),
    "Limit": o([
        { json: "type", js: "type", typ: r("ItemsType") },
        { json: "description", js: "description", typ: "" },
        { json: "minimum", js: "minimum", typ: 0 },
        { json: "maximum", js: "maximum", typ: u(undefined, 0) },
        { json: "examples", js: "examples", typ: u(undefined, a(0)) },
    ], false),
    "StringBlockStep": o([
        { json: "description", js: "description", typ: "" },
        { json: "type", js: "type", typ: r("ItemsType") },
        { json: "enum", js: "enum", typ: u(undefined, a("")) },
        { json: "default", js: "default", typ: u(undefined, "") },
        { json: "examples", js: "examples", typ: u(undefined, a("")) },
    ], false),
    "Step": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("BlockStepProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "BlockStepProperties": o([
        { json: "allow_dependency_failure", js: "allow_dependency_failure", typ: r("AgentsElement") },
        { json: "block", js: "block", typ: u(undefined, r("Block")) },
        { json: "blocked_state", js: "blocked_state", typ: u(undefined, r("StringBlockStep")) },
        { json: "branches", js: "branches", typ: r("AgentsElement") },
        { json: "depends_on", js: "depends_on", typ: r("AgentsElement") },
        { json: "fields", js: "fields", typ: u(undefined, r("AgentsElement")) },
        { json: "if", js: "if", typ: r("AgentsElement") },
        { json: "key", js: "key", typ: r("AgentsElement") },
        { json: "identifier", js: "identifier", typ: r("AgentsElement") },
        { json: "id", js: "id", typ: r("ID") },
        { json: "label", js: "label", typ: r("AgentsElement") },
        { json: "name", js: "name", typ: r("AgentsElement") },
        { json: "prompt", js: "prompt", typ: u(undefined, r("AgentsElement")) },
        { json: "type", js: "type", typ: r("TypeElement") },
        { json: "input", js: "input", typ: u(undefined, r("Block")) },
        { json: "continue_on_failure", js: "continue_on_failure", typ: u(undefined, r("AllowDependencyFailure")) },
        { json: "wait", js: "wait", typ: u(undefined, r("Wait")) },
        { json: "waiter", js: "waiter", typ: u(undefined, r("Waiter")) },
    ], false),
    "Block": o([
        { json: "type", js: "type", typ: r("ItemsType") },
        { json: "description", js: "description", typ: "" },
    ], false),
    "ID": o([
        { json: "$ref", js: "$ref", typ: "" },
        { json: "deprecated", js: "deprecated", typ: true },
    ], false),
    "TypeElement": o([
        { json: "type", js: "type", typ: r("ItemsType") },
        { json: "enum", js: "enum", typ: u(undefined, a("")) },
    ], false),
    "Wait": o([
        { json: "description", js: "description", typ: "" },
        { json: "type", js: "type", typ: a("") },
    ], false),
    "Waiter": o([
        { json: "type", js: "type", typ: a("") },
    ], false),
    "Branches": o([
        { json: "description", js: "description", typ: "" },
        { json: "anyOf", js: "anyOf", typ: a(r("AnyOf")) },
        { json: "examples", js: "examples", typ: a(u(a(""), "")) },
    ], false),
    "AnyOf": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "items", js: "items", typ: u(undefined, r("ItemsElement")) },
    ], false),
    "BuildNotify": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: r("BuildNotifyItems") },
    ], false),
    "BuildNotifyItems": o([
        { json: "oneOf", js: "oneOf", typ: a(r("PurpleOneOf")) },
    ], false),
    "PurpleOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "enum", js: "enum", typ: u(undefined, a("")) },
        { json: "properties", js: "properties", typ: u(undefined, r("PurpleProperties")) },
        { json: "additionalProperties", js: "additionalProperties", typ: u(undefined, true) },
    ], false),
    "PurpleProperties": o([
        { json: "email", js: "email", typ: u(undefined, r("ItemsElement")) },
        { json: "if", js: "if", typ: r("AgentsElement") },
        { json: "basecamp_campfire", js: "basecamp_campfire", typ: u(undefined, r("ItemsElement")) },
        { json: "slack", js: "slack", typ: u(undefined, r("PurpleSlack")) },
        { json: "webhook", js: "webhook", typ: u(undefined, r("ItemsElement")) },
        { json: "pagerduty_change_event", js: "pagerduty_change_event", typ: u(undefined, r("ItemsElement")) },
        { json: "github_commit_status", js: "github_commit_status", typ: u(undefined, r("GithubCommitStatus")) },
        { json: "github_check", js: "github_check", typ: u(undefined, r("GithubCheck")) },
    ], false),
    "GithubCheck": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("GithubCheckProperties") },
    ], false),
    "GithubCheckProperties": o([
        { json: "context", js: "context", typ: r("Block") },
    ], false),
    "GithubCommitStatus": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("GithubCheckProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "PurpleSlack": o([
        { json: "oneOf", js: "oneOf", typ: a(r("FluffyOneOf")) },
    ], false),
    "FluffyOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: u(undefined, r("FluffyProperties")) },
    ], false),
    "FluffyProperties": o([
        { json: "channels", js: "channels", typ: r("AnyOf") },
        { json: "message", js: "message", typ: r("ItemsElement") },
    ], false),
    "Cache": o([
        { json: "description", js: "description", typ: "" },
        { json: "anyOf", js: "anyOf", typ: a(r("CacheAnyOf")) },
        { json: "examples", js: "examples", typ: a(u(a(""), r("PurpleExample"), "")) },
    ], false),
    "CacheAnyOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "items", js: "items", typ: u(undefined, r("ItemsElement")) },
        { json: "properties", js: "properties", typ: u(undefined, r("TentacledProperties")) },
        { json: "required", js: "required", typ: u(undefined, a("")) },
    ], false),
    "TentacledProperties": o([
        { json: "paths", js: "paths", typ: r("AnyOf") },
        { json: "size", js: "size", typ: r("Size") },
        { json: "name", js: "name", typ: r("ItemsElement") },
    ], false),
    "Size": o([
        { json: "type", js: "type", typ: r("ItemsType") },
        { json: "pattern", js: "pattern", typ: "" },
    ], false),
    "PurpleExample": o([
        { json: "name", js: "name", typ: "" },
        { json: "size", js: "size", typ: "" },
        { json: "paths", js: "paths", typ: a("") },
    ], false),
    "CommandStep": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("CommandStepProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "CommandStepProperties": o([
        { json: "agents", js: "agents", typ: r("AgentsElement") },
        { json: "allow_dependency_failure", js: "allow_dependency_failure", typ: r("AgentsElement") },
        { json: "artifact_paths", js: "artifact_paths", typ: r("ArtifactPaths") },
        { json: "branches", js: "branches", typ: r("AgentsElement") },
        { json: "cache", js: "cache", typ: r("AgentsElement") },
        { json: "cancel_on_build_failing", js: "cancel_on_build_failing", typ: r("AgentsElement") },
        { json: "command", js: "command", typ: r("Command") },
        { json: "commands", js: "commands", typ: r("Commands") },
        { json: "concurrency", js: "concurrency", typ: r("Concurrency") },
        { json: "concurrency_group", js: "concurrency_group", typ: r("AgentsList") },
        { json: "concurrency_method", js: "concurrency_method", typ: r("AgentsList") },
        { json: "depends_on", js: "depends_on", typ: r("AgentsElement") },
        { json: "env", js: "env", typ: r("AgentsElement") },
        { json: "if", js: "if", typ: r("AgentsElement") },
        { json: "key", js: "key", typ: r("AgentsElement") },
        { json: "identifier", js: "identifier", typ: r("AgentsElement") },
        { json: "id", js: "id", typ: r("ID") },
        { json: "label", js: "label", typ: r("AgentsElement") },
        { json: "signature", js: "signature", typ: r("Signature") },
        { json: "matrix", js: "matrix", typ: r("Matrix") },
        { json: "name", js: "name", typ: r("AgentsElement") },
        { json: "notify", js: "notify", typ: r("Notify") },
        { json: "parallelism", js: "parallelism", typ: r("Concurrency") },
        { json: "plugins", js: "plugins", typ: r("Plugins") },
        { json: "soft_fail", js: "soft_fail", typ: r("AgentsElement") },
        { json: "retry", js: "retry", typ: r("Retry") },
        { json: "skip", js: "skip", typ: r("AgentsElement") },
        { json: "timeout_in_minutes", js: "timeout_in_minutes", typ: r("Limit") },
        { json: "type", js: "type", typ: r("TypeElement") },
        { json: "priority", js: "priority", typ: r("Concurrency") },
    ], false),
    "ArtifactPaths": o([
        { json: "anyOf", js: "anyOf", typ: a(r("AnyOf")) },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a(a("")) },
    ], false),
    "Command": o([
        { json: "description", js: "description", typ: "" },
        { json: "anyOf", js: "anyOf", typ: a(r("AnyOf")) },
    ], false),
    "Commands": o([
        { json: "description", js: "description", typ: "" },
        { json: "$ref", js: "$ref", typ: "" },
    ], false),
    "Concurrency": o([
        { json: "type", js: "type", typ: r("ItemsType") },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a(0) },
    ], false),
    "Matrix": o([
        { json: "oneOf", js: "oneOf", typ: a(r("MatrixOneOf")) },
    ], false),
    "MatrixOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: u(undefined, r("AgentsElement")) },
        { json: "examples", js: "examples", typ: u(undefined, a(a(""))) },
        { json: "properties", js: "properties", typ: u(undefined, r("StickyProperties")) },
        { json: "required", js: "required", typ: u(undefined, a("")) },
    ], false),
    "StickyProperties": o([
        { json: "setup", js: "setup", typ: r("Setup") },
        { json: "adjustments", js: "adjustments", typ: r("Adjustments") },
    ], false),
    "Adjustments": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: r("AdjustmentsItems") },
    ], false),
    "AdjustmentsItems": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "properties", js: "properties", typ: r("IndigoProperties") },
        { json: "required", js: "required", typ: a("") },
    ], false),
    "IndigoProperties": o([
        { json: "with", js: "with", typ: r("With") },
        { json: "skip", js: "skip", typ: r("AgentsElement") },
        { json: "soft_fail", js: "soft_fail", typ: r("AgentsElement") },
    ], false),
    "With": o([
        { json: "oneOf", js: "oneOf", typ: a(r("WithOneOf")) },
    ], false),
    "WithOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: u(undefined, r("AgentsElement")) },
        { json: "propertyNames", js: "propertyNames", typ: u(undefined, r("Block")) },
        { json: "additionalProperties", js: "additionalProperties", typ: u(undefined, r("Block")) },
        { json: "examples", js: "examples", typ: u(undefined, a(r("FluffyExample"))) },
    ], false),
    "FluffyExample": o([
        { json: "os", js: "os", typ: "" },
        { json: "arch", js: "arch", typ: "" },
    ], false),
    "Setup": o([
        { json: "oneOf", js: "oneOf", typ: a(r("SetupOneOf")) },
    ], false),
    "SetupOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: u(undefined, r("AgentsElement")) },
        { json: "examples", js: "examples", typ: a(u(a(""), r("TentacledExample"))) },
        { json: "propertyNames", js: "propertyNames", typ: u(undefined, r("PropertyNames")) },
        { json: "additionalProperties", js: "additionalProperties", typ: u(undefined, r("AdditionalProperties")) },
    ], false),
    "AdditionalProperties": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: r("AgentsElement") },
    ], false),
    "TentacledExample": o([
        { json: "os", js: "os", typ: a("") },
        { json: "arch", js: "arch", typ: a("") },
    ], false),
    "PropertyNames": o([
        { json: "type", js: "type", typ: r("ItemsType") },
        { json: "description", js: "description", typ: "" },
        { json: "pattern", js: "pattern", typ: "" },
    ], false),
    "Notify": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: r("NotifyItems") },
    ], false),
    "NotifyItems": o([
        { json: "oneOf", js: "oneOf", typ: a(r("TentacledOneOf")) },
    ], false),
    "TentacledOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "enum", js: "enum", typ: u(undefined, a("")) },
        { json: "properties", js: "properties", typ: u(undefined, r("IndecentProperties")) },
        { json: "additionalProperties", js: "additionalProperties", typ: u(undefined, true) },
    ], false),
    "IndecentProperties": o([
        { json: "basecamp_campfire", js: "basecamp_campfire", typ: u(undefined, r("ItemsElement")) },
        { json: "if", js: "if", typ: r("AgentsElement") },
        { json: "slack", js: "slack", typ: u(undefined, r("FluffySlack")) },
        { json: "github_commit_status", js: "github_commit_status", typ: u(undefined, r("GithubCommitStatus")) },
        { json: "github_check", js: "github_check", typ: u(undefined, r("GithubCheck")) },
    ], false),
    "FluffySlack": o([
        { json: "oneOf", js: "oneOf", typ: a(r("StickyOneOf")) },
    ], false),
    "StickyOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: u(undefined, r("FluffyProperties")) },
        { json: "additionalProperties", js: "additionalProperties", typ: u(undefined, true) },
    ], false),
    "Plugins": o([
        { json: "anyOf", js: "anyOf", typ: a(r("PluginsAnyOf")) },
    ], false),
    "PluginsAnyOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: u(undefined, r("PurpleItems")) },
    ], false),
    "PurpleItems": o([
        { json: "oneOf", js: "oneOf", typ: a(r("IndigoOneOf")) },
    ], false),
    "IndigoOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "maxProperties", js: "maxProperties", typ: u(undefined, 0) },
        { json: "examples", js: "examples", typ: u(undefined, a(r("StickyExample"))) },
    ], false),
    "StickyExample": o([
        { json: "docker-compose#v1.0.0", js: "docker-compose#v1.0.0", typ: r("DockerComposeV100") },
    ], false),
    "DockerComposeV100": o([
        { json: "run", js: "run", typ: "" },
    ], false),
    "Retry": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "properties", js: "properties", typ: r("RetryProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "RetryProperties": o([
        { json: "automatic", js: "automatic", typ: r("Automatic") },
        { json: "manual", js: "manual", typ: r("Manual") },
    ], false),
    "Automatic": o([
        { json: "anyOf", js: "anyOf", typ: a(r("AutomaticAnyOf")) },
        { json: "description", js: "description", typ: "" },
        { json: "default", js: "default", typ: a(r("DefaultElement")) },
    ], false),
    "AutomaticAnyOf": o([
        { json: "enum", js: "enum", typ: u(undefined, a(u(true, ""))) },
        { json: "$ref", js: "$ref", typ: u(undefined, "") },
        { json: "type", js: "type", typ: u(undefined, r("AgentsListType")) },
        { json: "items", js: "items", typ: u(undefined, r("AgentsElement")) },
    ], false),
    "DefaultElement": o([
        { json: "exit_status", js: "exit_status", typ: "" },
        { json: "limit", js: "limit", typ: 0 },
    ], false),
    "Manual": o([
        { json: "description", js: "description", typ: "" },
        { json: "anyOf", js: "anyOf", typ: a(r("ManualAnyOf")) },
        { json: "default", js: "default", typ: true },
    ], false),
    "ManualAnyOf": o([
        { json: "enum", js: "enum", typ: u(undefined, a(u(true, ""))) },
        { json: "type", js: "type", typ: u(undefined, "") },
        { json: "properties", js: "properties", typ: u(undefined, r("HilariousProperties")) },
        { json: "additionalProperties", js: "additionalProperties", typ: u(undefined, true) },
    ], false),
    "HilariousProperties": o([
        { json: "allowed", js: "allowed", typ: r("AllowDependencyFailure") },
        { json: "permit_on_passed", js: "permit_on_passed", typ: r("AllowDependencyFailure") },
        { json: "reason", js: "reason", typ: r("AgentsList") },
    ], false),
    "Signature": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "properties", js: "properties", typ: r("SignatureProperties") },
    ], false),
    "SignatureProperties": o([
        { json: "algorithm", js: "algorithm", typ: r("AgentsList") },
        { json: "value", js: "value", typ: r("Block") },
        { json: "signed_fields", js: "signed_fields", typ: r("SignedFields") },
    ], false),
    "SignedFields": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: r("ItemsElement") },
        { json: "examples", js: "examples", typ: a(a("")) },
    ], false),
    "DependsOn": o([
        { json: "description", js: "description", typ: "" },
        { json: "anyOf", js: "anyOf", typ: a(r("DependsOnAnyOf")) },
    ], false),
    "DependsOnAnyOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "items", js: "items", typ: u(undefined, r("FluffyItems")) },
    ], false),
    "FluffyItems": o([
        { json: "anyOf", js: "anyOf", typ: a(r("ItemsAnyOf")) },
    ], false),
    "ItemsAnyOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: u(undefined, r("AmbitiousProperties")) },
        { json: "additionalProperties", js: "additionalProperties", typ: u(undefined, true) },
    ], false),
    "AmbitiousProperties": o([
        { json: "step", js: "step", typ: r("ItemsElement") },
        { json: "allow_failure", js: "allow_failure", typ: r("AllowFailure") },
    ], false),
    "AllowFailure": o([
        { json: "enum", js: "enum", typ: a(u(true, "")) },
        { json: "default", js: "default", typ: true },
    ], false),
    "Env": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a(r("EnvExample")) },
    ], false),
    "EnvExample": o([
        { json: "NODE_ENV", js: "NODE_ENV", typ: "" },
    ], false),
    "Fields": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: r("FieldsItems") },
    ], false),
    "FieldsItems": o([
        { json: "oneOf", js: "oneOf", typ: a(r("IndecentOneOf")) },
    ], false),
    "IndecentOneOf": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("CunningProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
        { json: "required", js: "required", typ: a("") },
    ], false),
    "CunningProperties": o([
        { json: "text", js: "text", typ: u(undefined, r("AgentsList")) },
        { json: "key", js: "key", typ: r("AgentsList") },
        { json: "hint", js: "hint", typ: r("AgentsList") },
        { json: "format", js: "format", typ: u(undefined, r("AgentsList")) },
        { json: "required", js: "required", typ: r("AllowDependencyFailure") },
        { json: "default", js: "default", typ: r("PropertiesDefault") },
        { json: "select", js: "select", typ: u(undefined, r("AgentsList")) },
        { json: "multiple", js: "multiple", typ: u(undefined, r("AllowDependencyFailure")) },
        { json: "options", js: "options", typ: u(undefined, r("Options")) },
    ], false),
    "PropertiesDefault": o([
        { json: "type", js: "type", typ: u(undefined, r("ItemsType")) },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a(u(a(""), "")) },
        { json: "oneOf", js: "oneOf", typ: u(undefined, a(r("AnyOf"))) },
    ], false),
    "Options": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "minItems", js: "minItems", typ: 0 },
        { json: "items", js: "items", typ: r("OptionsItems") },
    ], false),
    "OptionsItems": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("MagentaProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
        { json: "required", js: "required", typ: a("") },
    ], false),
    "MagentaProperties": o([
        { json: "label", js: "label", typ: r("AgentsList") },
        { json: "value", js: "value", typ: r("AgentsList") },
        { json: "hint", js: "hint", typ: r("AgentsList") },
        { json: "required", js: "required", typ: r("AllowDependencyFailure") },
    ], false),
    "GroupStep": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("GroupStepProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "GroupStepProperties": o([
        { json: "depends_on", js: "depends_on", typ: r("AgentsElement") },
        { json: "group", js: "group", typ: r("Group") },
        { json: "if", js: "if", typ: r("AgentsElement") },
        { json: "key", js: "key", typ: r("AgentsElement") },
        { json: "identifier", js: "identifier", typ: r("AgentsElement") },
        { json: "id", js: "id", typ: r("ID") },
        { json: "label", js: "label", typ: r("AgentsElement") },
        { json: "name", js: "name", typ: r("AgentsElement") },
        { json: "allow_dependency_failure", js: "allow_dependency_failure", typ: r("AgentsElement") },
        { json: "notify", js: "notify", typ: r("AgentsElement") },
        { json: "skip", js: "skip", typ: r("AgentsElement") },
        { json: "steps", js: "steps", typ: r("Steps") },
    ], false),
    "Group": o([
        { json: "type", js: "type", typ: a("") },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a("") },
    ], false),
    "Steps": o([
        { json: "type", js: "type", typ: r("AgentsListType") },
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: r("StepsItems") },
        { json: "minItems", js: "minItems", typ: u(undefined, 0) },
    ], false),
    "StepsItems": o([
        { json: "anyOf", js: "anyOf", typ: a(r("AgentsElement")) },
    ], false),
    "MatrixElement": o([
        { json: "oneOf", js: "oneOf", typ: a(r("ItemsElement")) },
    ], false),
    "NestedBlockStep": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("NestedBlockStepProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "NestedBlockStepProperties": o([
        { json: "block", js: "block", typ: r("AgentsElement") },
    ], false),
    "NestedCommandStep": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("NestedCommandStepProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "NestedCommandStepProperties": o([
        { json: "command", js: "command", typ: r("AgentsElement") },
        { json: "commands", js: "commands", typ: r("AgentsElement") },
        { json: "script", js: "script", typ: r("AgentsElement") },
    ], false),
    "NestedInputStep": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("NestedInputStepProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "NestedInputStepProperties": o([
        { json: "input", js: "input", typ: r("AgentsElement") },
    ], false),
    "NestedTriggerStep": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("NestedTriggerStepProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "NestedTriggerStepProperties": o([
        { json: "trigger", js: "trigger", typ: r("AgentsElement") },
    ], false),
    "NestedWaitStep": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("NestedWaitStepProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "NestedWaitStepProperties": o([
        { json: "wait", js: "wait", typ: r("Commands") },
        { json: "waiter", js: "waiter", typ: r("AgentsElement") },
    ], false),
    "Skip": o([
        { json: "anyOf", js: "anyOf", typ: a(r("ItemsElement")) },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a(u(true, "")) },
    ], false),
    "SoftFail": o([
        { json: "description", js: "description", typ: "" },
        { json: "anyOf", js: "anyOf", typ: a(r("SoftFailAnyOf")) },
    ], false),
    "SoftFailAnyOf": o([
        { json: "enum", js: "enum", typ: u(undefined, a(u(true, ""))) },
        { json: "type", js: "type", typ: u(undefined, r("AgentsListType")) },
        { json: "items", js: "items", typ: u(undefined, r("TentacledItems")) },
    ], false),
    "TentacledItems": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("FriskyProperties") },
    ], false),
    "FriskyProperties": o([
        { json: "exit_status", js: "exit_status", typ: r("FluffyExitStatus") },
    ], false),
    "FluffyExitStatus": o([
        { json: "description", js: "description", typ: "" },
        { json: "anyOf", js: "anyOf", typ: a(r("TypeElement")) },
    ], false),
    "TriggerStep": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("TriggerStepProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
        { json: "required", js: "required", typ: a("") },
    ], false),
    "TriggerStepProperties": o([
        { json: "allow_dependency_failure", js: "allow_dependency_failure", typ: r("AgentsElement") },
        { json: "async", js: "async", typ: r("AllowDependencyFailure") },
        { json: "branches", js: "branches", typ: r("AgentsElement") },
        { json: "build", js: "build", typ: r("Build") },
        { json: "depends_on", js: "depends_on", typ: r("AgentsElement") },
        { json: "if", js: "if", typ: r("AgentsElement") },
        { json: "key", js: "key", typ: r("AgentsElement") },
        { json: "identifier", js: "identifier", typ: r("AgentsElement") },
        { json: "id", js: "id", typ: r("ID") },
        { json: "label", js: "label", typ: r("AgentsElement") },
        { json: "name", js: "name", typ: r("AgentsElement") },
        { json: "type", js: "type", typ: r("TypeElement") },
        { json: "trigger", js: "trigger", typ: r("Block") },
        { json: "skip", js: "skip", typ: r("AgentsElement") },
        { json: "soft_fail", js: "soft_fail", typ: r("AllowDependencyFailure") },
    ], false),
    "Build": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "properties", js: "properties", typ: r("BuildProperties") },
        { json: "additionalProperties", js: "additionalProperties", typ: true },
    ], false),
    "BuildProperties": o([
        { json: "branch", js: "branch", typ: r("AgentsList") },
        { json: "commit", js: "commit", typ: r("AgentsList") },
        { json: "env", js: "env", typ: r("AgentsElement") },
        { json: "message", js: "message", typ: r("StringBlockStep") },
        { json: "meta_data", js: "meta_data", typ: r("MetaData") },
    ], false),
    "MetaData": o([
        { json: "type", js: "type", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "examples", js: "examples", typ: a(r("MetaDataExample")) },
    ], false),
    "MetaDataExample": o([
        { json: "server", js: "server", typ: "" },
    ], false),
    "SchemaProperties": o([
        { json: "env", js: "env", typ: r("AgentsElement") },
        { json: "agents", js: "agents", typ: r("AgentsElement") },
        { json: "notify", js: "notify", typ: r("AgentsElement") },
        { json: "steps", js: "steps", typ: r("Steps") },
    ], false),
    "ItemsType": [
        "boolean",
        "integer",
        "string",
    ],
    "AgentsListType": [
        "array",
        "string",
    ],
};
