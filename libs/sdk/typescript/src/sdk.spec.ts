import * as buildkite from "./sdk";

describe("toJSON()", () => {
    it("should work", () => {
        expect(new buildkite.Pipeline().toJSON()).toBe({ steps: [] });
    });
});
