# API Reference <a name="API Reference" id="api-reference"></a>




## Protocols <a name="Protocols" id="Protocols"></a>

### IBlock <a name="IBlock" id="@cnunciato/buildkite-sdk.types.IBlock"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.IBlock


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.block">block</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.allowDependencyFailure">allowDependencyFailure</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.blockedState">blockedState</a></code> | <code>@cnunciato/buildkite-sdk.types.BlockedState</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.branches">branches</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.dependsOn">dependsOn</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.fields">fields</a></code> | <code>@cnunciato/buildkite-sdk.types.ITextInput \| @cnunciato/buildkite-sdk.types.ISelectInputAttribute[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.if">if</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.key">key</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBlock.property.prompt">prompt</a></code> | <code>string</code> | *No description.* |

---

##### `block`<sup>Required</sup> <a name="block" id="@cnunciato/buildkite-sdk.types.IBlock.property.block"></a>

```typescript
public readonly block: string;
```

- *Type:* string

---

##### `allowDependencyFailure`<sup>Optional</sup> <a name="allowDependencyFailure" id="@cnunciato/buildkite-sdk.types.IBlock.property.allowDependencyFailure"></a>

```typescript
public readonly allowDependencyFailure: boolean;
```

- *Type:* boolean

---

##### `blockedState`<sup>Optional</sup> <a name="blockedState" id="@cnunciato/buildkite-sdk.types.IBlock.property.blockedState"></a>

```typescript
public readonly blockedState: BlockedState;
```

- *Type:* @cnunciato/buildkite-sdk.types.BlockedState

---

##### `branches`<sup>Optional</sup> <a name="branches" id="@cnunciato/buildkite-sdk.types.IBlock.property.branches"></a>

```typescript
public readonly branches: string;
```

- *Type:* string

---

##### `dependsOn`<sup>Optional</sup> <a name="dependsOn" id="@cnunciato/buildkite-sdk.types.IBlock.property.dependsOn"></a>

```typescript
public readonly dependsOn: string[];
```

- *Type:* string[]

---

##### `fields`<sup>Optional</sup> <a name="fields" id="@cnunciato/buildkite-sdk.types.IBlock.property.fields"></a>

```typescript
public readonly fields: ITextInput | ISelectInputAttribute[];
```

- *Type:* @cnunciato/buildkite-sdk.types.ITextInput | @cnunciato/buildkite-sdk.types.ISelectInputAttribute[]

---

##### `if`<sup>Optional</sup> <a name="if" id="@cnunciato/buildkite-sdk.types.IBlock.property.if"></a>

```typescript
public readonly if: string;
```

- *Type:* string

---

##### `key`<sup>Optional</sup> <a name="key" id="@cnunciato/buildkite-sdk.types.IBlock.property.key"></a>

```typescript
public readonly key: string;
```

- *Type:* string

---

##### `prompt`<sup>Optional</sup> <a name="prompt" id="@cnunciato/buildkite-sdk.types.IBlock.property.prompt"></a>

```typescript
public readonly prompt: string;
```

- *Type:* string

---

### IBuildAttributes <a name="IBuildAttributes" id="@cnunciato/buildkite-sdk.types.IBuildAttributes"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.IBuildAttributes


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBuildAttributes.property.branch">branch</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBuildAttributes.property.commit">commit</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBuildAttributes.property.env">env</a></code> | <code>{[ key: string ]: string}</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBuildAttributes.property.message">message</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IBuildAttributes.property.metaData">metaData</a></code> | <code>{[ key: string ]: string}</code> | *No description.* |

---

##### `branch`<sup>Optional</sup> <a name="branch" id="@cnunciato/buildkite-sdk.types.IBuildAttributes.property.branch"></a>

```typescript
public readonly branch: string;
```

- *Type:* string

---

##### `commit`<sup>Optional</sup> <a name="commit" id="@cnunciato/buildkite-sdk.types.IBuildAttributes.property.commit"></a>

```typescript
public readonly commit: string;
```

- *Type:* string

---

##### `env`<sup>Optional</sup> <a name="env" id="@cnunciato/buildkite-sdk.types.IBuildAttributes.property.env"></a>

```typescript
public readonly env: {[ key: string ]: string};
```

- *Type:* {[ key: string ]: string}

---

##### `message`<sup>Optional</sup> <a name="message" id="@cnunciato/buildkite-sdk.types.IBuildAttributes.property.message"></a>

```typescript
public readonly message: string;
```

- *Type:* string

---

##### `metaData`<sup>Optional</sup> <a name="metaData" id="@cnunciato/buildkite-sdk.types.IBuildAttributes.property.metaData"></a>

```typescript
public readonly metaData: {[ key: string ]: string};
```

- *Type:* {[ key: string ]: string}

---

### ICommand <a name="ICommand" id="@cnunciato/buildkite-sdk.types.ICommand"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.ICommand


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.commands">commands</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.agents">agents</a></code> | <code>{[ key: string ]: string}</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.allowDependencyFailure">allowDependencyFailure</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.artifactPaths">artifactPaths</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.branches">branches</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.cancelOnBuildFailing">cancelOnBuildFailing</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.concurrency">concurrency</a></code> | <code>number</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.concurrencyGroup">concurrencyGroup</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.dependsOn">dependsOn</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.env">env</a></code> | <code>{[ key: string ]: string}</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.if">if</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.key">key</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.label">label</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.matrix">matrix</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.parallelism">parallelism</a></code> | <code>number</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.plugins">plugins</a></code> | <code>{[ key: string ]: any}[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.priority">priority</a></code> | <code>number</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.retry">retry</a></code> | <code>@cnunciato/buildkite-sdk.types.IRetry</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.skip">skip</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.softFail">softFail</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ICommand.property.timeoutInMinutes">timeoutInMinutes</a></code> | <code>number</code> | *No description.* |

---

##### `commands`<sup>Required</sup> <a name="commands" id="@cnunciato/buildkite-sdk.types.ICommand.property.commands"></a>

```typescript
public readonly commands: string[];
```

- *Type:* string[]

---

##### `agents`<sup>Optional</sup> <a name="agents" id="@cnunciato/buildkite-sdk.types.ICommand.property.agents"></a>

```typescript
public readonly agents: {[ key: string ]: string};
```

- *Type:* {[ key: string ]: string}

---

##### `allowDependencyFailure`<sup>Optional</sup> <a name="allowDependencyFailure" id="@cnunciato/buildkite-sdk.types.ICommand.property.allowDependencyFailure"></a>

```typescript
public readonly allowDependencyFailure: boolean;
```

- *Type:* boolean

---

##### `artifactPaths`<sup>Optional</sup> <a name="artifactPaths" id="@cnunciato/buildkite-sdk.types.ICommand.property.artifactPaths"></a>

```typescript
public readonly artifactPaths: string[];
```

- *Type:* string[]

---

##### `branches`<sup>Optional</sup> <a name="branches" id="@cnunciato/buildkite-sdk.types.ICommand.property.branches"></a>

```typescript
public readonly branches: string;
```

- *Type:* string

---

##### `cancelOnBuildFailing`<sup>Optional</sup> <a name="cancelOnBuildFailing" id="@cnunciato/buildkite-sdk.types.ICommand.property.cancelOnBuildFailing"></a>

```typescript
public readonly cancelOnBuildFailing: boolean;
```

- *Type:* boolean

---

##### `concurrency`<sup>Optional</sup> <a name="concurrency" id="@cnunciato/buildkite-sdk.types.ICommand.property.concurrency"></a>

```typescript
public readonly concurrency: number;
```

- *Type:* number

---

##### `concurrencyGroup`<sup>Optional</sup> <a name="concurrencyGroup" id="@cnunciato/buildkite-sdk.types.ICommand.property.concurrencyGroup"></a>

```typescript
public readonly concurrencyGroup: string;
```

- *Type:* string

---

##### `dependsOn`<sup>Optional</sup> <a name="dependsOn" id="@cnunciato/buildkite-sdk.types.ICommand.property.dependsOn"></a>

```typescript
public readonly dependsOn: string[];
```

- *Type:* string[]

---

##### `env`<sup>Optional</sup> <a name="env" id="@cnunciato/buildkite-sdk.types.ICommand.property.env"></a>

```typescript
public readonly env: {[ key: string ]: string};
```

- *Type:* {[ key: string ]: string}

---

##### `if`<sup>Optional</sup> <a name="if" id="@cnunciato/buildkite-sdk.types.ICommand.property.if"></a>

```typescript
public readonly if: string;
```

- *Type:* string

---

##### `key`<sup>Optional</sup> <a name="key" id="@cnunciato/buildkite-sdk.types.ICommand.property.key"></a>

```typescript
public readonly key: string;
```

- *Type:* string

---

##### `label`<sup>Optional</sup> <a name="label" id="@cnunciato/buildkite-sdk.types.ICommand.property.label"></a>

```typescript
public readonly label: string;
```

- *Type:* string

---

##### `matrix`<sup>Optional</sup> <a name="matrix" id="@cnunciato/buildkite-sdk.types.ICommand.property.matrix"></a>

```typescript
public readonly matrix: string[];
```

- *Type:* string[]

---

##### `parallelism`<sup>Optional</sup> <a name="parallelism" id="@cnunciato/buildkite-sdk.types.ICommand.property.parallelism"></a>

```typescript
public readonly parallelism: number;
```

- *Type:* number

---

##### `plugins`<sup>Optional</sup> <a name="plugins" id="@cnunciato/buildkite-sdk.types.ICommand.property.plugins"></a>

```typescript
public readonly plugins: {[ key: string ]: any}[];
```

- *Type:* {[ key: string ]: any}[]

---

##### `priority`<sup>Optional</sup> <a name="priority" id="@cnunciato/buildkite-sdk.types.ICommand.property.priority"></a>

```typescript
public readonly priority: number;
```

- *Type:* number

---

##### `retry`<sup>Optional</sup> <a name="retry" id="@cnunciato/buildkite-sdk.types.ICommand.property.retry"></a>

```typescript
public readonly retry: IRetry;
```

- *Type:* @cnunciato/buildkite-sdk.types.IRetry

---

##### `skip`<sup>Optional</sup> <a name="skip" id="@cnunciato/buildkite-sdk.types.ICommand.property.skip"></a>

```typescript
public readonly skip: boolean;
```

- *Type:* boolean

---

##### `softFail`<sup>Optional</sup> <a name="softFail" id="@cnunciato/buildkite-sdk.types.ICommand.property.softFail"></a>

```typescript
public readonly softFail: boolean;
```

- *Type:* boolean

---

##### `timeoutInMinutes`<sup>Optional</sup> <a name="timeoutInMinutes" id="@cnunciato/buildkite-sdk.types.ICommand.property.timeoutInMinutes"></a>

```typescript
public readonly timeoutInMinutes: number;
```

- *Type:* number

---

### IGroup <a name="IGroup" id="@cnunciato/buildkite-sdk.types.IGroup"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.IGroup


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.group">group</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.steps">steps</a></code> | <code>@cnunciato/buildkite-sdk.types.IBlock \| @cnunciato/buildkite-sdk.types.ICommand \| @cnunciato/buildkite-sdk.types.IInput \| @cnunciato/buildkite-sdk.types.ITrigger \| @cnunciato/buildkite-sdk.types.IWait[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.allowDependencyFailure">allowDependencyFailure</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.dependsOn">dependsOn</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.if">if</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.key">key</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.label">label</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.notify">notify</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IGroup.property.skip">skip</a></code> | <code>boolean</code> | *No description.* |

---

##### `group`<sup>Required</sup> <a name="group" id="@cnunciato/buildkite-sdk.types.IGroup.property.group"></a>

```typescript
public readonly group: string;
```

- *Type:* string

---

##### `steps`<sup>Required</sup> <a name="steps" id="@cnunciato/buildkite-sdk.types.IGroup.property.steps"></a>

```typescript
public readonly steps: IBlock | ICommand | IInput | ITrigger | IWait[];
```

- *Type:* @cnunciato/buildkite-sdk.types.IBlock | @cnunciato/buildkite-sdk.types.ICommand | @cnunciato/buildkite-sdk.types.IInput | @cnunciato/buildkite-sdk.types.ITrigger | @cnunciato/buildkite-sdk.types.IWait[]

---

##### `allowDependencyFailure`<sup>Optional</sup> <a name="allowDependencyFailure" id="@cnunciato/buildkite-sdk.types.IGroup.property.allowDependencyFailure"></a>

```typescript
public readonly allowDependencyFailure: boolean;
```

- *Type:* boolean

---

##### `dependsOn`<sup>Optional</sup> <a name="dependsOn" id="@cnunciato/buildkite-sdk.types.IGroup.property.dependsOn"></a>

```typescript
public readonly dependsOn: string[];
```

- *Type:* string[]

---

##### `if`<sup>Optional</sup> <a name="if" id="@cnunciato/buildkite-sdk.types.IGroup.property.if"></a>

```typescript
public readonly if: string;
```

- *Type:* string

---

##### `key`<sup>Optional</sup> <a name="key" id="@cnunciato/buildkite-sdk.types.IGroup.property.key"></a>

```typescript
public readonly key: string;
```

- *Type:* string

---

##### `label`<sup>Optional</sup> <a name="label" id="@cnunciato/buildkite-sdk.types.IGroup.property.label"></a>

```typescript
public readonly label: string;
```

- *Type:* string

---

##### `notify`<sup>Optional</sup> <a name="notify" id="@cnunciato/buildkite-sdk.types.IGroup.property.notify"></a>

```typescript
public readonly notify: string[];
```

- *Type:* string[]

---

##### `skip`<sup>Optional</sup> <a name="skip" id="@cnunciato/buildkite-sdk.types.IGroup.property.skip"></a>

```typescript
public readonly skip: boolean;
```

- *Type:* boolean

---

### IInput <a name="IInput" id="@cnunciato/buildkite-sdk.types.IInput"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.IInput


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.IInput.property.input">input</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IInput.property.allowDependencyFailure">allowDependencyFailure</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IInput.property.branches">branches</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IInput.property.dependsOn">dependsOn</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IInput.property.fields">fields</a></code> | <code>@cnunciato/buildkite-sdk.types.ITextInput \| @cnunciato/buildkite-sdk.types.ISelectInputAttribute[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IInput.property.if">if</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IInput.property.key">key</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IInput.property.prompt">prompt</a></code> | <code>string</code> | *No description.* |

---

##### `input`<sup>Required</sup> <a name="input" id="@cnunciato/buildkite-sdk.types.IInput.property.input"></a>

```typescript
public readonly input: string;
```

- *Type:* string

---

##### `allowDependencyFailure`<sup>Optional</sup> <a name="allowDependencyFailure" id="@cnunciato/buildkite-sdk.types.IInput.property.allowDependencyFailure"></a>

```typescript
public readonly allowDependencyFailure: boolean;
```

- *Type:* boolean

---

##### `branches`<sup>Optional</sup> <a name="branches" id="@cnunciato/buildkite-sdk.types.IInput.property.branches"></a>

```typescript
public readonly branches: string;
```

- *Type:* string

---

##### `dependsOn`<sup>Optional</sup> <a name="dependsOn" id="@cnunciato/buildkite-sdk.types.IInput.property.dependsOn"></a>

```typescript
public readonly dependsOn: string[];
```

- *Type:* string[]

---

##### `fields`<sup>Optional</sup> <a name="fields" id="@cnunciato/buildkite-sdk.types.IInput.property.fields"></a>

```typescript
public readonly fields: ITextInput | ISelectInputAttribute[];
```

- *Type:* @cnunciato/buildkite-sdk.types.ITextInput | @cnunciato/buildkite-sdk.types.ISelectInputAttribute[]

---

##### `if`<sup>Optional</sup> <a name="if" id="@cnunciato/buildkite-sdk.types.IInput.property.if"></a>

```typescript
public readonly if: string;
```

- *Type:* string

---

##### `key`<sup>Optional</sup> <a name="key" id="@cnunciato/buildkite-sdk.types.IInput.property.key"></a>

```typescript
public readonly key: string;
```

- *Type:* string

---

##### `prompt`<sup>Optional</sup> <a name="prompt" id="@cnunciato/buildkite-sdk.types.IInput.property.prompt"></a>

```typescript
public readonly prompt: string;
```

- *Type:* string

---

### IRetry <a name="IRetry" id="@cnunciato/buildkite-sdk.types.IRetry"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.IRetry


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.IRetry.property.automatic">automatic</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IRetry.property.manual">manual</a></code> | <code>boolean</code> | *No description.* |

---

##### `automatic`<sup>Optional</sup> <a name="automatic" id="@cnunciato/buildkite-sdk.types.IRetry.property.automatic"></a>

```typescript
public readonly automatic: boolean;
```

- *Type:* boolean

---

##### `manual`<sup>Optional</sup> <a name="manual" id="@cnunciato/buildkite-sdk.types.IRetry.property.manual"></a>

```typescript
public readonly manual: boolean;
```

- *Type:* boolean

---

### ISelectInputAttribute <a name="ISelectInputAttribute" id="@cnunciato/buildkite-sdk.types.ISelectInputAttribute"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.ISelectInputAttribute


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.key">key</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.options">options</a></code> | <code>@cnunciato/buildkite-sdk.types.ISelectInputOption[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.default">default</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.hint">hint</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.multiple">multiple</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.required">required</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.select">select</a></code> | <code>string</code> | *No description.* |

---

##### `key`<sup>Required</sup> <a name="key" id="@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.key"></a>

```typescript
public readonly key: string;
```

- *Type:* string

---

##### `options`<sup>Required</sup> <a name="options" id="@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.options"></a>

```typescript
public readonly options: ISelectInputOption[];
```

- *Type:* @cnunciato/buildkite-sdk.types.ISelectInputOption[]

---

##### `default`<sup>Optional</sup> <a name="default" id="@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.default"></a>

```typescript
public readonly default: string;
```

- *Type:* string

---

##### `hint`<sup>Optional</sup> <a name="hint" id="@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.hint"></a>

```typescript
public readonly hint: string;
```

- *Type:* string

---

##### `multiple`<sup>Optional</sup> <a name="multiple" id="@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.multiple"></a>

```typescript
public readonly multiple: boolean;
```

- *Type:* boolean

---

##### `required`<sup>Optional</sup> <a name="required" id="@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.required"></a>

```typescript
public readonly required: boolean;
```

- *Type:* boolean

---

##### `select`<sup>Optional</sup> <a name="select" id="@cnunciato/buildkite-sdk.types.ISelectInputAttribute.property.select"></a>

```typescript
public readonly select: string;
```

- *Type:* string

---

### ISelectInputOption <a name="ISelectInputOption" id="@cnunciato/buildkite-sdk.types.ISelectInputOption"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.ISelectInputOption


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputOption.property.label">label</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ISelectInputOption.property.value">value</a></code> | <code>string</code> | *No description.* |

---

##### `label`<sup>Required</sup> <a name="label" id="@cnunciato/buildkite-sdk.types.ISelectInputOption.property.label"></a>

```typescript
public readonly label: string;
```

- *Type:* string

---

##### `value`<sup>Required</sup> <a name="value" id="@cnunciato/buildkite-sdk.types.ISelectInputOption.property.value"></a>

```typescript
public readonly value: string;
```

- *Type:* string

---

### ITextInput <a name="ITextInput" id="@cnunciato/buildkite-sdk.types.ITextInput"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.ITextInput


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITextInput.property.key">key</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITextInput.property.text">text</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITextInput.property.default">default</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITextInput.property.hint">hint</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITextInput.property.required">required</a></code> | <code>boolean</code> | *No description.* |

---

##### `key`<sup>Required</sup> <a name="key" id="@cnunciato/buildkite-sdk.types.ITextInput.property.key"></a>

```typescript
public readonly key: string;
```

- *Type:* string

---

##### `text`<sup>Required</sup> <a name="text" id="@cnunciato/buildkite-sdk.types.ITextInput.property.text"></a>

```typescript
public readonly text: string;
```

- *Type:* string

---

##### `default`<sup>Optional</sup> <a name="default" id="@cnunciato/buildkite-sdk.types.ITextInput.property.default"></a>

```typescript
public readonly default: string;
```

- *Type:* string

---

##### `hint`<sup>Optional</sup> <a name="hint" id="@cnunciato/buildkite-sdk.types.ITextInput.property.hint"></a>

```typescript
public readonly hint: string;
```

- *Type:* string

---

##### `required`<sup>Optional</sup> <a name="required" id="@cnunciato/buildkite-sdk.types.ITextInput.property.required"></a>

```typescript
public readonly required: boolean;
```

- *Type:* boolean

---

### ITrigger <a name="ITrigger" id="@cnunciato/buildkite-sdk.types.ITrigger"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.ITrigger


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.trigger">trigger</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.allowDependencyFailure">allowDependencyFailure</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.async">async</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.attributes">attributes</a></code> | <code>@cnunciato/buildkite-sdk.types.IBuildAttributes</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.branches">branches</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.dependsOn">dependsOn</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.if">if</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.label">label</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.skip">skip</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.ITrigger.property.softFail">softFail</a></code> | <code>boolean</code> | *No description.* |

---

##### `trigger`<sup>Required</sup> <a name="trigger" id="@cnunciato/buildkite-sdk.types.ITrigger.property.trigger"></a>

```typescript
public readonly trigger: string;
```

- *Type:* string

---

##### `allowDependencyFailure`<sup>Optional</sup> <a name="allowDependencyFailure" id="@cnunciato/buildkite-sdk.types.ITrigger.property.allowDependencyFailure"></a>

```typescript
public readonly allowDependencyFailure: boolean;
```

- *Type:* boolean

---

##### `async`<sup>Optional</sup> <a name="async" id="@cnunciato/buildkite-sdk.types.ITrigger.property.async"></a>

```typescript
public readonly async: boolean;
```

- *Type:* boolean

---

##### `attributes`<sup>Optional</sup> <a name="attributes" id="@cnunciato/buildkite-sdk.types.ITrigger.property.attributes"></a>

```typescript
public readonly attributes: IBuildAttributes;
```

- *Type:* @cnunciato/buildkite-sdk.types.IBuildAttributes

---

##### `branches`<sup>Optional</sup> <a name="branches" id="@cnunciato/buildkite-sdk.types.ITrigger.property.branches"></a>

```typescript
public readonly branches: string;
```

- *Type:* string

---

##### `dependsOn`<sup>Optional</sup> <a name="dependsOn" id="@cnunciato/buildkite-sdk.types.ITrigger.property.dependsOn"></a>

```typescript
public readonly dependsOn: string[];
```

- *Type:* string[]

---

##### `if`<sup>Optional</sup> <a name="if" id="@cnunciato/buildkite-sdk.types.ITrigger.property.if"></a>

```typescript
public readonly if: string;
```

- *Type:* string

---

##### `label`<sup>Optional</sup> <a name="label" id="@cnunciato/buildkite-sdk.types.ITrigger.property.label"></a>

```typescript
public readonly label: string;
```

- *Type:* string

---

##### `skip`<sup>Optional</sup> <a name="skip" id="@cnunciato/buildkite-sdk.types.ITrigger.property.skip"></a>

```typescript
public readonly skip: boolean;
```

- *Type:* boolean

---

##### `softFail`<sup>Optional</sup> <a name="softFail" id="@cnunciato/buildkite-sdk.types.ITrigger.property.softFail"></a>

```typescript
public readonly softFail: boolean;
```

- *Type:* boolean

---

### IWait <a name="IWait" id="@cnunciato/buildkite-sdk.types.IWait"></a>

- *Implemented By:* @cnunciato/buildkite-sdk.types.IWait


#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.IWait.property.wait">wait</a></code> | <code>string</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IWait.property.allowDependencyFailure">allowDependencyFailure</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IWait.property.continueOnFailure">continueOnFailure</a></code> | <code>boolean</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IWait.property.dependsOn">dependsOn</a></code> | <code>string[]</code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.IWait.property.if">if</a></code> | <code>string</code> | *No description.* |

---

##### `wait`<sup>Required</sup> <a name="wait" id="@cnunciato/buildkite-sdk.types.IWait.property.wait"></a>

```typescript
public readonly wait: string;
```

- *Type:* string

---

##### `allowDependencyFailure`<sup>Optional</sup> <a name="allowDependencyFailure" id="@cnunciato/buildkite-sdk.types.IWait.property.allowDependencyFailure"></a>

```typescript
public readonly allowDependencyFailure: boolean;
```

- *Type:* boolean

---

##### `continueOnFailure`<sup>Optional</sup> <a name="continueOnFailure" id="@cnunciato/buildkite-sdk.types.IWait.property.continueOnFailure"></a>

```typescript
public readonly continueOnFailure: boolean;
```

- *Type:* boolean

---

##### `dependsOn`<sup>Optional</sup> <a name="dependsOn" id="@cnunciato/buildkite-sdk.types.IWait.property.dependsOn"></a>

```typescript
public readonly dependsOn: string[];
```

- *Type:* string[]

---

##### `if`<sup>Optional</sup> <a name="if" id="@cnunciato/buildkite-sdk.types.IWait.property.if"></a>

```typescript
public readonly if: string;
```

- *Type:* string

---

## Enums <a name="Enums" id="Enums"></a>

### BlockedState <a name="BlockedState" id="@cnunciato/buildkite-sdk.types.BlockedState"></a>

#### Members <a name="Members" id="Members"></a>

| **Name** | **Description** |
| --- | --- |
| <code><a href="#@cnunciato/buildkite-sdk.types.BlockedState.PASSED">PASSED</a></code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.BlockedState.FAILED">FAILED</a></code> | *No description.* |
| <code><a href="#@cnunciato/buildkite-sdk.types.BlockedState.RUNNING">RUNNING</a></code> | *No description.* |

---

##### `PASSED` <a name="PASSED" id="@cnunciato/buildkite-sdk.types.BlockedState.PASSED"></a>

---


##### `FAILED` <a name="FAILED" id="@cnunciato/buildkite-sdk.types.BlockedState.FAILED"></a>

---


##### `RUNNING` <a name="RUNNING" id="@cnunciato/buildkite-sdk.types.BlockedState.RUNNING"></a>

---

