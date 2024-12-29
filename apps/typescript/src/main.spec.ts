import { Pipeline } from "@cnunciato/buildkite-sdk";

describe("toJSON()", () => {
    it("should work", () => {
        expect(new Pipeline().toJSON()).toBe(
            JSON.stringify({ steps: [] }, null, 4)
        );
    });
});
