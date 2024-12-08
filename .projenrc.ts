import { cdk } from 'projen';
const project = new cdk.JsiiProject({
  author: 'Christian Nunciato',
  authorAddress: 'chris@nunciato.org',
  defaultReleaseBranch: 'main',
  jsiiVersion: '~5.5.0',
  name: 'buildkite-sdk-test',
  projenrcTs: true,
  repositoryUrl: 'https://github.com/chris/buildkite-sdk-test.git',

  // deps: [],                /* Runtime dependencies of this module. */
  // description: undefined,  /* The description is just a string that helps people understand the purpose of the package. */
  // devDeps: [],             /* Build dependencies for this module. */
  // packageName: undefined,  /* The "name" in package.json. */
});
project.synth();