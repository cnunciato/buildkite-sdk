import { buildkiteSdk } from "./sdk";

describe("buildkiteSdk", () => {
    it("should work", () => {
        expect(buildkiteSdk()).toEqual("buildkite-sdk");
    });
});
