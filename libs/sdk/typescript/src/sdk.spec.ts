import * as buildkite from "./sdk";

describe("toJSON()", () => {
    it("should render the pipeline steps", () => {
        const pipeline = new buildkite.Pipeline();

        pipeline.addStep({
            label: "some-label",
        });

        expect(pipeline.toJSON()).toBe(
            JSON.stringify({ steps: [{ label: "some-label" }] }, null, 4)
        );
    });
});
