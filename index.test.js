const { execSync } = require("child_process");

test("prints Hello, World! when run", () => {
  const output = execSync("node index.js").toString().trim();
  expect(output).toBe("Hello, World!");
});
