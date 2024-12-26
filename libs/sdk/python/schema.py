from typing import Any, List, Optional, Union, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_stringified_bool(x: str) -> bool:
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


class AgentsElement:
    ref: str

    def __init__(self, ref: str) -> None:
        self.ref = ref

    @staticmethod
    def from_dict(obj: Any) -> 'AgentsElement':
        assert isinstance(obj, dict)
        ref = from_str(obj.get("$ref"))
        return AgentsElement(ref)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$ref"] = from_str(self.ref)
        return result


class DefinitionsAgents:
    one_of: List[AgentsElement]

    def __init__(self, one_of: List[AgentsElement]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'DefinitionsAgents':
        assert isinstance(obj, dict)
        one_of = from_list(AgentsElement.from_dict, obj.get("oneOf"))
        return DefinitionsAgents(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(AgentsElement, x), self.one_of)
        return result


class Not:
    pattern: str

    def __init__(self, pattern: str) -> None:
        self.pattern = pattern

    @staticmethod
    def from_dict(obj: Any) -> 'Not':
        assert isinstance(obj, dict)
        pattern = from_str(obj.get("pattern"))
        return Not(pattern)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pattern"] = from_str(self.pattern)
        return result


class ItemsType(Enum):
    BOOLEAN = "boolean"
    INTEGER = "integer"
    STRING = "string"


class ItemsElement:
    type: ItemsType

    def __init__(self, type: ItemsType) -> None:
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'ItemsElement':
        assert isinstance(obj, dict)
        type = ItemsType(obj.get("type"))
        return ItemsElement(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(ItemsType, self.type)
        return result


class AgentsListType(Enum):
    ARRAY = "array"
    STRING = "string"


class AgentsList:
    type: AgentsListType
    description: str
    examples: List[str]
    items: Optional[ItemsElement]
    enum: Optional[List[str]]
    format: Optional[str]
    pattern: Optional[str]
    agents_list_not: Optional[Not]
    default: Optional[str]

    def __init__(self, type: AgentsListType, description: str, examples: List[str], items: Optional[ItemsElement], enum: Optional[List[str]], format: Optional[str], pattern: Optional[str], agents_list_not: Optional[Not], default: Optional[str]) -> None:
        self.type = type
        self.description = description
        self.examples = examples
        self.items = items
        self.enum = enum
        self.format = format
        self.pattern = pattern
        self.agents_list_not = agents_list_not
        self.default = default

    @staticmethod
    def from_dict(obj: Any) -> 'AgentsList':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        description = from_str(obj.get("description"))
        examples = from_list(from_str, obj.get("examples"))
        items = from_union([ItemsElement.from_dict, from_none], obj.get("items"))
        enum = from_union([lambda x: from_list(from_str, x), from_none], obj.get("enum"))
        format = from_union([from_str, from_none], obj.get("format"))
        pattern = from_union([from_str, from_none], obj.get("pattern"))
        agents_list_not = from_union([Not.from_dict, from_none], obj.get("not"))
        default = from_union([from_str, from_none], obj.get("default"))
        return AgentsList(type, description, examples, items, enum, format, pattern, agents_list_not, default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(from_str, self.examples)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.items)
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_str, x), from_none], self.enum)
        if self.format is not None:
            result["format"] = from_union([from_str, from_none], self.format)
        if self.pattern is not None:
            result["pattern"] = from_union([from_str, from_none], self.pattern)
        if self.agents_list_not is not None:
            result["not"] = from_union([lambda x: to_class(Not, x), from_none], self.agents_list_not)
        if self.default is not None:
            result["default"] = from_union([from_str, from_none], self.default)
        return result


class AgentsObjectExample:
    queue: Optional[str]
    ruby: Optional[str]

    def __init__(self, queue: Optional[str], ruby: Optional[str]) -> None:
        self.queue = queue
        self.ruby = ruby

    @staticmethod
    def from_dict(obj: Any) -> 'AgentsObjectExample':
        assert isinstance(obj, dict)
        queue = from_union([from_str, from_none], obj.get("queue"))
        ruby = from_union([from_str, from_none], obj.get("ruby"))
        return AgentsObjectExample(queue, ruby)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.queue is not None:
            result["queue"] = from_union([from_str, from_none], self.queue)
        if self.ruby is not None:
            result["ruby"] = from_union([from_str, from_none], self.ruby)
        return result


class AgentsObject:
    type: str
    description: str
    examples: List[AgentsObjectExample]

    def __init__(self, type: str, description: str, examples: List[AgentsObjectExample]) -> None:
        self.type = type
        self.description = description
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'AgentsObject':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        examples = from_list(AgentsObjectExample.from_dict, obj.get("examples"))
        return AgentsObject(type, description, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(lambda x: to_class(AgentsObjectExample, x), self.examples)
        return result


class AllowDependencyFailure:
    enum: List[bool]
    description: str
    default: bool

    def __init__(self, enum: List[bool], description: str, default: bool) -> None:
        self.enum = enum
        self.description = description
        self.default = default

    @staticmethod
    def from_dict(obj: Any) -> 'AllowDependencyFailure':
        assert isinstance(obj, dict)
        enum = from_list(lambda x: from_union([from_bool, lambda x: from_stringified_bool(from_str(x))], x), obj.get("enum"))
        description = from_str(obj.get("description"))
        default = from_bool(obj.get("default"))
        return AllowDependencyFailure(enum, description, default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enum"] = from_list(from_bool, self.enum)
        result["description"] = from_str(self.description)
        result["default"] = from_bool(self.default)
        return result


class ExitStatusAnyOf:
    type: str
    enum: Optional[List[str]]
    items: Optional[ItemsElement]

    def __init__(self, type: str, enum: Optional[List[str]], items: Optional[ItemsElement]) -> None:
        self.type = type
        self.enum = enum
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'ExitStatusAnyOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        enum = from_union([lambda x: from_list(from_str, x), from_none], obj.get("enum"))
        items = from_union([ItemsElement.from_dict, from_none], obj.get("items"))
        return ExitStatusAnyOf(type, enum, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_str, x), from_none], self.enum)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.items)
        return result


class PurpleExitStatus:
    description: str
    any_of: List[ExitStatusAnyOf]

    def __init__(self, description: str, any_of: List[ExitStatusAnyOf]) -> None:
        self.description = description
        self.any_of = any_of

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleExitStatus':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        any_of = from_list(ExitStatusAnyOf.from_dict, obj.get("anyOf"))
        return PurpleExitStatus(description, any_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["anyOf"] = from_list(lambda x: to_class(ExitStatusAnyOf, x), self.any_of)
        return result


class Limit:
    type: ItemsType
    description: str
    minimum: int
    maximum: Optional[int]
    examples: Optional[List[int]]

    def __init__(self, type: ItemsType, description: str, minimum: int, maximum: Optional[int], examples: Optional[List[int]]) -> None:
        self.type = type
        self.description = description
        self.minimum = minimum
        self.maximum = maximum
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'Limit':
        assert isinstance(obj, dict)
        type = ItemsType(obj.get("type"))
        description = from_str(obj.get("description"))
        minimum = from_int(obj.get("minimum"))
        maximum = from_union([from_int, from_none], obj.get("maximum"))
        examples = from_union([lambda x: from_list(from_int, x), from_none], obj.get("examples"))
        return Limit(type, description, minimum, maximum, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(ItemsType, self.type)
        result["description"] = from_str(self.description)
        result["minimum"] = from_int(self.minimum)
        if self.maximum is not None:
            result["maximum"] = from_union([from_int, from_none], self.maximum)
        if self.examples is not None:
            result["examples"] = from_union([lambda x: from_list(from_int, x), from_none], self.examples)
        return result


class StringBlockStep:
    description: str
    type: ItemsType
    enum: Optional[List[str]]
    default: Optional[str]
    examples: Optional[List[str]]

    def __init__(self, description: str, type: ItemsType, enum: Optional[List[str]], default: Optional[str], examples: Optional[List[str]]) -> None:
        self.description = description
        self.type = type
        self.enum = enum
        self.default = default
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'StringBlockStep':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        type = ItemsType(obj.get("type"))
        enum = from_union([lambda x: from_list(from_str, x), from_none], obj.get("enum"))
        default = from_union([from_str, from_none], obj.get("default"))
        examples = from_union([lambda x: from_list(from_str, x), from_none], obj.get("examples"))
        return StringBlockStep(description, type, enum, default, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["type"] = to_enum(ItemsType, self.type)
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_str, x), from_none], self.enum)
        if self.default is not None:
            result["default"] = from_union([from_str, from_none], self.default)
        if self.examples is not None:
            result["examples"] = from_union([lambda x: from_list(from_str, x), from_none], self.examples)
        return result


class AutomaticRetryProperties:
    exit_status: PurpleExitStatus
    limit: Limit
    signal: AgentsList
    signal_reason: StringBlockStep

    def __init__(self, exit_status: PurpleExitStatus, limit: Limit, signal: AgentsList, signal_reason: StringBlockStep) -> None:
        self.exit_status = exit_status
        self.limit = limit
        self.signal = signal
        self.signal_reason = signal_reason

    @staticmethod
    def from_dict(obj: Any) -> 'AutomaticRetryProperties':
        assert isinstance(obj, dict)
        exit_status = PurpleExitStatus.from_dict(obj.get("exit_status"))
        limit = Limit.from_dict(obj.get("limit"))
        signal = AgentsList.from_dict(obj.get("signal"))
        signal_reason = StringBlockStep.from_dict(obj.get("signal_reason"))
        return AutomaticRetryProperties(exit_status, limit, signal, signal_reason)

    def to_dict(self) -> dict:
        result: dict = {}
        result["exit_status"] = to_class(PurpleExitStatus, self.exit_status)
        result["limit"] = to_class(Limit, self.limit)
        result["signal"] = to_class(AgentsList, self.signal)
        result["signal_reason"] = to_class(StringBlockStep, self.signal_reason)
        return result


class AutomaticRetry:
    type: str
    properties: AutomaticRetryProperties
    additional_properties: bool

    def __init__(self, type: str, properties: AutomaticRetryProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'AutomaticRetry':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = AutomaticRetryProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return AutomaticRetry(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(AutomaticRetryProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class Trigger:
    type: ItemsType
    description: str

    def __init__(self, type: ItemsType, description: str) -> None:
        self.type = type
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'Trigger':
        assert isinstance(obj, dict)
        type = ItemsType(obj.get("type"))
        description = from_str(obj.get("description"))
        return Trigger(type, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(ItemsType, self.type)
        result["description"] = from_str(self.description)
        return result


class ID:
    ref: str
    deprecated: bool

    def __init__(self, ref: str, deprecated: bool) -> None:
        self.ref = ref
        self.deprecated = deprecated

    @staticmethod
    def from_dict(obj: Any) -> 'ID':
        assert isinstance(obj, dict)
        ref = from_str(obj.get("$ref"))
        deprecated = from_bool(obj.get("deprecated"))
        return ID(ref, deprecated)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$ref"] = from_str(self.ref)
        result["deprecated"] = from_bool(self.deprecated)
        return result


class TypeElement:
    type: ItemsType
    enum: Optional[List[str]]

    def __init__(self, type: ItemsType, enum: Optional[List[str]]) -> None:
        self.type = type
        self.enum = enum

    @staticmethod
    def from_dict(obj: Any) -> 'TypeElement':
        assert isinstance(obj, dict)
        type = ItemsType(obj.get("type"))
        enum = from_union([lambda x: from_list(from_str, x), from_none], obj.get("enum"))
        return TypeElement(type, enum)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(ItemsType, self.type)
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_str, x), from_none], self.enum)
        return result


class Wait:
    description: str
    type: List[str]

    def __init__(self, description: str, type: List[str]) -> None:
        self.description = description
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Wait':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        type = from_list(from_str, obj.get("type"))
        return Wait(description, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["type"] = from_list(from_str, self.type)
        return result


class Waiter:
    type: List[str]

    def __init__(self, type: List[str]) -> None:
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Waiter':
        assert isinstance(obj, dict)
        type = from_list(from_str, obj.get("type"))
        return Waiter(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_list(from_str, self.type)
        return result


class BlockStepProperties:
    allow_dependency_failure: AgentsElement
    block: Optional[Trigger]
    blocked_state: Optional[StringBlockStep]
    branches: AgentsElement
    depends_on: AgentsElement
    fields: Optional[AgentsElement]
    properties_if: AgentsElement
    key: AgentsElement
    identifier: AgentsElement
    id: ID
    label: AgentsElement
    name: AgentsElement
    prompt: Optional[AgentsElement]
    type: TypeElement
    input: Optional[Trigger]
    continue_on_failure: Optional[AllowDependencyFailure]
    wait: Optional[Wait]
    waiter: Optional[Waiter]

    def __init__(self, allow_dependency_failure: AgentsElement, block: Optional[Trigger], blocked_state: Optional[StringBlockStep], branches: AgentsElement, depends_on: AgentsElement, fields: Optional[AgentsElement], properties_if: AgentsElement, key: AgentsElement, identifier: AgentsElement, id: ID, label: AgentsElement, name: AgentsElement, prompt: Optional[AgentsElement], type: TypeElement, input: Optional[Trigger], continue_on_failure: Optional[AllowDependencyFailure], wait: Optional[Wait], waiter: Optional[Waiter]) -> None:
        self.allow_dependency_failure = allow_dependency_failure
        self.block = block
        self.blocked_state = blocked_state
        self.branches = branches
        self.depends_on = depends_on
        self.fields = fields
        self.properties_if = properties_if
        self.key = key
        self.identifier = identifier
        self.id = id
        self.label = label
        self.name = name
        self.prompt = prompt
        self.type = type
        self.input = input
        self.continue_on_failure = continue_on_failure
        self.wait = wait
        self.waiter = waiter

    @staticmethod
    def from_dict(obj: Any) -> 'BlockStepProperties':
        assert isinstance(obj, dict)
        allow_dependency_failure = AgentsElement.from_dict(obj.get("allow_dependency_failure"))
        block = from_union([Trigger.from_dict, from_none], obj.get("block"))
        blocked_state = from_union([StringBlockStep.from_dict, from_none], obj.get("blocked_state"))
        branches = AgentsElement.from_dict(obj.get("branches"))
        depends_on = AgentsElement.from_dict(obj.get("depends_on"))
        fields = from_union([AgentsElement.from_dict, from_none], obj.get("fields"))
        properties_if = AgentsElement.from_dict(obj.get("if"))
        key = AgentsElement.from_dict(obj.get("key"))
        identifier = AgentsElement.from_dict(obj.get("identifier"))
        id = ID.from_dict(obj.get("id"))
        label = AgentsElement.from_dict(obj.get("label"))
        name = AgentsElement.from_dict(obj.get("name"))
        prompt = from_union([AgentsElement.from_dict, from_none], obj.get("prompt"))
        type = TypeElement.from_dict(obj.get("type"))
        input = from_union([Trigger.from_dict, from_none], obj.get("input"))
        continue_on_failure = from_union([AllowDependencyFailure.from_dict, from_none], obj.get("continue_on_failure"))
        wait = from_union([Wait.from_dict, from_none], obj.get("wait"))
        waiter = from_union([Waiter.from_dict, from_none], obj.get("waiter"))
        return BlockStepProperties(allow_dependency_failure, block, blocked_state, branches, depends_on, fields, properties_if, key, identifier, id, label, name, prompt, type, input, continue_on_failure, wait, waiter)

    def to_dict(self) -> dict:
        result: dict = {}
        result["allow_dependency_failure"] = to_class(AgentsElement, self.allow_dependency_failure)
        if self.block is not None:
            result["block"] = from_union([lambda x: to_class(Trigger, x), from_none], self.block)
        if self.blocked_state is not None:
            result["blocked_state"] = from_union([lambda x: to_class(StringBlockStep, x), from_none], self.blocked_state)
        result["branches"] = to_class(AgentsElement, self.branches)
        result["depends_on"] = to_class(AgentsElement, self.depends_on)
        if self.fields is not None:
            result["fields"] = from_union([lambda x: to_class(AgentsElement, x), from_none], self.fields)
        result["if"] = to_class(AgentsElement, self.properties_if)
        result["key"] = to_class(AgentsElement, self.key)
        result["identifier"] = to_class(AgentsElement, self.identifier)
        result["id"] = to_class(ID, self.id)
        result["label"] = to_class(AgentsElement, self.label)
        result["name"] = to_class(AgentsElement, self.name)
        if self.prompt is not None:
            result["prompt"] = from_union([lambda x: to_class(AgentsElement, x), from_none], self.prompt)
        result["type"] = to_class(TypeElement, self.type)
        if self.input is not None:
            result["input"] = from_union([lambda x: to_class(Trigger, x), from_none], self.input)
        if self.continue_on_failure is not None:
            result["continue_on_failure"] = from_union([lambda x: to_class(AllowDependencyFailure, x), from_none], self.continue_on_failure)
        if self.wait is not None:
            result["wait"] = from_union([lambda x: to_class(Wait, x), from_none], self.wait)
        if self.waiter is not None:
            result["waiter"] = from_union([lambda x: to_class(Waiter, x), from_none], self.waiter)
        return result


class Step:
    type: str
    properties: BlockStepProperties
    additional_properties: bool

    def __init__(self, type: str, properties: BlockStepProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'Step':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = BlockStepProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return Step(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(BlockStepProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class AnyOf:
    type: AgentsListType
    items: Optional[ItemsElement]

    def __init__(self, type: AgentsListType, items: Optional[ItemsElement]) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'AnyOf':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        items = from_union([ItemsElement.from_dict, from_none], obj.get("items"))
        return AnyOf(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.items)
        return result


class Branches:
    description: str
    any_of: List[AnyOf]
    examples: List[Union[List[str], str]]

    def __init__(self, description: str, any_of: List[AnyOf], examples: List[Union[List[str], str]]) -> None:
        self.description = description
        self.any_of = any_of
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'Branches':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        any_of = from_list(AnyOf.from_dict, obj.get("anyOf"))
        examples = from_list(lambda x: from_union([lambda x: from_list(from_str, x), from_str], x), obj.get("examples"))
        return Branches(description, any_of, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["anyOf"] = from_list(lambda x: to_class(AnyOf, x), self.any_of)
        result["examples"] = from_list(lambda x: from_union([lambda x: from_list(from_str, x), from_str], x), self.examples)
        return result


class GithubCheckProperties:
    context: Trigger

    def __init__(self, context: Trigger) -> None:
        self.context = context

    @staticmethod
    def from_dict(obj: Any) -> 'GithubCheckProperties':
        assert isinstance(obj, dict)
        context = Trigger.from_dict(obj.get("context"))
        return GithubCheckProperties(context)

    def to_dict(self) -> dict:
        result: dict = {}
        result["context"] = to_class(Trigger, self.context)
        return result


class GithubCheck:
    type: str
    properties: GithubCheckProperties

    def __init__(self, type: str, properties: GithubCheckProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'GithubCheck':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = GithubCheckProperties.from_dict(obj.get("properties"))
        return GithubCheck(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(GithubCheckProperties, self.properties)
        return result


class GithubCommitStatus:
    type: str
    properties: GithubCheckProperties
    additional_properties: bool

    def __init__(self, type: str, properties: GithubCheckProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'GithubCommitStatus':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = GithubCheckProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return GithubCommitStatus(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(GithubCheckProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class FluffyProperties:
    channels: AnyOf
    message: ItemsElement

    def __init__(self, channels: AnyOf, message: ItemsElement) -> None:
        self.channels = channels
        self.message = message

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyProperties':
        assert isinstance(obj, dict)
        channels = AnyOf.from_dict(obj.get("channels"))
        message = ItemsElement.from_dict(obj.get("message"))
        return FluffyProperties(channels, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channels"] = to_class(AnyOf, self.channels)
        result["message"] = to_class(ItemsElement, self.message)
        return result


class FluffyOneOf:
    type: str
    properties: Optional[FluffyProperties]

    def __init__(self, type: str, properties: Optional[FluffyProperties]) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = from_union([FluffyProperties.from_dict, from_none], obj.get("properties"))
        return FluffyOneOf(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: to_class(FluffyProperties, x), from_none], self.properties)
        return result


class PurpleSlack:
    one_of: List[FluffyOneOf]

    def __init__(self, one_of: List[FluffyOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleSlack':
        assert isinstance(obj, dict)
        one_of = from_list(FluffyOneOf.from_dict, obj.get("oneOf"))
        return PurpleSlack(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(FluffyOneOf, x), self.one_of)
        return result


class PurpleProperties:
    email: Optional[ItemsElement]
    properties_if: AgentsElement
    basecamp_campfire: Optional[ItemsElement]
    slack: Optional[PurpleSlack]
    webhook: Optional[ItemsElement]
    pagerduty_change_event: Optional[ItemsElement]
    github_commit_status: Optional[GithubCommitStatus]
    github_check: Optional[GithubCheck]

    def __init__(self, email: Optional[ItemsElement], properties_if: AgentsElement, basecamp_campfire: Optional[ItemsElement], slack: Optional[PurpleSlack], webhook: Optional[ItemsElement], pagerduty_change_event: Optional[ItemsElement], github_commit_status: Optional[GithubCommitStatus], github_check: Optional[GithubCheck]) -> None:
        self.email = email
        self.properties_if = properties_if
        self.basecamp_campfire = basecamp_campfire
        self.slack = slack
        self.webhook = webhook
        self.pagerduty_change_event = pagerduty_change_event
        self.github_commit_status = github_commit_status
        self.github_check = github_check

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleProperties':
        assert isinstance(obj, dict)
        email = from_union([ItemsElement.from_dict, from_none], obj.get("email"))
        properties_if = AgentsElement.from_dict(obj.get("if"))
        basecamp_campfire = from_union([ItemsElement.from_dict, from_none], obj.get("basecamp_campfire"))
        slack = from_union([PurpleSlack.from_dict, from_none], obj.get("slack"))
        webhook = from_union([ItemsElement.from_dict, from_none], obj.get("webhook"))
        pagerduty_change_event = from_union([ItemsElement.from_dict, from_none], obj.get("pagerduty_change_event"))
        github_commit_status = from_union([GithubCommitStatus.from_dict, from_none], obj.get("github_commit_status"))
        github_check = from_union([GithubCheck.from_dict, from_none], obj.get("github_check"))
        return PurpleProperties(email, properties_if, basecamp_campfire, slack, webhook, pagerduty_change_event, github_commit_status, github_check)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.email is not None:
            result["email"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.email)
        result["if"] = to_class(AgentsElement, self.properties_if)
        if self.basecamp_campfire is not None:
            result["basecamp_campfire"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.basecamp_campfire)
        if self.slack is not None:
            result["slack"] = from_union([lambda x: to_class(PurpleSlack, x), from_none], self.slack)
        if self.webhook is not None:
            result["webhook"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.webhook)
        if self.pagerduty_change_event is not None:
            result["pagerduty_change_event"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.pagerduty_change_event)
        if self.github_commit_status is not None:
            result["github_commit_status"] = from_union([lambda x: to_class(GithubCommitStatus, x), from_none], self.github_commit_status)
        if self.github_check is not None:
            result["github_check"] = from_union([lambda x: to_class(GithubCheck, x), from_none], self.github_check)
        return result


class PurpleOneOf:
    type: str
    enum: Optional[List[str]]
    properties: Optional[PurpleProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: str, enum: Optional[List[str]], properties: Optional[PurpleProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.enum = enum
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        enum = from_union([lambda x: from_list(from_str, x), from_none], obj.get("enum"))
        properties = from_union([PurpleProperties.from_dict, from_none], obj.get("properties"))
        additional_properties = from_union([from_bool, from_none], obj.get("additionalProperties"))
        return PurpleOneOf(type, enum, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_str, x), from_none], self.enum)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: to_class(PurpleProperties, x), from_none], self.properties)
        if self.additional_properties is not None:
            result["additionalProperties"] = from_union([from_bool, from_none], self.additional_properties)
        return result


class BuildNotifyItems:
    one_of: List[PurpleOneOf]

    def __init__(self, one_of: List[PurpleOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'BuildNotifyItems':
        assert isinstance(obj, dict)
        one_of = from_list(PurpleOneOf.from_dict, obj.get("oneOf"))
        return BuildNotifyItems(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(PurpleOneOf, x), self.one_of)
        return result


class BuildNotify:
    type: AgentsListType
    description: str
    items: BuildNotifyItems

    def __init__(self, type: AgentsListType, description: str, items: BuildNotifyItems) -> None:
        self.type = type
        self.description = description
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'BuildNotify':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        description = from_str(obj.get("description"))
        items = BuildNotifyItems.from_dict(obj.get("items"))
        return BuildNotify(type, description, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["description"] = from_str(self.description)
        result["items"] = to_class(BuildNotifyItems, self.items)
        return result


class Size:
    type: ItemsType
    pattern: str

    def __init__(self, type: ItemsType, pattern: str) -> None:
        self.type = type
        self.pattern = pattern

    @staticmethod
    def from_dict(obj: Any) -> 'Size':
        assert isinstance(obj, dict)
        type = ItemsType(obj.get("type"))
        pattern = from_str(obj.get("pattern"))
        return Size(type, pattern)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(ItemsType, self.type)
        result["pattern"] = from_str(self.pattern)
        return result


class TentacledProperties:
    paths: AnyOf
    size: Size
    name: ItemsElement

    def __init__(self, paths: AnyOf, size: Size, name: ItemsElement) -> None:
        self.paths = paths
        self.size = size
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledProperties':
        assert isinstance(obj, dict)
        paths = AnyOf.from_dict(obj.get("paths"))
        size = Size.from_dict(obj.get("size"))
        name = ItemsElement.from_dict(obj.get("name"))
        return TentacledProperties(paths, size, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["paths"] = to_class(AnyOf, self.paths)
        result["size"] = to_class(Size, self.size)
        result["name"] = to_class(ItemsElement, self.name)
        return result


class CacheAnyOf:
    type: str
    items: Optional[ItemsElement]
    properties: Optional[TentacledProperties]
    required: Optional[List[str]]

    def __init__(self, type: str, items: Optional[ItemsElement], properties: Optional[TentacledProperties], required: Optional[List[str]]) -> None:
        self.type = type
        self.items = items
        self.properties = properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'CacheAnyOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = from_union([ItemsElement.from_dict, from_none], obj.get("items"))
        properties = from_union([TentacledProperties.from_dict, from_none], obj.get("properties"))
        required = from_union([lambda x: from_list(from_str, x), from_none], obj.get("required"))
        return CacheAnyOf(type, items, properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.items)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: to_class(TentacledProperties, x), from_none], self.properties)
        if self.required is not None:
            result["required"] = from_union([lambda x: from_list(from_str, x), from_none], self.required)
        return result


class PurpleExample:
    name: str
    size: str
    paths: List[str]

    def __init__(self, name: str, size: str, paths: List[str]) -> None:
        self.name = name
        self.size = size
        self.paths = paths

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleExample':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        size = from_str(obj.get("size"))
        paths = from_list(from_str, obj.get("paths"))
        return PurpleExample(name, size, paths)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["size"] = from_str(self.size)
        result["paths"] = from_list(from_str, self.paths)
        return result


class Cache:
    description: str
    any_of: List[CacheAnyOf]
    examples: List[Union[List[str], PurpleExample, str]]

    def __init__(self, description: str, any_of: List[CacheAnyOf], examples: List[Union[List[str], PurpleExample, str]]) -> None:
        self.description = description
        self.any_of = any_of
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'Cache':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        any_of = from_list(CacheAnyOf.from_dict, obj.get("anyOf"))
        examples = from_list(lambda x: from_union([lambda x: from_list(from_str, x), PurpleExample.from_dict, from_str], x), obj.get("examples"))
        return Cache(description, any_of, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["anyOf"] = from_list(lambda x: to_class(CacheAnyOf, x), self.any_of)
        result["examples"] = from_list(lambda x: from_union([lambda x: from_list(from_str, x), lambda x: to_class(PurpleExample, x), from_str], x), self.examples)
        return result


class ArtifactPaths:
    any_of: List[AnyOf]
    description: str
    examples: List[List[str]]

    def __init__(self, any_of: List[AnyOf], description: str, examples: List[List[str]]) -> None:
        self.any_of = any_of
        self.description = description
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'ArtifactPaths':
        assert isinstance(obj, dict)
        any_of = from_list(AnyOf.from_dict, obj.get("anyOf"))
        description = from_str(obj.get("description"))
        examples = from_list(lambda x: from_list(from_str, x), obj.get("examples"))
        return ArtifactPaths(any_of, description, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["anyOf"] = from_list(lambda x: to_class(AnyOf, x), self.any_of)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(lambda x: from_list(from_str, x), self.examples)
        return result


class Command:
    description: str
    any_of: List[AnyOf]

    def __init__(self, description: str, any_of: List[AnyOf]) -> None:
        self.description = description
        self.any_of = any_of

    @staticmethod
    def from_dict(obj: Any) -> 'Command':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        any_of = from_list(AnyOf.from_dict, obj.get("anyOf"))
        return Command(description, any_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["anyOf"] = from_list(lambda x: to_class(AnyOf, x), self.any_of)
        return result


class Commands:
    description: str
    ref: str

    def __init__(self, description: str, ref: str) -> None:
        self.description = description
        self.ref = ref

    @staticmethod
    def from_dict(obj: Any) -> 'Commands':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        ref = from_str(obj.get("$ref"))
        return Commands(description, ref)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["$ref"] = from_str(self.ref)
        return result


class Concurrency:
    type: ItemsType
    description: str
    examples: List[int]

    def __init__(self, type: ItemsType, description: str, examples: List[int]) -> None:
        self.type = type
        self.description = description
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'Concurrency':
        assert isinstance(obj, dict)
        type = ItemsType(obj.get("type"))
        description = from_str(obj.get("description"))
        examples = from_list(from_int, obj.get("examples"))
        return Concurrency(type, description, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(ItemsType, self.type)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(from_int, self.examples)
        return result


class FluffyExample:
    os: str
    arch: str

    def __init__(self, os: str, arch: str) -> None:
        self.os = os
        self.arch = arch

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyExample':
        assert isinstance(obj, dict)
        os = from_str(obj.get("os"))
        arch = from_str(obj.get("arch"))
        return FluffyExample(os, arch)

    def to_dict(self) -> dict:
        result: dict = {}
        result["os"] = from_str(self.os)
        result["arch"] = from_str(self.arch)
        return result


class WithOneOf:
    type: str
    description: str
    items: Optional[AgentsElement]
    property_names: Optional[Trigger]
    additional_properties: Optional[Trigger]
    examples: Optional[List[FluffyExample]]

    def __init__(self, type: str, description: str, items: Optional[AgentsElement], property_names: Optional[Trigger], additional_properties: Optional[Trigger], examples: Optional[List[FluffyExample]]) -> None:
        self.type = type
        self.description = description
        self.items = items
        self.property_names = property_names
        self.additional_properties = additional_properties
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'WithOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        items = from_union([AgentsElement.from_dict, from_none], obj.get("items"))
        property_names = from_union([Trigger.from_dict, from_none], obj.get("propertyNames"))
        additional_properties = from_union([Trigger.from_dict, from_none], obj.get("additionalProperties"))
        examples = from_union([lambda x: from_list(FluffyExample.from_dict, x), from_none], obj.get("examples"))
        return WithOneOf(type, description, items, property_names, additional_properties, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(AgentsElement, x), from_none], self.items)
        if self.property_names is not None:
            result["propertyNames"] = from_union([lambda x: to_class(Trigger, x), from_none], self.property_names)
        if self.additional_properties is not None:
            result["additionalProperties"] = from_union([lambda x: to_class(Trigger, x), from_none], self.additional_properties)
        if self.examples is not None:
            result["examples"] = from_union([lambda x: from_list(lambda x: to_class(FluffyExample, x), x), from_none], self.examples)
        return result


class With:
    one_of: List[WithOneOf]

    def __init__(self, one_of: List[WithOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'With':
        assert isinstance(obj, dict)
        one_of = from_list(WithOneOf.from_dict, obj.get("oneOf"))
        return With(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(WithOneOf, x), self.one_of)
        return result


class IndigoProperties:
    properties_with: With
    skip: AgentsElement
    soft_fail: AgentsElement

    def __init__(self, properties_with: With, skip: AgentsElement, soft_fail: AgentsElement) -> None:
        self.properties_with = properties_with
        self.skip = skip
        self.soft_fail = soft_fail

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoProperties':
        assert isinstance(obj, dict)
        properties_with = With.from_dict(obj.get("with"))
        skip = AgentsElement.from_dict(obj.get("skip"))
        soft_fail = AgentsElement.from_dict(obj.get("soft_fail"))
        return IndigoProperties(properties_with, skip, soft_fail)

    def to_dict(self) -> dict:
        result: dict = {}
        result["with"] = to_class(With, self.properties_with)
        result["skip"] = to_class(AgentsElement, self.skip)
        result["soft_fail"] = to_class(AgentsElement, self.soft_fail)
        return result


class AdjustmentsItems:
    type: str
    description: str
    properties: IndigoProperties
    required: List[str]

    def __init__(self, type: str, description: str, properties: IndigoProperties, required: List[str]) -> None:
        self.type = type
        self.description = description
        self.properties = properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'AdjustmentsItems':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        properties = IndigoProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        return AdjustmentsItems(type, description, properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["properties"] = to_class(IndigoProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        return result


class Adjustments:
    type: AgentsListType
    description: str
    items: AdjustmentsItems

    def __init__(self, type: AgentsListType, description: str, items: AdjustmentsItems) -> None:
        self.type = type
        self.description = description
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'Adjustments':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        description = from_str(obj.get("description"))
        items = AdjustmentsItems.from_dict(obj.get("items"))
        return Adjustments(type, description, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["description"] = from_str(self.description)
        result["items"] = to_class(AdjustmentsItems, self.items)
        return result


class AdditionalProperties:
    type: AgentsListType
    description: str
    items: AgentsElement

    def __init__(self, type: AgentsListType, description: str, items: AgentsElement) -> None:
        self.type = type
        self.description = description
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'AdditionalProperties':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        description = from_str(obj.get("description"))
        items = AgentsElement.from_dict(obj.get("items"))
        return AdditionalProperties(type, description, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["description"] = from_str(self.description)
        result["items"] = to_class(AgentsElement, self.items)
        return result


class TentacledExample:
    os: List[str]
    arch: List[str]

    def __init__(self, os: List[str], arch: List[str]) -> None:
        self.os = os
        self.arch = arch

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledExample':
        assert isinstance(obj, dict)
        os = from_list(from_str, obj.get("os"))
        arch = from_list(from_str, obj.get("arch"))
        return TentacledExample(os, arch)

    def to_dict(self) -> dict:
        result: dict = {}
        result["os"] = from_list(from_str, self.os)
        result["arch"] = from_list(from_str, self.arch)
        return result


class PropertyNames:
    type: ItemsType
    description: str
    pattern: str

    def __init__(self, type: ItemsType, description: str, pattern: str) -> None:
        self.type = type
        self.description = description
        self.pattern = pattern

    @staticmethod
    def from_dict(obj: Any) -> 'PropertyNames':
        assert isinstance(obj, dict)
        type = ItemsType(obj.get("type"))
        description = from_str(obj.get("description"))
        pattern = from_str(obj.get("pattern"))
        return PropertyNames(type, description, pattern)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(ItemsType, self.type)
        result["description"] = from_str(self.description)
        result["pattern"] = from_str(self.pattern)
        return result


class SetupOneOf:
    type: str
    description: str
    items: Optional[AgentsElement]
    examples: List[Union[List[str], TentacledExample]]
    property_names: Optional[PropertyNames]
    additional_properties: Optional[AdditionalProperties]

    def __init__(self, type: str, description: str, items: Optional[AgentsElement], examples: List[Union[List[str], TentacledExample]], property_names: Optional[PropertyNames], additional_properties: Optional[AdditionalProperties]) -> None:
        self.type = type
        self.description = description
        self.items = items
        self.examples = examples
        self.property_names = property_names
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'SetupOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        items = from_union([AgentsElement.from_dict, from_none], obj.get("items"))
        examples = from_list(lambda x: from_union([lambda x: from_list(from_str, x), TentacledExample.from_dict], x), obj.get("examples"))
        property_names = from_union([PropertyNames.from_dict, from_none], obj.get("propertyNames"))
        additional_properties = from_union([AdditionalProperties.from_dict, from_none], obj.get("additionalProperties"))
        return SetupOneOf(type, description, items, examples, property_names, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(AgentsElement, x), from_none], self.items)
        result["examples"] = from_list(lambda x: from_union([lambda x: from_list(from_str, x), lambda x: to_class(TentacledExample, x)], x), self.examples)
        if self.property_names is not None:
            result["propertyNames"] = from_union([lambda x: to_class(PropertyNames, x), from_none], self.property_names)
        if self.additional_properties is not None:
            result["additionalProperties"] = from_union([lambda x: to_class(AdditionalProperties, x), from_none], self.additional_properties)
        return result


class Setup:
    one_of: List[SetupOneOf]

    def __init__(self, one_of: List[SetupOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'Setup':
        assert isinstance(obj, dict)
        one_of = from_list(SetupOneOf.from_dict, obj.get("oneOf"))
        return Setup(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(SetupOneOf, x), self.one_of)
        return result


class StickyProperties:
    setup: Setup
    adjustments: Adjustments

    def __init__(self, setup: Setup, adjustments: Adjustments) -> None:
        self.setup = setup
        self.adjustments = adjustments

    @staticmethod
    def from_dict(obj: Any) -> 'StickyProperties':
        assert isinstance(obj, dict)
        setup = Setup.from_dict(obj.get("setup"))
        adjustments = Adjustments.from_dict(obj.get("adjustments"))
        return StickyProperties(setup, adjustments)

    def to_dict(self) -> dict:
        result: dict = {}
        result["setup"] = to_class(Setup, self.setup)
        result["adjustments"] = to_class(Adjustments, self.adjustments)
        return result


class MatrixOneOf:
    type: str
    description: str
    items: Optional[AgentsElement]
    examples: Optional[List[List[str]]]
    properties: Optional[StickyProperties]
    required: Optional[List[str]]

    def __init__(self, type: str, description: str, items: Optional[AgentsElement], examples: Optional[List[List[str]]], properties: Optional[StickyProperties], required: Optional[List[str]]) -> None:
        self.type = type
        self.description = description
        self.items = items
        self.examples = examples
        self.properties = properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'MatrixOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        items = from_union([AgentsElement.from_dict, from_none], obj.get("items"))
        examples = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("examples"))
        properties = from_union([StickyProperties.from_dict, from_none], obj.get("properties"))
        required = from_union([lambda x: from_list(from_str, x), from_none], obj.get("required"))
        return MatrixOneOf(type, description, items, examples, properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(AgentsElement, x), from_none], self.items)
        if self.examples is not None:
            result["examples"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.examples)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: to_class(StickyProperties, x), from_none], self.properties)
        if self.required is not None:
            result["required"] = from_union([lambda x: from_list(from_str, x), from_none], self.required)
        return result


class Matrix:
    one_of: List[MatrixOneOf]

    def __init__(self, one_of: List[MatrixOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'Matrix':
        assert isinstance(obj, dict)
        one_of = from_list(MatrixOneOf.from_dict, obj.get("oneOf"))
        return Matrix(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(MatrixOneOf, x), self.one_of)
        return result


class StickyOneOf:
    type: str
    properties: Optional[FluffyProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: str, properties: Optional[FluffyProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'StickyOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = from_union([FluffyProperties.from_dict, from_none], obj.get("properties"))
        additional_properties = from_union([from_bool, from_none], obj.get("additionalProperties"))
        return StickyOneOf(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: to_class(FluffyProperties, x), from_none], self.properties)
        if self.additional_properties is not None:
            result["additionalProperties"] = from_union([from_bool, from_none], self.additional_properties)
        return result


class FluffySlack:
    one_of: List[StickyOneOf]

    def __init__(self, one_of: List[StickyOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'FluffySlack':
        assert isinstance(obj, dict)
        one_of = from_list(StickyOneOf.from_dict, obj.get("oneOf"))
        return FluffySlack(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(StickyOneOf, x), self.one_of)
        return result


class IndecentProperties:
    basecamp_campfire: Optional[ItemsElement]
    properties_if: AgentsElement
    slack: Optional[FluffySlack]
    github_commit_status: Optional[GithubCommitStatus]
    github_check: Optional[GithubCheck]

    def __init__(self, basecamp_campfire: Optional[ItemsElement], properties_if: AgentsElement, slack: Optional[FluffySlack], github_commit_status: Optional[GithubCommitStatus], github_check: Optional[GithubCheck]) -> None:
        self.basecamp_campfire = basecamp_campfire
        self.properties_if = properties_if
        self.slack = slack
        self.github_commit_status = github_commit_status
        self.github_check = github_check

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentProperties':
        assert isinstance(obj, dict)
        basecamp_campfire = from_union([ItemsElement.from_dict, from_none], obj.get("basecamp_campfire"))
        properties_if = AgentsElement.from_dict(obj.get("if"))
        slack = from_union([FluffySlack.from_dict, from_none], obj.get("slack"))
        github_commit_status = from_union([GithubCommitStatus.from_dict, from_none], obj.get("github_commit_status"))
        github_check = from_union([GithubCheck.from_dict, from_none], obj.get("github_check"))
        return IndecentProperties(basecamp_campfire, properties_if, slack, github_commit_status, github_check)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.basecamp_campfire is not None:
            result["basecamp_campfire"] = from_union([lambda x: to_class(ItemsElement, x), from_none], self.basecamp_campfire)
        result["if"] = to_class(AgentsElement, self.properties_if)
        if self.slack is not None:
            result["slack"] = from_union([lambda x: to_class(FluffySlack, x), from_none], self.slack)
        if self.github_commit_status is not None:
            result["github_commit_status"] = from_union([lambda x: to_class(GithubCommitStatus, x), from_none], self.github_commit_status)
        if self.github_check is not None:
            result["github_check"] = from_union([lambda x: to_class(GithubCheck, x), from_none], self.github_check)
        return result


class TentacledOneOf:
    type: str
    enum: Optional[List[str]]
    properties: Optional[IndecentProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: str, enum: Optional[List[str]], properties: Optional[IndecentProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.enum = enum
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        enum = from_union([lambda x: from_list(from_str, x), from_none], obj.get("enum"))
        properties = from_union([IndecentProperties.from_dict, from_none], obj.get("properties"))
        additional_properties = from_union([from_bool, from_none], obj.get("additionalProperties"))
        return TentacledOneOf(type, enum, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_str, x), from_none], self.enum)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: to_class(IndecentProperties, x), from_none], self.properties)
        if self.additional_properties is not None:
            result["additionalProperties"] = from_union([from_bool, from_none], self.additional_properties)
        return result


class NotifyItems:
    one_of: List[TentacledOneOf]

    def __init__(self, one_of: List[TentacledOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'NotifyItems':
        assert isinstance(obj, dict)
        one_of = from_list(TentacledOneOf.from_dict, obj.get("oneOf"))
        return NotifyItems(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(TentacledOneOf, x), self.one_of)
        return result


class Notify:
    type: AgentsListType
    description: str
    items: NotifyItems

    def __init__(self, type: AgentsListType, description: str, items: NotifyItems) -> None:
        self.type = type
        self.description = description
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'Notify':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        description = from_str(obj.get("description"))
        items = NotifyItems.from_dict(obj.get("items"))
        return Notify(type, description, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["description"] = from_str(self.description)
        result["items"] = to_class(NotifyItems, self.items)
        return result


class DockerComposeV100:
    run: str

    def __init__(self, run: str) -> None:
        self.run = run

    @staticmethod
    def from_dict(obj: Any) -> 'DockerComposeV100':
        assert isinstance(obj, dict)
        run = from_str(obj.get("run"))
        return DockerComposeV100(run)

    def to_dict(self) -> dict:
        result: dict = {}
        result["run"] = from_str(self.run)
        return result


class StickyExample:
    docker_compose_v1_00: DockerComposeV100

    def __init__(self, docker_compose_v1_00: DockerComposeV100) -> None:
        self.docker_compose_v1_00 = docker_compose_v1_00

    @staticmethod
    def from_dict(obj: Any) -> 'StickyExample':
        assert isinstance(obj, dict)
        docker_compose_v1_00 = DockerComposeV100.from_dict(obj.get("docker-compose#v1.0.0"))
        return StickyExample(docker_compose_v1_00)

    def to_dict(self) -> dict:
        result: dict = {}
        result["docker-compose#v1.0.0"] = to_class(DockerComposeV100, self.docker_compose_v1_00)
        return result


class IndigoOneOf:
    type: str
    max_properties: Optional[int]
    examples: Optional[List[StickyExample]]

    def __init__(self, type: str, max_properties: Optional[int], examples: Optional[List[StickyExample]]) -> None:
        self.type = type
        self.max_properties = max_properties
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        max_properties = from_union([from_int, from_none], obj.get("maxProperties"))
        examples = from_union([lambda x: from_list(StickyExample.from_dict, x), from_none], obj.get("examples"))
        return IndigoOneOf(type, max_properties, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.max_properties is not None:
            result["maxProperties"] = from_union([from_int, from_none], self.max_properties)
        if self.examples is not None:
            result["examples"] = from_union([lambda x: from_list(lambda x: to_class(StickyExample, x), x), from_none], self.examples)
        return result


class PurpleItems:
    one_of: List[IndigoOneOf]

    def __init__(self, one_of: List[IndigoOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleItems':
        assert isinstance(obj, dict)
        one_of = from_list(IndigoOneOf.from_dict, obj.get("oneOf"))
        return PurpleItems(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(IndigoOneOf, x), self.one_of)
        return result


class PluginsAnyOf:
    type: str
    description: str
    items: Optional[PurpleItems]

    def __init__(self, type: str, description: str, items: Optional[PurpleItems]) -> None:
        self.type = type
        self.description = description
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'PluginsAnyOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        items = from_union([PurpleItems.from_dict, from_none], obj.get("items"))
        return PluginsAnyOf(type, description, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(PurpleItems, x), from_none], self.items)
        return result


class Plugins:
    any_of: List[PluginsAnyOf]

    def __init__(self, any_of: List[PluginsAnyOf]) -> None:
        self.any_of = any_of

    @staticmethod
    def from_dict(obj: Any) -> 'Plugins':
        assert isinstance(obj, dict)
        any_of = from_list(PluginsAnyOf.from_dict, obj.get("anyOf"))
        return Plugins(any_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["anyOf"] = from_list(lambda x: to_class(PluginsAnyOf, x), self.any_of)
        return result


class AutomaticAnyOf:
    enum: Optional[List[bool]]
    ref: Optional[str]
    type: Optional[AgentsListType]
    items: Optional[AgentsElement]

    def __init__(self, enum: Optional[List[bool]], ref: Optional[str], type: Optional[AgentsListType], items: Optional[AgentsElement]) -> None:
        self.enum = enum
        self.ref = ref
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'AutomaticAnyOf':
        assert isinstance(obj, dict)
        enum = from_union([lambda x: from_list(lambda x: from_union([from_bool, lambda x: from_stringified_bool(from_str(x))], x), x), from_none], obj.get("enum"))
        ref = from_union([from_str, from_none], obj.get("$ref"))
        type = from_union([AgentsListType, from_none], obj.get("type"))
        items = from_union([AgentsElement.from_dict, from_none], obj.get("items"))
        return AutomaticAnyOf(enum, ref, type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_bool, x), from_none], self.enum)
        if self.ref is not None:
            result["$ref"] = from_union([from_str, from_none], self.ref)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(AgentsListType, x), from_none], self.type)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(AgentsElement, x), from_none], self.items)
        return result


class DefaultElement:
    exit_status: str
    limit: int

    def __init__(self, exit_status: str, limit: int) -> None:
        self.exit_status = exit_status
        self.limit = limit

    @staticmethod
    def from_dict(obj: Any) -> 'DefaultElement':
        assert isinstance(obj, dict)
        exit_status = from_str(obj.get("exit_status"))
        limit = from_int(obj.get("limit"))
        return DefaultElement(exit_status, limit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["exit_status"] = from_str(self.exit_status)
        result["limit"] = from_int(self.limit)
        return result


class Automatic:
    any_of: List[AutomaticAnyOf]
    description: str
    default: List[DefaultElement]

    def __init__(self, any_of: List[AutomaticAnyOf], description: str, default: List[DefaultElement]) -> None:
        self.any_of = any_of
        self.description = description
        self.default = default

    @staticmethod
    def from_dict(obj: Any) -> 'Automatic':
        assert isinstance(obj, dict)
        any_of = from_list(AutomaticAnyOf.from_dict, obj.get("anyOf"))
        description = from_str(obj.get("description"))
        default = from_list(DefaultElement.from_dict, obj.get("default"))
        return Automatic(any_of, description, default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["anyOf"] = from_list(lambda x: to_class(AutomaticAnyOf, x), self.any_of)
        result["description"] = from_str(self.description)
        result["default"] = from_list(lambda x: to_class(DefaultElement, x), self.default)
        return result


class HilariousProperties:
    allowed: AllowDependencyFailure
    permit_on_passed: AllowDependencyFailure
    reason: AgentsList

    def __init__(self, allowed: AllowDependencyFailure, permit_on_passed: AllowDependencyFailure, reason: AgentsList) -> None:
        self.allowed = allowed
        self.permit_on_passed = permit_on_passed
        self.reason = reason

    @staticmethod
    def from_dict(obj: Any) -> 'HilariousProperties':
        assert isinstance(obj, dict)
        allowed = AllowDependencyFailure.from_dict(obj.get("allowed"))
        permit_on_passed = AllowDependencyFailure.from_dict(obj.get("permit_on_passed"))
        reason = AgentsList.from_dict(obj.get("reason"))
        return HilariousProperties(allowed, permit_on_passed, reason)

    def to_dict(self) -> dict:
        result: dict = {}
        result["allowed"] = to_class(AllowDependencyFailure, self.allowed)
        result["permit_on_passed"] = to_class(AllowDependencyFailure, self.permit_on_passed)
        result["reason"] = to_class(AgentsList, self.reason)
        return result


class ManualAnyOf:
    enum: Optional[List[bool]]
    type: Optional[str]
    properties: Optional[HilariousProperties]
    additional_properties: Optional[bool]

    def __init__(self, enum: Optional[List[bool]], type: Optional[str], properties: Optional[HilariousProperties], additional_properties: Optional[bool]) -> None:
        self.enum = enum
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'ManualAnyOf':
        assert isinstance(obj, dict)
        enum = from_union([lambda x: from_list(lambda x: from_union([from_bool, lambda x: from_stringified_bool(from_str(x))], x), x), from_none], obj.get("enum"))
        type = from_union([from_str, from_none], obj.get("type"))
        properties = from_union([HilariousProperties.from_dict, from_none], obj.get("properties"))
        additional_properties = from_union([from_bool, from_none], obj.get("additionalProperties"))
        return ManualAnyOf(enum, type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_bool, x), from_none], self.enum)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: to_class(HilariousProperties, x), from_none], self.properties)
        if self.additional_properties is not None:
            result["additionalProperties"] = from_union([from_bool, from_none], self.additional_properties)
        return result


class Manual:
    description: str
    any_of: List[ManualAnyOf]
    default: bool

    def __init__(self, description: str, any_of: List[ManualAnyOf], default: bool) -> None:
        self.description = description
        self.any_of = any_of
        self.default = default

    @staticmethod
    def from_dict(obj: Any) -> 'Manual':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        any_of = from_list(ManualAnyOf.from_dict, obj.get("anyOf"))
        default = from_bool(obj.get("default"))
        return Manual(description, any_of, default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["anyOf"] = from_list(lambda x: to_class(ManualAnyOf, x), self.any_of)
        result["default"] = from_bool(self.default)
        return result


class RetryProperties:
    automatic: Automatic
    manual: Manual

    def __init__(self, automatic: Automatic, manual: Manual) -> None:
        self.automatic = automatic
        self.manual = manual

    @staticmethod
    def from_dict(obj: Any) -> 'RetryProperties':
        assert isinstance(obj, dict)
        automatic = Automatic.from_dict(obj.get("automatic"))
        manual = Manual.from_dict(obj.get("manual"))
        return RetryProperties(automatic, manual)

    def to_dict(self) -> dict:
        result: dict = {}
        result["automatic"] = to_class(Automatic, self.automatic)
        result["manual"] = to_class(Manual, self.manual)
        return result


class Retry:
    type: str
    description: str
    properties: RetryProperties
    additional_properties: bool

    def __init__(self, type: str, description: str, properties: RetryProperties, additional_properties: bool) -> None:
        self.type = type
        self.description = description
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'Retry':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        properties = RetryProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return Retry(type, description, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["properties"] = to_class(RetryProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class SignedFields:
    type: AgentsListType
    description: str
    items: ItemsElement
    examples: List[List[str]]

    def __init__(self, type: AgentsListType, description: str, items: ItemsElement, examples: List[List[str]]) -> None:
        self.type = type
        self.description = description
        self.items = items
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'SignedFields':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        description = from_str(obj.get("description"))
        items = ItemsElement.from_dict(obj.get("items"))
        examples = from_list(lambda x: from_list(from_str, x), obj.get("examples"))
        return SignedFields(type, description, items, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["description"] = from_str(self.description)
        result["items"] = to_class(ItemsElement, self.items)
        result["examples"] = from_list(lambda x: from_list(from_str, x), self.examples)
        return result


class SignatureProperties:
    algorithm: AgentsList
    value: Trigger
    signed_fields: SignedFields

    def __init__(self, algorithm: AgentsList, value: Trigger, signed_fields: SignedFields) -> None:
        self.algorithm = algorithm
        self.value = value
        self.signed_fields = signed_fields

    @staticmethod
    def from_dict(obj: Any) -> 'SignatureProperties':
        assert isinstance(obj, dict)
        algorithm = AgentsList.from_dict(obj.get("algorithm"))
        value = Trigger.from_dict(obj.get("value"))
        signed_fields = SignedFields.from_dict(obj.get("signed_fields"))
        return SignatureProperties(algorithm, value, signed_fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["algorithm"] = to_class(AgentsList, self.algorithm)
        result["value"] = to_class(Trigger, self.value)
        result["signed_fields"] = to_class(SignedFields, self.signed_fields)
        return result


class Signature:
    type: str
    description: str
    properties: SignatureProperties

    def __init__(self, type: str, description: str, properties: SignatureProperties) -> None:
        self.type = type
        self.description = description
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Signature':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        properties = SignatureProperties.from_dict(obj.get("properties"))
        return Signature(type, description, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["properties"] = to_class(SignatureProperties, self.properties)
        return result


class CommandStepProperties:
    agents: AgentsElement
    allow_dependency_failure: AgentsElement
    artifact_paths: ArtifactPaths
    branches: AgentsElement
    cache: AgentsElement
    cancel_on_build_failing: AgentsElement
    command: Command
    commands: Commands
    concurrency: Concurrency
    concurrency_group: AgentsList
    concurrency_method: AgentsList
    depends_on: AgentsElement
    env: AgentsElement
    properties_if: AgentsElement
    key: AgentsElement
    identifier: AgentsElement
    id: ID
    label: AgentsElement
    signature: Signature
    matrix: Matrix
    name: AgentsElement
    notify: Notify
    parallelism: Concurrency
    plugins: Plugins
    soft_fail: AgentsElement
    retry: Retry
    skip: AgentsElement
    timeout_in_minutes: Limit
    type: TypeElement
    priority: Concurrency

    def __init__(self, agents: AgentsElement, allow_dependency_failure: AgentsElement, artifact_paths: ArtifactPaths, branches: AgentsElement, cache: AgentsElement, cancel_on_build_failing: AgentsElement, command: Command, commands: Commands, concurrency: Concurrency, concurrency_group: AgentsList, concurrency_method: AgentsList, depends_on: AgentsElement, env: AgentsElement, properties_if: AgentsElement, key: AgentsElement, identifier: AgentsElement, id: ID, label: AgentsElement, signature: Signature, matrix: Matrix, name: AgentsElement, notify: Notify, parallelism: Concurrency, plugins: Plugins, soft_fail: AgentsElement, retry: Retry, skip: AgentsElement, timeout_in_minutes: Limit, type: TypeElement, priority: Concurrency) -> None:
        self.agents = agents
        self.allow_dependency_failure = allow_dependency_failure
        self.artifact_paths = artifact_paths
        self.branches = branches
        self.cache = cache
        self.cancel_on_build_failing = cancel_on_build_failing
        self.command = command
        self.commands = commands
        self.concurrency = concurrency
        self.concurrency_group = concurrency_group
        self.concurrency_method = concurrency_method
        self.depends_on = depends_on
        self.env = env
        self.properties_if = properties_if
        self.key = key
        self.identifier = identifier
        self.id = id
        self.label = label
        self.signature = signature
        self.matrix = matrix
        self.name = name
        self.notify = notify
        self.parallelism = parallelism
        self.plugins = plugins
        self.soft_fail = soft_fail
        self.retry = retry
        self.skip = skip
        self.timeout_in_minutes = timeout_in_minutes
        self.type = type
        self.priority = priority

    @staticmethod
    def from_dict(obj: Any) -> 'CommandStepProperties':
        assert isinstance(obj, dict)
        agents = AgentsElement.from_dict(obj.get("agents"))
        allow_dependency_failure = AgentsElement.from_dict(obj.get("allow_dependency_failure"))
        artifact_paths = ArtifactPaths.from_dict(obj.get("artifact_paths"))
        branches = AgentsElement.from_dict(obj.get("branches"))
        cache = AgentsElement.from_dict(obj.get("cache"))
        cancel_on_build_failing = AgentsElement.from_dict(obj.get("cancel_on_build_failing"))
        command = Command.from_dict(obj.get("command"))
        commands = Commands.from_dict(obj.get("commands"))
        concurrency = Concurrency.from_dict(obj.get("concurrency"))
        concurrency_group = AgentsList.from_dict(obj.get("concurrency_group"))
        concurrency_method = AgentsList.from_dict(obj.get("concurrency_method"))
        depends_on = AgentsElement.from_dict(obj.get("depends_on"))
        env = AgentsElement.from_dict(obj.get("env"))
        properties_if = AgentsElement.from_dict(obj.get("if"))
        key = AgentsElement.from_dict(obj.get("key"))
        identifier = AgentsElement.from_dict(obj.get("identifier"))
        id = ID.from_dict(obj.get("id"))
        label = AgentsElement.from_dict(obj.get("label"))
        signature = Signature.from_dict(obj.get("signature"))
        matrix = Matrix.from_dict(obj.get("matrix"))
        name = AgentsElement.from_dict(obj.get("name"))
        notify = Notify.from_dict(obj.get("notify"))
        parallelism = Concurrency.from_dict(obj.get("parallelism"))
        plugins = Plugins.from_dict(obj.get("plugins"))
        soft_fail = AgentsElement.from_dict(obj.get("soft_fail"))
        retry = Retry.from_dict(obj.get("retry"))
        skip = AgentsElement.from_dict(obj.get("skip"))
        timeout_in_minutes = Limit.from_dict(obj.get("timeout_in_minutes"))
        type = TypeElement.from_dict(obj.get("type"))
        priority = Concurrency.from_dict(obj.get("priority"))
        return CommandStepProperties(agents, allow_dependency_failure, artifact_paths, branches, cache, cancel_on_build_failing, command, commands, concurrency, concurrency_group, concurrency_method, depends_on, env, properties_if, key, identifier, id, label, signature, matrix, name, notify, parallelism, plugins, soft_fail, retry, skip, timeout_in_minutes, type, priority)

    def to_dict(self) -> dict:
        result: dict = {}
        result["agents"] = to_class(AgentsElement, self.agents)
        result["allow_dependency_failure"] = to_class(AgentsElement, self.allow_dependency_failure)
        result["artifact_paths"] = to_class(ArtifactPaths, self.artifact_paths)
        result["branches"] = to_class(AgentsElement, self.branches)
        result["cache"] = to_class(AgentsElement, self.cache)
        result["cancel_on_build_failing"] = to_class(AgentsElement, self.cancel_on_build_failing)
        result["command"] = to_class(Command, self.command)
        result["commands"] = to_class(Commands, self.commands)
        result["concurrency"] = to_class(Concurrency, self.concurrency)
        result["concurrency_group"] = to_class(AgentsList, self.concurrency_group)
        result["concurrency_method"] = to_class(AgentsList, self.concurrency_method)
        result["depends_on"] = to_class(AgentsElement, self.depends_on)
        result["env"] = to_class(AgentsElement, self.env)
        result["if"] = to_class(AgentsElement, self.properties_if)
        result["key"] = to_class(AgentsElement, self.key)
        result["identifier"] = to_class(AgentsElement, self.identifier)
        result["id"] = to_class(ID, self.id)
        result["label"] = to_class(AgentsElement, self.label)
        result["signature"] = to_class(Signature, self.signature)
        result["matrix"] = to_class(Matrix, self.matrix)
        result["name"] = to_class(AgentsElement, self.name)
        result["notify"] = to_class(Notify, self.notify)
        result["parallelism"] = to_class(Concurrency, self.parallelism)
        result["plugins"] = to_class(Plugins, self.plugins)
        result["soft_fail"] = to_class(AgentsElement, self.soft_fail)
        result["retry"] = to_class(Retry, self.retry)
        result["skip"] = to_class(AgentsElement, self.skip)
        result["timeout_in_minutes"] = to_class(Limit, self.timeout_in_minutes)
        result["type"] = to_class(TypeElement, self.type)
        result["priority"] = to_class(Concurrency, self.priority)
        return result


class CommandStep:
    type: str
    properties: CommandStepProperties
    additional_properties: bool

    def __init__(self, type: str, properties: CommandStepProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'CommandStep':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = CommandStepProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return CommandStep(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(CommandStepProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class AllowFailure:
    enum: List[bool]
    default: bool

    def __init__(self, enum: List[bool], default: bool) -> None:
        self.enum = enum
        self.default = default

    @staticmethod
    def from_dict(obj: Any) -> 'AllowFailure':
        assert isinstance(obj, dict)
        enum = from_list(lambda x: from_union([from_bool, lambda x: from_stringified_bool(from_str(x))], x), obj.get("enum"))
        default = from_bool(obj.get("default"))
        return AllowFailure(enum, default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enum"] = from_list(from_bool, self.enum)
        result["default"] = from_bool(self.default)
        return result


class AmbitiousProperties:
    step: ItemsElement
    allow_failure: AllowFailure

    def __init__(self, step: ItemsElement, allow_failure: AllowFailure) -> None:
        self.step = step
        self.allow_failure = allow_failure

    @staticmethod
    def from_dict(obj: Any) -> 'AmbitiousProperties':
        assert isinstance(obj, dict)
        step = ItemsElement.from_dict(obj.get("step"))
        allow_failure = AllowFailure.from_dict(obj.get("allow_failure"))
        return AmbitiousProperties(step, allow_failure)

    def to_dict(self) -> dict:
        result: dict = {}
        result["step"] = to_class(ItemsElement, self.step)
        result["allow_failure"] = to_class(AllowFailure, self.allow_failure)
        return result


class ItemsAnyOf:
    type: str
    properties: Optional[AmbitiousProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: str, properties: Optional[AmbitiousProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'ItemsAnyOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = from_union([AmbitiousProperties.from_dict, from_none], obj.get("properties"))
        additional_properties = from_union([from_bool, from_none], obj.get("additionalProperties"))
        return ItemsAnyOf(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.properties is not None:
            result["properties"] = from_union([lambda x: to_class(AmbitiousProperties, x), from_none], self.properties)
        if self.additional_properties is not None:
            result["additionalProperties"] = from_union([from_bool, from_none], self.additional_properties)
        return result


class FluffyItems:
    any_of: List[ItemsAnyOf]

    def __init__(self, any_of: List[ItemsAnyOf]) -> None:
        self.any_of = any_of

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyItems':
        assert isinstance(obj, dict)
        any_of = from_list(ItemsAnyOf.from_dict, obj.get("anyOf"))
        return FluffyItems(any_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["anyOf"] = from_list(lambda x: to_class(ItemsAnyOf, x), self.any_of)
        return result


class DependsOnAnyOf:
    type: str
    items: Optional[FluffyItems]

    def __init__(self, type: str, items: Optional[FluffyItems]) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'DependsOnAnyOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = from_union([FluffyItems.from_dict, from_none], obj.get("items"))
        return DependsOnAnyOf(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(FluffyItems, x), from_none], self.items)
        return result


class DependsOn:
    description: str
    any_of: List[DependsOnAnyOf]

    def __init__(self, description: str, any_of: List[DependsOnAnyOf]) -> None:
        self.description = description
        self.any_of = any_of

    @staticmethod
    def from_dict(obj: Any) -> 'DependsOn':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        any_of = from_list(DependsOnAnyOf.from_dict, obj.get("anyOf"))
        return DependsOn(description, any_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["anyOf"] = from_list(lambda x: to_class(DependsOnAnyOf, x), self.any_of)
        return result


class EnvExample:
    node_env: str

    def __init__(self, node_env: str) -> None:
        self.node_env = node_env

    @staticmethod
    def from_dict(obj: Any) -> 'EnvExample':
        assert isinstance(obj, dict)
        node_env = from_str(obj.get("NODE_ENV"))
        return EnvExample(node_env)

    def to_dict(self) -> dict:
        result: dict = {}
        result["NODE_ENV"] = from_str(self.node_env)
        return result


class Env:
    type: str
    description: str
    examples: List[EnvExample]

    def __init__(self, type: str, description: str, examples: List[EnvExample]) -> None:
        self.type = type
        self.description = description
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'Env':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        examples = from_list(EnvExample.from_dict, obj.get("examples"))
        return Env(type, description, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(lambda x: to_class(EnvExample, x), self.examples)
        return result


class PropertiesDefault:
    type: Optional[ItemsType]
    description: str
    examples: List[Union[List[str], str]]
    one_of: Optional[List[AnyOf]]

    def __init__(self, type: Optional[ItemsType], description: str, examples: List[Union[List[str], str]], one_of: Optional[List[AnyOf]]) -> None:
        self.type = type
        self.description = description
        self.examples = examples
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'PropertiesDefault':
        assert isinstance(obj, dict)
        type = from_union([ItemsType, from_none], obj.get("type"))
        description = from_str(obj.get("description"))
        examples = from_list(lambda x: from_union([lambda x: from_list(from_str, x), from_str], x), obj.get("examples"))
        one_of = from_union([lambda x: from_list(AnyOf.from_dict, x), from_none], obj.get("oneOf"))
        return PropertiesDefault(type, description, examples, one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(ItemsType, x), from_none], self.type)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(lambda x: from_union([lambda x: from_list(from_str, x), from_str], x), self.examples)
        if self.one_of is not None:
            result["oneOf"] = from_union([lambda x: from_list(lambda x: to_class(AnyOf, x), x), from_none], self.one_of)
        return result


class MagentaProperties:
    label: AgentsList
    value: AgentsList
    hint: AgentsList
    required: AllowDependencyFailure

    def __init__(self, label: AgentsList, value: AgentsList, hint: AgentsList, required: AllowDependencyFailure) -> None:
        self.label = label
        self.value = value
        self.hint = hint
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'MagentaProperties':
        assert isinstance(obj, dict)
        label = AgentsList.from_dict(obj.get("label"))
        value = AgentsList.from_dict(obj.get("value"))
        hint = AgentsList.from_dict(obj.get("hint"))
        required = AllowDependencyFailure.from_dict(obj.get("required"))
        return MagentaProperties(label, value, hint, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["label"] = to_class(AgentsList, self.label)
        result["value"] = to_class(AgentsList, self.value)
        result["hint"] = to_class(AgentsList, self.hint)
        result["required"] = to_class(AllowDependencyFailure, self.required)
        return result


class OptionsItems:
    type: str
    properties: MagentaProperties
    additional_properties: bool
    required: List[str]

    def __init__(self, type: str, properties: MagentaProperties, additional_properties: bool, required: List[str]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'OptionsItems':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = MagentaProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        required = from_list(from_str, obj.get("required"))
        return OptionsItems(type, properties, additional_properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(MagentaProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        result["required"] = from_list(from_str, self.required)
        return result


class Options:
    type: AgentsListType
    min_items: int
    items: OptionsItems

    def __init__(self, type: AgentsListType, min_items: int, items: OptionsItems) -> None:
        self.type = type
        self.min_items = min_items
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'Options':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        min_items = from_int(obj.get("minItems"))
        items = OptionsItems.from_dict(obj.get("items"))
        return Options(type, min_items, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["minItems"] = from_int(self.min_items)
        result["items"] = to_class(OptionsItems, self.items)
        return result


class CunningProperties:
    text: Optional[AgentsList]
    key: AgentsList
    hint: AgentsList
    format: Optional[AgentsList]
    required: AllowDependencyFailure
    default: PropertiesDefault
    select: Optional[AgentsList]
    multiple: Optional[AllowDependencyFailure]
    options: Optional[Options]

    def __init__(self, text: Optional[AgentsList], key: AgentsList, hint: AgentsList, format: Optional[AgentsList], required: AllowDependencyFailure, default: PropertiesDefault, select: Optional[AgentsList], multiple: Optional[AllowDependencyFailure], options: Optional[Options]) -> None:
        self.text = text
        self.key = key
        self.hint = hint
        self.format = format
        self.required = required
        self.default = default
        self.select = select
        self.multiple = multiple
        self.options = options

    @staticmethod
    def from_dict(obj: Any) -> 'CunningProperties':
        assert isinstance(obj, dict)
        text = from_union([AgentsList.from_dict, from_none], obj.get("text"))
        key = AgentsList.from_dict(obj.get("key"))
        hint = AgentsList.from_dict(obj.get("hint"))
        format = from_union([AgentsList.from_dict, from_none], obj.get("format"))
        required = AllowDependencyFailure.from_dict(obj.get("required"))
        default = PropertiesDefault.from_dict(obj.get("default"))
        select = from_union([AgentsList.from_dict, from_none], obj.get("select"))
        multiple = from_union([AllowDependencyFailure.from_dict, from_none], obj.get("multiple"))
        options = from_union([Options.from_dict, from_none], obj.get("options"))
        return CunningProperties(text, key, hint, format, required, default, select, multiple, options)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.text is not None:
            result["text"] = from_union([lambda x: to_class(AgentsList, x), from_none], self.text)
        result["key"] = to_class(AgentsList, self.key)
        result["hint"] = to_class(AgentsList, self.hint)
        if self.format is not None:
            result["format"] = from_union([lambda x: to_class(AgentsList, x), from_none], self.format)
        result["required"] = to_class(AllowDependencyFailure, self.required)
        result["default"] = to_class(PropertiesDefault, self.default)
        if self.select is not None:
            result["select"] = from_union([lambda x: to_class(AgentsList, x), from_none], self.select)
        if self.multiple is not None:
            result["multiple"] = from_union([lambda x: to_class(AllowDependencyFailure, x), from_none], self.multiple)
        if self.options is not None:
            result["options"] = from_union([lambda x: to_class(Options, x), from_none], self.options)
        return result


class IndecentOneOf:
    type: str
    properties: CunningProperties
    additional_properties: bool
    required: List[str]

    def __init__(self, type: str, properties: CunningProperties, additional_properties: bool, required: List[str]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentOneOf':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = CunningProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        required = from_list(from_str, obj.get("required"))
        return IndecentOneOf(type, properties, additional_properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(CunningProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        result["required"] = from_list(from_str, self.required)
        return result


class FieldsItems:
    one_of: List[IndecentOneOf]

    def __init__(self, one_of: List[IndecentOneOf]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'FieldsItems':
        assert isinstance(obj, dict)
        one_of = from_list(IndecentOneOf.from_dict, obj.get("oneOf"))
        return FieldsItems(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(IndecentOneOf, x), self.one_of)
        return result


class Fields:
    type: AgentsListType
    description: str
    items: FieldsItems

    def __init__(self, type: AgentsListType, description: str, items: FieldsItems) -> None:
        self.type = type
        self.description = description
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'Fields':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        description = from_str(obj.get("description"))
        items = FieldsItems.from_dict(obj.get("items"))
        return Fields(type, description, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["description"] = from_str(self.description)
        result["items"] = to_class(FieldsItems, self.items)
        return result


class Group:
    type: List[str]
    description: str
    examples: List[str]

    def __init__(self, type: List[str], description: str, examples: List[str]) -> None:
        self.type = type
        self.description = description
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        assert isinstance(obj, dict)
        type = from_list(from_str, obj.get("type"))
        description = from_str(obj.get("description"))
        examples = from_list(from_str, obj.get("examples"))
        return Group(type, description, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_list(from_str, self.type)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(from_str, self.examples)
        return result


class StepsItems:
    any_of: List[AgentsElement]

    def __init__(self, any_of: List[AgentsElement]) -> None:
        self.any_of = any_of

    @staticmethod
    def from_dict(obj: Any) -> 'StepsItems':
        assert isinstance(obj, dict)
        any_of = from_list(AgentsElement.from_dict, obj.get("anyOf"))
        return StepsItems(any_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["anyOf"] = from_list(lambda x: to_class(AgentsElement, x), self.any_of)
        return result


class Steps:
    type: AgentsListType
    description: str
    items: StepsItems
    min_items: Optional[int]

    def __init__(self, type: AgentsListType, description: str, items: StepsItems, min_items: Optional[int]) -> None:
        self.type = type
        self.description = description
        self.items = items
        self.min_items = min_items

    @staticmethod
    def from_dict(obj: Any) -> 'Steps':
        assert isinstance(obj, dict)
        type = AgentsListType(obj.get("type"))
        description = from_str(obj.get("description"))
        items = StepsItems.from_dict(obj.get("items"))
        min_items = from_union([from_int, from_none], obj.get("minItems"))
        return Steps(type, description, items, min_items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(AgentsListType, self.type)
        result["description"] = from_str(self.description)
        result["items"] = to_class(StepsItems, self.items)
        if self.min_items is not None:
            result["minItems"] = from_union([from_int, from_none], self.min_items)
        return result


class GroupStepProperties:
    depends_on: AgentsElement
    group: Group
    properties_if: AgentsElement
    key: AgentsElement
    identifier: AgentsElement
    id: ID
    label: AgentsElement
    name: AgentsElement
    allow_dependency_failure: AgentsElement
    notify: AgentsElement
    skip: AgentsElement
    steps: Steps

    def __init__(self, depends_on: AgentsElement, group: Group, properties_if: AgentsElement, key: AgentsElement, identifier: AgentsElement, id: ID, label: AgentsElement, name: AgentsElement, allow_dependency_failure: AgentsElement, notify: AgentsElement, skip: AgentsElement, steps: Steps) -> None:
        self.depends_on = depends_on
        self.group = group
        self.properties_if = properties_if
        self.key = key
        self.identifier = identifier
        self.id = id
        self.label = label
        self.name = name
        self.allow_dependency_failure = allow_dependency_failure
        self.notify = notify
        self.skip = skip
        self.steps = steps

    @staticmethod
    def from_dict(obj: Any) -> 'GroupStepProperties':
        assert isinstance(obj, dict)
        depends_on = AgentsElement.from_dict(obj.get("depends_on"))
        group = Group.from_dict(obj.get("group"))
        properties_if = AgentsElement.from_dict(obj.get("if"))
        key = AgentsElement.from_dict(obj.get("key"))
        identifier = AgentsElement.from_dict(obj.get("identifier"))
        id = ID.from_dict(obj.get("id"))
        label = AgentsElement.from_dict(obj.get("label"))
        name = AgentsElement.from_dict(obj.get("name"))
        allow_dependency_failure = AgentsElement.from_dict(obj.get("allow_dependency_failure"))
        notify = AgentsElement.from_dict(obj.get("notify"))
        skip = AgentsElement.from_dict(obj.get("skip"))
        steps = Steps.from_dict(obj.get("steps"))
        return GroupStepProperties(depends_on, group, properties_if, key, identifier, id, label, name, allow_dependency_failure, notify, skip, steps)

    def to_dict(self) -> dict:
        result: dict = {}
        result["depends_on"] = to_class(AgentsElement, self.depends_on)
        result["group"] = to_class(Group, self.group)
        result["if"] = to_class(AgentsElement, self.properties_if)
        result["key"] = to_class(AgentsElement, self.key)
        result["identifier"] = to_class(AgentsElement, self.identifier)
        result["id"] = to_class(ID, self.id)
        result["label"] = to_class(AgentsElement, self.label)
        result["name"] = to_class(AgentsElement, self.name)
        result["allow_dependency_failure"] = to_class(AgentsElement, self.allow_dependency_failure)
        result["notify"] = to_class(AgentsElement, self.notify)
        result["skip"] = to_class(AgentsElement, self.skip)
        result["steps"] = to_class(Steps, self.steps)
        return result


class GroupStep:
    type: str
    properties: GroupStepProperties
    required: List[str]
    additional_properties: bool

    def __init__(self, type: str, properties: GroupStepProperties, required: List[str], additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.required = required
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'GroupStep':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = GroupStepProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return GroupStep(type, properties, required, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(GroupStepProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class MatrixElement:
    one_of: List[ItemsElement]

    def __init__(self, one_of: List[ItemsElement]) -> None:
        self.one_of = one_of

    @staticmethod
    def from_dict(obj: Any) -> 'MatrixElement':
        assert isinstance(obj, dict)
        one_of = from_list(ItemsElement.from_dict, obj.get("oneOf"))
        return MatrixElement(one_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oneOf"] = from_list(lambda x: to_class(ItemsElement, x), self.one_of)
        return result


class NestedBlockStepProperties:
    block: AgentsElement

    def __init__(self, block: AgentsElement) -> None:
        self.block = block

    @staticmethod
    def from_dict(obj: Any) -> 'NestedBlockStepProperties':
        assert isinstance(obj, dict)
        block = AgentsElement.from_dict(obj.get("block"))
        return NestedBlockStepProperties(block)

    def to_dict(self) -> dict:
        result: dict = {}
        result["block"] = to_class(AgentsElement, self.block)
        return result


class NestedBlockStep:
    type: str
    properties: NestedBlockStepProperties
    additional_properties: bool

    def __init__(self, type: str, properties: NestedBlockStepProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'NestedBlockStep':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = NestedBlockStepProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return NestedBlockStep(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(NestedBlockStepProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class NestedCommandStepProperties:
    command: AgentsElement
    commands: AgentsElement
    script: AgentsElement

    def __init__(self, command: AgentsElement, commands: AgentsElement, script: AgentsElement) -> None:
        self.command = command
        self.commands = commands
        self.script = script

    @staticmethod
    def from_dict(obj: Any) -> 'NestedCommandStepProperties':
        assert isinstance(obj, dict)
        command = AgentsElement.from_dict(obj.get("command"))
        commands = AgentsElement.from_dict(obj.get("commands"))
        script = AgentsElement.from_dict(obj.get("script"))
        return NestedCommandStepProperties(command, commands, script)

    def to_dict(self) -> dict:
        result: dict = {}
        result["command"] = to_class(AgentsElement, self.command)
        result["commands"] = to_class(AgentsElement, self.commands)
        result["script"] = to_class(AgentsElement, self.script)
        return result


class NestedCommandStep:
    type: str
    properties: NestedCommandStepProperties
    additional_properties: bool

    def __init__(self, type: str, properties: NestedCommandStepProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'NestedCommandStep':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = NestedCommandStepProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return NestedCommandStep(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(NestedCommandStepProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class NestedInputStepProperties:
    input: AgentsElement

    def __init__(self, input: AgentsElement) -> None:
        self.input = input

    @staticmethod
    def from_dict(obj: Any) -> 'NestedInputStepProperties':
        assert isinstance(obj, dict)
        input = AgentsElement.from_dict(obj.get("input"))
        return NestedInputStepProperties(input)

    def to_dict(self) -> dict:
        result: dict = {}
        result["input"] = to_class(AgentsElement, self.input)
        return result


class NestedInputStep:
    type: str
    properties: NestedInputStepProperties
    additional_properties: bool

    def __init__(self, type: str, properties: NestedInputStepProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'NestedInputStep':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = NestedInputStepProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return NestedInputStep(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(NestedInputStepProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class NestedTriggerStepProperties:
    trigger: AgentsElement

    def __init__(self, trigger: AgentsElement) -> None:
        self.trigger = trigger

    @staticmethod
    def from_dict(obj: Any) -> 'NestedTriggerStepProperties':
        assert isinstance(obj, dict)
        trigger = AgentsElement.from_dict(obj.get("trigger"))
        return NestedTriggerStepProperties(trigger)

    def to_dict(self) -> dict:
        result: dict = {}
        result["trigger"] = to_class(AgentsElement, self.trigger)
        return result


class NestedTriggerStep:
    type: str
    properties: NestedTriggerStepProperties
    additional_properties: bool

    def __init__(self, type: str, properties: NestedTriggerStepProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'NestedTriggerStep':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = NestedTriggerStepProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return NestedTriggerStep(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(NestedTriggerStepProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class NestedWaitStepProperties:
    wait: Commands
    waiter: AgentsElement

    def __init__(self, wait: Commands, waiter: AgentsElement) -> None:
        self.wait = wait
        self.waiter = waiter

    @staticmethod
    def from_dict(obj: Any) -> 'NestedWaitStepProperties':
        assert isinstance(obj, dict)
        wait = Commands.from_dict(obj.get("wait"))
        waiter = AgentsElement.from_dict(obj.get("waiter"))
        return NestedWaitStepProperties(wait, waiter)

    def to_dict(self) -> dict:
        result: dict = {}
        result["wait"] = to_class(Commands, self.wait)
        result["waiter"] = to_class(AgentsElement, self.waiter)
        return result


class NestedWaitStep:
    type: str
    properties: NestedWaitStepProperties
    additional_properties: bool

    def __init__(self, type: str, properties: NestedWaitStepProperties, additional_properties: bool) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'NestedWaitStep':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = NestedWaitStepProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return NestedWaitStep(type, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(NestedWaitStepProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class Skip:
    any_of: List[ItemsElement]
    description: str
    examples: List[Union[bool, str]]

    def __init__(self, any_of: List[ItemsElement], description: str, examples: List[Union[bool, str]]) -> None:
        self.any_of = any_of
        self.description = description
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'Skip':
        assert isinstance(obj, dict)
        any_of = from_list(ItemsElement.from_dict, obj.get("anyOf"))
        description = from_str(obj.get("description"))
        examples = from_list(lambda x: from_union([from_bool, from_str], x), obj.get("examples"))
        return Skip(any_of, description, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["anyOf"] = from_list(lambda x: to_class(ItemsElement, x), self.any_of)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(lambda x: from_union([from_bool, from_str], x), self.examples)
        return result


class FluffyExitStatus:
    description: str
    any_of: List[TypeElement]

    def __init__(self, description: str, any_of: List[TypeElement]) -> None:
        self.description = description
        self.any_of = any_of

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyExitStatus':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        any_of = from_list(TypeElement.from_dict, obj.get("anyOf"))
        return FluffyExitStatus(description, any_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["anyOf"] = from_list(lambda x: to_class(TypeElement, x), self.any_of)
        return result


class FriskyProperties:
    exit_status: FluffyExitStatus

    def __init__(self, exit_status: FluffyExitStatus) -> None:
        self.exit_status = exit_status

    @staticmethod
    def from_dict(obj: Any) -> 'FriskyProperties':
        assert isinstance(obj, dict)
        exit_status = FluffyExitStatus.from_dict(obj.get("exit_status"))
        return FriskyProperties(exit_status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["exit_status"] = to_class(FluffyExitStatus, self.exit_status)
        return result


class TentacledItems:
    type: str
    properties: FriskyProperties

    def __init__(self, type: str, properties: FriskyProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledItems':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = FriskyProperties.from_dict(obj.get("properties"))
        return TentacledItems(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(FriskyProperties, self.properties)
        return result


class SoftFailAnyOf:
    enum: Optional[List[bool]]
    type: Optional[AgentsListType]
    items: Optional[TentacledItems]

    def __init__(self, enum: Optional[List[bool]], type: Optional[AgentsListType], items: Optional[TentacledItems]) -> None:
        self.enum = enum
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'SoftFailAnyOf':
        assert isinstance(obj, dict)
        enum = from_union([lambda x: from_list(lambda x: from_union([from_bool, lambda x: from_stringified_bool(from_str(x))], x), x), from_none], obj.get("enum"))
        type = from_union([AgentsListType, from_none], obj.get("type"))
        items = from_union([TentacledItems.from_dict, from_none], obj.get("items"))
        return SoftFailAnyOf(enum, type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.enum is not None:
            result["enum"] = from_union([lambda x: from_list(from_bool, x), from_none], self.enum)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(AgentsListType, x), from_none], self.type)
        if self.items is not None:
            result["items"] = from_union([lambda x: to_class(TentacledItems, x), from_none], self.items)
        return result


class SoftFail:
    description: str
    any_of: List[SoftFailAnyOf]

    def __init__(self, description: str, any_of: List[SoftFailAnyOf]) -> None:
        self.description = description
        self.any_of = any_of

    @staticmethod
    def from_dict(obj: Any) -> 'SoftFail':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        any_of = from_list(SoftFailAnyOf.from_dict, obj.get("anyOf"))
        return SoftFail(description, any_of)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["anyOf"] = from_list(lambda x: to_class(SoftFailAnyOf, x), self.any_of)
        return result


class MetaDataExample:
    server: str

    def __init__(self, server: str) -> None:
        self.server = server

    @staticmethod
    def from_dict(obj: Any) -> 'MetaDataExample':
        assert isinstance(obj, dict)
        server = from_str(obj.get("server"))
        return MetaDataExample(server)

    def to_dict(self) -> dict:
        result: dict = {}
        result["server"] = from_str(self.server)
        return result


class MetaData:
    type: str
    description: str
    examples: List[MetaDataExample]

    def __init__(self, type: str, description: str, examples: List[MetaDataExample]) -> None:
        self.type = type
        self.description = description
        self.examples = examples

    @staticmethod
    def from_dict(obj: Any) -> 'MetaData':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        examples = from_list(MetaDataExample.from_dict, obj.get("examples"))
        return MetaData(type, description, examples)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["examples"] = from_list(lambda x: to_class(MetaDataExample, x), self.examples)
        return result


class BuildProperties:
    branch: AgentsList
    commit: AgentsList
    env: AgentsElement
    message: StringBlockStep
    meta_data: MetaData

    def __init__(self, branch: AgentsList, commit: AgentsList, env: AgentsElement, message: StringBlockStep, meta_data: MetaData) -> None:
        self.branch = branch
        self.commit = commit
        self.env = env
        self.message = message
        self.meta_data = meta_data

    @staticmethod
    def from_dict(obj: Any) -> 'BuildProperties':
        assert isinstance(obj, dict)
        branch = AgentsList.from_dict(obj.get("branch"))
        commit = AgentsList.from_dict(obj.get("commit"))
        env = AgentsElement.from_dict(obj.get("env"))
        message = StringBlockStep.from_dict(obj.get("message"))
        meta_data = MetaData.from_dict(obj.get("meta_data"))
        return BuildProperties(branch, commit, env, message, meta_data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["branch"] = to_class(AgentsList, self.branch)
        result["commit"] = to_class(AgentsList, self.commit)
        result["env"] = to_class(AgentsElement, self.env)
        result["message"] = to_class(StringBlockStep, self.message)
        result["meta_data"] = to_class(MetaData, self.meta_data)
        return result


class Build:
    type: str
    description: str
    properties: BuildProperties
    additional_properties: bool

    def __init__(self, type: str, description: str, properties: BuildProperties, additional_properties: bool) -> None:
        self.type = type
        self.description = description
        self.properties = properties
        self.additional_properties = additional_properties

    @staticmethod
    def from_dict(obj: Any) -> 'Build':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        properties = BuildProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        return Build(type, description, properties, additional_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["properties"] = to_class(BuildProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        return result


class TriggerStepProperties:
    allow_dependency_failure: AgentsElement
    properties_async: AllowDependencyFailure
    branches: AgentsElement
    build: Build
    depends_on: AgentsElement
    properties_if: AgentsElement
    key: AgentsElement
    identifier: AgentsElement
    id: ID
    label: AgentsElement
    name: AgentsElement
    type: TypeElement
    trigger: Trigger
    skip: AgentsElement
    soft_fail: AllowDependencyFailure

    def __init__(self, allow_dependency_failure: AgentsElement, properties_async: AllowDependencyFailure, branches: AgentsElement, build: Build, depends_on: AgentsElement, properties_if: AgentsElement, key: AgentsElement, identifier: AgentsElement, id: ID, label: AgentsElement, name: AgentsElement, type: TypeElement, trigger: Trigger, skip: AgentsElement, soft_fail: AllowDependencyFailure) -> None:
        self.allow_dependency_failure = allow_dependency_failure
        self.properties_async = properties_async
        self.branches = branches
        self.build = build
        self.depends_on = depends_on
        self.properties_if = properties_if
        self.key = key
        self.identifier = identifier
        self.id = id
        self.label = label
        self.name = name
        self.type = type
        self.trigger = trigger
        self.skip = skip
        self.soft_fail = soft_fail

    @staticmethod
    def from_dict(obj: Any) -> 'TriggerStepProperties':
        assert isinstance(obj, dict)
        allow_dependency_failure = AgentsElement.from_dict(obj.get("allow_dependency_failure"))
        properties_async = AllowDependencyFailure.from_dict(obj.get("async"))
        branches = AgentsElement.from_dict(obj.get("branches"))
        build = Build.from_dict(obj.get("build"))
        depends_on = AgentsElement.from_dict(obj.get("depends_on"))
        properties_if = AgentsElement.from_dict(obj.get("if"))
        key = AgentsElement.from_dict(obj.get("key"))
        identifier = AgentsElement.from_dict(obj.get("identifier"))
        id = ID.from_dict(obj.get("id"))
        label = AgentsElement.from_dict(obj.get("label"))
        name = AgentsElement.from_dict(obj.get("name"))
        type = TypeElement.from_dict(obj.get("type"))
        trigger = Trigger.from_dict(obj.get("trigger"))
        skip = AgentsElement.from_dict(obj.get("skip"))
        soft_fail = AllowDependencyFailure.from_dict(obj.get("soft_fail"))
        return TriggerStepProperties(allow_dependency_failure, properties_async, branches, build, depends_on, properties_if, key, identifier, id, label, name, type, trigger, skip, soft_fail)

    def to_dict(self) -> dict:
        result: dict = {}
        result["allow_dependency_failure"] = to_class(AgentsElement, self.allow_dependency_failure)
        result["async"] = to_class(AllowDependencyFailure, self.properties_async)
        result["branches"] = to_class(AgentsElement, self.branches)
        result["build"] = to_class(Build, self.build)
        result["depends_on"] = to_class(AgentsElement, self.depends_on)
        result["if"] = to_class(AgentsElement, self.properties_if)
        result["key"] = to_class(AgentsElement, self.key)
        result["identifier"] = to_class(AgentsElement, self.identifier)
        result["id"] = to_class(ID, self.id)
        result["label"] = to_class(AgentsElement, self.label)
        result["name"] = to_class(AgentsElement, self.name)
        result["type"] = to_class(TypeElement, self.type)
        result["trigger"] = to_class(Trigger, self.trigger)
        result["skip"] = to_class(AgentsElement, self.skip)
        result["soft_fail"] = to_class(AllowDependencyFailure, self.soft_fail)
        return result


class TriggerStep:
    type: str
    properties: TriggerStepProperties
    additional_properties: bool
    required: List[str]

    def __init__(self, type: str, properties: TriggerStepProperties, additional_properties: bool, required: List[str]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'TriggerStep':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = TriggerStepProperties.from_dict(obj.get("properties"))
        additional_properties = from_bool(obj.get("additionalProperties"))
        required = from_list(from_str, obj.get("required"))
        return TriggerStep(type, properties, additional_properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(TriggerStepProperties, self.properties)
        result["additionalProperties"] = from_bool(self.additional_properties)
        result["required"] = from_list(from_str, self.required)
        return result


class Definitions:
    allow_dependency_failure: AllowDependencyFailure
    agents: DefinitionsAgents
    agents_object: AgentsObject
    agents_list: AgentsList
    automatic_retry: AutomaticRetry
    branches: Branches
    cache: Cache
    cancel_on_build_failing: AllowDependencyFailure
    depends_on: DependsOn
    env: Env
    definitions_if: AgentsList
    key: AgentsList
    label: AgentsList
    build_notify: BuildNotify
    fields: Fields
    matrix_element: MatrixElement
    prompt: AgentsList
    skip: Skip
    soft_fail: SoftFail
    block_step: Step
    nested_block_step: NestedBlockStep
    string_block_step: StringBlockStep
    input_step: Step
    nested_input_step: NestedInputStep
    string_input_step: StringBlockStep
    command_step: CommandStep
    nested_command_step: NestedCommandStep
    string_wait_step: StringBlockStep
    wait_step: Step
    nested_wait_step: NestedWaitStep
    trigger_step: TriggerStep
    nested_trigger_step: NestedTriggerStep
    group_step: GroupStep

    def __init__(self, allow_dependency_failure: AllowDependencyFailure, agents: DefinitionsAgents, agents_object: AgentsObject, agents_list: AgentsList, automatic_retry: AutomaticRetry, branches: Branches, cache: Cache, cancel_on_build_failing: AllowDependencyFailure, depends_on: DependsOn, env: Env, definitions_if: AgentsList, key: AgentsList, label: AgentsList, build_notify: BuildNotify, fields: Fields, matrix_element: MatrixElement, prompt: AgentsList, skip: Skip, soft_fail: SoftFail, block_step: Step, nested_block_step: NestedBlockStep, string_block_step: StringBlockStep, input_step: Step, nested_input_step: NestedInputStep, string_input_step: StringBlockStep, command_step: CommandStep, nested_command_step: NestedCommandStep, string_wait_step: StringBlockStep, wait_step: Step, nested_wait_step: NestedWaitStep, trigger_step: TriggerStep, nested_trigger_step: NestedTriggerStep, group_step: GroupStep) -> None:
        self.allow_dependency_failure = allow_dependency_failure
        self.agents = agents
        self.agents_object = agents_object
        self.agents_list = agents_list
        self.automatic_retry = automatic_retry
        self.branches = branches
        self.cache = cache
        self.cancel_on_build_failing = cancel_on_build_failing
        self.depends_on = depends_on
        self.env = env
        self.definitions_if = definitions_if
        self.key = key
        self.label = label
        self.build_notify = build_notify
        self.fields = fields
        self.matrix_element = matrix_element
        self.prompt = prompt
        self.skip = skip
        self.soft_fail = soft_fail
        self.block_step = block_step
        self.nested_block_step = nested_block_step
        self.string_block_step = string_block_step
        self.input_step = input_step
        self.nested_input_step = nested_input_step
        self.string_input_step = string_input_step
        self.command_step = command_step
        self.nested_command_step = nested_command_step
        self.string_wait_step = string_wait_step
        self.wait_step = wait_step
        self.nested_wait_step = nested_wait_step
        self.trigger_step = trigger_step
        self.nested_trigger_step = nested_trigger_step
        self.group_step = group_step

    @staticmethod
    def from_dict(obj: Any) -> 'Definitions':
        assert isinstance(obj, dict)
        allow_dependency_failure = AllowDependencyFailure.from_dict(obj.get("allowDependencyFailure"))
        agents = DefinitionsAgents.from_dict(obj.get("agents"))
        agents_object = AgentsObject.from_dict(obj.get("agentsObject"))
        agents_list = AgentsList.from_dict(obj.get("agentsList"))
        automatic_retry = AutomaticRetry.from_dict(obj.get("automaticRetry"))
        branches = Branches.from_dict(obj.get("branches"))
        cache = Cache.from_dict(obj.get("cache"))
        cancel_on_build_failing = AllowDependencyFailure.from_dict(obj.get("cancelOnBuildFailing"))
        depends_on = DependsOn.from_dict(obj.get("dependsOn"))
        env = Env.from_dict(obj.get("env"))
        definitions_if = AgentsList.from_dict(obj.get("if"))
        key = AgentsList.from_dict(obj.get("key"))
        label = AgentsList.from_dict(obj.get("label"))
        build_notify = BuildNotify.from_dict(obj.get("buildNotify"))
        fields = Fields.from_dict(obj.get("fields"))
        matrix_element = MatrixElement.from_dict(obj.get("matrixElement"))
        prompt = AgentsList.from_dict(obj.get("prompt"))
        skip = Skip.from_dict(obj.get("skip"))
        soft_fail = SoftFail.from_dict(obj.get("softFail"))
        block_step = Step.from_dict(obj.get("blockStep"))
        nested_block_step = NestedBlockStep.from_dict(obj.get("nestedBlockStep"))
        string_block_step = StringBlockStep.from_dict(obj.get("stringBlockStep"))
        input_step = Step.from_dict(obj.get("inputStep"))
        nested_input_step = NestedInputStep.from_dict(obj.get("nestedInputStep"))
        string_input_step = StringBlockStep.from_dict(obj.get("stringInputStep"))
        command_step = CommandStep.from_dict(obj.get("commandStep"))
        nested_command_step = NestedCommandStep.from_dict(obj.get("nestedCommandStep"))
        string_wait_step = StringBlockStep.from_dict(obj.get("stringWaitStep"))
        wait_step = Step.from_dict(obj.get("waitStep"))
        nested_wait_step = NestedWaitStep.from_dict(obj.get("nestedWaitStep"))
        trigger_step = TriggerStep.from_dict(obj.get("triggerStep"))
        nested_trigger_step = NestedTriggerStep.from_dict(obj.get("nestedTriggerStep"))
        group_step = GroupStep.from_dict(obj.get("groupStep"))
        return Definitions(allow_dependency_failure, agents, agents_object, agents_list, automatic_retry, branches, cache, cancel_on_build_failing, depends_on, env, definitions_if, key, label, build_notify, fields, matrix_element, prompt, skip, soft_fail, block_step, nested_block_step, string_block_step, input_step, nested_input_step, string_input_step, command_step, nested_command_step, string_wait_step, wait_step, nested_wait_step, trigger_step, nested_trigger_step, group_step)

    def to_dict(self) -> dict:
        result: dict = {}
        result["allowDependencyFailure"] = to_class(AllowDependencyFailure, self.allow_dependency_failure)
        result["agents"] = to_class(DefinitionsAgents, self.agents)
        result["agentsObject"] = to_class(AgentsObject, self.agents_object)
        result["agentsList"] = to_class(AgentsList, self.agents_list)
        result["automaticRetry"] = to_class(AutomaticRetry, self.automatic_retry)
        result["branches"] = to_class(Branches, self.branches)
        result["cache"] = to_class(Cache, self.cache)
        result["cancelOnBuildFailing"] = to_class(AllowDependencyFailure, self.cancel_on_build_failing)
        result["dependsOn"] = to_class(DependsOn, self.depends_on)
        result["env"] = to_class(Env, self.env)
        result["if"] = to_class(AgentsList, self.definitions_if)
        result["key"] = to_class(AgentsList, self.key)
        result["label"] = to_class(AgentsList, self.label)
        result["buildNotify"] = to_class(BuildNotify, self.build_notify)
        result["fields"] = to_class(Fields, self.fields)
        result["matrixElement"] = to_class(MatrixElement, self.matrix_element)
        result["prompt"] = to_class(AgentsList, self.prompt)
        result["skip"] = to_class(Skip, self.skip)
        result["softFail"] = to_class(SoftFail, self.soft_fail)
        result["blockStep"] = to_class(Step, self.block_step)
        result["nestedBlockStep"] = to_class(NestedBlockStep, self.nested_block_step)
        result["stringBlockStep"] = to_class(StringBlockStep, self.string_block_step)
        result["inputStep"] = to_class(Step, self.input_step)
        result["nestedInputStep"] = to_class(NestedInputStep, self.nested_input_step)
        result["stringInputStep"] = to_class(StringBlockStep, self.string_input_step)
        result["commandStep"] = to_class(CommandStep, self.command_step)
        result["nestedCommandStep"] = to_class(NestedCommandStep, self.nested_command_step)
        result["stringWaitStep"] = to_class(StringBlockStep, self.string_wait_step)
        result["waitStep"] = to_class(Step, self.wait_step)
        result["nestedWaitStep"] = to_class(NestedWaitStep, self.nested_wait_step)
        result["triggerStep"] = to_class(TriggerStep, self.trigger_step)
        result["nestedTriggerStep"] = to_class(NestedTriggerStep, self.nested_trigger_step)
        result["groupStep"] = to_class(GroupStep, self.group_step)
        return result


class SchemaProperties:
    env: AgentsElement
    agents: AgentsElement
    notify: AgentsElement
    steps: Steps

    def __init__(self, env: AgentsElement, agents: AgentsElement, notify: AgentsElement, steps: Steps) -> None:
        self.env = env
        self.agents = agents
        self.notify = notify
        self.steps = steps

    @staticmethod
    def from_dict(obj: Any) -> 'SchemaProperties':
        assert isinstance(obj, dict)
        env = AgentsElement.from_dict(obj.get("env"))
        agents = AgentsElement.from_dict(obj.get("agents"))
        notify = AgentsElement.from_dict(obj.get("notify"))
        steps = Steps.from_dict(obj.get("steps"))
        return SchemaProperties(env, agents, notify, steps)

    def to_dict(self) -> dict:
        result: dict = {}
        result["env"] = to_class(AgentsElement, self.env)
        result["agents"] = to_class(AgentsElement, self.agents)
        result["notify"] = to_class(AgentsElement, self.notify)
        result["steps"] = to_class(Steps, self.steps)
        return result


class Schema:
    title: str
    schema: str
    file_match: List[str]
    type: str
    required: List[str]
    definitions: Definitions
    properties: SchemaProperties

    def __init__(self, title: str, schema: str, file_match: List[str], type: str, required: List[str], definitions: Definitions, properties: SchemaProperties) -> None:
        self.title = title
        self.schema = schema
        self.file_match = file_match
        self.type = type
        self.required = required
        self.definitions = definitions
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Schema':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        schema = from_str(obj.get("$schema"))
        file_match = from_list(from_str, obj.get("fileMatch"))
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        definitions = Definitions.from_dict(obj.get("definitions"))
        properties = SchemaProperties.from_dict(obj.get("properties"))
        return Schema(title, schema, file_match, type, required, definitions, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        result["$schema"] = from_str(self.schema)
        result["fileMatch"] = from_list(from_str, self.file_match)
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["definitions"] = to_class(Definitions, self.definitions)
        result["properties"] = to_class(SchemaProperties, self.properties)
        return result


def schema_from_dict(s: Any) -> Schema:
    return Schema.from_dict(s)


def schema_to_dict(x: Schema) -> Any:
    return to_class(Schema, x)
